class Gato:
    def __init__(self,nome,cor,raça,idade,sexo):
        self.cor = cor
        self.raça = raça
        self.idade = idade
        self.sexo = sexo
    def come(self,colocar_comida):
        self.colocar_comida = colocar_comida
        print("Comer")    
    def levar_ao_veterinario(self,hora,dia):
        self.hora = hora
        self.dia = dia     

class Caneta:
    def __init__(self,tinta,quantidade,fabricante,valor):
        self.tinta = tinta
        self.quantidade = quantidade
        self.fabricante = fabricante
        self.valor = valor
    def comprar(self,valor,quantidade):
        return valor*quantidade 
class Relogio:
    def __init__(self,marca,preço,qnt,cor,material):
        self.marca = marca
        self.preço = preço
        self.qnt = qnt
        self.cor = cor
        self.material = material
    def comprar(self,qnt,valor):
        return qnt*valor                      
