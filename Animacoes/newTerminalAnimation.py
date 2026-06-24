from Sistemas.terminalCleaner import clean
from Classes.estacao import estacoes
from random import randint
from time import sleep

# Geração legada de frames upper e lower

#upper_ani2 = f'\n                     [{estacoes[0]}]               [{estacoes[1]}]               [{estacoes[2]}]               [{estacoes[3]}]' # 5 espaços
#lower_ani2 = '###][###==================================================================================\n'

#print(upper_ani2)
#print(lower_ani2)

# Nova forma de geração de frames (tamanho aleatório dos trilhos):

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
nomesEstacoes = []
stationsLocations = []

for nome in estacoes:
    nomesEstacoes.append(str(nome))

upper_ani = f'\n                     [{estacoes[0]}]' # 5 espaços
lower_ani = '###][###============='

stationsLocations.append(upper_ani.find('[')-1) # o -1 se dá pelo \n no começo do upper_ani

for nome in nomesEstacoes.copy()[1:]:
    randomNum = randint(20, 28)
    upper_ani = upper_ani+' '*randomNum+f'[{nome}]'
    stationsLocations.append(len(upper_ani)-4)
    lower_ani = lower_ani+'='*(randomNum+9)

'''for i in range(len(upper_ani)): # essa validação posterior é desnecessária, visto que as posições de [ podem ser capturadas na geração aleatória 
    if upper_ani[i] != '[':
        pass
    else:
        stationsLocations.append(i-1) # o -1 se dá pelo \n no começo do upper_ani'''
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def proximoFrame(frame):
    global lower_ani

    frameList = list(frame)
    frameList.insert(0, frameList.pop(-2))

    lower_ani = ''.join(frameList)

    print(''.join(frameList))

def portaTrem(frame: str, action: int):
    global lower_ani

    sleep(0.4)
    clean()

    if action == 0:
        frameAberto = frame.replace('][', '[]')

        print(upper_ani)
        print(frameAberto)

    elif action == 1:
        frameFechado = frame.replace('[]', '][')

        print(upper_ani)
        print(frameFechado)

    else:
        print('Erro: Condição de porta não encontrada. Fechando porta')
        portaTrem(frame, 1)

def proximaEstacao():
    if lower_ani.find('][') == -1:
        portaTrem(lower_ani, 1)

    showStation = estacoes.copy()

    for loc in stationsLocations.copy():
        if loc <= lower_ani.find(']'):
            showStation.pop(stationsLocations.index(loc))
            stationsLocations.remove(loc)

    sleep(0.2)
    clean()

    print(upper_ani)
    print(lower_ani)

    while stationsLocations[0] != lower_ani.find("]"): # essa diferença se dá pelo \n no começo do upper_ani
        sleep(0.2)
        clean()

        print(upper_ani)
        proximoFrame(lower_ani)
    portaTrem(lower_ani, 0)

    print(f'\nO trem chegou na estação [{showStation[0]}]!')

    #portaTrem(lower_ani, 1)

# Testando animações no terminal direto:
'''input('Aperte enter para começar!\n')

proximaEstacao()

input('\nAperte Enter para ir para a próxima estação!\n')

proximaEstacao()'''