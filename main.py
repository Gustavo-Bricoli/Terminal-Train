from npcAleatorio import criar_npcs
from trem import Trem
from estacao import estacoes

# Criar NPCs e adicioná-los às filas
npcs = criar_npcs(estacoes)

# Criar o trem
trem = Trem(estacoes)

# Testando as filas das estações
print("=== Filas iniciais ===")
for estacao in estacoes:
    print(f"Estação {estacao.nome}: {estacao.fila}")

# Faz o trem dar 2 voltas
print("\n=== Simulação ===")
for _ in range(8):
    print(f"\nEstação {trem.estacao_atual().nome}")
    trem.processar_estacao()
    print("Passageiros no trem:", trem.passageiros)
    trem.proxima_estacao()

print(f"\n=== Final ===")
print(f"Passageiros no trem: {trem.passageiros}")
