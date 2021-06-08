"""Programa 1 - No escurinho do cinema"""
nome = input("Nome: ")
idade = int(input("Idade: "))
if idade >= 18:
    print('-'*5)
    print('Menu:')
    print('-'*5)
    print('-'*30)
    print("1-Entrada Padrão:R$ 35,00")
    print("2-Entrada Vip:R$ 60,00")
    print('-'*30)
    tipo_entrada = int(input("Digite aqui opção: ")) 
    print("Opção escolhida:",tipo_entrada)
    deconto_estudante = input("Você e estudante de Python?SIM OU NÃO? ")
    deconto_estudante.lower()
    if deconto_estudante == 'sim':
        print("Estudante Python tem desconto de 50%!")
        if tipo_entrada == 1:
            print("Valor total:",35-(0.5*35))  
        else:
            print("Valor total:",60-(0.5*60))  
    else:
        print('Não obteve desconto!')
    print("Compra relizada!")      
else:
    print("Ingresso indisponivél para menores de idade!")
    print(f"Nos próximos {18-idade} anos você terá acesso!")        