nota_matematica = float(input('DIGITE NOTA DE MATEMATICA: '))
nota_biologia = float(input('DIGITE NOTA DE BIOLOGIA: '))
nota_fisica = float(input('DIGITE NOTA DE FISICA: '))
 
media = (nota_biologia+nota_fisica+nota_matematica)/3
 
if  6 <= media <= 10:
     print(f'Aprovado!{media :.1f}')
else:
     print(f'Reprovado!{media :.1f}')  
