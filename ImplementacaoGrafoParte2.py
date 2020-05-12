import math


# classe de grafo orientado para usar na segunda parte da atividade de implementação
class GrafoOrientado:
    def __init__(self):
        self.estrutura = {"v1": ["v3", "v4"],
                          "v2": ["v4", "v7"],
                          "v3": ["v5", "v6"],
                          "v4": ["v6"],
                          "v5": [],
                          "v6": ["v8"],
                          "v7": ["v8"],
                          "v8": []
                          }

    def add_vertice(self, v, arestas):

        self.estrutura[v] = []  # adiciona o vértice ao grafo

        for i in range(len(arestas)):
            self.estrutura[v].append(arestas[i])  # adiciona as arestas do novo vértice

    def remove_vertice(self, vertice):
        try:
            for i in self.estrutura:
                if i != vertice:
                    #   checa os adjacentes de todos os vertices do grafo para remover o vertice
                    for j in self.estrutura[i]:
                        if j == vertice:
                            self.estrutura[i].remove(vertice)
            self.estrutura.pop(vertice)
        except KeyError:
            print("Não foi possível remover o vértice", vertice, ", pois ele não se encontra no grafo.")

    def imprime_grafo(self):
        if len(self.estrutura) > 0:
            for i in self.estrutura:
                print("[", i, "] -> [ ", end="")
                for j in range(len(self.estrutura[i])):
                    print(self.estrutura[i][j], end="")
                    if j < len(self.estrutura[i]) - 1:
                        print(end=", ")
                    else:
                        print(end="")
                print(" ]")
        else:
            print("O grafo se encontra vazio.")

    def ordenacao_topologica(self):

        ordem = []

        # dicionario com a relacao dos vertices e seus graus
        vertices = {}

        # lista auxiliar que vai ser alterada
        lista_vertices = []

        # inicializa
        for vertice in self.estrutura:
            vertices[vertice] = 0
            lista_vertices.append(vertice)

        while len(ordem) != len(self.estrutura):

            removeu = False

            # reseta os graus
            for v0 in lista_vertices:
                vertices[v0] = 0

            # calcula os graus de entrada
            for v1 in lista_vertices:
                for v2 in lista_vertices:
                    for adjacentes in self.estrutura[v2]:
                        if v1 == adjacentes:
                            if v2 == v1:  # se o vertice for adjacente a ele mesmo nao pode ser feita a ordenação topologica
                                print(
                                    "Devido ao vértice ser adjacente a ele mesmo, a ordenação topológica não pode ser feita.")
                            else:
                                vertices[v1] += 1  # incrementa o grau de entrada

            for v in lista_vertices:
                if vertices[v] == 0:  # procura por algum vertice de grau nulo
                    ordem.append(v)  # adiciona na lista da ordem topologica
                    lista_vertices.remove(v)  # remove da lista de vertices restantes
                    vertices.pop(v)  # remove da relacao de graus
                    removeu = True

            # caso entre no while e não remova nenhum vertice significa que nao existem vertices de grau nulo
            if not removeu:
                print("O grafo precisa ser aciclico para efetuar a ordenação topológica, tente com outro grafo. ")
                return 0

        print("Ordem topológica: ")
        for i in ordem:
            print(i, " ", end="")

    def menu(self):

        acabou = False

        while not acabou:

            print("")
            print("###################################")
            print("#     Menu de grafo orientado     #")
            print("###################################")
            print("#Escolha uma das opções a seguir: #")
            print("# 1. Adicionar vértice ao grafo   #")
            print("# 2. Remover vértice do grafo     #")
            print("# 3. Imprimir grafo               #")
            print("# 4. Reiniciar grafo              #")
            print("# 5. Aplicar ordenação topológica #")
            print("# 0. Voltar ao menu principal     #")
            print("###################################")
            print("")
            opt = input(":")

            if opt == "1":
                Arestas = []
                vertice = input("Entre com o nome do vértice: ")
                sair = False
                for i in go.estrutura:
                    if i == vertice:
                        print("O grafo já possui um vértice com este nome, tente outro.")
                        sair = True
                if not sair:
                    print("O vértice", vertice, "possui algum adjacente? s/n")
                    opt = input("")
                    while opt == "s":
                        maisdeuma = False
                        tem = False
                        adj = input("Entre com o vertice adjacente: ")
                        for i in go.estrutura:
                            if i == adj:
                                tem = True
                        for k in Arestas:  # caso tente adicionar o mesmo adjacente mais de uma vez
                            if adj == k:
                                tem = False
                                maisdeuma = True
                        if tem:
                            Arestas.append(adj)
                            tem = False
                        else:
                            if maisdeuma == False:
                                print(
                                    "O vértice adjacente escolhido não pode ser adicionado pois não se encontra no grafo.")
                            else:
                                print("O vértice adjacente que você escolheu já é adjacente ao vértice, tente outro.")
                        print("O vértice", vertice, "possui mais algum adjacente? s/n")
                        opt = input("")
                    go.add_vertice(vertice, Arestas)
                    print("O vértice", vertice, "foi adicionado com sucesso.")

            elif opt == "2":
                vertice = input("Entre com o nome do vértice: ")
                go.remove_vertice(vertice)
                print("O vértice", vertice, "foi removido com sucesso.")

            elif opt == "3":
                go.imprime_grafo()

            elif opt == "4":
                go.estrutura.clear()
                print("O grafo foi esvaziado.")

            elif opt == "5":
                go.ordenacao_topologica()

            elif opt == "0":
                break

            else:
                print("Opção inválida. Para selecionar uma opção do menu utilize o respectivo número.")


#######################################################################################################################

class Grafo:
    # Inicializei um grafo para facilitar os testes, caso queira pode fazer um do zero pelo menu de opções
    def __init__(self):
        self.estrutura = {"v1": ["v2", "v4"],
                          "v2": ["v1", "v3"],
                          "v3": ["v2", "v4", "v6"],
                          "v4": ["v1", "v3", "v5", "v7"],
                          "v5": ["v4", "v6", "v9"],
                          "v6": ["v3", "v5", "v9"],
                          "v7": ["v4", "v8"],
                          "v8": ["v7", "v9"],
                          "v9": ["v5", "v6", "v8"]
                          }

    def add_vertice(self, v, arestas):
        # adiciona um vértice ao grafo
        self.estrutura[v] = []

        for i in range(len(arestas)):
            self.estrutura[v].append(arestas[i])  # adiciona as arestas que contem o novo vértice ao grafo
            # A[] é uma lista formatada das arestas, contém apenas os vértices com os quais o vértice v se conecta

        for i in self.estrutura:
            if i != v:
                for j in range(len(arestas)):
                    if i == arestas[j]:
                        self.estrutura[i].append(v)
            else:
                break

    def remove_vertice(self, vertice):
        try:
            for i in self.estrutura[vertice]:
                self.estrutura[i].remove(vertice)
            self.estrutura.pop(vertice)
        except KeyError:
            print("Não foi possível remover o vértice", vertice, ", pois ele não se encontra no grafo.")

    def imprime_grafo(self):
        if len(self.estrutura) > 0:
            for i in self.estrutura:
                print("[", i, "] -> [ ", end="")
                for j in range(len(self.estrutura[i])):
                    print(self.estrutura[i][j], end="")
                    if j < len(self.estrutura[i]) - 1:
                        print(end=", ")
                    else:
                        print(end="")
                print(" ]")
        else:
            print("O grafo se encontra vazio.")

    def get_adjacentes(self, vertice):
        for i in self.estrutura:
            if i == vertice:
                if self.estrutura[i] == []:
                    print("O vértice não possui adjacentes.")
                return self.estrutura[i]
        print("O vértice escolhido não se encontra no grafo.")

    def eh_regular(self):
        p = True
        aux = 0
        for i in self.estrutura:
            k = len(self.estrutura[i])
            if p:  # se for a primeira iteração
                aux = k  # seta o auxiliar com o mesmo valor de k
                p = False
            else:  # caso contrário faz a comparação normalmente pois ele ja foi setado
                if k != aux:  # checa se todos os vértices tem a mesma quantidade de adjacentes
                    return False
        return True

    def eh_completo(self):
        for i in self.estrutura:
            for j in self.estrutura:
                if i != j:
                    if j not in self.estrutura[i]:
                        return False
        return True

    def busca_em_largura(self, vertice, raiz):
        fila = [raiz]  # coloca no fim da fila
        visitados = [raiz]  # marca o vertice como visitado
        while fila:
            v = fila[0]
            fila.pop(0)
            if vertice == v:
                return True
            for adj in self.estrutura[v]:
                if adj not in visitados:
                    visitados.append(adj)
                    fila.append(adj)
        return False

    def eh_conexo(self):
        for i in self.estrutura:
            for j in self.estrutura:
                if j not in self.estrutura[i]:
                    if not self.busca_em_largura(j, i):
                        return False
        return True

    def primeiro_dijskra(self, vertice):

        # parte que inicializa a tabela de busca de dijkstra
        inf = math.inf

        path = {}
        dist = {}

        # seta a distância da raiz para 0 e o resto para infinito
        for v in self.estrutura:
            if v == vertice:
                dist[v] = 0
            else:
                dist[v] = inf
            path[v] = "-"

        # começa BFS
        fila = [vertice]
        visitados = [vertice]
        while fila:
            v = fila[0]
            fila.pop(0)
            for adj in self.estrutura[v]:
                if dist[v] + 1 < dist[adj]:
                    path[adj] = v
                    dist[adj] = dist[v] + 1

            menor_dist = inf
            entrou = False

            for vaux in self.estrutura:
                if vaux not in visitados:
                    if dist[vaux] < menor_dist:
                        menor_dist = dist[vaux]
                        prox_visitado = vaux
                        entrou = True
            if entrou:
                visitados.append(prox_visitado)
                fila.append(prox_visitado)

        # imprime a tabela de path/distância
        print("#Tabela em função do vértice: ", vertice)
        print("  V    path    dist  ")
        for v in self.estrutura:
            print(" ", v, "   ", path[v], "   ", dist[v])

        print("")
        print("V      caminho")
        # imprime os caminhos de cada vértice
        for v in self.estrutura:
            print(v, "  ", end="")
            p = path[v]
            first = True
            while p != "-":
                if first:
                    first = False
                else:
                    print(" <- ", end="")
                print(p, end="")
                p = path[p]
            print(end="\n")

    def segundo_dijskra(self, vertice1, vertice2):

        # parte que inicializa a tabela de busca de dijkstra
        inf = math.inf

        path = {}
        dist = {}

        # seta a distância da raiz para 0 e o resto para infinito
        for v in self.estrutura:
            if v == vertice1:
                dist[v] = 0
            else:
                dist[v] = inf
            path[v] = "-"

        # começa BFS
        fila = [vertice1]
        visitados = [vertice1]
        while fila:
            v = fila[0]
            fila.pop(0)
            for adj in self.estrutura[v]:
                if dist[v] + 1 < dist[adj]:
                    path[adj] = v
                    dist[adj] = dist[v] + 1

            menor_dist = inf
            entrou = False

            for vaux in self.estrutura:
                if vaux not in visitados:
                    if dist[vaux] < menor_dist:
                        menor_dist = dist[vaux]
                        prox_visitado = vaux
                        entrou = True
            if entrou:
                visitados.append(prox_visitado)
                fila.append(prox_visitado)

            # verifica se o menor caminho ja foi calculado para o vertice2
            if vertice2 in visitados:
                break

        p = path[vertice2]
        first = True
        print(vertice2, "<- ", end="")
        while p != "-":
            if first:
                first = False
            else:
                print(" <- ", end="")
            print(p, end="")
            p = path[p]
        print(end="\n")

    # aplica coloração ao grafo
    def colorir(self):
        relacao = [[]]  # vetor que armazena a relacao de vertices/cores

        #  as cores sao os indices do vetor principal, uma lista de vertices é associada para cada cor

        for vertice in self.estrutura:
            if relacao == [[]]:  # se é o primeiro coloca na primeira cor
                relacao[0].append(vertice)
                print("Inicializou")
            else:
                adicionou = False
                for cor in relacao:  # percorre os vetores de cores existentes
                    for v in cor:  # percorre o vetor de vertices associados a cor
                        ehAdj = False
                        for adj in self.estrutura[v]:  # percorre os adjacentes do vertice atual
                            if vertice == adj:  # verifica se o vertice e adjacente ao vertice da cor em questao
                                ehAdj = True
                                break
                        if ehAdj:
                            break
                    if not ehAdj:
                        cor.append(vertice)  # se o vertice n e adjacente a nenhum vertice da cor entao ele recebe a cor
                        adicionou = True
                        break

                # caso acabem as cores e o vertice ainda n foi adicionado cria uma cor nova e insere nela

                if not adicionou:
                    novacor = []
                    relacao.append(novacor)
                    novacor.append(vertice)

        corIndex = 0
        for cor in relacao:
            print("Cor ", corIndex, " : [ ", end="")
            corIndex += 1
            for v in cor:
                print(v, " ", end="")
            print("]")


####################
# PROGRAMA PRINCIPAL#
####################

# terminou = False
g = Grafo()
go = GrafoOrientado()

#  verificação para usar o grafo orientado ou simples, caso escolha parte 1 usará o simples e seus métodos
#  caso contrário usará o orientado e os métodos implementados na segunda parte da atividade de implementação

terminou = False

while not terminou:

    print("")
    print("###################################")
    print("#   Bem vindo ao menu principal   #")
    print("###################################")
    print("#Escolha uma das opções a seguir: #")
    print("# 1. Adicionar vértice ao grafo   #")
    print("# 2. Remover vértice do grafo     #")
    print("# 3. Imprimir grafo               #")
    print("# 4. Reiniciar grafo              #")
    print("# 5. Mostrar adjacentes           #")
    print("# 6. Dizer se o grafo é regular   #")
    print("# 7. Dizer se o grafo é completo  #")
    print("# 8. Dizer se o grafo é conexo    #")
    print("# 9. Menor caminho primeira forma #")
    print("# 10.Menor caminho segunda forma  #")
    print("# 11.Aplicar coloração no grafo   #")
    print("# 12.Aplicar ordenação topológica #")
    print("# 0. Encerrar programa            #")
    print("###################################")
    print("")
    opt = input(":")

    if opt == "1":
        Arestas = []
        vertice = input("Entre com o nome do vértice: ")
        sair = False
        for i in g.estrutura:
            if i == vertice:
                print("O grafo já possui um vértice com este nome, tente outro.")
                sair = True
        if not sair:
            print("O vértice", vertice, "possui algum adjacente? s/n")
            opt = input("")
            while opt == "s":
                tem = False
                adj = input("Entre com o vertice adjacente: ")
                for i in g.estrutura:
                    if i == adj:
                        tem = True
                if tem:
                    Arestas.append(adj)
                    tem = False
                else:
                    print("O vértice adjacente escolhido não pode ser adicionado pois não se encontra no grafo.")
                print("O vértice", vertice, "possui mais algum adjacente? s/n")
                opt = input("")
            g.add_vertice(vertice, Arestas)
            print("O vértice", vertice, "foi adicionado com sucesso.")

    elif opt == "2":
        vertice = input("Entre com o nome do vértice: ")
        g.remove_vertice(vertice)
        print("O vértice", vertice, "foi removido com sucesso.")

    elif opt == "3":
        g.imprime_grafo()

    elif opt == "4":
        g.estrutura.clear()
        print("O grafo foi esvaziado.")

    elif opt == "5":
        vertice = input("Entre com o nome do vértice: ")
        Adjacentes = g.get_adjacentes(vertice)
        for i in Adjacentes:
            print(i, end=" ")
        print("")
    elif opt == "6":
        if g.eh_regular():
            print("O grafo é regular.")
        else:
            print("O grafo não é regular.")

    elif opt == "7":
        if g.eh_completo():
            print("O grafo é completo.")
        else:
            print("O grafo não é completo.")

    elif opt == "8":
        if g.eh_conexo():
            print("O grafo é conexo.")
        else:
            print("O grafo não é conexo.")

    elif opt == "9":
        g.primeiro_dijskra(input("Entre com o nome do vértice que deseja calcular a distancia para os outros: "))

    elif opt == "10":
        g.segundo_dijskra(input("Entre com o vértice de origem: "), input("Entre com o vértice de destino: "))

    elif opt == "11":
        g.colorir()

    elif opt == "12":
        print("")
        print("Para aplicar a ordenação topológica um grafo orientado vai ser inicializado.")
        print("Um novo menu será disponibilizado para que faça as operações necessárias.")
        go.menu()

    elif opt == "0":
        print("Obrigado por usar o programa!")
        terminou = True

    else:
        print("Opção inválida. Para selecionar uma opção do menu utilize o respectivo número.")
