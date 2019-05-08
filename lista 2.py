# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
#exercício 1
g=float(input('Qual o valor da gasolina? '))
a=float(input('Qual o valor do álcool? '))
if g/a < 0.7:
    print('Gasolina')
else:
    print('Álcool')
    if g/a > 0.7:
        print('Tanto faz')


#exercício 2
n1=float(input('Digite um número: '))
n2=float(input('Digite outro número: '))
if n1 > n2:
    print('o número {} é o maior'.format(n1))
else:
    if n2 > n1:
      print('o número {} é o maior'.format(n2))

#exercício 3
n1=float(input('Digite um número: '))
n2=float(input('Digite outro número: '))
n3=float(input('Digite mais um número: '))
if n1>n2>n3:
    print('o número {} é o maior'.format(n1))
else:
    if n2>n1>n3:
        print('o número {} é o maior'.format(n2))
    elif n3>n2>n1:
        print('o número {} é o maior'.format(n3))

#exercício 4
n1=float(int(input('Digite um número para a divisão: ')))
n2=float(input('Digite outro número para a divisão: '))
n3=n1/n2
#n1=dividendo
#n2=divisor
if n2==0:
    print('Favor, digite número maior que 0')
print(n3)