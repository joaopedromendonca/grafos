# Sistema de recomendação de filmes
Relatório

Atividade de implementação 2 de grafos

Dupla: João Pedro Mendonça Oliveira e Vinícius Oliveira Gouveia

Professor: Adolfo Guimarães

O arquivo a ser executado é o my_rec.py. 
Utilizei a avaliação do gosto dos usuários por gêneros de filme como métrica, classificando em uma estrutura de adjacência todos os usuários (como vértices), com seu grau de compatibilidade (como peso das arestas). 
Todos os métodos utilizados estão no arquivo, utilizei bibliotecas recomendadas pelo professor no exemplo de sistema de recomendação. 
Para testar o programa  quem for executar pode modificar algumas variáveis no final do arquivo, são elas: 
- usuario_id: que determina para qual usuário deverá ser feita a recomendação;
- filme_id: que verifica se um filme deve ser recomendado ao usuário escolhido no usuario_id;
- numero_de_usuarios_proximos: que limita a quantidade de usuário utilizados para recomendar filmes ao usuário escolhido

Seu método vai funcionar da seguinte forma, serão escolhidos n usuários correspondente ao valor dessa variável, os n usuário serão os usuários de maior similaridade com o usuário escolhido no usuario_id, a partir destes usuários serão selecionados filmes que estes usuários avaliaram bem e que correspondem ao perfil do usuario_id. O método imprime_lista_de_filmes() vai imprimir todos os filmes selecionados para serem recomendados ao usuário, por id e nome. Ao executar pela primeira vez será feito o cálculo da similaridade, que pode levar alguns segundos, a função calcula_similaridade(g) e salvar_similaridade(g) podem ser executadas apenas na primeira vez, nas seguintes vezes é possível utilizar a função carregar_similaridade(g) para não ter o trabalho de calcular e esperar novamente, basta comentar as duas primeiras e descomentar a ultima. É possível modificar também as variáveis globais que estou utilizando como métrica, NOTA_BOA, que serve para coletar informações sobre os filmes que foram avaliados muito bem e seus gêneros, NOTA_EXIGENCIA, que serve para filtrar os filmes a serem recomendados pelos usuarios similares, somente filmes com notas acima desta devem ser recomendados ao usuario final, e FATOR_DIV que foi a métrica utilizada para filtrar gêneros que não são os preferidos dos usuários.
