'''Faça um programa de calculadora simples com as seguintes operações
possíveis: adição, subtração, multiplicação e divisão. O programa inicia
apresentando ao usuário um menu de opções como mostrado abaixo:

**********************************************************************
* Calculadora. Opções possíveis:
* 1. Adição
* 2. Subtração
* 3. Multiplicação
* 4. Divisão
* 5. Exponenciação
* 6. Raiz quadrada
* 7. Porcentagem
* 8. Resto da divisão
* 9. Divisão de inteiro
* 0. Sair do programa
*********************************************************************
Informe a opção desejada:


** Instruções**

- A opção informada é então analisada e o programa executa a operação apropriada,
se a opção for inválida, informe ao usuário e peça a ele para entrar com uma
opção válida.
- Após a execução da operação o programa volta a apresentar o menu inicial até
que o usuário encerre o programa com a opção 0.
- Utilize funções para realizar os cálculos, inclusive para o menu.
- Utilize a estrutura de comparação que melhor se adeque ao problema.
- Mantenha o código fonte organizado.
- Não será aceito utilização de bibliotecas.'''

#Imprime o menu
def menu():

    print('-' * 40)
    print("CALCULADORA".center(40))
    print('-' * 40)
    print("Escolha uma das opções a baixo:".center(40))
    print('''
    * [1] Adição
    * [2] Subtração
    * [3] Multiplicação
    * [4] Divisão
    * [5] Exponenciação
    * [6] Raiz quadrada
    * [7] Porcentagem
    * [8] Resto da divisão
    * [9] Divisão de inteiro
    * [0] Sair do programa''')
    print('-' * 40)

#Tranforma descimais em inteiros caso tenha valor decimal 0
def decimal_em_inteiro(decimal):
    if int(decimal) == decimal:
        resu = int(decimal)
    else:
        resu = round(decimal, 2)
    
    return resu

#Todas as Operações para dar o valor a resu(resultado) e operacao
def resultado_operação(opcao, num1, num2=0):

    try:
        #Todas as Operações para dar o valor a resu(resultado) e operacao
        match opcao:

            #Adição
            case 1:
                operacao = "A adição"
                resu = num1 + num2

            #Subtração
            case 2:
                operacao = "A subtração"
                resu = num1 - num2

            #Multiplicação
            case 3:
                operacao = "A multiplicação"
                resu = num1 * num2
            
            #Divisão
            case 4:
                operacao = "A divisão"
                resu = num1 / num2

            #Exponenciação    
            case 5:
                operacao = "A exponenciação"
                resu = num1 ** num2

            #Raiz quadrada
            case 6:
                operacao = "A raiz"
                resu = num1 ** (1/2)

            #Porcentagem
            case 7:
                operacao = "A porcentagem"
                resu = num1 * (num2 * 0.01)
            
            #Resto da divisão
            case 8:
                operacao = "O resto da divisão"
                resu = num1 % num2

            #Divisão inteira
            case 9:
                operacao = "A divisão inteira"
                resu = num1 // num2
        
        resultado = decimal_em_inteiro(resu)

        #Adicionando '%'
        if opcao == 7:
            resultado = str(resultado) + '%'
        
        return resultado, operacao
    
    except(ZeroDivisionError):
        print('-' * 40)
        print("ERRO! É impossivel dividir por zero.")

#Criando variavel de controle
opcao = ''
resultado = []

#Main principal
while True:
    
    #Imprime o menu, input de controle
    menu()

    #Recebendo Opção
    try:
        opcao = int(input("Qual Opção?: "))
        print('-' * 40)

    #Opção invalida
    except:
        print('-' * 40)
        print("Opção invalida! Tente de novo.")
        continue

    #Validando a opcao
    if opcao > 0 and opcao <= 9:

        try:
            #Valores da operação
            num1 = float(input("Informe um número: "))

            #Caso seja raiz quadrada não perguntara o segundo valor
            if opcao != 6:
                num2 = float(input("Informe um segundo número: "))
            else:
                num2 = 2

            #Todas as Operações para dar o valor a resu(resultado) e operacao
            resultado = resultado_operação(opcao, num1, num2)

            #Tranforma descimais em inteiros caso tenha valor decimal 0
            num1 = decimal_em_inteiro(num1)
            num2 = decimal_em_inteiro(num2)


            print('-' * 40)
            print(f"{resultado[1]} entre {num1} e {num2} tem o resulatado: {resultado[0]}")

        except:
            print('-' * 40)
            print("Valor invalido! Tente de novo!")
            continue

    #Opção de saida
    elif opcao == 0:
        print("Saindo do programa...")
        print("Fim! Volte sempre!")
        break
    
    else:
        print("Opção invalida! Tente de novo.")