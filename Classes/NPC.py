from listaNomesNPC import nomes, sobrenomes
import random

class NPC:
    def __init__(self, nome, destino, origem):
        self.nome = nome
        self.destino = destino
        self.origem = origem

    def __repr__(self):
        return self.nome

def criar_npcs(estacoes):
    npcs = []
    for i in range(10):
        nome = random.choice(nomes)
        sobrenome = random.choice(sobrenomes)
        nome_completo = f"{nome} {sobrenome}"
        origem = random.choice(estacoes)
        destino = random.choice(estacoes)
        while destino == origem:
            destino = random.choice(estacoes)
        npc = NPC(nome_completo, destino, origem)
        origem.fila.append(npc)
        npcs.append(npc)
    return npcs