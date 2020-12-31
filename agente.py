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

div_Atual = ""

## Memória
lista_Divisoes = []
lista_objetos_vistos = []
historico_objetos = []
historico_tempos = []

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
    global lista_Divisoes
    for div in lista_Divisoes:
        if _id == div.nomeDivisao:
            return div
    return None


# TODO: Remover Hard code
def divisao_Atual(x, y):
    if 100 <= x < 540 and 30 <= y < 160:
        return "Corredor1"
    elif 30 <= x < 100 and 70 <= y < 300:
        return "Corredor2"
    elif 540 <= x < 655 and 30 <= y < 305:
        return "Corredor3"
    elif 30 <= x < 800 and 300 <= y < 430:
        return "Corredor4"
    elif 100 <= x < 255 and 160 <= y < 300:
        return "Quarto5"
    elif 255 <= x < 405 and 160 <= y < 300:
        return "Quarto6"
    elif 405 <= x < 540 and 160 <= y < 300:
        return "Quarto7"
    elif 655 <= x < 800 and 30 <= y < 110:
        return "Quarto8"
    elif 655 <= x < 800 and 110 <= y < 210:
        return "Quarto9"
    elif 655 <= x < 800 and 210 <= y < 305:
        return "Quarto10"
    elif 30 <= x < 255 and 430 <= y < 600:
        return "Quarto11"
    elif 255 <= x < 405 and 430 <= y < 600:
        return "Quarto12"
    elif 405 <= x < 590 and 430 <= y < 600:
        return "Quarto13"
    elif 590 <= x < 770 and 430 <= y < 600:
        return "Quarto14"
    else:
        print("ZONA INVALIDA")
        return "INVALIDO"


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
    if div_Atual == "":
        div_Atual = divisao_Atual(posicao[0], posicao[1])

    # Para a resposta 6.
    historico_bateria.append(bateria)
    historico_tempos.append(time.time())

    nova_divisao = divisao_Atual(posicao[0], posicao[1])

    # Para sabermos a localização de portas e interceção de corredores

    # Para descobrirmos portas
    if nova_divisao != div_Atual:
        nome_intercecao = "intercecao_" + nova_divisao + "_" + div_Atual
        adicionar_lista_objetos_vistos(nome_intercecao, posicao[0], posicao[1])

    div_Atual = nova_divisao

    if ultimo_objeto_list != objetos and objetos != [] and objetos is not None:
        for objeto in objetos:
            historico_objetos.append(objeto)
            adicionar_lista_objetos_vistos(objeto, posicao[0], posicao[1])
        div = get_divisao(div_Atual)
        div.div_obj(objetos)
        div.tipar_divisao()

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
    div = get_divisao(div_Atual)
    print(div.get_tipo())
    pass


# 3. Qual o caminho para a sala de enfermeiros mais próxima?
def resp3():
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
    for i in range(len(historico_bateria)):
        print(f"{i}, {historico_bateria[i]}")
    pass


# 7. Qual a probabilidade de encontrar um livro numa divisão, se já encontraste uma cadeira?
def resp7():
    pass


# 8. Se encontrares um enfermeiro numa divisão, qual é a probabilidade de estar lá um doente?


def resp8():
    pass
