class Divisao:

    def __init__(self, x0, x1, y0, y1, id):

        self.nomeDivisao = id
        self.descoberta = False

        # Área da divisao
        #  x0,y0
        #
        #
        #           x1,y1
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1

        self.medio = (round((((x0 - x1) / 2) + x1), 2), round((((y0 - y1) / 2) + y1), 2))

        self.objetos = {
            "cadeiras": [],
            "livros": [],
            "mesas": [],
            "camas": [],
            "enfermeiros": [],
            "medicos": [],
            "doentes": []
        }

    def div_obj(self, objeto):
        nomes = objeto.split("_", 1)
        if nomes[0] == "cadeira" and nomes[1] not in self.objetos["cadeiras"]:
            self.objetos["cadeiras"].append(nomes[1])
        elif nomes[0] == "livro" and nomes[1] not in self.objetos["livros"]:
            self.objetos["livros"].append(nomes[1])
        elif nomes[0] == "mesa" and nomes[1] not in self.objetos["mesas"]:
            self.objetos["mesas"].append(nomes[1])
        elif nomes[0] == "cama" and nomes[1] not in self.objetos["camas"]:
            self.objetos["camas"].append(nomes[1])
        elif nomes[0] == "enfermeiro" and nomes[1] not in self.objetos["enfermeiros"]:
            self.objetos["enfermeiros"].append(nomes[1])
        elif nomes[0] == "medico" and nomes[1] not in self.objetos["medicos"]:
            self.objetos["medicos"].append(nomes[1])
        elif nomes[0] == "doente" and nomes[1] not in self.objetos["doentes"]:
            self.objetos["doentes"].append(nomes[1])

    def get_tipo(self):
        if len(self.objetos["camas"]) > 0:
            return "quarto"
        elif len(self.objetos["cadeiras"]) > 0 and len(self.objetos["mesas"]) > 0:
            return "sala_Enfermeiros"
        elif len(self.objetos["cadeiras"]) > 2 and len(self.objetos["mesas"]) == 0:
            return "sala_Espera"
        else:
            return "generico"

    # Redundante
    def tipar_divisao(self):
        if len(self.objetos["camas"]) > 0:
            self.tipoDivisao = "quarto"
        elif len(self.objetos["cadeiras"]) > 0 and len(self.objetos["mesas"]) > 0:
            self.tipoDivisao = "sala_Enfermeiros"
        elif len(self.objetos["cadeiras"]) > 2 and len(self.objetos["mesas"]) == 0:
            self.tipoDivisao = "sala_Espera"
        else:
            self.tipoDivisao = "generico"

        # • quarto: tem sempre pelo menos uma cama
        # • sala de enfermeiros: não tem camas e tem cadeiras e mesas
        # • sala de espera: tem mais de 2 cadeiras e não tem mesas nem camas

    def esta_dentro(self, x, y):
        if self.x0 <= x < self.x1 and self.y0 <= y < self.y1:
            return True
        return False
