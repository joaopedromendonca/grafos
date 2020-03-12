class Grafo:
    def __init__(self):
        self.estrutura = {}

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
                    if not self.busca_em_largura(j,i):
                        return False
        return True


####################
#PROGRAMA PRINCIPAL#
####################

terminou = False
g = Grafo()

print("Bem vindo ao menu de construção de grafo")

while not terminou:

    print("##################################")
    print("#Escolha uma das opções a seguir:#")
    print("# 1. Adicionar vértice ao grafo  #")
    print("# 2. Remover vértice do grafo    #")
    print("# 3. Imprimir grafo              #")
    print("# 4. Reiniciar grafo             #")
    print("# 5. Mostrar adjacentes          #")
    print("# 6. Dizer se o grafo é regular  #")
    print("# 7. Dizer se o grafo é completo #")
    print("# 8. Dizer se o grafo é conexo   #")
    print("# 0. Encerrar programa           #")
    print("##################################")
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
            print("O vértice", vertice,"possui algum adjacente? s/n")
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

    elif opt == "0":
        print("Obrigado por usar o programa!")
        terminou = True

    else:
        print("Opção inválida. Para selecionar uma opção do menu utilize o respectivo número.")