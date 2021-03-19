def adiciona_valores(valores,dicionario):
    for i in dicionario.values():
      valores.append(i)
    return valores  

def adiciona_chaves(chaves,dicionario):
    for i in dicionario.keys():
      chaves.append(i)
    return chaves 

def procura_chave_na_lista(dicionario):
    valores = []
    chaves = [] 
    adiciona_chaves(chaves,dicionario)
    adiciona_valores(valores,dicionario)
    for i in chaves:
        for j in valores:
            if i in j:
                dicionario[i] = True
                break
            else:
                dicionario[i] = False
                break
    return dicionario        
dicionario = {"a":[4,6,"a"],"b":5}
print(procura_chave_na_lista(dicionario))            
   