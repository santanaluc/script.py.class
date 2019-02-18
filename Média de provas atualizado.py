
# coding: utf-8

# In[1]:


n1=input('Qual é seu nome? ')
print('Prazer, {}'.format(n1))
# In[ ]:
# In[23]:
p1 = float(input('Qual é a sua nota P1? '))
p2 = float(input('Qual sua nota P2? '))
if(p1>10 or p2>10):
  print('Digite números menores ou iguais que 10')
else:    
  media = (p1+p2)/2
  print('Com as notas da P1: {} e da P2: {}\nA média é igual a: {}'.format(p1, p2, media))
  if(media>=6):
      print('PARABÉNS VOCÊ FOI MUITO BEM')
  else:
      print('Você não atingiu a média.')
      p3 = float(input('Qual sua nota P3? '))
      if(p1>p2):
          media1 = (p1+p3)/2
          print('Com as notas da P1: {} e da P3: {}\nA média é igual a: {}'.format(p1, p3, media1))
          if(media1>=6):
              print('PARABÉNS VOCÊ FOI MUITO BEM!')
          else:
              print('Tu é um lixo mesmo.')
      else:
          media2 = (p2+p3)/2
          print('Com as notas da P2: {} e da P3: {}\nA média é igual a: {}'.format(p2, p3, media2))
          if(media2>=6):
              print('PARABÉNS VOCÊ FOI MUITO BEM!')
          else:
              print('Tu é um lixo mesmo.')

