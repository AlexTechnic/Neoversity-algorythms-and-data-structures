import timeit
import random


def insertion_sort(arr):
    """Сортування вставками"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    """Сортування злиттям"""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def sort_insertion():
    """Сортування вставками з використанням тестового набору даних"""
    return insertion_sort(test_data.copy())


def sort_merge():
    """Сортування злиттям з використанням тестового набору даних"""
    return merge_sort(test_data.copy())


def sort_timsort():
    """Сортування Timsort (вбудованого  в Python алгоритму) з використанням тестового набору даних"""
    return sorted(test_data.copy())


def measure_time():
    """Вимірювання часу для кожного алгоритму на різних наборах даних"""
    global test_data


    # Генерація тестових наборів даних
    small_data = [random.randint(1, 100) for _ in range(100)]
    medium_data = [random.randint(1, 1000) for _ in range(1000)]
    large_data = [random.randint(1, 10000) for _ in range(10000)]

    test_data = small_data
    print("Сортування вставками (малий набір):", timeit.timeit(sort_insertion, number=1))
    print("Сортування злиттям (малий набір):", timeit.timeit(sort_merge, number=1))
    print("Timsort (малий набір):", timeit.timeit(sort_timsort, number=1))

    test_data = medium_data
    print("\nСортування вставками (середній набір):", timeit.timeit(sort_insertion, number=1))
    print("Сортування злиттям (середній набір):", timeit.timeit(sort_merge, number=1))
    print("Timsort (середній набір):", timeit.timeit(sort_timsort, number=1))

    test_data = large_data
    print("\nСортування вставками (великий набір):", timeit.timeit(sort_insertion, number=1))
    print("Сортування злиттям (великий набір):", timeit.timeit(sort_merge, number=1))
    print("Timsort (великий набір):", timeit.timeit(sort_timsort, number=1))

if __name__ == "__main__":
    measure_time()


"""Було використано наступні тестові набори даних: 
малий, середній, великий - 100, 1000, 10000 елементів відповідно.

Результат виконання:

Сортування вставками (малий набір): 0.0006688000030408148
Сортування злиттям (малий набір): 0.0009494999976595864  
Timsort (малий набір): 3.680000008898787e-05

Сортування вставками (середній набір): 0.08420309999928577
Сортування злиттям (середній набір): 0.014626700001826975 
Timsort (середній набір): 0.00023099999816622585

Сортування вставками (великий набір): 8.072852199999033
Сортування злиттям (великий набір): 0.1243681000014476
Timsort (великий набір): 0.001251800000318326

Висновки щодо результатів:
1. Сортування злиттям виявилося швидшим за сортування вставками на всіх наборах даних.
2. Найшвидшим алгоритмом сортування є Timsort, який вбудований в Python.
3. Сортування злиттям виявилося швидшим за Timsort на малих і середніх наборах даних.
4. Сортування вставками виявилося найповільнішим на всіх наборах даних.
5. Сортування злиттям є оптимальним алгоритмом для сортування великих наборів даних.
"""