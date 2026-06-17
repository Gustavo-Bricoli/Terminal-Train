import vlc

class Jumpscare:
    def tocar():
        player = vlc.MediaPlayer("Sons/mp3/fnaf-foxy-scream-sfx.mp3")
        player.audio_set_volume(100)
        resultado = player.play()
        return resultado
        #time.sleep(10)