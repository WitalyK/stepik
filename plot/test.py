import matplotlib.pyplot as plt  # подключаем библиотеку с коротким названием, чтобы не писать каждый раз много букв
import math
from pprint import pprint

fig = plt.figure()  # создаем график
pprint(sorted(list(fig.__class__.__dict__)))
plt.axis([0, 10, -1.5, 1.5])  # на оси x будет изображаться участок от 0 до 10, а на оси y от -1.5 до 1.5

plt.xlabel('x')  # подпись оси x
plt.ylabel('sin(x)')  # подпись оси y

xs = []  # здесь будут параметры функции (x координаты изображаемых точек)
sin_vals = []  # здесь будут значения функции (y координаты изображаемых точек)

x = 0.0
while x < 10.0:  # заполняем списки
    sin_vals.append(math.sin(x))
    xs.append(x)
    x += 0.01

plt.plot(xs, sin_vals)  # создаем график: первый аргумент - список x-координат, второй - соответствующие y-координаты
plt.savefig('sin1.png')  # сохраняем график в файл
plt.show()