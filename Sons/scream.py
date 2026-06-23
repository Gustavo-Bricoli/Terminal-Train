import vlc
from utils import resource_path

class Jumpscare:
    player = None

    @staticmethod
    def tocar():
        Jumpscare.player = vlc.MediaPlayer(
            resource_path("Sons/mp3/fnaf-foxy-scream-sfx.mp3")
        )

        Jumpscare.player.audio_set_volume(100)
        Jumpscare.player.play()
