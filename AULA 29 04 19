#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Fatorial

def fatorial(n):
    p=1
    if n!=0:
        for i in range(1,n+1):
             p=p*i
    return p

n = int(input('Digita algum número ai fdp: '))
print(fatorial(n))


# In[27]:


def fatorial(n):
    p=1
    if n!=0:
        for i in range(1,n+1):
             p=p*i
    return p


def combinacao(n,p):
    c = fatorial(n)/(fatorial(p)*fatorial(n-p))
    return c

def arranjo(n,p):
    a=fatorial(n)/fatorial(n-p)
    return a
print('C5,2 = ',combinacao(5,2))
print('A5,2 = ',arranjo(5,2))


# In[1]:


from time import sleep
def mensagem(msg):
    print(msg)

def fatorial(n):
    p=1
    if n!=0:
        for i in range(1,n+1):
             p=p*i
    return p

def combinacao(n,p):
    c = fatorial(n)/(fatorial(p)*fatorial(n-p))
    return c

def arranjo(n,p):
    a=fatorial(n)/fatorial(n-p)
    return a

opc=1
while opc != 9:
    
    opc = int(input('1 - Combinação\n2 - Arranjo\n9 - Fim\nSelecione = '))
    if opc in [1,2]:
        n=int(input('Digite o valor de N: '))
        p=int(input('Digite o valor de P: '))
        print('CALCULANDO...')
        if opc == 1:
            sleep(1)
            print('Combinação = ',combinacao(n,p))
        elif opc == 2:
            sleep(1)
            print('Arranjo = ',arranjo(n,p))
        elif opc == 9:
            print('Flw')
        else:
            print('N.a usuário')


# In[ ]:


#sem retorno:
def mensagem(msg):
    print(msg)


# In[ ]:




