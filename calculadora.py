from operacoes import *

op = input('Digite a operação desejada (+, -, x ou /): ')
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if op == '+':
    resultado = soma(num1,num2)
if op == '-':
    resultado = sub(num1,num2)
if op.lower() == 'x':
    resultado = mult(num1,num2)
if op == '/':
    resultado = div(num1,num2)

print('O resultado da operação escolhida é: ' + str(resultado))