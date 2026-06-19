import vlc
from utils import resource_path

class AlguemViu:
    player = None

    @staticmethod
    def tocar():
        AlguemViu.player = vlc.MediaPlayer(
            resource_path("Sons/mp3/after-skeleton.mp3")
        )

        AlguemViu.player.audio_set_volume(100)
        AlguemViu.player.play()