""" Задача: вибір страви з максимальною калорійністю при заданому бюджеті (задача рюкзака, knapsack problem)."""

# Дані про страви: вартість і калорійність
items = {
    "піцца": {"cost": 50, "calories": 300},
    "гамбургер": {"cost": 40, "calories": 250},
    "хот-дог": {"cost": 30, "calories": 200},
    "пепсі": {"cost": 10, "calories": 100},
    "кола": {"cost": 15, "calories": 220},
    "картопля": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    """ Жадібний алгоритм для вибору страв з максимальним співвідношенням калорій до вартості.
    :param items: словник з даними про страви
    :param budget: загальний бюджет
    :return: список обраних страв
    """
    # Сортуємо страви за співвідношенням калорій до вартості у порядку спадання
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']
    
    return selected_items, total_calories


# Динамічне програмування
def dynamic_programming(items, budget):
    """ Алгоритм динамічного програмування для вибору страв з максимальною калорійністю при заданому бюджеті.
    :param items: словник з даними про страви
    :param budget: загальний бюджет
    :return: список обраних страв
    """
    n = len(items)
    item_names = list(items.keys())
    
    # dp[i][j] означає максимальну калорійність, яку можна отримати, якщо враховувати лише перші i страв з бюджетом j
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item = item_names[i - 1]
        cost = items[item]['cost']
        calories = items[item]['calories']
        
        for j in range(1, budget + 1):
            if cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Відновлення обраних страв з dp таблиці
    selected_items = []
    total_calories = dp[n][budget]
    w = budget
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= items[item_names[i - 1]]['cost']
    
    return selected_items, total_calories


# Приклад використання 
budget = 100

# Жадібний алгоритм
greedy_selected_items, greedy_calories = greedy_algorithm(items, budget)
print(f"Жадібний алгоритм обрав страви: {greedy_selected_items}, загальна калорійність: {greedy_calories}")

# Динамічне програмування
dp_selected_items, dp_calories = dynamic_programming(items, budget)
print(f"Динамічне програмування обрало страви: {dp_selected_items}, загальна калорійність: {dp_calories}")


""" 
Результат виконання:

Жадібний алгоритм обрав страви: ['кола', 'картопля', 'пепсі', 'хот-дог'], загальна калорійність: 870
Динамічне програмування обрало страви: ['картопля', 'кола', 'пепсі', 'піцца'], загальна калорійність: 970
"""
