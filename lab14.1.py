import matplotlib.pyplot as plt
import numpy as np

#інтервал для x
x = np.linspace(-2, 2, 100) 

#функція
y = 1/x * np.sin(x) * np.cos(x**2 + 1/x)

#створення графіку
plt.plot(x, y, label=r'$\frac{1}{x}\bullet\sin(x)\bullet\cos(x^{2}+\frac{1}{x})$', color = "red", linewidth = 2)
#назва графіку
plt.title('Графік функції', fontsize=15) 
#позначення вісі х
plt.xlabel('x', fontsize=12, color='red') 
#позначення вісі у
plt.ylabel('y', fontsize=12, color='red') 
#позначення легенди
plt.legend()
#позначення сітки
plt.grid()

#збереження
plt.savefig("1.png")
#відображення
plt.show()