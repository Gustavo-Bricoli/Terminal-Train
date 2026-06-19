from time import sleep
import Sons.after_run
from Classes.terminalCleaner import clean

def yallsee():
    for i in range(0,32):
        with open(f'Animacoes/skeleton/{i}.txt', 'r') as file:
            print(file.read())
        sleep(0.015)

    Sons.after_run.AlguemViu.tocar()
    clean()