"""Programa 3 - Grandes mulheres em STEM"""
print('-'*50)
print('Quiz sobre Grace Hopper')
print('-'*50)
print('Qual país  ou continente nasceu Grace Hopper:')
print('|1-Alemanha|--|2-America Latina|--|3-China|--|4-EUA|--|5-Europa|')
pergunta_1 = int(input('Digite alternativa correta: '))
cont = 0
if   ( pergunta_1 == 2) or (pergunta_1 == 4):
    cont+=1

print('-'*60)
print('Computador desenvolvido por  Grace Hopper:')
print('|1-Commodore 64|--|2-UNIVAC I|--|3-Deep Blue|--|4-iMac|--|5-Mark I|')
pergunta_2 = int(input('Digite alternativa correta: '))
if (pergunta_2 == 2) or (pergunta_2 == 5):
    cont+=1

print('-'*60)
print('Formação de Grace Hopper:')
print('|1-Eng Mecanica--|2-Matemática|--|3-Analista de Sistema|--|4-Fisica|')
pergunta_3 = int(input('Digite alternativa correta: '))
print('-'*60)
if (pergunta_3 == 2) or (pergunta_3 == 4):   
    cont+=1 
print('-'*60)
print('Quantidade acertos: ',cont)
print('-'*60)

filename="resumo.txt"
with open(filename)as file:
  content = file.readlines()
for line in content:
  print(line),