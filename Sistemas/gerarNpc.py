import random
from Sistemas.NPC_names.listaNomesNPC import nomes, sobrenomes
from Classes.NPC import NPC

def gerarNome():
    return f"{random.choice(nomes)} {random.choice(sobrenomes)}"

def criarNpcs(estacoes, quantidade):
    npcs = []
    for i in range(quantidade):
        nome_completo = gerarNome()
        origem = random.choice(estacoes)
        destino = random.choice(estacoes)
        while destino == origem:
            destino = random.choice(estacoes)
        npc = NPC(nome_completo, destino, origem)
        origem.fila.append(npc)
        npcs.append(npc)
    return npcs