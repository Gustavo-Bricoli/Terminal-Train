from time import sleep
import Sons.after_run
from Classes.terminalCleaner import clean
from utils import resource_path

def yallsee():
    for i in range(0,32):
        path = resource_path(f'Animacoes/skeleton/{i}.txt')
        with open(path, 'r', encoding='utf-8') as file:
            print(file.read())
        sleep(0.015)        
    Sons.after_run.AlguemViu.tocar()
    clean()