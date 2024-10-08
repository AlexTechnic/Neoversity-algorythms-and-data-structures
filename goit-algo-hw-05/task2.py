def binary_search(arr, x, epsilon=1e-9):
    """
    Реалізація двійкового пошуку для відсортованого масиву з дробовими числами.
    Повертає кількість ітерацій і найменше значення, більше або рівне x.

    :param arr: Відсортований масив з дробовими числами.
    :param x: Значення, яке необхідно знайти.
    :param epsilon: Поріг точності для порівняння дробових чисел.
    :return: Кортеж, де перший елемент - кількість ітерацій для пошуку,
             а другий - верхня межа (найменший елемент, який є більшим або рівним цільовому значенню).
    """
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        # Якщо x дорівнює значенню в середині масиву (з урахуванням точності epsilon)
        if abs(arr[mid] - x) < epsilon:
            return (iterations, arr[mid])

        # Якщо x більше, ігноруємо ліву половину
        elif arr[mid] < x:
            low = mid + 1

        # Якщо x менше, ігноруємо праву половину і оновлюємо upper_bound
        else:
            upper_bound = arr[mid]
            high = mid - 1

    # Після завершення циклу повертаємо кількість ітерацій і upper_bound
    return (iterations, upper_bound)

# Тестування функції
arr = [2.1, 3.5, 4.7, 10.0, 40.2]
x = 5.0

result = binary_search(arr, x)
print(result)  # результат: (2, 10.0)   (2 ітерації, верхня межа - 10.0)

# Пояснення: алгоритм двійкового пошуку для відсортованого масиву розділяє масив на дві частини:
# [2.1, 3.5, 4.7] та [10.0, 40.2]. Після першої ітерації алгоритм знаходить,
# що x = 5.0 більше за середнє значення 4.7, тому ігнорує ліву частину.
# На другій ітерації алгоритм знаходить, що x = 5.0 менше за 10.0, тому
# оновлює верхню межу upper_bound = 10.0 і ігнорує праву частину.
# Після цього алгоритм завершує роботу і повертає результат (2, 10.0).
