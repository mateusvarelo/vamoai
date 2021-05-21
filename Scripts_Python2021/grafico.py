
import matplotlib.pyplot  as plt

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]

plt.plot(meses,valores)
plt.ylim(100000, 120000)
plt.title('Faturamento no primeiro semestre de 2017')
plt.xlabel('Meses')
plt.ylabel('Faturamento em R$')
plt.savefig("mygraph.png")
##