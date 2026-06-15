from Classes.estacao import estacoes
from time import sleep

train_doors = ['][','[]']

upper_ani = f'\n                     [{estacoes[0]}]               [{estacoes[1]}]               [{estacoes[2]}]               [{estacoes[3]}]' # 5 espaços
base_ani = f'☰☰☰{train_doors[0]}☰☰☰==================================================================================\n'

base_animation = list(base_ani)
'''for i in range(9):
    #print(list(base_ani))
    
    base_animation.insert(0, base_animation.pop(-2))

    print(upper_ani)
    print(''.join(base_animation))
    print('\n\n\n\n\n')

    sleep(0.2)

#print((base_animation.index('['))) #type: ignore

base_animation.insert(base_animation.index('[')-1, base_animation.pop(base_animation.index('[')))
print(upper_ani)
print(''.join(base_animation))
print('\n\n\n\n\n')

sleep(2)

base_animation.insert(base_animation.index(']')-1, base_animation.pop(base_animation.index(']')))
print(upper_ani)
print(''.join(base_animation))
print('\n\n\n\n\n')

sleep(0.2)'''

'''
Precisa de uma funcao proximaEstacao() e uma voltarInicio(). 
Ai consigo arrumar pra ele nao printar mais a estacao A quando ele volta pro comeco
'''


def terminalAnimation():
    #for i in range(5):
        for j in range(18): #animacao ir para proxima estacao
            #print(list(base_ani))
            
            base_animation.insert(0, base_animation.pop(-2))

            print(upper_ani)
            print(''.join(base_animation))
            print('\n\n\n\n\n')

            sleep(0.2)

        #print((base_animation.index('['))) #type: ignore
        if base_animation[0] != '☰': #mesma coisa mas nao abre a porta quando volta pro comeco
            base_animation.insert(base_animation.index('[')-1, base_animation.pop(base_animation.index('[')))
            print(upper_ani)
            print(''.join(base_animation))
            print('\n\n\n\n\n')

            sleep(2)

            base_animation.insert(base_animation.index(']')-1, base_animation.pop(base_animation.index(']')))
            print(upper_ani)
            print(''.join(base_animation))
            print('\n\n\n\n\n')

            sleep(0.2)