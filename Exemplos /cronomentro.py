import time

print("Digite algo para lembrar")
text = str(input())

print("Quantos minutos?")
tempo = float(input())
tempo*=60
time.sleep(tempo)
print(text)