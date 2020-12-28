class Divisao:

    def __init__(self, id):

        self.tipoDivisao = ""
        self.nomeDivisao = id

        self.objetos = {
            "cadeiras": [],
            "livros": [],
            "mesas": [],
            "camas": [],
            "enfermeiros": [],
            "medicos": [],
            "doentes": []
        }

    def div_obj(self, lista_objetos):
        for objeto in lista_objetos:
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
