import pandas as pd
import math
import numpy
import joblib

# nota classificada como boa para recomendação de filmes (0..5)
NOTA_BOA = 4

# nota usada para recomendar filmes, somente filmes com nota acima da nota de exigencia podem ser recomendados
NOTA_EXIGENCIA = 4

# FATOR_DIV filtra os generos que o usuario mais de notas boas:  total_notas_boas_genero/total_notas_boas
FATOR_DIV = 1 / 3

idx = pd.IndexSlice

links = pd.read_csv("links.csv", index_col=['movieId'])
movies = pd.read_csv("movies.csv", sep=",", index_col=['movieId'])
ratings = pd.read_csv("ratings.csv", index_col=['userId', 'movieId'])
tags = pd.read_csv("tags.csv", index_col=['userId', 'movieId'])


class Grafo_de_similaridade:
    # as tuplas dos usuarios representam as arestas do grafo e a similaridade o seu peso
    similaridade = {}

    # salva os filmes avaliados por usuarios no formato: filmes_por_usuarios[usuario][(usuario,filme)] = nota
    filmes_por_usuarios = {}

    generos_dos_filmes = {}

    perfil_usuarios = {}

    # salva no formato:
    # usuario_gosta[usuario][genero] = (media, quantidade, total, tba)
    # media -> media das notas em que o usuario avaliou bem o genero
    # quantidade -> quantidade de avaliações boas do genero
    # total -> total de filmes avaliados pelo usuario
    # tba -> total de boas avaliações do usuario

    usuario_gosta = {}

    usuarios = []
    filmes = []


def foi_visto(g, usuario, filme):
    for vistos in g.filmes_por_usuarios[usuario]:
        if vistos[1] == filme[1]:
            return True
    return False


def recomenda_filmes(usuario, g, n_users):
    mais_proximos = top_similares(usuario, g, n_users)

    filmes = []

    for usr in mais_proximos:
        for f in g.filmes_por_usuarios[usr[0]]:
            if (not foi_visto(g, usuario, f)) and (g.filmes_por_usuarios[usr[0]][f] >= NOTA_EXIGENCIA) and (
                    f not in filmes):
                filmes.append((f[1], g.filmes_por_usuarios[usr[0]][f]))

    return filmes


def top_similares(usuario, g, n_users):
    # lista das notas do top n usuarios compativeis
    top_n = []

    for usr, nota in g.similaridade[usuario]:
        if len(top_n) < n_users:
            top_n.append((usr, nota))
        else:
            top_n.sort(key=lambda x: x[1])
            if top_n[0][1] < nota:
                top_n[0] = (usr, nota)

    return top_n


def salvar_similaridade(g):
    joblib.dump(g.similaridade, "similaridade.pkl")


def carregar_similaridade(g):
    g.similaridade = joblib.load('similaridade.pkl')


def imprime_grafo(g):
    for i in g.similaridade:
        print("Usuários: ", i, "Total similares:", len(g.similaridade[i]), " similaridade: ", g.similaridade[i])


def compatibilidade_usuarios(usr_x, usr_y, g, top=False):
    # referente aos generos
    total_x = 0
    total_y = 0
    ambos_gostam = 0

    # lista com os generos comparados sem repetição
    lista = []

    for x_gosta in g.usuario_gosta[usr_x]:
        total_x += 1
        for y_gosta in g.usuario_gosta[usr_y]:
            total_y += 1

            if x_gosta == y_gosta:
                ambos_gostam += 1

            if x_gosta not in lista:
                lista.append(x_gosta)
            if y_gosta not in lista:
                lista.append(y_gosta)

    if (total_y == 0) or (total_x) == 0:
        total_y = 0
    else:
        total_y = total_y / total_x

    # total de generos do conjunto
    total = len(lista)

    # se ambos gostam pelo menos da metade dos generos do conjunto união então são compativeis
    # o grau pode ser alterado para obter maior compatibilidade ou menor
    if (ambos_gostam == 0) or (total == 0):
        return 0.0
    return ambos_gostam / total


# função que calcula a similaridade entre dois usuários
def calcula_similaridade(g):
    for usr_x in g.usuarios:
        for usr_y in g.usuarios:
            if usr_x < usr_y:
                # os usuarios similares se tornam vertices adjacentes na lista de adjacencia do grafo de similaridade
                comp = compatibilidade_usuarios(usr_x, usr_y, g)
                g.similaridade[usr_x].append((usr_y, comp))
                g.similaridade[usr_y].append((usr_x, comp))
        print("%.2f" % (100 * (usr_x / len(g.usuarios))), "%")


# função que pega os filmes avaliados e a avaliação deles por um dado um usuario
def filmes_avaliados_por_usuario(usuario):
    filmes_avaliados = ratings.loc[idx[usuario, :], 'rating',].T.to_dict()
    return filmes_avaliados


def carrega_generos(g):
    for filme_id in g.filmes:
        generos = movies.loc[filme_id, 'genres']
        generos = generos.split("|")
        g.generos_dos_filmes[filme_id] = generos


def generos_por_usuario(usuario, g):
    # cada usuario vai ter um dicionario com os generos e as notas medias para cada genero
    g.usuario_gosta[usuario] = {}

    total_filmes = 0
    total_boas_av = 0

    for filme in g.filmes_por_usuarios[usuario]:
        total_filmes += 1
        # se a nota do filme for maior que a nota desejada ele reconhece que os generos do filme agradam o usuario
        if g.filmes_por_usuarios[usuario][filme] >= NOTA_BOA:
            total_boas_av += 1
            for genero in g.generos_dos_filmes[filme[1]]:
                if genero in g.usuario_gosta[usuario]:
                    # se o genero ja existi ele adicionar a nota para o filme referente na lista de notas do genero
                    g.usuario_gosta[usuario][genero].append(g.filmes_por_usuarios[usuario][filme])
                else:
                    # se o genero for novo ele cria uma lista com a nota do filme referente
                    g.usuario_gosta[usuario][genero] = [g.filmes_por_usuarios[usuario][filme]]

    for genero in g.usuario_gosta[usuario]:
        qt = len(g.usuario_gosta[usuario][genero])
        soma = sum(g.usuario_gosta[usuario][genero])
        media = soma / qt
        g.usuario_gosta[usuario][genero] = (media, qt, total_filmes, total_boas_av)


def generos_favoritos_por_usuario(g, usuario):
    # aplicando a métrica escolhida para avaliar se um gênero é do agrado do usuário
    # todos os generos que estão no usuario_gosta são bem avaliados, vou filtrar pela quantidade
    # vou utilizar a relação da quantidade de avaliações positivas do genero e quantidade de avaliações positivas
    g.perfil_usuarios[usuario] = []

    for genero in g.usuario_gosta[usuario]:
        # FATOR_DIV filtra os generos que o usuario mais de notas boas:  total_notas_boas_genero/total_notas_boas
        if (g.usuario_gosta[usuario][genero][1] / g.usuario_gosta[usuario][genero][3]) > FATOR_DIV:
            g.perfil_usuarios[usuario].append(genero)


def carrega_usuarios(g):
    for usr, movie in ratings.index.values:
        if usr not in g.usuarios:
            g.usuarios.append(usr)
            g.similaridade[usr] = []


def carrega_filmes(g):
    for movie in movies.index.values:
        g.filmes.append(movie)


def imprime_lista_de_filmes(filmes):
    cont = 0
    for f in filmes:
        cont += 1
        print("Id do filme: ", f[0], "\tTítulo do filme: ", movies.loc[f[0], 'title'])
    print("Foram encontrados: ", cont, "filmes recomendados para o usuário.")


def deve_ser_recomendado(usuario, filme, g):
    lista_filmes = recomenda_filmes(usuario_id, g, numero_de_usuarios_proximos)
    for tuplas in lista_filmes:
        if filme == tuplas[0]:
            return 0
    if foi_visto(g, usuario, (0, filme)):
        return 1
    return 2


############################################################################################################


g = Grafo_de_similaridade()

# salva todos os usuarios no grafo
carrega_filmes(g)
carrega_generos(g)
carrega_usuarios(g)

for usr in g.usuarios:
    g.filmes_por_usuarios[usr] = filmes_avaliados_por_usuario(usr)
    generos_por_usuario(usr, g)
    generos_favoritos_por_usuario(g, usr)

# para a primeira execução é preciso calcular mas depois pode apenas carregar o arquivo para poupar tempo
calcula_similaridade(g)
salvar_similaridade(g)

# se tiver o arquivo pode apenas carregalo ao inves de calcular novamente
# carregar_similaridade(g)

# função auxiliar para imprimir o grafo de similaridade com as relações entre os usuarios
# imprime_grafo(g)

##########################################################################################################
# AS VARIÁVEIS ABAIXO DEVEM SER MODIFICADAS PARA UTILIZAR O SISTEMA DE RECOMENDAÇÃO PARA OUTROS CENÁRIOS #
##########################################################################################################
# escolha o usuário para recomendar alguns filmes
usuario_id = 300

# serve somente para o método que verifica se o filme deve ser recomendado
filme_id = 1

# numero de usuarios a serem usados como base para o cálculo, aumente para uma amostra maior
numero_de_usuarios_proximos = 20
##########################################################################################################


# método que imprime a lista de filmes recomendados ao usuário escolhido utilizando os critérios globais na parte de
# cima do arquivo para fazer o cálculo da métrica de similaridade e o número de usuários similares mais próximos
# utilizados para fazer a recomendação

imprime_lista_de_filmes((recomenda_filmes(usuario_id, g, numero_de_usuarios_proximos)))

# método para ver se um filme deve ser recomendado para um usuário
print("")
if deve_ser_recomendado(usuario_id, filme_id, g) == 0:
    print("O filme ", movies.loc[filme_id, 'title'], " deve ser recomendado ao usuário ", usuario_id)
elif deve_ser_recomendado(usuario_id, filme_id, g) == 1:
    print("O filme ", movies.loc[filme_id, 'title'], " já foi assistido pelo usuário ", usuario_id)
elif deve_ser_recomendado(usuario_id, filme_id, g) == 2:
    print("O filme ", movies.loc[filme_id, 'title'], " não deve ser recomendado ao usuário ", usuario_id)

########################################################################################################
# código para comparar os generos do filme com os do usuario e verificar se faz sentido a recomendação #
########################################################################################################

# print("")
# print("Generos que o usuário gosta: ", end="")
# for g in g.usuario_gosta[usuario_id]:
#     print(g, "\t", end="")
# print("")
# print("Título do filme: ", movies.loc[filme_id, 'title'], "Generos: ", movies.loc[filme_id, 'genres'])
