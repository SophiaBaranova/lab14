import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#назва файлу з вхідними даними
filename = "data2.csv"
#відкриття файлу
try:
    f = open(filename, "r")
except:
    print(filename, "couldn't be opened")
    exit(1)
reader = csv.DictReader(f)
#зчитування даних із файлу у list
data = list(reader)

#значення по вісі х - роки від 2000 до 2020
x = np.arange(2000, 2021)

#назва
title = data[0]['Series Name']
#список країн
country = []
for index in data:
    country.append(index['Country Name'])
    #видалення зайвих ключів
    index.pop('Series Name')
    index.pop('Country Name')

print(title)
#виведення назв країн у списку
print("countries available:")
print(country)
#введення назви країни для побудови стовпчатої діаграми
c = input("enter country name to create a bar chart: ")
c = c.title()
#якщо країни немає у списку
if c not in country:
    print(f"no data for {c} available")
    exit(2)

#значення по вісі у для кожної з країн
y = dict()
for i in range(len(country)):
    y[country[i]] = list(map(float, data[i].values()))

#створення figure
fig, axs = plt.subplots(nrows=2, layout="constrained")
#ширина figure
fig.set_figwidth(12)
for i in range(len(country)):
    #створення графіку для кожної з країн
    axs[0].plot(x, np.array(y[country[i]]), label=country[i])

#назва графіку
axs[0].set_title(title, fontsize=15)
#позначення легенди
axs[0].legend()

#створення стовпчатої діаграми
axs[1].bar(x, y[c], label=c)
#назва діаграми
axs[1].set_title(title+": "+c, fontsize=15)

for i in range(2):
    #позначення вісі х
    axs[i].set_xlabel('year', fontsize=12)
    #позначення вісі у
    axs[i].set_ylabel('value', fontsize=12)
    #підписи даних по вісі х
    axs[i].xaxis.set_major_locator(ticker.MultipleLocator(1, offset = 2000))
    #масштаб для вісі х
    axs[i].set_yscale('symlog')
    axs[i].set_aspect(aspect=0.7)
    #позначення сітки
    axs[i].grid()

#збереження
plt.savefig("2.png")
#відображення
plt.show()

