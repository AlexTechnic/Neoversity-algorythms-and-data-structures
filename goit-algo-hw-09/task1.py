import random
import timeit

# Набір монет для видачі решти (номінали монет)
COINS = [50, 25, 10, 5, 2, 1]


# Функція для розрахунку мінімальної кількості монет за допомогою жадібного алгоритму (greedy algorithm)
def find_coins_greedy(amount):
    result = {}
    for coin in COINS:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    total_coins = sum(result.values())
    return result, total_coins

# Функція для розрахунку мінімальної кількості монет за допомогою динамічного програмування (dynamic programming)
def find_min_coins(amount):
    min_coins = [0] + [float("inf")] * amount
    coin_count = [{} for _ in range(amount + 1)]

    for coin in COINS:
        for x in range(coin, amount + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                coin_count[x] = coin_count[x - coin].copy()
                coin_count[x][coin] = coin_count[x].get(coin, 0) + 1

    total_coins = sum(coin_count[amount].values())
    return coin_count[amount], total_coins

# Функція для генерування випадкових цілих чисел (випадкових сум) у заданому діапазоні 
def generate_random_integers(num_values, min_value, max_value, sort_ascending=False):
    amounts = [random.randint(min_value, max_value) for _ in range(num_values)]
    if sort_ascending:
        amounts.sort()  # Сортуємо за зростанням
    return amounts

# Приклад використання для задачі з фіксованою сумою 113
amount = 113
greedy_result, greedy_total = find_coins_greedy(amount)
dp_result, dp_total = find_min_coins(amount)

print(f"Результат жадібного алгоритму для видачі решти для суми {amount}: {greedy_result} (Кількість монет: {greedy_total})")
print(f"Результат динамічного програмування для видачі решти для суми {amount}: {dp_result} (Кількість монет: {dp_total})")

# Параметри для генерування випадкових сум
num_values = 5  # Кількість значень
min_value = 10  # Мінімальне значення
max_value = 1000  # Максимальне значення

# Генерація випадкових сум
amounts = generate_random_integers(num_values, min_value, max_value, sort_ascending=True)
print("\nЗгенеровані випадкові суми для порвіняння швидкості виконання:", amounts)

# Тестування жадібного алгоритму та динамічного програмування для кожної згенерованої суми (amount)
results = []
for amount in amounts:
    time_greedy = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
    time_dp = timeit.timeit(lambda: find_min_coins(amount), number=1000)
    
    greedy_result, greedy_total = find_coins_greedy(amount)
    dp_result, dp_total = find_min_coins(amount)
    
    results.append([amount, time_greedy, greedy_total, time_dp, dp_total])

# Виведення результатів тестування
print("\nAmount || Greedy: s | сoins || DP:     s |  сoins")
for result in results:
    print(f"{result[0]:>6} || {result[1]:>9.7f} | {result[2]:>5} || {result[3]:>6.7f} | {result[4]:>6}")


""" Результат:

Результат жадібного алгоритму для видачі решти для суми 113: {50: 2, 10: 1, 2: 1, 1: 1} (Кількість монет: 5)
Результат динамічного програмування для видачі решти для суми 113: {50: 2, 10: 1, 2: 1, 1: 1} (Кількість монет: 5)

Згенеровані випадкові суми для порвіняння швидкості виконання: [95, 151, 483, 497, 863]

Amount || Greedy: s | сoins || DP:     s |  сoins
    95 || 0.0006727 |     4 || 0.0829640 |      4
   151 || 0.0005773 |     4 || 0.1287578 |      4
   483 || 0.0009742 |    13 || 0.4733289 |     13
   497 || 0.0007661 |    13 || 0.4507949 |     13
   863 || 0.0012116 |    20 || 0.8812348 |     20
"""
