import vlc
class Corrida:
    player = None

    @staticmethod
    def tocar():
        Corrida.player = vlc.MediaPlayer(
            "Sons/mp3/foxyrun.mp3"
        )

        Corrida.player.audio_set_volume(100)
        Corrida.player.play()