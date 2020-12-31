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
from objeto import Objeto
import networkx as nx
import numpy as np

# Grafo
G = nx.Graph()

# Divisoes
lista_Divisoes = [Divisao(100, 540, 30, 160, "Corredor1"), Divisao(30, 100, 70, 300, "Corredor2"),
                  Divisao(540, 655, 30, 305, "Corredor3"), Divisao(30, 800, 300, 430, "Corredor4"),
                  Divisao(100, 255, 160, 300, "Quarto5"), Divisao(255, 405, 160, 300, "Quarto6"),
                  Divisao(405, 540, 160, 300, "Quarto7"), Divisao(655, 800, 30, 110, "Quarto8"),
                  Divisao(655, 800, 110, 210, "Quarto9"), Divisao(655, 800, 210, 305, "Quarto10"),
                  Divisao(30, 255, 430, 600, "Quarto11"), Divisao(255, 405, 430, 600, "Quarto12"),
                  Divisao(405, 590, 430, 600, "Quarto13"), Divisao(590, 770, 430, 600, "Quarto14")]

for divisao in lista_Divisoes:
    G.add_node(divisao.nomeDivisao)

# Lista de todos os quartos
div_Atual = None

## Memória
lista_objetos_vistos = []
historico_objetos = []
historico_tempos = []
tempo_inicial = time.time()

# útil para a resposta 6
historico_bateria = []

# Para evitar duplicados
ultimo_objeto_list = []


# Verifica se o nome de uma divisão (ID) já foi adicionada à lista de divisões
def verifica_lista_divisoes(id):
    global lista_Divisoes
    for div in lista_Divisoes:
        if id == div.nomeDivisao:
            return True
    return False


# Retorna uma divisão, segundo o ID/nome se existir
def get_divisao(_id):
    for div in lista_Divisoes:
        if _id == div.nomeDivisao:
            return div
    return None


def get_divisao_atual(x, y):
    for divisao in lista_Divisoes:
        if divisao.esta_dentro(x, y):
            divisao.descoberta = True
            return divisao
    print("Error")


def adicionar_lista_objetos_vistos(novo_objeto, x, y):
    nomes = novo_objeto.split("_", 1)
    if nomes[0] == "intercecao":
        # Evita que ao passar pela intercecao pelas duas direcoes que tenha nome diferente
        # Por exemplo: Corredor1_Quarto5 e Quarto5_Corredor1
        divisoes = sorted(nomes[1].split("_", 1))
        novo_objeto = f"intercecao_{divisoes[0]}_{divisoes[1]}"

    for objeto_visto in lista_objetos_vistos:
        if novo_objeto == objeto_visto.identificacao:
            return
    lista_objetos_vistos.append(Objeto(novo_objeto, x, y))


# esta função é invocada em cada ciclo de clock
# e pode servir para armazenar informação recolhida pelo agente
# recebe:
# posicao = a posição atual do agente, uma lista [X,Y]
# bateria = valor de energia na bateria, um número inteiro >= 0
# objetos = o nome do(s) objeto(s) próximos do agente, uma string

# podem achar o tempo atual usando, p.ex.
# time.time()

def work(posicao, bateria, objetos):
    global lista_Divisoes, ultimo_objeto_list, historico_bateria, div_Atual
    if div_Atual is None:
        div_Atual = get_divisao_atual(posicao[0], posicao[1])

    # Para a resposta 6.
    historico_bateria.append(bateria)
    historico_tempos.append(time.time() - tempo_inicial)

    nova_divisao = get_divisao_atual(posicao[0], posicao[1])

    # Para sabermos a localização de portas e interceção de corredores
    if nova_divisao != div_Atual:
        nome_intercecao = "intercecao_" + nova_divisao.nomeDivisao + "_" + div_Atual.nomeDivisao
        adicionar_lista_objetos_vistos(nome_intercecao, posicao[0], posicao[1])

    div_Atual = nova_divisao
    # -----

    if ultimo_objeto_list != objetos and objetos != [] and objetos is not None:
        for objeto in objetos:
            historico_objetos.append(objeto)
            adicionar_lista_objetos_vistos(objeto, posicao[0], posicao[1])
        div_Atual.div_obj(objetos)

    if objetos:
        ultimo_objeto_list = objetos


# 1. Qual foi a penúltima pessoa que viste?
# Ou seja, procurar na lista por Doentes, Enfermeiros ou Médicos
def resp1():
    # Como queremos saber o penúltimo temos de saber qual foi o último
    ultimo = ""
    # [::-1] tem o propósito de reverter a lista, porque novos objetos são adicionados ao fim da lista
    for objeto in historico_objetos[::-1]:

        # in para verificarmos se é uma pessoa
        if objeto.split("_", 1)[0] in ["enfermeiro", "medico", "doente"]:

            # queremos saber qual foi o último para saber quem vem a seguir
            if ultimo != "" and ultimo != objeto:
                print(objeto)
                break
            ultimo = objeto
    pass


# 2. Em que tipo de sala estás agora?
def resp2():
    print(div_Atual.get_tipo())


# 3. Qual o caminho para a sala de enfermeiros mais próxima?
def resp3():
    # REMOVER
    print(div_Atual.__dict__)
    pass


# 4. Qual a distância até ao médico mais próximo?
def resp4():
    for objeto in lista_objetos_vistos:
        print(objeto)
    pass


# 5. Quanto tempo achas que demoras a ir de onde estás até às escadas?

def resp5():
    pass


# 6. Quanto tempo achas que falta até ficares sem bateria?

def resp6():
    trend = np.polyfit(historico_tempos, historico_bateria, 3)
    trendpoly = np.poly1d(trend)
    print([x for x in trendpoly.roots if x > 0][0], "segundos")


# 7. Qual a probabilidade de encontrar um livro numa divisão, se já encontraste uma cadeira?
def resp7():
    pass


# 8. Se encontrares um enfermeiro numa divisão, qual é a probabilidade de estar lá um doente?
def resp8():
    # Só queremos ver as divisões já vistas

    # Número de divisões com enfermeiros
    nB = 0

    # Número de divisões com enfermeiros e doentes
    nAiB = 0
    for divisao in [divisao for divisao in lista_Divisoes if divisao.descoberta]:
        if len(divisao.objetos["enfermeiros"]) > 0:
            nB = nB + 1
            if len(divisao.objetos["doentes"]) > 0:
                nAiB = nAiB + 1

    print(nAiB // nB)
    pass
