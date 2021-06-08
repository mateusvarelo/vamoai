def diferenca(minha,stem):
   return stem - minha

def compara(stringUm,stringDois):
    stringUm = stringUm
    stringDois = stringDois
    
    if (stringUm != stringDois):
        print("Cidade e Estados distintos!")
    else:
        print("locais iguais!")

minhaIdade = 24
mulherStem = 85

compara("Brasil","EUA")
compara("Rio de janeiro","Condado de Arlington")

print(
     f"A diferença de idade entre Grace Hopper e a minha é de " 
     f"{diferenca(minhaIdade,mulherStem)} anos."
     )
     