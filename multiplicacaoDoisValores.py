def multiplica(numeroUmFunc,numeroDoisFunc):
    return numeroUmFunc * numeroDoisFunc

numeroUm = int(input("Digite um numero entre 1 e 50: "))
numeroDois = int(input("Digite outro numero entre 1 e 50: "))

if (1 <= numeroUm <= 50) and (0 <= numeroDois <= 50):
    print("Resultado da multiplicação:",multiplica(numeroUm,numeroDois)) 
else:
    print("Numeros invalidos!")
    
       