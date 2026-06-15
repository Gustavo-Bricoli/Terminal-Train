from Classes.NPC import criarNpcs
from Classes.trem import Trem
from Classes.estacao import estacoes
from Animacões.terminalAnimation import terminalAnimation

# Criar NPCs e adicioná-los às filas
npcs = criarNpcs(estacoes)

# Criar o trem
trem = Trem(estacoes)

# Testando as filas das estações
print("=== Filas iniciais ===")
for estacao in estacoes:
    print(f"Estação {estacao.nome}: {estacao.fila}")

answer = input("Começar o jogo? (y/n):\n")

contador = 0
while answer == 'y':
    contador += 1
    if contador % 5 != 0:
        terminalAnimation()
        print(f"\nEstação {trem.estacao_atual().nome}")
        trem.processar_estacao()
        print("Passageiros no trem:", trem.passageiros)
        trem.proxima_estacao()
        answer = input("Ir para a próxima estação? (y/n):\n")
    else:
        terminalAnimation()
        contador = 0
    

print(f"\n=== Final ===")
print(f"Passageiros no trem: {trem.passageiros}")
