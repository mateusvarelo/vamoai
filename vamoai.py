import random
cont=3
inicio=True
while inicio and cont >=0:
 n=int(input(f'Digite um número entre 10 e 30. Resta {cont} tentativas: '))
 sorteio=random.randint(10, 30)
 if n==sorteio:
    print('Você acertou')
    inicio=False
 elif n!=sorteio:
    print("Errou") 
    cont-=1   

print(f'Número sorteado foi {sorteio}')    