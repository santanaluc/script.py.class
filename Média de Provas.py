
# coding: utf-8

# In[3]:


n1=input('QUAL É O SEU NOME? ')
print('prazer, {}'.format(n1))


# In[ ]:


p1 = float(input('qual é a sua nota p1? '))
p2 = float(input('qual sua nota p2? '))
media = (p1+p2)/2
print('com as notas da p1 {} e da p2 {}\n a média é igual a {}'.format(p1, p2, media))
if(media>=6):
      print('PARABÉNS VOCE FOI MUITO BEM')
else:
      print('precisa estudar mais!')


# In[23]:


p1 = float(input('qual é a sua nota p1? '))
p2 = float(input('qual sua nota p2? '))
if(p1>10 or p2>10):
    print('Digite números menores ou iguais que 10')
else:    
    media = (p1+p2)/2
    print('com as notas da p1 {} e da p2 {}\n a média é igual a {}'.format(p1, p2, media))
    if(media>=6):
        print('PARABÉNS VOCE FOI MUITO BEM')
    else:
        if(media >=5 and media <6):
            print('QUASE MANO')
        else: 
            print('precisa estudar mais!')

    

