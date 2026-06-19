class NPC:
    def __init__(self, nome, destino, origem):
        self.nome = nome
        self.destino = destino
        self.origem = origem

    def __repr__(self):
        return f"{self.nome} ({self.origem.nome}->{self.destino.nome})"