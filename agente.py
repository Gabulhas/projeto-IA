"""
agente.py

criar aqui as funções que respondem às perguntas
e quaisquer outras que achem necessário criar

colocar aqui os nomes e número de aluno:
41558, Guilherme Lopes
38991, Cristina Pinto

"""
import time
from divisao import *

lista_Divisoes = []


# Verifica se o nome de uma divisão (ID) já foi adicionada à lista de divisões
def verificaListaDivisoes(divisoes, id):
    for div in divisoes:
        if id == div.nomeDivisao:
            return True
    return False

# Retorna uma divisão, segundo o ID/nome se existir


def getDivisaoInstance(divisoes, id):
    for div in divisoes:
        if id == div.nomeDivisao:
            return div
    return None


coordenadas_divisoes = [
    ((100, 30), (540, 160)),    # Corredor 1
    ((30, 70), (100, 300)),     # Corredor 2
    ((540, 30), (655, 305)),    # Corredor 3
    ((30, 300), (770, 430)),    # Corredor 4

    ((100, 160), (255, 300)),   # Quarto 5
    ((255, 160), (405, 300)),   # Quarto 6
    ((405, 160), (540, 300)),    # Quarto 7

    ((655, 30), (770, 110)),    # Quarto 8
    ((655, 110), (770, 210)),   # Quarto 9
    ((655, 210), (770, 305)),   # Quarto 10

    ((30, 430), (255, 570)),    # Quarto 11
    ((255, 430), (405, 570)),   # Quarto 12
    ((405, 430), (590, 570)),   # Quarto 13
    ((590, 430), (770, 570)),   # Quarto 14
]

corredores = [1, 2, 3, 4]


def divisao_Atual(x, y):
    if 100 <= x < 540 and 30 <= y < 160:
        return "Corredor1"
    elif 30 <= x < 100 and 70 <= y < 300:
        return "Corredor2"
    elif 540 <= x < 655 and 30 <= y < 305:
        return "Corredor3"
    elif 30 <= x < 770 and 300 <= y < 430:
        return "Corredor4"
    elif 100 <= x < 255 and 160 <= y < 300:
        return "Quarto5"
    elif 255 <= x < 405 and 160 <= y < 300:
        return "Quarto6"
    elif 405 <= x < 540 and 160 <= y < 300:
        return "Quarto7"
    elif 655 <= x < 770 and 30 <= y < 110:
        return "Quarto8"
    elif 655 <= x < 770 and 110 <= y < 210:
        return "Quarto9"
    elif 655 <= x < 770 and 210 <= y < 305:
        return "Quarto10"
    elif 30 <= x < 255 and 430 <= y < 570:
        return "Quarto11"
    elif 255 <= x < 405 and 430 <= y < 570:
        return "Quarto12"
    elif 405 <= x < 590 and 430 <= y < 570:
        return "Quarto13"
    elif 590 <= x < 770 and 430 <= y < 570:
        return "Quarto14"


def work(posicao, bateria, objetos):
    # esta função é invocada em cada ciclo de clock
    # e pode servir para armazenar informação recolhida pelo agente
    # recebe:
    # posicao = a posição atual do agente, uma lista [X,Y]
    # bateria = valor de energia na bateria, um número inteiro >= 0
    # objetos = o nome do(s) objeto(s) próximos do agente, uma string

    # podem achar o tempo atual usando, p.ex.
    # time.time()

    global lista_Divisoes

    div_Atual = divisao_Atual(posicao[0], posicao[1])

    if not verificaListaDivisoes(lista_Divisoes, div_Atual):
        lista_Divisoes.append(Divisao(div_Atual))

    if objetos != []:
        div = getDivisaoInstance(lista_Divisoes, div_Atual)
        div.div_obj(objetos)


def resp1():
    pass


def resp2():
    pass


def resp3():
    pass


def resp4():
    pass


def resp5():
    pass


def resp6():
    pass


def resp7():
    pass


def resp8():
    pass
