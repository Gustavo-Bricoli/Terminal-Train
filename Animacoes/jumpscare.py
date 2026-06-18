from time import sleep
import Sons.run, Sons.scream, os

def foxy():
    Sons.run.Corrida.tocar()
    sleep(2)
    Sons.scream.Jumpscare.tocar()
    for i in range(0,14):
        print("\n"*20)
        with open(f'Animacoes/ascii foxy/{i}.txt', 'r') as file:
            print(file.read())
        sleep(0.05)
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')