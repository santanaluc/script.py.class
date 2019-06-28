#!/usr/bin/env python
# coding: utf-8

# In[30]:


# Exercício 1
import random 
lista1 = []
for i in range(10):
    a=int(input('Digite um número inteiro: '))
    lista1.append(a)
print(lista1)


# In[31]:


#Exercício 2
import random
lista2 = []
for i in range(6):
    b=str(input('Digite uma string: '))
    lista2.append(b)
print(lista2)


# In[ ]:





# In[32]:


#Exercício 3
import random
lista3 = []
for i in range(50):
    numero=random.randint(1,100)
    lista3.append(numero)
for elemento in lista3:
    print(elemento, end=" ")
    
#maior
maior=lista3[0]
for i in range(len(lista3)):
    if maior < lista[i]:
        maior=lista[i]
print("\n\nO maior = ",maior) 

#menor
menor = lista3[0]
for i in range(len(lista3)):
    if menor > lista3[i]:
        menor = lista[i]
print("\nO menor = ",menor)


# In[35]:


#Exercício 4
import random
lista1 = []
lista2 = []
lista3 = []
for i in range(20):
    n=random.randint(30,50)
    lista1.append(n)
    n=random.randint(50,70)
    lista2.append(n)
print(lista1)

print(lista2)

lista3 = lista1 + lista2
print(lista3)

#Maior
maior=lista3[0]
for i in range(len(lista3)):
    if maior < lista3[i]:
        maior=lista3[i]
print("\n\nO maior = ",maior)

#Menor
menor=lista3[0]
for i in range(len(lista3)):
    if menor > lista3[i]:
        menor = lista3[i]
print("\n\nO menor = ",menor)

#Média Aritmética
media += lista3[i]
for i in range(40):
    media1 = media/40
print("\n\nA Média Aritmética é = ",media)


# In[ ]:





# In[ ]:




