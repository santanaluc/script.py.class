#!/usr/bin/env python
# coding: utf-8

# <h1>Exercício 1</h1>
#     <p>Número par - Construir uma função que retorna Verdadeiro ou Falso conforme um número seja par ou não. Faça o teste para 50 números aleatórios compreendidos entre 25 e 92.</p>

# In[26]:


import random
def par():
    resultado = n%2
    if resultado == 0:
        print(True, end=' / ')
    else:
        print(False, end=' / ')
        
    
#Programa Principal
for i in range(51):
    n = random.randint(25,92)
    print(n, end=' ')
    par()


# <h1>Exercício 2</h1>
# <p>Numeração de 1 a 100  - Elaborar uma função que exiba a sequencia numérica compreendida entre 1 a 100.</p>

# In[ ]:





# In[ ]:




