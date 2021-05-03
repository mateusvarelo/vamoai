def array_diff(a, b):
    pilha = []
    for i in a: 
       if b not in a:
           pilha.append(i)
       else:
           pilha.remove(i)
    return pilha             
 
a = [1,2,2]

print(array_diff(a,[2]))
