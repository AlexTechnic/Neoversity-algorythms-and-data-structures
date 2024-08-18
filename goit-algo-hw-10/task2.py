import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції та межі інтегрування (тут взято функцію sin(x), від 0 до pi)
def f(x):
    return np.sin(x)

a = 0  # Нижня межа інтегрування
b = np.pi  # Верхня межа інтегрування

# Побудова графіка функції та області інтегрування (заштрихована область)
x = np.linspace(-0.5, np.pi + 0.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, 1.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = sin(x) від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Метод Монте-Карло для обчислення інтегралу від функції f на відрізку [a, b] з n точками
def monte_carlo_integration(f, a, b, n=10000):
    x_random = np.random.uniform(a, b, n)
    y_random = f(x_random)
    integral = (b - a) * np.mean(y_random)
    return integral

# Використання методу Монте-Карло для обчислення інтегралу (за замовчуванням n=10000)
monte_carlo_result = monte_carlo_integration(f, a, b)
print(f"Результат інтеграції методом Монте-Карло: {monte_carlo_result}")

# Обчислення інтегралу за допомогою функції quad (квадратурні методи з бібліотеки SciPy), error - оцінка похибки (необов'язково)
quad_result, error = spi.quad(f, a, b)
print(f"Результат інтеграції функцією quad: {quad_result} з похибкою {error} ")

# Порівняння результатів методів Монте-Карло та quad
difference = abs(monte_carlo_result - quad_result)
print("\nПорівняння результатів:\n")
print(f"Метод Монте-Карло: {monte_carlo_result}")
print(f"Метод quad: {quad_result}")
print(f"Різниця між результатами: {difference}")


"""Результат виконання:

Результат інтеграції методом Монте-Карло: 2.0021960120868023
Результат інтеграції функцією quad: 2.0 з похибкою 2.220446049250313e-14 

Порівняння результатів:

Метод Монте-Карло: 2.0021960120868023
Метод quad: 2.0
Різниця між результатами: 0.0021960120868023125
"""

""" Висновок: результати обох методів (Монте-Карло та quad) близькі один до одного, 
але метод quad дає більш точний результат 
"""