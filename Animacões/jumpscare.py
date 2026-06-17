from time import sleep
import os

def foxy():
    for i in range(0,14):
        print("\n"*20)
        with open(f'ascii foxy/{i}.txt', 'r') as file:
            print(file.read())
        sleep(0.05)
    sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')