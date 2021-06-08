def procura_chave_na_lista(dicionario):
    if len(dicionario) == 0:
      return dicionario
    else:
      for i in dicionario.keys():
        print(i)
        for j in dicionario.values():
           print(j)
           if i in j:
              print("ok")
              dicionario[i] = True
              break
           else:
              dicionario[i] = False
      return dicionario        
dicionario = {"d": ["a", "b", "c"], "b": [1, 2, 3, "b"]}              
print(procura_chave_na_lista(dicionario))              