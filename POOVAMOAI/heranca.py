class People:
    def __init__(self,name,email):
        self.name = name
        self.email = email

class Aluno(People):
    def __init__(self,name,email,matricula):
        super(). __init__(name,email)
        self.matricula = matricula

    def  display(self):
          return f"{self.name}  {self.matricula}  {self.email}" 

class Professor(People):
    def __init__(self,name,email,salario):
        super(). __init__(name,email)
        self.salario = salario

    def mostra(self):
        return f"{self.name}  {self.email}  {self.salario} " 
    
   
    def acrescenta(self,soma):
           self.soma = soma
           return  soma + self.salario

aluno1 = Aluno([])
for i in range(4):
   pass    


print(aluno1.display())
print(prof1.mostra())
print(prof1.acrescenta(100))


