X = float(input('Digite o primeiro número: '))
Y = float(input('Digite o segundo número: '))
operacoes = ['soma', 'subtração', 'divisão', 'multiplicação']
print('''Operações:
[0] Soma
[1] Subtração
[2] Divisão
[3] Multiplicação ''')
escolha = int(input('Digite o número da operação que deseja fazer: '))
if escolha == 0:
    print('A operação escolhida foi de {}'.format(operacoes[escolha]))
    som = X + Y
    print('{} + {} = {}'.format(X, Y, som))
elif escolha == 1:
    print('A operação escolhida foi de {}'.format(operacoes[escolha]))
    sub = X - Y
    print('{} - {} = {}'.format(X, Y, sub))
elif escolha == 2:
    print('A operação escolhida foi de {}'.format(operacoes[escolha]))
    div = X / Y
    print('{} / {} = {}'.format(X, Y, div))
elif escolha == 3:
    print('A operação escolhida foi de {}'.format(operacoes[escolha]))
    mul = X * Y
    print('{} * {} = {}'.format(X, Y, mul))
else:
    print('Operação inválida!')