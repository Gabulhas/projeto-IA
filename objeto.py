class Objeto:
    def __init__(self, identificacao, x, y):
        nomes = identificacao.split("_", 1)
        self.tipo = nomes[0]
        self.nome = nomes[1]
        self.identificacao = identificacao
        self.x = x
        self.y = y

    def __str__(self):
        return f"Tipo:{self.tipo} Nome:{self.nome} X: {self.x} Y:{self.y}"
