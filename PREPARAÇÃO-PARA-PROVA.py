# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 09:03:36 2019

@author: lucas
"""
#EX1
a=int(input("Digite um valor:"))

b=a+2*3%5

print(a,b)

#ex2

C=float(input('digite a temperatura em Celsius para conversão: '))
F=(9/5)*C+32
print(F)

#ex3
#n1=float(input('Digite o número de vezes para a sequência: '))
#1+n1
#while 1<n1:
#    print(n1)

#ex4
num = int(input("Digite um inteiro: "))

for num in range(0+1,num+1):
    print(num, end=' ')