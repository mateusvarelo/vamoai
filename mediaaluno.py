def media_aluno(av1,av2):
    return (av1+av2)/2      

def situacao_media(media,nome):
    if (10 >= media >=7):
        print(f"O aluno {nome}!Foi aprovado com media:{media}")
    elif (media == 4):
        print("Precisa fazer a AV3 e tirar 10.00!")
    elif(0 < media < 4 ):
        print("Precisa refazer a matéria!")  
    else:
        print("Precisa fazer av3!")

def escolhe_nota(av1,av2,av3):
    if(av1 > av3) and (av2 >= av3):
        return media_aluno(av1,av2)
    elif(av2 >= av1) and (av3 > av1):
        return media_aluno(av2,av3)
    elif(av1 >= av2) and (av3 > av2):
        return media_aluno(av1,av3) 
    return media_aluno(av1,av2)          

nome_aluno = input ("Nome:")
nota_av1 = float(input("Nota AV1: "))
nota_av2 = float(input("Nota av2: "))

media = media_aluno(nota_av1,nota_av2)

situacao_media(media,nome_aluno)

if (media >= 4) and (media < 7):
    nota_av3 = float(input("Nota AV3: "))
    media = escolhe_nota(nota_av1,nota_av2,nota_av3)
    print("Nova media: ",media)