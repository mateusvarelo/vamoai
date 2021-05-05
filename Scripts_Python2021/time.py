from datetime import date,datetime 
import threading as thr

data_atual = datetime.now()
data_em_texto = data_atual.strftime("%d/%m/%Y %H:%M")
print(data_em_texto)

#######
def final():
    print("FiM")
    print("\U0001F600")
    
timer = thr.Timer(5.0,final)

timer.start()
