import vlc

class Corrida:
    def tocar():
        player = vlc.MediaPlayer("Sons/mp3/foxyrun.mp3")
        player.audio_set_volume(100)
        resultado = player.play()
        return resultado