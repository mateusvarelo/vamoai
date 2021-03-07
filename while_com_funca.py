def fun_com_while(inicio):
    i = 0
    while inicio:
        i+=1
        if i == 2:
         inicio = False
         return inicio    
inicio = True

while inicio:
    inicio = fun_com_while(inicio)
print(inicio)
