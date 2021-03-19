dicipline_technique = { }
code_dicipline =""

for i in range(2):
   code_dicipline = input(f"Digite o {i+1}º codigo da diciplina:")
   dicipline_technique[code_dicipline] = input(f"Digite  o nome da {i+1}º materia:")

dicipline_general = {600:"Matemática Discreta"}    

dicipline_general.update(dicipline_technique)#Junta dois dicionarios com metodo update().
print(dicipline_general)
print(dicipline_general.get(600))#Usando o metodo get(), que  retorna o valor da chave associado.
print(dicipline_general.items())#retorna uma tupla com cada uma com valor e chave d dicionarios.
print(dicipline_general.keys())#ostra todas as chaves do dicionarios.
print(dicipline_general.values())#Retorna valores do dicionarios.
print(dicipline_general.pop(600))#exclui a chave espeficada entre parenteses
print(dicipline_general.popitem())#remove elemento aleatorio
print(dicipline_general)