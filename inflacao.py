preco_anterior=float(input('Informe o preço do Kg do tomate 1 ano atrás: R$'))
preco_atual=float(input('Informe o preço do Kg do tomate atual: R$'))
print(
     'A diferença de preço do KG do tomate e um ano é de R$',
      preco_atual-preco_anterior
     )
print(
    'A inflação do KG do tomate e um ano é de ',
    (preco_atual-preco_anterior)/preco_anterior*100,"%."
     )