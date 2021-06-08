#LIFO -Last in , firs out
stack = []
#pilha
i = 0
for i in range(10):
  if i % 2 == 0:
    stack.append(i)

print(stack)
stack.pop()
print(stack)

stack.pop()
print(stack)