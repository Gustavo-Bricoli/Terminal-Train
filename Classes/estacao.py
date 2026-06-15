class Estacao:
    def __init__(self, nome):
        self.nome = nome
        self.fila = []
    def __repr__(self):
        return self.nome 
    
def criarEstacao(nome):
    pass

a = Estacao("A")
b = Estacao("B")
c = Estacao("C")
d = Estacao("D")
estacoes = [a,b,c,d]