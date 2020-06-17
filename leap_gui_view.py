# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'leap_gui.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(350, 190)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(350, 190))
        Form.setMaximumSize(QtCore.QSize(350, 190))
        Form.setStyleSheet(_fromUtf8("border:1px solid black;"))
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.movement_name_txt = QtGui.QLineEdit(Form)
        self.movement_name_txt.setObjectName(_fromUtf8("movement_name_txt"))
        self.gridLayout.addWidget(self.movement_name_txt, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.user_name_txt = QtGui.QLineEdit(Form)
        self.user_name_txt.setObjectName(_fromUtf8("user_name_txt"))
        self.gridLayout.addWidget(self.user_name_txt, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.start_btn = QtGui.QPushButton(Form)
        self.start_btn.setMinimumSize(QtCore.QSize(60, 0))
        self.start_btn.setObjectName(_fromUtf8("start_btn"))
        self.horizontalLayout_2.addWidget(self.start_btn)
        self.stop_btn = QtGui.QPushButton(Form)
        self.stop_btn.setMinimumSize(QtCore.QSize(60, 0))
        self.stop_btn.setObjectName(_fromUtf8("stop_btn"))
        self.horizontalLayout_2.addWidget(self.stop_btn)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.file_name_lbl = QtGui.QLabel(Form)
        self.file_name_lbl.setText(_fromUtf8(""))
        self.file_name_lbl.setObjectName(_fromUtf8("file_name_lbl"))
        self.horizontalLayout.addWidget(self.file_name_lbl)
        self.select_btn = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_btn.sizePolicy().hasHeightForWidth())
        self.select_btn.setSizePolicy(sizePolicy)
        self.select_btn.setMinimumSize(QtCore.QSize(60, 0))
        self.select_btn.setObjectName(_fromUtf8("select_btn"))
        self.horizontalLayout.addWidget(self.select_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.no_of_features = QtGui.QLCDNumber(Form)
        self.no_of_features.setObjectName(_fromUtf8("no_of_features"))
        self.gridLayout_2.addWidget(self.no_of_features, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "leap feature collector", None))
        self.label.setText(_translate("Form", "movement_name", None))
        self.label_2.setText(_translate("Form", "user name", None))
        self.start_btn.setText(_translate("Form", "Start", None))
        self.stop_btn.setText(_translate("Form", "Stop", None))
        self.select_btn.setText(_translate("Form", "select", None))

