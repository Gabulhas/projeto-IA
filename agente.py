"""
agente.py

criar aqui as funções que respondem às perguntas
e quaisquer outras que achem necessário criar

colocar aqui os nomes e número de aluno:
41558, Guilherme Lopes
38991, Cristina Pinto

"""
import time

quartos = [
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


def work(posicao, bateria, objetos):
    # esta função é invocada em cada ciclo de clock
    # e pode servir para armazenar informação recolhida pelo agente
    # recebe:
    # posicao = a posição atual do agente, uma lista [X,Y]
    # bateria = valor de energia na bateria, um número inteiro >= 0
    # objetos = o nome do(s) objeto(s) próximos do agente, uma string

    # podem achar o tempo atual usando, p.ex.
    # time.time()
    pass


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
