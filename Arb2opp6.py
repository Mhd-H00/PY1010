#forelesning 4 og 5. brukt.

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return -x**2 - 5

x = np.linspace(-10, 10, 200)


y = f(x)


plt.plot(x, y, label='f(x) = -x^2 - 5')
plt.xlabel('x')
plt.title('Plot av f(x) = -x^2 - 5')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()