import vlc
from utils import resource_path

class Corrida:
    player = None

    @staticmethod
    def tocar():
        Corrida.player = vlc.MediaPlayer(
            resource_path("Sons/mp3/foxyrun.mp3")
        )

        Corrida.player.audio_set_volume(100)
        Corrida.player.play()