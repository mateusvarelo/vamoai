class Queue:
    def __init__(self):
        self.queue = []

    def insert(self,element):
        self.queue.append(element)  
        return self.queue  
    
    def to_remove(self):
        if self.size() == 0:
           return None   
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)        

element = Queue()

print(element.queue)
print(element.to_remove())

for i in range(10): 
   if i % 2 == 0: 
     element.insert(i)

print(element.size())
element.insert(8)
print(element.queue)
print(element.size())
print(element.queue) 

element.to_remove()
print(element.queue)
print(element.size())

