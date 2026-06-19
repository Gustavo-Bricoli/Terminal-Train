class Trem:
    def __init__(self, estacoes):
        self.estacoes = estacoes
        self.indice_atual = 0
        self.passageiros = []
        self.pontos = 0

    def embarcar(self, npc):
        self.passageiros.append(npc)
        
    def desembarcar(self, npc):
        if npc.destino == self.estacao_atual():
            self.passageiros.remove(npc)
            self.pontos += 1
            print(f"{npc.nome} desembarcou em {self.estacao_atual().nome}")
            print(f"Pontos: {self.pontos}")
            
    def proxima_estacao(self):
        self.indice_atual = (self.indice_atual + 1) % len(self.estacoes)

    def processar_estacao(self):
        estacao = self.estacao_atual()
        for passageiro in self.passageiros[:]:
            self.desembarcar(passageiro)
        print(f"Total de pontos na estação {estacao.nome}: {self.pontos}")
        while len(estacao.fila) > 0:
            npc = estacao.fila.pop(0)
            self.embarcar(npc)
            print(f"{npc.nome} embarcou em {estacao.nome}")
        
    def estacao_atual(self):
        return self.estacoes[self.indice_atual]