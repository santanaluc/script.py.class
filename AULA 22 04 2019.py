# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 07:58:11 2019

@author: lucas
"""
#Learning List

lista=[1,2,3,"Jose","Fatec",[3,4,5]]
print(lista[0])
print(lista[4])
print(lista[4][3])
print(lista[5])
print(lista[5][1])
lista[3]="Yodão"
for elemento in lista:
    print(elemento, end=" ")



import random 
lista=[]

for i in range(10):
    numero=random.randint(1,50)
    lista.append(numero)

for elemento in lista:
    print(elemento)


#Digitando 10 elementos na lista
#lista=[]
#for i in range(1,10):
  #  numero=int(input("Digite um número inteiro: "))
 #   lista.append(numero)

#lista=lista*3

#print("Tamanho da lista ",len(lista))
#for elemento in lista:
#    print(elemento, end=" ")



#gerar uma lista de 50 números aleatórios
import random 
lista=[]

for i in range(50):
    numero=random.randint(1,100)
    lista.append(numero)
#exibindo elemento
for elemento in lista:
    print(elemento, end=" ")
print(len(lista))

#definindo o maior 

maior=lista[0]
for i in range(len(lista)):
    print(lista[i], end=" ")
    if maior < lista[i]:
        maior=lista[i]
print("\n\nO maior = ",maior)

#definindo o menor

menor=lista[0]
for i in range(len(lista)):
    print(lista[i], end=" ")
    if menor > lista[i]:
        menor=lista[i]
print("\n\nO menor = ",menor )



#concatenando listas
import random
lista1=[]
lista2=[]
lista3=[]
for i in range(10):
    n=random.randint(1,10)
    lista1.append(n)
    n=random.randint(1,10)
    lista2.append(n)
print(lista1)
print(lista2)  
lista3= lista1+lista2
print(lista3)
#mostrando os pares
x = 0
while x <= 10:
    if x%2 == 0:
        print("Pares = ", x)
    x = x + 1
#mostrando os ímpares
y = 1
while y <= 10:
    if y%2 != 0:
        print("Ímpar = ", y)
    y += 1
#removendo elementos pares
#lista3.remove(0,2,4,6,8,10)
    