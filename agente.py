"""
agente.py

criar aqui as funções que respondem às perguntas
e quaisquer outras que achem necessário criar

colocar aqui os nomes e número de aluno:
41558, Guilherme Lopes
38991, Cristina Pinto

"""

# TODO Limpar código, criar perguntas novas
# TODO Limpar principalmente as perguntas que usam gráficos, muito código duplicado
# TODO Corrigir a 8

import matplotlib.pyplot as plt

import time
import math
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
                  Divisao(405, 590, 430, 600, "Quarto13"), Divisao(590, 800, 430, 600, "Quarto14")]

for divisao in lista_Divisoes:
    G.add_node(divisao.nomeDivisao, pos=divisao.medio)

# Lista de todos os quartos
div_Atual = None
posicao_atual = None

## Memória
lista_objetos_vistos = []
historico_objetos = []
historico_tempos = []
historico_velocidades = []
tempo_inicial = time.time()
ultimo_tempo = time.time()
posicao_track = [-1, -1]

# útil para a resposta 6
historico_bateria = []

# Para evitar duplicados
ultimo_objeto_list = []
intersecoes = []


def mostrar_grafo(grafo):
    grafo.add_node("EU", pos=(posicao_atual[0], posicao_atual[1]))
    ligar_vizinhos(grafo, "EU", div_Atual.nomeDivisao, posicao_atual[0], posicao_atual[1])

    # TEMPORÁRIO
    plt.gca().invert_yaxis()
    pos = nx.get_node_attributes(grafo, 'pos')
    nx.draw(grafo, pos, node_size=10, node_color='yellow', font_size=8, font_weight='bold', with_labels=True)
    plt.show()
    plt.savefig("Graph.png", format="PNG")

    lista = list(grafo.edges("EU"))
    grafo.remove_edges_from(lista)
    grafo.remove_node("EU")


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


def distance_between_points(ax, ay, bx, by):
    return round(math.hypot(ax - bx, ay - by), 2)


# Retorna um boolean que confirma se o objeto já estava na lista
def adicionar_lista_objetos_vistos(novo_objeto, x, y):
    global lista_objetos_vistos
    nomes = novo_objeto.split("_", 1)
    if nomes[0] == "intercecao":
        # Evita que ao passar pela intercecao pelas duas direcoes que tenha nome diferente
        # Por exemplo: Corredor1_Quarto5 e Quarto5_Corredor1
        divisoes = sorted(nomes[1].split("_", 1))
        novo_objeto = f"intercecao_{divisoes[0]}_{divisoes[1]}"

    for objeto_visto in lista_objetos_vistos:
        if novo_objeto == objeto_visto.identificacao:
            return False
    lista_objetos_vistos.append(Objeto(novo_objeto, x, y))
    return True


def ligar_vizinhos(grafo, intersecao, node, intersecaox, intersecaoy):
    for neighbor in grafo.neighbors(node):
        vizinho_pos = grafo.nodes[neighbor]["pos"]
        grafo.add_edge(intersecao, neighbor,
                       weight=distance_between_points(intersecaox, intersecaoy, vizinho_pos[0], vizinho_pos[1]))
    pass


# 0,0, 180,85
meio_escadas = (round((((0 - 180) / 2) + 180), 2), round((((0 - 85) / 2) + 85), 2))
G.add_node("escadas", pos=meio_escadas)
G.add_edge(lista_Divisoes[0].nomeDivisao, "escadas",
           pos=distance_between_points(*meio_escadas, *lista_Divisoes[0].medio))
G.add_edge(lista_Divisoes[1].nomeDivisao, "escadas",
           pos=distance_between_points(*meio_escadas, *lista_Divisoes[1].medio))


# esta função é invocada em cada ciclo de clock
# e pode servir para armazenar informação recolhida pelo agente
# recebe:
# posicao = a posição atual do agente, uma lista [X,Y]
# bateria = valor de energia na bateria, um número inteiro >= 0
# objetos = o nome do(s) objeto(s) próximos do agente, uma string

# podem achar o tempo atual usando, p.ex.
# time.time()

def work(posicao, bateria, objetos):
    global lista_Divisoes, ultimo_objeto_list, historico_bateria, div_Atual, G, posicao_atual, ultimo_tempo, tick_wait, posicao_track
    posicao_atual = posicao

    if posicao_track[0] != posicao[0] and posicao_track[1] != posicao[1]:
        distancia = distance_between_points(posicao[0], posicao[1], posicao_track[0], posicao_track[1])
        velocidade = distancia / (time.time() - ultimo_tempo)
        posicao_track = posicao.copy()
        historico_velocidades.append(velocidade)
        ultimo_tempo = time.time()

    if div_Atual is None:
        div_Atual = get_divisao_atual(posicao[0], posicao[1])

    # Para a resposta 6.
    historico_bateria.append(bateria)
    historico_tempos.append(time.time() - tempo_inicial)

    nova_divisao = get_divisao_atual(posicao[0], posicao[1])

    # Para sabermos a localização de portas e interceção de corredores
    if nova_divisao != div_Atual:
        divisoes = sorted([nova_divisao.nomeDivisao, div_Atual.nomeDivisao])

        nome_intercecao = "intercecao_" + divisoes[0] + "_" + divisoes[1]
        if nome_intercecao not in intersecoes:
            intersecoes.append(nome_intercecao)
            # adicionar as restantes intersecoes a esta intercecao
            G.add_node(nome_intercecao, pos=(posicao[0], posicao[1]))
            G.add_edge(nova_divisao.nomeDivisao, nome_intercecao,
                       weight=distance_between_points(nova_divisao.medio[0], nova_divisao.medio[1], posicao[0],
                                                      posicao[1]))
            G.add_edge(div_Atual.nomeDivisao, nome_intercecao,
                       weight=distance_between_points(div_Atual.medio[0], div_Atual.medio[1], posicao[0], posicao[1]))

        # ligar_vizinhos(nome_intercecao, nova_divisao.nomeDivisao, posicao[0], posicao[1])
        # ligar_vizinhos(nome_intercecao, div_Atual.nomeDivisao, posicao[0], posicao[1])

    div_Atual = nova_divisao
    # -----

    if ultimo_objeto_list != objetos and objetos != [] and objetos is not None:
        for objeto in objetos:
            historico_objetos.append(objeto)
            if adicionar_lista_objetos_vistos(objeto, posicao[0], posicao[1]):
                G.add_node(objeto, pos=(posicao[0], posicao[1]))
                G.add_edge(div_Atual.nomeDivisao, objeto,
                           weight=distance_between_points(div_Atual.medio[0], div_Atual.medio[1], posicao[0],
                                                          posicao[1]))

            div_Atual.div_obj(objeto)

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
    # TODO: Usar o mesmo método usado na resp4(), só para calcular a mais perto e depois de calcular a mais perto
    #  usar o método que já está para escrever o caminho

    # Assumo que seja preciso a definição de um grafo, para sabermos quais os caminhos possiveis
    # Adicionar temporáriamente a nossa posição para fazer cálculos
    G.add_node("EU", pos=(posicao_atual[0], posicao_atual[1]))
    ligar_vizinhos(G, "EU", div_Atual.nomeDivisao, posicao_atual[0], posicao_atual[1])

    div_mais_perto = None
    distancia_mais_perto = 2000000000

    for divs in lista_Divisoes:
        if divs.get_tipo() == "sala_Enfermeiros":
            distancia = nx.shortest_path_length(G, "EU", divs.nomeDivisao, weight='weight')
            if distancia_mais_perto > distancia:
                distancia_mais_perto = distancia
                div_mais_perto = divs

    if not div_mais_perto:
        print("Sala Enfermeiros não encotrada")
        return

    for parts in nx.shortest_path(G, "EU", div_mais_perto.nomeDivisao):
        # Talvez isto não seja necessário
        if "_" not in parts:
            print(parts, end="->")

    lista = list(G.edges("EU"))
    G.remove_edges_from(lista)
    G.remove_node("EU")
    mostrar_grafo(G)


# 4. Qual a distância até ao médico mais próximo?
def resp4():
    # ADICIONAR VIZINHOS ÁS INTERSEÇÔES
    G.add_node("EU", pos=(posicao_atual[0], posicao_atual[1]))
    ligar_vizinhos(G, "EU", div_Atual.nomeDivisao, posicao_atual[0], posicao_atual[1])
    tempG = G.copy()

    for divisao in lista_Divisoes:
        for neighbors in tempG.neighbors(divisao.nomeDivisao):
            pos = tempG.nodes[neighbors]["pos"]
            ligar_vizinhos(tempG, neighbors, divisao.nomeDivisao, pos[0], pos[1])

    medico_mais_perto = None
    distancia_mais_perto = 2000000000

    for objs in lista_objetos_vistos:
        if objs.tipo == "medico":
            distancia = nx.shortest_path_length(tempG, "EU", objs.identificacao, weight='weight')
            if distancia_mais_perto > distancia:
                distancia_mais_perto = distancia
                medico_mais_perto = objs

    if not medico_mais_perto:
        print("Nenhum médico encontrado")
    else:

        print(medico_mais_perto.nome, distancia_mais_perto)

    mostrar_grafo(tempG)
    lista = list(G.edges("EU"))
    G.remove_edges_from(lista)
    G.remove_node("EU")


# 5. Quanto tempo achas que demoras a ir de onde estás até às escadas?

def resp5():
    if not historico_velocidades:
        print("Erro na velocidade, mexa o robot")
        return

    # ADICIONAR VIZINHOS ÁS INTERSEÇÔES
    G.add_node("EU", pos=(posicao_atual[0], posicao_atual[1]))
    ligar_vizinhos(G, "EU", div_Atual.nomeDivisao, posicao_atual[0], posicao_atual[1])
    tempG = G.copy()

    for divisao in lista_Divisoes:
        for neighbors in tempG.neighbors(divisao.nomeDivisao):
            pos = tempG.nodes[neighbors]["pos"]
            ligar_vizinhos(tempG, neighbors, divisao.nomeDivisao, pos[0], pos[1])

    distancia = nx.shortest_path_length(tempG, "EU", "escadas", weight='weight')

    print("Tempo:", distancia / np.average(historico_velocidades), "Segundos")

    lista = list(G.edges("EU"))
    G.remove_edges_from(lista)
    G.remove_node("EU")
    average_velocity = np.average(historico_velocidades)
    print(average_velocity)


# 6. Quanto tempo achas que falta até ficares sem bateria?

def resp6():
    # TODO ACABAR ESTA
    trend = np.polyfit(historico_tempos, historico_bateria, 2)
    trendpoly = np.poly1d(trend)
    # print([x for x in trendpoly.roots if x > 0][0], "segundos")
    roots = [x for x in trendpoly.roots if x > 0]
    ultima_time_stamp = historico_tempos[len(historico_tempos) - 1]
    print(roots)
    print("Faltam ", str(int(roots[0]) - ultima_time_stamp), "segundos")
    plt.plot(historico_tempos, historico_bateria, '.')
    plt.plot(historico_tempos, trendpoly(historico_tempos))
    plt.show()


# 7. Qual a probabilidade de encontrar um livro numa divisão, se já encontraste uma cadeira?
def resp7():
    pC = 0  # existir uma cadeira na divisão
    pLC = 0  # pelo menos 1 livro e 1 cadeira na mesma div
    tot = 0

    # probabilidade condicionada (encontrar um livro, sabendo que já foi encontrada uma cadeira)
    # P(Livro | Cadeira) = P (LeC) / P(C)

    for divisao in [divisao for divisao in lista_Divisoes if divisao.descoberta]:
        tot = tot + 1
        if len(divisao.objetos["cadeiras"] > 0):
            pC = pC + 1
            if len(divisao.objetos["livros"] > 0):
                pLC = pLC + 1

    pLC = pLC / pC  # prob de encontrar livro em todas as div que têm cadeiras
    pC = pC / tot  # prob de ter uma cadeira em todas as divisões

    print(pLC / pC)

    # if len(divisao.objetos["livros"] > 0) and len(divisao.objetos["cadeiras"] > 0):
    #     pLC = pLC + 1


# 8. Se encontrares um enfermeiro numa divisão, qual é a probabilidade de estar lá um doente?
def resp8():
    # Isto deve estar errado!
    # Só queremos ver as divisões já vistas

    # Número de divisões com enfermeiros
    nB = 0

    # Número de divisões com enfermeiros e doentes
    nAiB = 0

    divisões_visitadas = [divisao for divisao in lista_Divisoes if divisao.descoberta]

    for divisao in divisões_visitadas:

        if len(divisao.objetos["enfermeiros"]) > 0:
            nB = nB + 1
            if len(divisao.objetos["doentes"]) > 0:
                nAiB = nAiB + 1

    print(nAiB // nB)
    pass
