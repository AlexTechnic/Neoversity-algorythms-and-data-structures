import heapq

def min_cost_to_connect_cables(cables):
    """ Функція для розрахунку мінімальних витрат на з'єднання кабелів
    :param cables: список довжин кабелів
    :return: мінімальні витрати на з'єднання кабелів
    """
    # Ініціалізуємо купу з початковими довжинами кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки є більше ніж один кабель у купі
    while len(cables) > 1:
        # Витягуємо два найменших кабелі
        first_min = heapq.heappop(cables)
        second_min = heapq.heappop(cables)
        
        # Витрати на з'єднання цих двох кабелів
        cost = first_min + second_min
        total_cost += cost
        
        # Додаємо новий кабель (об'єднаний) назад до купи
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]

print("Наявні кабелі з наступними довжинами (перелік кабелів):\n")
for cable in cables:
    print(f"Кабель довжиною {cable} одиниць")

min_cost = min_cost_to_connect_cables(cables[:])
print("\nМінімальні загальні витрати на з'єднання кабелів:", min_cost)


""" Результат виконання:

Наявні кабелі з наступними довжинами (перелік кабелів):

Кабель довжиною 4 одиниць
Кабель довжиною 3 одиниць
Кабель довжиною 2 одиниць
Кабель довжиною 6 одиниць

Мінімальні загальні витрати на з'єднання кабелів: 29
"""