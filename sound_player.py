import os
import logging
import time
import vlc
class SoundPlayer(object):
    def __init__(self):
        self.player = None

    def play_song(self , song_path , supress_playing= False):
        if os.path.isfile(song_path):
            if not self.player is None:
                if supress_playing  and self.player.is_playing():
                    self.player.stop()
                    self.__play(song_path)
                elif not self.player.is_playing():
                    self.__play(song_path)
            else:
                self.__play(song_path)
        else:
            print("file not existed")

    def __play(self , song_path):
        self.player = vlc.MediaPlayer(song_path)
        self.player.play()
        time.sleep(0.1)

    def wait_to_end(self):
        if not self.player is None:
            while self.player.is_playing():
                time.sleep(0.05)


if __name__ == "__main__":
    import os
    SOUND_FILES_PATH = os.path.join(os.getcwd(), "sound_files")
    test = SoundPlayer()
    file_name = "{}.mp3".format(1)
    music_file_name = os.path.join(SOUND_FILES_PATH, file_name)
    test.play_song(music_file_name)
    input("pls press any key")
