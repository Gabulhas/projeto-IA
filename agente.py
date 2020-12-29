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
        div.tipar_divisao()


# 1. Qual foi a penúltima pessoa que viste?
def resp1():
    pass

# 2. Em que tipo de sala estás agora?


def resp2():
    pass

# 3. Qual o caminho para a sala de enfermeiros mais próxima?


def resp3():
    pass


# 4. Qual a distância até ao médico mais próximo?

def resp4():
    pass


# 5. Quanto tempo achas que demoras a ir de onde estás até às escadas?

def resp5():
    pass


# 6. Quanto tempo achas que falta até ficares sem bateria?

def resp6():
    pass


# 7. Qual a probabilidade de encontrar um livro numa divisão, se já encontraste uma cadeira?
def resp7():
    pass

# 8. Se encontrares um enfermeiro numa divisão, qual é a probabilidade de estar lá um doente?


def resp8():
    pass
