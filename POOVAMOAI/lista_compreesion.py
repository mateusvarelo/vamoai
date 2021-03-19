##  if pares  != 6 else 12  forma de fazer operador ternario.
"""pares = [
        pares 
        for pares in range(10) 
        if pares % 2 == 0
        ]
impares = [impares for impares in range(10) if impares % 2 != 0 ]
print(pares,impares) 
print(pares.copy())

lihas_e_coluna = [
       (x,y)
        if y == 2 else (x, y * 1000)
        for x in range (1,11)
        for y in range (1,6)
        if x !=2
       ]
print(lihas_e_coluna)       
"""
string = "Mateus Varelo"
nova_string = "".join([letra for letra in string])
print(nova_string)
