# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 18:25:28 2019

@author: lucas
"""

#Lista 4

#exercício 1

f1=input('Digite uma frase para ser feita as variações: ')
print(len(f1))
print(f1.split())
print(f1[::-1])
print(f1.upper())
print(f1.lower())

#exercício 2

f2=input('Digite a frase para a verificação: ')

if f2==f2[::-1]:
    print(f2, 'é um palíndromo')
else:
    print(f2, 'não é um palíndromo')

#exercício 3

f3=str(input("Digite uma frase para contar as vogais: "))
print(f3.count('a'))
print(f3.count('e'))
print(f3.count('i'))
print(f3.count('o'))
print(f3.count('u'))

#exercício 4
f4=input('Digite a frase: ')
c1=input('Digite o caractere que você quer saber quantas vezes repete: ')
palavra=f4
print(palavra.count(c1))

#exercício 5
f5 = input('Digite uma palavra para a repetição: ')
f6 = ''
a = 0
for i, in f5:
    f6 += i*2
    
print(f6)

#exercício 6
frase = input('Sua frase: ')
frase2 = ''
c = 0
vogais = 'aeiou'
for i in frase:
    frase2 += i
    if i in vogais:
        frase2 += i * 2
print(frase2)

#exercício 7
palavra = input('Digite algo: ').lower()
palavra2 = ''
p1 = int(0)
p2 = int(2)
cont = int(0)

while cont < len(palavra):
    palavra2 += palavra[p1:p2][::-1]
    p1 += 2
    p2 += 2
    cont += 2

print(palavra2)

#exercício 8
palavra1 = input('Palavra 1: ').lower()
palavra2 = input('Palavra 2: ').lower()
res = ''

for i in palavra1:
    if i in palavra2:
        res += i + ", "
print(res)

#exercício 9
premio1 = input('Digite o número do Primeiro prêmio: ')
premio2 = input('Digite o número do Segundo prêmio: ')
print(f'O número sorteado é {premio1[-3:]}{premio2[-3:]}')