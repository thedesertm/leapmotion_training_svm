import sys
import os
import math
import csv
import time
from leap_gui_view import Ui_Form
from PyQt4 import QtGui
sys.path.append(os.path.join(os.getcwd() , "lib"))
import Leap
import qdarkstyle

class SampleListener(Leap.Listener):
    __current_frame_counter = 0
    __cupture_every = 0.5  # 0.5 sec
    __last_time_capture = time.time()
    __is_stored_enabled = False
    __new_feature_signal = None
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    def on_init(self, controller):
        print ("Initialized")

    def on_connect(self, controller):
        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print ("Disconnected")

    def on_exit(self, controller):
        print ("Exited")

    def on_frame(self, controller):
        self.current_feature_dict = dict()
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        current_time = time.time()
        if len(frame.hands) > 0:
            elapsed_time = current_time  - self.__last_time_capture
            if elapsed_time > self.__cupture_every :
                self.__last_time_capture = time.time()
                features = {
                    "left":[0.0 for i in range(88)],
                    "right": [0.0 for i in range(88)],
                }
                for hand in frame.hands:
                    feature_fector = []
                    hand_type = "left" if hand.is_left else "right"
                    # get palm possition
                    feature_fector.append(math.fabs(hand.palm_position[0]))  # pos in  x dir
                    feature_fector.append(math.fabs(hand.palm_position[1]))  # pos in y dir
                    feature_fector.append(math.fabs(hand.palm_position[2]))  # pos in z dir
                    # palm directions and angels
                    feature_fector.append(math.fabs(hand.direction[0]))  # dir in  x dir
                    feature_fector.append(math.fabs(hand.direction[1]))  # dir in y dir
                    feature_fector.append(math.fabs(hand.direction[2]))  # dir in z dir
                    feature_fector.append(hand.direction.pitch * Leap.RAD_TO_DEG)
                    feature_fector.append(hand.direction.roll * Leap.RAD_TO_DEG)
                    feature_fector.append(hand.direction.yaw * Leap.RAD_TO_DEG)
                    # fingures
                    hand_x_basis = hand.basis.x_basis
                    hand_y_basis = hand.basis.y_basis
                    hand_z_basis = hand.basis.z_basis
                    hand_origin = hand.palm_position
                    hand_transform = Leap.Matrix(hand_x_basis, hand_y_basis, hand_z_basis, hand_origin)
                    hand_transform = hand_transform.rigid_inverse()
                    fingures_vectors = {
                        'Thumb': None, 'Index': None, 'Middle': None, 'Ring': None, 'Pinky': None
                    }
                    for finger in hand.fingers:
                        fingure_name = self.finger_names[finger.type]
                        transformed_direction = hand_transform.transform_direction(finger.direction)
                        fingures_vectors[fingure_name] = Leap.Vector(finger.direction)
                        feature_fector.append(math.fabs(transformed_direction[0]))
                        feature_fector.append(math.fabs(transformed_direction[1]))
                        feature_fector.append(math.fabs(transformed_direction[3]))
                        for i in range(0, 4):
                            bone = finger.bone(i)
                            diff_x = math.fabs(bone.next_joint[0] - hand.palm_position[0])
                            diff_y = math.fabs(bone.next_joint[1] - hand.palm_position[1])
                            diff_z = math.fabs(bone.next_joint[2] - hand.palm_position[2])
                            feature_fector.extend([diff_x , diff_y , diff_z])

                    # get angles between fingures
                    for count in range(len(self.finger_names) - 1):
                        current_fingure_vector = fingures_vectors[self.finger_names[count]]
                        next_fingure_vector = fingures_vectors[self.finger_names[count + 1]]
                        feature_fector.append(current_fingure_vector.angle_to( next_fingure_vector) * (180.0 / math.pi))
                    features[hand_type]= feature_fector

                total_fingure_vector = [len(frame.hands)]
                total_fingure_vector.extend(features['left'])
                total_fingure_vector.extend(features['right'])
                if self.__new_feature_signal:
                    self.__new_feature_signal(total_fingure_vector)
    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return ("STATE_START")

        if state == Leap.Gesture.STATE_UPDATE:
            return ("STATE_UPDATE")

        if state == Leap.Gesture.STATE_STOP:
            return ("STATE_STOP")

        if state == Leap.Gesture.STATE_INVALID:
            return ("STATE_INVALID")

    def set_callBack(self , call_back):
        self.__new_feature_signal = call_back

class LeapInterface(Ui_Form , QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.__listener = SampleListener()
        self.__controller = Leap.Controller()
        self.__controller.add_listener(self.__listener)
        self.start_btn.clicked.connect(self._start_recording)
        self.stop_btn.clicked.connect(self._stop_recording)
        self.select_btn.clicked.connect(self.choose_file_name)
        self.__listener.set_callBack(self.on_feature)
        self.__csv_file_handler = None
        self.__file_writer = None
        self.__csv_file_path = ''
        self.counter = 0
        self.show()

    def choose_file_name(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        if len(name) > 0:
            self.__csv_file_path = name
            if len(name)>25:
                self.file_name_lbl.setText(name[-25:])
            else:
                self.file_name_lbl.setText(name)


    def _start_recording(self):
        if self.__csv_file_handler is None:
            if self.__csv_file_path == '':
                self.showdialog("Error" , "you have to choose file to store the info first")
                return
            file_path = self.__csv_file_path
            self.counter = 0
            if not os.path.isfile(file_path):
                self.__csv_file_handler = open(file_path , 'w')
            else:
                self.__csv_file_handler = open(file_path, 'a')
            self.__file_writer = csv.writer(self.__csv_file_handler, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        else:
            self.showdialog("Error", "already running you have to stop it first")

    def _stop_recording(self):
        if (self.__csv_file_handler is None):
            self.showdialog("Error", "already stopped .......")
        else:
            try:
                self.__csv_file_handler.close()
            except:
                pass
            self.__csv_file_handler = None
            self.__file_writer = None

    def on_feature(self , fet):
        print("got it")
        if self.__file_writer:
            self.counter += 1
            self.no_of_features.display(self.counter)
            gesture_name = str(self.movement_name_txt.text())
            user_name = str(self.user_name_txt.text())
            new_feature = [user_name]
            new_feature.extend(fet)
            new_feature.append(gesture_name)
            self.__file_writer.writerow(new_feature)


    def __del__(self):
        try:
            self.__controller.remove_listener(self.__listener)
            if self.__file_writer:
                self.__csv_file_handler.close()
        except Exception as e:
            print(e)






    def showdialog(self , title , body):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText(body)
        msg.setWindowTitle(title)
        msg.exec_()

def Main():
    app = QtGui.QApplication(sys.argv)
    interface = LeapInterface()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt())
    app.exec_()
if __name__ == "__main__":
    Main()