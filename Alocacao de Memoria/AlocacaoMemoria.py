from random import *  # importação da biblioteca random para gerar números aleatórios
import time  # importação da biblioteca time para a contagem de tempo

matriz = []  # matriz global criada esperando o append de seus elementos


def menu():  # função de menu principal
    print('=' * 20)
    print('Alocação de memória')  # título
    print('=' * 20, "\n")
    print('Para alocar memória, digite 0 \nPara desalocar memória, digite 1 \nPara entrar no modo de teste, digite 2 \nPara visualizar o gráfico da Memória, digite 3 \nVisualizar matriz normalmente = 4')
    n = int(input("\nO que deseja fazer? "))  # número da ação que o usuário deseja realizar
    if n == 0:
        m = int(input("\nFirst Fit = 1   Best Fit = 2   Worst Fit = 3\nQue estratégia de alocação deseja utilizar? "))
        if m == 1:
            num = int(input("Insira o tamanho da alocação que deseja fazer: "))
            firstFit(num, l, c, matriz, 0)  # chama a função FirstFit assim que ele for selecionado, usando o tamanho da alocação, que ele pede logo acima, e no número da ação no menu
        elif m == 2:
            num2 = int(input("Insira o tamanho da alocação que deseja fazer: "))
            if num2 <= 0:  # verifica se o tamanho da alocaçao é valido
                print("Valor inválido para alocar")
                menu()  # retorna ao menu
            bestFit(num2, l, c, matriz, 0)   # Chama a função BestFit com base no tamanho da alocação acima e no número da ação no menu
        elif m == 3:
            num3 = int(input("Insira o tamanho da alocação que deseja fazer: "))
            worstFit(num3, l, c, matriz, 0)  # Chama a função WorstFit com base no tamanho da alocação acima e no número da ação no menu
        else:
            print("Valor Inválido")
            menu()
    elif n == 1:
        var1 = int(input("Qual o tamanho da desalocação? "))  # Inserção do tamanho da alocação, para determinar se são necessárias uma, ou mais coordenadas
        if var1 <= 0:  # Critério de erro
            print("Tamanho de Alocação Inválido")
            menu()
        if var1 == 1:
            cord1 = int(input("Linha do elemento: "))
            if cord1 < 0 or cord1 > (l - 1):  # Estrutura de verificação da coordenada
                print("Linha inválida")
                menu()
            cord2 = int(input("Coluna do elemento: "))
            if cord2 < 0 or cord2 > (c - 1):  # Estrutura de verificação da coordenada
                print("Linha Inválida")
                menu()
            desalocacao(cord1, cord2, 0, 0, var1, l, c,
                        matriz)  # Chama-se a função de desalocação com os dados abaixo passados como parâmetros
        else:
            cord1 = int(input("Linha do primeiro elemento: "))
            if cord1 < 0 or cord1 > (l - 1):
                print("Linha inválida")
                menu()
            cord2 = int(input("Coluna do primeiro elemento: "))
            if cord2 < 0 or cord2 > (c - 1):
                print("Coluna Inválida")
                menu()
            cord3 = int(input("Linha do último elemento: "))
            if cord3 < 0 or cord3 > (l - 1):
                print("Linha inválida")
                menu()
            cord4 = int(input("Coluna do último elemento: "))
            if cord4 < 0 or cord4 > (c - 1):
                print("Coluna Inválida")
                menu()
            if cord1 == cord3 and cord2 > cord4:  # Estrutura de verificação da coordenada
                print("Coordenadas inválidas")
                menu()
            if cord1 > cord3:  # Estrutura de verificação da coordenada
                print("Coordenadas inválidas")
                menu()
            # Chama a função de desalocação com as coordenadas iniciais e finais para desalocar
            desalocacao(cord1, cord2, cord3, cord4, var1, l, c, matriz)
    elif n == 3:
        visu()  # Chama a função de vizualização de matriz gráfica
    elif n == 2:
        teste(50, 50)  # Chama a função do Modo de teste que cria uma matriz 5000x5000
    
    elif n == 4:  # Vizualização da matriz normalmente, sem ser graficamente
        for i in matriz:  # Passa por cada linha da matriz, imprimindo todas as linhas
            print(i)
        menu()  # Retorna-se ao menu principal


def criaMatriz(l, c):  # Função criaMatriz
    for i in range(l):  # Cria linhas na matriz com base no número de linhas
        linha = []
        for j in range(c):  # Adiciona a quantidade de colunas inserida pelo usuário em cada linha
            linha.append(0)  # Preenchimento da matriz com espaços vazios representados por '0'
        matriz.append(linha)  # Inserção das linhas
    print("\nMatriz criada com sucesso!\n")
    menu()


def firstFit(num, l, c, matriz, diff): # função de alocação de memória no estilo firstFit
    if num <= 0: # verifica se o tamanho da alocação está valido para a alocação
        print("Valor inválido para alocação")
        menu()

    count0 = 0 # contador de zeros 1
    count0_2 = 0 # contador de zeros 2
    count1 = 0 # contador de um n.1
    count1_2 = 0 # contador de um n.2
    for x in range(l):
        for y in range(c): # Laço que passa por todos os elementos da matriz
            if matriz[x][y] == 0: # Verifica se o valor é 0 para começar a contagem do espaço
                count0 += 1 # Adiciona 1 à contagem
                if count0 == num: # verifica se a contagem é igual ao tamanho desejado para iniciar a alocação
                    if count1 == 0: # caso essa condição seja real, não haviam "1" no começo da matriz, por isso o count1 == 0
                        for x in range(l): # repassa na matriz desde o começo da matriz alocando até dar o tamanho
                            for y in range(c):
                                matriz[x][y] = 1 # Sempre que houver: "matriz[x][y] = 1", significa que uma posição na matriz está sendo substituída por 1
                                count0_2 += 1 # adiciona 1 na segunda contagem de 0 até que ela seja igual a primeira
                                if count0_2 == count0:
                                    if diff == 1: # condição que verifica se está no modo de teste
                                        return 1
                                    print("\nSucesso!")
                                    menu()
                    for x in range(l): # caso count1 != 0, ele repassa pela matriz contando novamente os "1"
                        for y in range(c): # Assim que a primeira contagem for igual a segunda, o y seguinte será onde se inicia a alocação
                            if matriz[x][y] == 1: # Verifica os "1" para realizar a contagem
                                count1_2 += 1 # Adiciona uma unidade ao contador
                                if count1 == count1_2: # caso a contagem 1 serja igual a 2, começa a substituir
                                    if y == (c - 1) and x != (l - 1): # Verifica se está no ultimo dígito de qualquer linha, para começar a substituição na linha seguinte desde o começo
                                        for x in range(x + 1, l):
                                            for y in range(c): # A partir de uma certa linha adiante, substitui-se '0' por '1' fazendo uma segunda contagem de '0'
                                                matriz[x][y] = 1 # Substitui um elemento da matriz por '1'
                                                count0_2 += 1 # Adiciona uma unidade ao contador
                                                if count0_2 == count0: # assim que a segunda contagem de 0 estiver igual a primeira, a alocação termina
                                                    if diff == 1: # Verifica se está no modo de teste
                                                        return 1
                                                    print("\nSucesso!")
                                                    menu()
                                    elif x == (l - 1): # Caso esteja na última linha, substitui o resto da linha até alcançar o tamanho da alocação
                                        for y in range(y + 1, c): # laço a partir do último "1"
                                            matriz[x][y] = 1 # Substitui um elemento da matriz por '1'
                                            count0_2 += 1 # Faz a contagem de substituições feitas
                                            if count0_2 == count0: # quando ela for igual a primeira contagem de zeros, a alocação termina
                                                if diff == 1: # Verifica se está no modo de teste
                                                    return 1
                                                print("\nSucesso!")
                                                menu()
                                    else:
                                        for y in range(y + 1, c): # faz o laço para substituir o resto da linha que se encontra
                                            matriz[x][y] = 1 # Substitui um elemento da matriz por '1'
                                            count0_2 += 1 # Adiciona uma unidade ao contador
                                            if count0_2 == count0: # faz a contagem para verificar se o tamanho da alocação é suprido ate o fim da linha
                                                if diff == 1: # verifica se está no modo de teste
                                                    return 1
                                                print("\nSucesso!")
                                                menu()
                                        if x + 1 == l - 1: # caso a proxima linha seja a ultima e ainda não foi alocado o solicitado
                                            for y in range(c):
                                                matriz[l - 1][y] = 1 # Aloca os termos da ultima linha enquanto o tamanho não foi alcançado
                                                count0_2 += 1 # Adiciona uma unidade ao contador
                                                if count0_2 == count0: #assim que alcançado o tamanho requisitado, a alocação para
                                                    if diff == 1: # Verifica se está no modo de teste
                                                        return 1
                                                    print("\nSucesso!")
                                                    menu()
                                        else: # caso a próxima linha não seja a última
                                            for x in range(x + 1, l):
                                                for y in range(c): # a partir da próxima linha, serão alocados todos os espaços até que o tamanho desejado seja alcançado
                                                    matriz[x][y] = 1 # faz a alocação
                                                    count0_2 += 1 # contagem para saber quando acabar
                                                    if count0_2 == count0: # condição para acabar de alocar
                                                        if diff == 1: # verifica se esta no modo de teste
                                                            return 1
                                                        print("\nSucesso!")
                                                        menu()
            if x == l - 1 and y == c - 1 and count0 < num: # Condição suportada quando não é encontrado espaço na matriz
                if diff == 1: # verifica se esta no modo de teste
                    return 0
                print("Sem espaços disponíveis")
                menu()

            if matriz[x][y] == 1: # Caso o número encontrado na busca inicial seja "1" ele soma a primeira contagem dos "1" e zera a contagem de zeros,
                                  # visto que o tamanho encontrado não foi suficiente
                count1 += 1 # Adiciona mais uma unidade à contagem se existir um '1' na matriz
                count0 = 0
    if count0 < num and diff == 1:
        return 0 # Condição de segurança caso ele saia do laço de repetição


def bestFit(num, l, c, matriz, diff):


    numm = c * l
    for number in range(0, numm):
        # laço que soma ao valor do tamanho do range 0 ao tamanho da matriz; Primeiro busca o tamanho normal requisitado, caso não encontra, o tamanho + 1
        # e assim até o tamanho total da matriz, no caso, linhas * colunas. Assim encontra o menor valor possivel para alocar
        verify = num + number
        count0 = 0 # contador de zeros 1
        count0_2 = 0  # contador de zeros 2
        count1 = 0  # contador de 'uns' 1
        count1_2 = 0  # contador de 'uns' 2
        for x in range(l):  # Loop que varre toda a matriz
            for y in range(c): # loop que varre coluna por coluna
                if matriz[x][y] == 0:  # Condicional que encontra um elemento que seja igual a zero
                    count0 += 1 # Se verdadeiro, a variável count0 adiciona '1' ao seu valor
                    if count1 == 0 and  count0 == c*l:
                        for x in range(l):  # Para cada elemento no alcance das linhas
                            for y in range(c):  # E internamente às linhas, para cada elemento dentro delas
                                matriz[x][y] = 1  # Os elementos selecionados serão substituídos por '1'
                                count0_2 += 1  # A variável count0_2 adiciona '1' ao seu valor
                                if count0_2 == num:
                                    if diff == 1:  # Condição que verifica se está no modo de teste
                                        return 1  # retorna um para a contagem de sucessos e erros diferenciar
                                    print("\nSucesso!")
                                    menu()  # retorna ao menu
                elif matriz[x][y] == 1: # Caso o elemento seja 1, verifica se o tamanho anterior foi suficiente
                    if count0 == verify:  # Se o valor de 'count0' for igual à soma de 'num' e 'number', o espaço é suficiente
                        if num == 1 and y == 0: # Verifica se apenas um espaço será alocado e se ele não esta no começo de uma linha
                            matriz[x-1][c-1] = 1 # Alocação do ultimo termo da linha anterior
                            print("\nSucesso!")
                            menu() # retorna ao menu
                        elif num == 1 and y != 0: # se for um termo qualquer sem ser o primeiro da linha:
                            matriz[x][y-1] = 1  # Alocação  do termo anterior, visto que o atual é um "1"
                            print("\nSucesso!")
                            menu() #volta ao menu
                        for x in range(l):  # Caso count1 for diferente de zero, o programa percorrerá a matriz contando novamente os 'uns'
                            for y in range(c):
                                if matriz[x][y] == 1:  # Identifica índices que sejam iguais a 1
                                    count1_2 += 1  # Se verdadeiro, 'count1_2' recebe mais uma unidade ao seu valor
                                    if count1 == count1_2:  # Se 'count1' e 'count1_2' se igualarem
                                        if y == (c - 1) and x != (l - 1):  # Verifica se y e x forem iguais às posições dos últimos índices
                                            for x in range(x + 1, l):
                                                for y in range(c):
                                                    matriz[x][y] = 1  # Substitui um elemento da matriz por '1'
                                                    count0_2 += 1  # 'Count0_2' tem '1' adicionado ao seu valor
                                                    if count0_2 == num:  # A partir de uma certa linha adiante, substitui-se '0' por '1' fazendo uma segunda contagem de '0'
                                                        if diff == 1:  # Verifica se está no modo de teste
                                                            return 1
                                                        print("\nSucesso!")
                                                        menu()
                                        elif x == (l - 1):
                                            for y in range(y + 1, c):
                                                matriz[x][y] = 1  # Substitui um espaço por '1'
                                                count0_2 += 1  # 'Count0_2' recebe mais uma unidade ao seu valor
                                                if count0_2 == num:  # Se 'count0' e 'count0_2' se igualarem
                                                    if diff == 1:  # Verifica se está no modo teste
                                                        return 1
                                                    print("\nSucesso!")
                                                    menu()
                                        else:
                                            for h in range(y + 1, c):
                                                matriz[x][h] = 1  # Substitui um espaço por '1'
                                                count0_2 += 1  # Adiciona uma unidade ao contador
                                                if count0_2 == num:  # Se 'count0' e 'count0_2' se igualarem
                                                    if diff == 1:  # Verifica se está no modo teste
                                                        return 1
                                                    print("\nSucesso!")
                                                    menu()
                                            if x + 1 == l - 1:
                                                for y in range(c):
                                                    matriz[l - 1][y] = 1  # Substitui um espaço por '1'
                                                    count0_2 += 1  # Adiciona uma unidade ao contador
                                                    if count0_2 == num:  # Se 'count0' e 'count0_2' se igualarem
                                                        if diff == 1:  # Verifica se está no modo teste
                                                            return 1
                                                        print("\nSucesso!")
                                                        menu()
                                            else:
                                                for x in range(x + 1, l):
                                                    for y in range(c):
                                                        matriz[x][y] = 1  # Substitui um espaço por '1'
                                                        count0_2 += 1  # Adiciona uma unidade ao contador
                                                        if count0_2 == num:
                                                            if diff == 1:  # Verifica se está no modo teste
                                                                return 1
                                                            print("\nSucesso!")
                                                            menu()
                    # Caso o número encontrado na busca inicial seja "1" ele soma a primeira contagem dos "1" e zera a contagem de zeros,
                    # visto que o tamanho encontrado não foi suficiente
                    count1 += 1  # Adiciona mais uma unidade à contagem se existir um '1' na matriz
                    count0 = 0  # Reinicia a contagem de zeros
    if count0 < num and diff == 1:  # Condição de segurança caso ele saia do laço de repetição
        return 0


def worstFit(num, l, c, matriz, diff):
    numm = c * l
    if num > numm and diff == 1:
        return 0
    for number in range(numm, -1, -1):
        # Exatamente o contrário do best fit, primeiro ele soma ao tamanho o resultado de linhas * colunas e vai diminuindo até tamanho + 0,
        # de modo a encontrar o maior tamanho possível para fazer a alocação
        count0 = 0  # contador de zeros 1
        count0_2 = 0  # contador de zeros 2
        count1 = 0  # contador de 'uns' 1
        count1_2 = 0  # contador de 'uns' 2
        for x in range(l):  # Varre a matriz inteira à procura de espaços livres
            for y in range(c):  # Procura internamente pela matriz, nas sublistas que são as linhas
                if matriz[x][y] == 0:  # Se houver um espaço vago, representado por '0'
                    count0 += 1  # Adiciona uma unidade ao contador
                    if count0 == (num + number):
                        if count1 == 0:  # Se não houver nenhum '1' na contagem
                            for x in range(l):  # Para cada elemento nas linhas
                                for y in range(c):  # E para cada elemento nas colunas
                                    matriz[x][y] = 1  # Substitui um espaço por '1'
                                    count0_2 += 1  # Adiciona uma unidade ao contador
                                    if count0_2 == num:  # Se a contagem de zeros for igual ao valor de 'num'
                                        if diff == 1:  # Verifica se está no modo teste
                                            return 1
                                        print("\nSucesso!")
                                        menu()
                        for x in range(l):  # Para cada elemento dentro da matriz
                            for y in range(c):
                                if matriz[x][y] == 1:  # Substitui um espaço por '1'
                                    count1_2 += 1  # Adiciona uma unidade ao contador
                                    if count1 == count1_2:  # Se 'count1' e 'count1_2' se igualarem
                                        if y == (c - 1) and x != (l - 1):  # Verifica se y e x forem iguais às posições dos últimos índices
                                            for x in range(x + 1, l):
                                                for y in range(c):
                                                    matriz[x][y] = 1  # Substitui um espaço por '1'
                                                    count0_2 += 1  # Adiciona uma unidade ao contador
                                                    if count0_2 == num:
                                                        if diff == 1:  # Verifica se está no modo teste
                                                            return 1
                                                        print("\nSucesso!")
                                                        menu()
                                        elif x == (l - 1):  # Se 'x' for o último índice
                                            for y in range(y + 1, c):
                                                matriz[x][y] = 1  # Substitui um espaço por '1'
                                                count0_2 += 1  # Adiciona uma unidade ao contador
                                                if count0_2 == num:
                                                    if diff == 1:  # Verifica se está no modo teste
                                                        return 1
                                                    print("\nSucesso!")
                                                    menu()
                                        else:
                                            for y in range(y + 1, c):
                                                matriz[x][y] = 1  # Substitui um espaço por '1'
                                                count0_2 += 1  # Adiciona uma unidade ao contador
                                                if count0_2 == num:
                                                    if diff == 1:  # Verifica se está no modo teste
                                                        return 1
                                                    print("\nSucesso!")
                                                    menu()
                                            if x + 1 == l - 1:
                                                for y in range(c):
                                                    matriz[l - 1][y] = 1  # Substitui um espaço por '1'
                                                    count0_2 += 1  # Adiciona uma unidade ao contador
                                                    if count0_2 == num:
                                                        if diff == 1:  # Verifica se está no modo teste
                                                            return 1
                                                        print("\nSucesso!")
                                                        menu()
                                            else:
                                                for x in range(x + 1, l):
                                                    for y in range(c):
                                                        matriz[x][y] = 1  # Substitui um espaço por '1'
                                                        count0_2 += 1  # Adiciona uma unidade ao contador
                                                        if count0_2 == num:
                                                            if diff == 1:  # Verifica se está no modo teste
                                                                return 1
                                                            print("\nSucesso!")
                                                            menu()
                if matriz[x][y] == 1:
                    # Substitui um espaço por '1'
                    count1 += 1  # Adiciona uma unidade ao contador
                    count0 = 0  # Reinicia a contagem de zeros
    if x == l - 1 and y == c - 1 and count0 < num:  # Caso o número encontrado na busca inicial seja "1" ele soma a primeira contagem dos "1" e zera a contagem de zeros,
         # visto que o tamanho encontrado não foi suficiente
        if diff == 1:  # Verifica se está no modo teste
            return 0
        print("Sem espaços disponíveis")
        menu()


    #if count0 < num and diff == 1:
        #return 0


def desalocacao(l1, c1, l2, c2, var1, l, c, matriz):  # função para desalocar elementos da matriz
    if var1 == 1:  # verifica se o tamanho da desalocação é 1
        for x in range(l):  # passa pelas linhas
            for y in range(c):  # passa pelas colunas
                if x == l1 and y == c1:  # verifica se é a coordenada correta
                    matriz[x][y] = 0  # substitui o valor por 0 (vazio)
                    print("Desalocação concluída")
                    menu()  # Retorna ao menu

    if var1 > (l * c):  # verifica se o tamanho da alocação é menor que a quantidade de elementos da matriz
        print("Tamanho excede o limite")
        menu()  # retorna ao menu
    # Codigo executado quando o tamanho da desalocação inserido é maior que 1 e menor que a quantidade de elementos da matriz
    for x in range(l):  # passa pelas linhas
        for y in range(c):  # Passa por cada coluna
            if x == l1 and y == c1:  # Caso ele ache a coordenada inicial
                if y == (c - 1) and (l - 1) == (x + 1):
                    # verifica se esta na ultima coluna da penultima linha pois
                    # sobra apenas uma linha para desalocar
                    matriz[x][y] = 0  # substitui o valor da coordenada inicial
                    for y in range(c):  # Passa por cada colua
                        matriz[l - 1][y] = 0  # substitui as colunas da ultima linha
                        if x == l2 and y == c2:  # Assim que encontrado o valor final, desalocação é concluida
                            print("\nSucesso!")
                            menu()  # volta ao menu
                if x == (l - 1):  # Caso ja esteja na ultima linha
                    matriz[x][y] = 0  # desaloca o primeiro elemento
                    for y in range(y + 1, c):  # a partir do proximo, ate o fim da linha...
                        matriz[l - 1][y] = 0  # desalocar cada elemento...
                        if x == l2 and y == c2:  # ate que chegue na coordenada final
                            print("\nSucesso!")
                            menu()  # volta ao menu
                matriz[x][y] = 0  # substitui a primeira coordenada
                if y == (c - 1) and (l - 1) != (
                        x + 1):  # caso esteja no ultimo elemento e uma linha que não seja a penultima linha
                    for x in range(x + 1, l):  # a partir da proxima linha ate a ultima
                        for y in range(c):  # em cada coluna
                            matriz[x][y] = 0  # desaloca o elemento
                            if x == l2 and y == c2:  # verifica se chegou a coordenada final
                                print("\nSucesso!")
                                menu()  # Volta ao menu
                # Caso não seja o ultimo elemento da linha
                for y in range(y + 1, c):
                    # substitui a partir do proximo ate o fim da linha
                    matriz[x][y] = 0
                    # caso chegue ao ultimo desejado, para a desalocação
                    if x == l2 and y == c2:
                        print("\nSucesso!")
                        menu()  # volta ao menu
                # Caso não tenha chego o fim da desalocaçõa,
                # continua da proxima linha em diante
                for x in range(x + 1, l):  # a partir da proxima linha...
                    for y in range(c):  # em cada coluna...
                        matriz[x][y] = 0  # desaloca cada elemento
                        if x == l2 and y == c2:  # Finaliza caso chegue na coordenada final
                            print("\nSucesso!")
                            menu()  # Retorna ao menu


def teste(l, c):  # função do modo de teste
    matrizff = []  # Matriz usada no first fit
    for i in range(l):  # cria linhas com base na quantidade desejada
        linha = []
        for j in range(c):  # cria cada uma das colunas com base na quantidade desejada
            linha.append(0)  # adiciona um 0 a cada coluna ate que a linha se complete
        matrizff.append(linha)  # Adiciona a linha na matriz
    counterros = 0  # contador de erros de alocação
    countsucessos = 0  # contador de sucessos de alocação
    alocações = []  # armazena o tamanho das alocações
    start_time = time.time()  # começa a contagem de tempo
    for x in range(500):  #
        # Gera 1 milhão de numeros randomicos no tamanho da matriz e armazena na lista de alocações
        alocation = randint(1, l * c)  # gera o numero aleatorio
        alocações.append(alocation)  # insere na lista de alocações
    for x in alocações:  # Passa por cada elemento de alocação
        resultado = firstFit(x, l, c, matrizff, 1)  # Tenta alocar com a função first fit
        if resultado == 0:  # Caso o valor retornado seja 0, é um erro de alocação a mais
            counterros += 1  # adiciona 1 a contagem de erros
        else:  # Caso o valor retornado seja diferente de 0, a alocação foi um sucesso
            countsucessos += 1  # Adiciona 1 a contagem de sucessos
    # printa todas as variaveis necessárias
    print("=" * 20)
    print("Teste com First Fit")
    print(f"Sucessos:{countsucessos}")  # sucessos
    print(f"Erros:{counterros}")  # erros
    print(f"Tempo decorrido: {time.time() - start_time:.2f}s")  # tempo decorrido
    matrizbf = []  # cria a matriz para realizar o BestFit
    for i in range(l):  # cria linhas com base na quantidade desejada
        linha = []
        for j in range(c):  # cria cada uma das colunas com base na quantidade desejada
            linha.append(0)  # adiciona um 0 a cada coluna ate que a linha se complete
        matrizbf.append(linha)  # Adiciona a linha na matriz
    counterros = 0  # registro de alocações sem sucesso
    countsucessos = 0  # Registro de alocações com sucesso
    start_time = time.time()  # Começa a contagem de tempo
    for k in alocações:  # passa por cada elemento de alocação
        resultado = bestFit(k, l, c, matrizbf, 1)  # Tenta alocar com a função BestFit
        if resultado == 0:  # Caso o valor retornado seja 0, é um erro de alocação a mais
            counterros += 1
            print(counterros)# adiciona 1 a contagem de erros
        else:  # Caso o valor retornado seja diferente de 0, a alocação foi um sucesso
            countsucessos += 1
            # Adiciona 1 a contagem de sucessos
    # printa todas as variaveis necessárias
    print("=" * 20)
    print("Teste com Best Fit")
    print(f"Sucessos:{countsucessos}")  # sucessos
    print(f"Erros:{counterros}")  # Erros
    print(f"Tempo decorrido: {time.time() - start_time:.2f}s")  # Tempo decorrido

    counterros = 0  # Contagem de erros
    countsucessos = 0  # Contagem de sucessos
    matrizwf = []  # Cria a matriz usada no worst Fit
    start_time = time.time()
    for i in range(l):  # cria linhas com base na quantidade desejada
        linha = []
        for j in range(c):  # cria linhas com base na quantidade desejada
            linha.append(0)  # adiciona um 0 a cada coluna ate que a linha se complete
        matrizwf.append(linha)  # Adiciona a linha na matriz
    for x in alocações:  # passa por cada elemento de alocação
        resultado = worstFit(x, l, c, matrizwf, 1)  # Tenta alocar com a função WorstFit
        if resultado == 0:  # Caso o valor retornado seja 0, é um erro de alocação a mais
            counterros += 1  # adiciona 1 a contagem de erros
        else:  # Caso o valor retornado seja diferente de 0, a alocação foi um sucesso
            countsucessos += 1  # Adiciona 1 a contagem de sucessos
    # printa todas as variaveis necessárias
    print("=" * 20)
    print("Teste com Worst Fit")
    print(f"Sucessos:{countsucessos}")  # sucessos
    print(f"Erros:{counterros}")  # Erros
    print(f"Tempo decorrido: {time.time() - start_time:.2f}s")  # Tempo decorrido
    menu()


def visu():  # Função de visualização gráfica da matriz
    print("\nVisualização gráfica:\n")
    for a in range(len(matriz)):  # passa por cada linha da matriz
        linha = ''
        for b in range(len(matriz[0])):  # passa por cada coluna da matriz
            if matriz[a][b] == 0:
                linha = linha + ('|   ')  # Quando o espaço estiver ocupado por '0', a representação gráfica será "vazia"
            else:
                linha = linha + ('| X ')  # Quando o espaço estiver ocupado por '1', a representação gráfica será representada com um "X"
        print(linha + "|")  # Adiciona-se uma barra vertical para fechar a linha
    print("\n")
    menu()  # Retorna o usuário ao menu principal


l = int(input("Insira o número de linhas: "))  # pede o numero de linhas da matriz principal
c = int(input("Insira o número de colunas: "))  # pede o numero de colunas da matriz principal
if l <= 0 or c <= 0:
    raise ValueError("Numero invalido, reinicie o código")

criaMatriz(l, c)  # chama a função que cria a matriz com base no valor inserido
