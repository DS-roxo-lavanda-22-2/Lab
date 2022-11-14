#Calculadora em Python 
import os
import Dif
import Div
import Prod
import Soma

def Leitura():
    print('Qual será o primeiro número?');
    n1 = float(input('Número: '));
    print('Qual será o segundo número?');        
    n2 = float(input('Número: '));
    print('Qual será a operação entre eles?(Escreva somente o sinal da operação)\nOperações: Adição(+), Subtração(-), Multiplicação(*) e Divisão(/)');
    op = input('Operação: ')
    if op == '+':
        Resultado = Soma.Som(n1, n2);
        print('{} + {} = {}'.format(n1, n2, Resultado))
    elif op == '-':
        Resultado = Dif.Di(n1, n2);
        print('{} - {} = {}'.format(n1, n2, Resultado))
    elif op == '*':
        Resultado = Prod.Pr(n1, n2);
        print('{} * {} = {}'. format(n1, n2, Resultado)) 
    elif op == '/':
        if n2 == 0:
            print('Não é possível dividir por 0')
        else: 
         Resultado = Div.Div(n1, n2);
         print('{} / {} = {}'.format(n1, n2, Resultado))
    anwser = str(input("Deseja fazer mais alguma conta?\nResposta: "))
    anwser = anwser.upper();
    if anwser == 'SIM':
        os.system('cls' if os.name == 'nt' else 'clear')
        ola();
    else: 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Fim");
    def ola():
        print('Calculadora de console em Python.');
        print('Operações realizavéis:\nAdição, Subttração, Multiplicação e Divisão')
        Leitura();
    ola();
#Menuzin pra Loop