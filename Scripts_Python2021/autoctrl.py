import os

class CtrlSystem():
    
   def limpaTela(self):
       return os.system('clear') or None
   
   def desligaMaquina(self):
       return os.system('sudo shutdown now')
   
   def reiniciaMaquina(self):
       return os.system('sudo shutdown --reboot')
   
   def sleepMaquina(self,min,op):
       if op == 1: 
         print(f"Será desligado em {min*60} min")  
         return os.system(f'sudo shutdown --poweroff {min*60}')
       elif op == 2:
         print(f"Será desligado em {min} min ")    
         return os.system(f'sudo shutdown --poweroff {min}')
       return "Tente novamente."
         
p = CtrlSystem()
print("Digite em minutos ou em horas para executar:")
tempo = int (input(":"))
print("Tecle 1-Hora ou 2 -Min: ")
op = int(input(":"))
p.limpaTela()
p.sleepMaquina(tempo,op)
    


