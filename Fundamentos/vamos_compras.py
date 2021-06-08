"""Programa 2 - Vamos as compras"""
nome_produto_1 = (input('Digite o nome do produto 1: '))
valor_produto_1 = float(input(f'Valor do {nome_produto_1}: '))
nome_produto_2 = (input('Digite o nome do produto 2: '))
valor_produto_2 = float(input(f'Valor do {nome_produto_2}: '))
nome_produto_3 = (input('Digite o nome do produto 3: '))
valor_produto_3 = float(input(f'Valor do {nome_produto_3}: '))

if (valor_produto_3 > valor_produto_1 < valor_produto_2):
    print(f"O produto {nome_produto_1} é o mais barato!") 
elif (valor_produto_3 > valor_produto_2 < valor_produto_1):
    print(f"O produto {nome_produto_2} é o mais barato!") 
elif (valor_produto_2 > valor_produto_3 < valor_produto_1):
    print(f"O produto {nome_produto_3} é o mais barato!")
else:
    print("Preço iguais!")         