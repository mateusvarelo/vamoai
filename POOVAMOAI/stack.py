class Stack:
    def __init__(self):
        self.stack = []

    def insert(self,element):
         self.stack.append(element)
         return self.stack   

    def to_remove(self):
        if self.size() == 0:
            return None 
        else:    
            return self.stack.pop()     

    def size(self):
        return len(self.stack)   

numeros = Stack()

print(numeros.stack)

"""for i in range(10): 
   if i % 2 == 0: 
     numeros.insert(i)

print(numeros.stack)

print(numeros.size())

print(numeros.to_remove())

print(numeros.size())

print(numeros.stack)
"""
print(numeros.to_remove())
