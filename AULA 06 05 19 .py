#!/usr/bin/env python
# coding: utf-8

# In[8]:


m = [[3,1,2,5],[8,1,4,2],[9,8,1,3],[0,1,2,3]]

print(m)
for i in range(len(m)):
    print(m[i])
    
print()
print(m[0][2])
print(m[1][1])


# In[12]:



m = [[3,1,2,5],[8,1,4,2],[9,8,1,3],[0,1,2,3]]

#print(m)
for i in range(len(m)):
    for j in range(4):
        
        print(m[i][j],end=' ')
    print()
#print()
#print(m[0][2])
#print(m[1][1])


# In[24]:


#definindo uma matriz com entrada de dados
#Professor
m3x4 = []
for i in range(3):
    linha=[]
    for j in range(4):
        n=int(input('Digite o número: '))
        linha.append(n)
    m3x4.append(linha)
    
for i in range(3):
    for j in range(4):
        print(m3x4[i][j],end = ' ')
    print()


# In[4]:


#definindo uma função para matrizes
def matrizmxn(lin,col):
    mlc = []
    for i in range(lin):
        linha = []
        for j in range(col):
            n=int(input('Digite um numero: '))
            linha.append(n)
        mlc.append(linha)
    return mlc
    


def exibematriz(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j],end=' ')
        print()

matriz = matrizmxn(2,3) 
exibematriz(matriz)


# In[27]:


#definindo uma função para matrizes
def matrizmxn(lin,col):
    mlc = []
    for i in range(lin):
        linha = []
        for j in range(col):
            n=int(input('Digite um numero: '))
            linha.append(n)
        mlc.append(linha)
    return mlc
    
    
#exibindo a matriz

def exibematriz(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j],end=' ')
        print()

matriz = matrizmxn(2,3) 
exibematriz(matriz)

#retornar o maior valor

def maior(lista):
    maior = [0][0]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if(maior < lista[i][j]):
                maior = lista[i][j]
    return maior
    print()

#retornar o meno valor 
def menor(lista):
    menor = lista[0][0]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if(menor > lista[i][j]):
                menor = lista[i][j]
    return menor
    print()

print('Menor =  ',menor(matriz))
print('Maior =  ',maior(matriz))


# In[40]:


#definindo uma função para matrizes
def matrizmxn(lin,col):
    mlc = []
    for i in range(lin):
        linha = []
        for j in range(col):
            n=int(input('Digite um numero: '))
            linha.append(n)
        mlc.append(linha)
    return mlc
    
    
#exibindo a matriz

def exibematriz(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j],end=' ')
        print()

matriz = matrizmxn(2,3) 
exibematriz(matriz)

#retornar o maior valor

def maior(lista):
    maior = [0][0]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if(maior < lista[i][j]):
                maior = lista[i][j]
    return maior
    print()

#retornar o meno valor 
def menor(lista):
    menor = lista[0][0]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if(menor > lista[i][j]):
                menor = lista[i][j]
    return menor
    print()

print('Menor =  ',menor(matriz))
print('Maior =  ',maior(matriz))

#função soma matriz

def matrizmxn2(lin1,col1):
    mlc2 = []
    for i in range(lin1):
        linha2 = []
        for j in range(col1):
            n=int(input('Digite um numero: '))
            linha.append(n)
        mlc.append(linha2)
    return mlc2

def soma(m1,m2):
    m3=[]
    if len(m1) != len(m2) and len(m1[0]) != len(m2[0]):
        print('Não executável')
    else:
        for i in range(len(m1)):
            linha=[]
            for j in range(len(m1)):
                linha.append(m1[i][j] + m2[i][j])
            m3.append(linha)
        return m3

matriz1=matrizmxn(3,3)
matriz2=matrizmxn(3,3)
matriz3=soma(matriz1,matriz2)
matriz4=soma(matriz,matriz1)

print('soma matrizes: ',exibematriz(soma(matriz1,matriz2)))


# 

# In[ ]:




