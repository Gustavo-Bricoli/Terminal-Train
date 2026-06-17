import vlc
import time

player = vlc.MediaPlayer("Sons/fnaf-foxy-scream-sfx.mp3")

resultado = player.play()

print("Resultado:", resultado)

time.sleep(10)
