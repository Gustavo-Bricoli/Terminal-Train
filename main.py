from Classes.NPC import criar_npcs
from Classes.trem import Trem
from Classes.estacao import estacoes
from Animacões.terminalAnimation import terminalAnimation

# Criar NPCs e adicioná-los às filas
npcs = criar_npcs(estacoes)

# Criar o trem
trem = Trem(estacoes)

# Testando as filas das estações
print("=== Filas iniciais ===")
for estacao in estacoes:
    print(f"Estação {estacao.nome}: {estacao.fila}")


answer = input("Começar o jogo? (y/n):\n")
while answer == 'y':
    terminalAnimation()
    print(f"\nEstação {trem.estacao_atual().nome}")
    trem.processar_estacao()
    print("Passageiros no trem:", trem.passageiros)
    trem.proxima_estacao()
    answer = input("Ir para a próxima estação? (y/n)\n")

print(f"\n=== Final ===")
print(f"Passageiros no trem: {trem.passageiros}")
