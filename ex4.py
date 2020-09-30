import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-10, 10.01, 0.01)
plt.plot(x, eval(input("Введите функцию, график которой хотите увидеть: ")))

plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid(True)

plt.show()
