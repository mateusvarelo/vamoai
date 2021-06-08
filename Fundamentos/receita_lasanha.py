def quebralinha():
    print('*'*45)

def ingredientes():
                print('-1 massa de lassanha(pronta)')
                print('-500 g de presunto')
                print('-500 g de queijo mussarela')
                print('-500 g carne moida')
                print('-1 massa de tomate pronta e sal a gosto')
                print('-Pimenta-do-reino a gosto')
                print('-Orégano a gosto')

def preparamassa():
        print(
               "-Cozinha a massa da lasanha em aproximadamente"
               "em 2 litros de água por 5 min"
             )

def preparacarne():
        print(
               "-Em uma panela cozinhe a carne moída,depois de cozida coloque"
               "molo de tomate, o sal e temperos a gosto"
             )

def juntado():
         print(
               "-Comece montando com uma camda de molho, a massa lasanha, o" 
               "presunto e o queijo"
              )
         print("-Faça esse processo até tudo terminar.")
         print("-Aqueça o forno a 180ºC durante 5 min")
         print("Coloque a lasanha no forno de 20 a 30 min,")

print("Vamos aprender a fazer lasanha?")
opcao = input("Sim ou Não?")
opcao.lower()

if opcao == "sim":
    ingredientes()
    print("Vamos mistura ingredientes?")
    opcao = input("Sim ou Não?")
    opcao.lower()
    if opcao == "sim":
        preparamassa()
        preparacarne()
        juntado()
    else:
        print("Estavamos tão perto!")
else:
    print("Que pena!")
   


