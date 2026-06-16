from Classes.NPC_names.listaNomesNPC import nomes, sobrenomes # esse import é curioso, porque a pasta que o arquivo considera para dar import é aquela do arquivo aberto inicialmente, ou seja, o main.py na root. Por isso o Classes de novo
import random

class NPC:
    def __init__(self, nome, destino, origem):
        self.nome = nome
        self.destino = destino
        self.origem = origem

    def __repr__(self):
        return f"{self.nome} ({self.origem.nome}->{self.destino.nome})"

def gerarNome():
    return f"{random.choice(nomes)} {random.choice(sobrenomes)}"

def criarNpcs(estacoes):
    npcs = []
    for i in range(1000):
        nome_completo = gerarNome()
        origem = random.choice(estacoes)
        destino = random.choice(estacoes)
        while destino == origem:
            destino = random.choice(estacoes)
        npc = NPC(nome_completo, destino, origem)
        origem.fila.append(npc)
        npcs.append(npc)
    return npcs