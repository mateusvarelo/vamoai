import matplotlib.pyplot as plt
import numpy as np 

lista = np.array([20,30,30,15])

minhalista = ["Maças","Bananas","Laranjas","Melancias"]

myexplode = [0.2,0,0,0]

plt.pie(lista,labels = minhalista, explode = myexplode, shadow = True)

plt.show()