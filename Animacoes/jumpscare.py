from time import sleep
import Sons.run, Sons.scream
from Sistemas.terminalCleaner import clean
from utils import resource_path

def foxy():
    Sons.run.Corrida.tocar()
    sleep(2)
    Sons.scream.Jumpscare.tocar()
    for i in range(0,14):
        print("\n"*20)
        path = resource_path(f'Animacoes/ascii foxy/{i}.txt')
        with open(path, 'r', encoding='utf-8') as file:
            print(file.read())
        sleep(0.05)
    sleep(1)
    clean()