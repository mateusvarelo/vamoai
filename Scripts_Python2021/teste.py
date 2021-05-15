class Dicionario():
    def __init__(self):
        self.dicionario = {}
        
    def nova_entrada(self, palavra, frase):
        self.dicionario[palavra] = frase 
    def checar(self, palavra):
        if palavra in self.dicionario:
           return self.dicionario[palavra]
        else:
           return f"Não foi possível encontrar a palavra {palavra}"
d = Dicionario()  
d.nova_entrada('Maçã', 'Uma fruta que cresce em árvores')
print(d.checar('Maçã'))
#helloworld