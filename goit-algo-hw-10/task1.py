import pulp  # Підключення бібліотеки (PuLP) для розв'язання задач лінійного програмування

# Створення задачі лінійного програмування для максимізації виробництва напоїв (Лимонад та Фруктовий сік, в літрах)
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні для кількості виробництва напоїв (в літрах)
limonad = pulp.LpVariable("Limonad", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("FruitJuice", lowBound=0, cat='Integer')

# Цільова функція: максимізація загальної кількості вироблених напоїв
model += limonad + fruit_juice, "Total Production"

# Обмеження на ресурси (вода, цукор, лимонний сік, фруктове пюре)
model += 2 * limonad + 1 * fruit_juice <= 100, "Water Constraint"
model += 1 * limonad <= 50, "Sugar Constraint"
model += 1 * limonad <= 30, "Lemon Juice Constraint"
model += 2 * fruit_juice <= 40, "Fruit Puree Constraint"

# Розв'язання задачі лінійного програмування
model.solve()

# Виведення результатів (оптимальних значень змінних та цільової функції)
print("Статус розв'язку:", pulp.LpStatus[model.status])
print(f"Оптимальна кількість Лимонаду: {limonad.varValue} одиниць")
print(f"Оптимальна кількість Фруктового соку: {fruit_juice.varValue} одиниць")
print(f"Максимальна загальна кількість виробництва: {pulp.value(model.objective)} одиниць")


""" Результат виконання:

Статус розв'язку: Optimal
Оптимальна кількість Лимонаду: 30.0 одиниць
Оптимальна кількість Фруктового соку: 20.0 одиниць
Максимальна загальна кількість виробництва: 50.0 одиниць
"""