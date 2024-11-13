import csv
import numpy as np
import matplotlib.pyplot as plt

#форматування підписів даних
def func(pct, allvals):
    return f"{pct:.2f}%"

#назва файлу з вхідними даними
filename = "data3.csv"
#відкриття файлу
try:
    f = open(filename, "r")
except:
    print(filename, "couldn't be opened")
    exit(1)

reader = csv.DictReader(f, delimiter=';')
#зчитування даних із файлу у list
data = list(reader)
#назва
title = data[0]['Series Name']
#списки країн і значень показника
country = []
value = []
for index in data:
    country.append(index['Country Name'])
    value.append(index['2020 [YR2020]'])

#перетворення списків у np.array
country = np.array(country)
value = np.array(value, dtype=np.float64)

#визначення відсотків
s = np.sum(value) / 100
value = np.divide(value, s)
value = np.round(value, 2)

#кольори
colors = plt.cm.Set3(np.linspace(0,1,len(value)))

#створення figure
fig, ax = plt.subplots()
#вирівнювання figure
fig.subplots_adjust(left=0, wspace = 0.2)
#ширина figure
fig.set_figwidth(8)
#створення кругової діаграми
ax.pie(value, autopct=lambda pct: func(pct, value), colors=colors)
#назва діаграми
ax.set_title(title, fontsize=15)
#позначення легенди
ax.legend(country, title="Countries", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

#збереження
plt.savefig("3.png")
#відображення
plt.show()



