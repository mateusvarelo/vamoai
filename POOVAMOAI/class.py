class Cachorros:
    def __init__(self,nome,cor,raca,porte,patas): 
        self.nome = nome
        self.cor = cor
        self.raca = raca
        self.porte = porte
        self.patas = patas
     #metodos do cachorro
    def comer(self,hora_comer):
        self.hora_comer = hora_comer    
    def dormi(self,onde_dormi):
        self.onde_dormi = onde_dormi
    def latir(self,late):
        self.late = late
    def coco(self,lugar_de_fazer):
        self.lugar_de_fazer = lugar_de_fazer       
    def xixi(self,onde_fazer):
        self.onde_fazer = onde_fazer

Grace = Cachorros("Rupica","Marrom","Chual","Domestico",4)         
f"(self.Grace)"