import vlc
import time

player = vlc.MediaPlayer("Sons/foxyrun.mp3")

resultado = player.play()

print("Resultado:", resultado)

time.sleep(10)