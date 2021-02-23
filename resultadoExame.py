def resultado(notaMedica):
    if  (7 <= notaMedica <= 10):
      print("Estado BOM!Continuar assim!")
    
    elif (4 <= notaMedica <= 6):
      print("Estado Médio!Buscar se cuidar mais, e fazer acompanhamento medico!")
    
    elif (0 <= notaMedica <= 3):
      print("Estado Ruim!Procurar equipe médica!")

for i in range(3):
    nome = input("Digite nome: ")
    notaExame = int(input("Digite resultado: "))
    resultado(notaExame)

