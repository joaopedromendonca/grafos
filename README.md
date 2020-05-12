# grafos
Relatório

Atividade de implementação de grafos

Dupla: João Pedro Mendonça Oliveira e Vinícius Oliveira Gouveia

Professor: Adolfo Guimarães

O arquivo a ser executado é o ImplementacaoGrafo.py
O trabalho foi feito em conjunto por mim ( João Pedro ) e meu colega Vinícius. O arquivo se divide entre os métodos e o programa principal, no qual foi feito um menu de controle das funcionalidades implementadas do grafo. É possível adicionar e remover vértices, imprimir o grafo atual, reiniciar o grafo, mostrar os adjacentes de um vértice do grafo, dizer se o grafo é regular, completo ou conexo, exibir o menor caminho de dijsktra a partir de um vértice para todos os vértices do grafo, ou para um vértice específico.
O projeto foi feito inicialmente em java, até a parte da representação do grafo, porém, após conversarmos decidimos fazer em python, pois é uma linguagem nova para ambos e seria um desafio.

Complemento do relatório referente à parte 2

O arquivo a ser executado é o ImplementacaoGrafosParte2.py que está neste repositório junto ao arquivo da parte 1.

Como foi pedido, escolhemos os métodos de coloração e ordenação topológica, para o primeiro simplesmente adicionei uma função de coloração à classe original do grafo simples, esta função pode ser acessada pelo mesmo menu que havia na parte 1, ele foi atualizado, já para a ordenação topológica, que requer um grafo orientado, criei uma classe de grafo orientado com as funcionalidades: adicionar vertice, remover vertice, imprimir grafo e reiniciar grafo, que são funcionalidades básicas para efetuar os testes. A função referente a ordenação topológica foi adicionada como método desta classe, e um submenu foi implementado para ela, está tudo documentado no código e pode ser intuitivamente acessado ao executar o programa. Para aplicar coloração deve escolher a opção 11 do menu principal, já para aplicar a ordenação topológica deve escolher a opção 12, e em seguida a opção 5 do submenu, assim a ordenação será aplicada para o grafo pré-estabelecido na inicialização. Assim como na parte 1 da implementação, disponibilizei métodos de manipulação do grafo para o caso do usuário querer testar em diferentes grafos, tudo pode ser acessado pelos menus.
