import timeit

# Реалізація алгоритму Боєра-Мура (Boyer-Moore)
def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1

# Реалізація алгоритму Кнута-Морріса-Пратта (KMP)
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)
    lps = compute_lps(pattern)
    i = j = 0
    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
        if j == M:
            return i - j
    return -1

# Реалізація алгоритму Рабіна-Карпа
def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)
    base = 256
    modulus = 101
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    h_multiplier = pow(base, substring_length - 1) % modulus
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return i
        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus
    return -1

# Функція для зчитування текстового файлу
def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

# Основна функція для порівняння алгоритмів
def compare_algorithms(text1, text2, search_str1, search_str2):
    algorithms = {
        "Boyer-Moore": boyer_moore_search,
        "KMP": kmp_search,
        "Rabin-Karp": rabin_karp_search
    }

    for search_str in [search_str1, search_str2]:
        times_text1 = {}
        times_text2 = {}

        print(f"\nПошук підрядка '{search_str}':")

        for alg_name, alg_func in algorithms.items():
            # Вимірювання часу для тексту 1
            time1 = timeit.timeit(lambda: alg_func(text1, search_str), number=1)
            times_text1[alg_name] = time1

            # Вимірювання часу для тексту 2
            time2 = timeit.timeit(lambda: alg_func(text2, search_str), number=1)
            times_text2[alg_name] = time2

            print(f"{alg_name}:")
            print(f"Текст 1: {time1:.8f} секунд")
            print(f"Текст 2: {time2:.8f} секунд")

        # Визначення найшвидшого алгоритму для кожного тексту
        fastest_alg1 = min(times_text1, key=times_text1.get)
        fastest_alg2 = min(times_text2, key=times_text2.get)

        print(f"\nНайшвидший алгоритм для тексту 1: {fastest_alg1}")
        print(f"Найшвидший алгоритм для тексту 2: {fastest_alg2}")

# Імена файлів для зчитування тексту (вказувати повний шлях до файлів)
text_file1 = r"D:\Programming\GoIT Neoversity\Neoversity-algorythms-and-data-structures\goit-algo-hw-05\article1.txt"
text_file2 = r"D:\Programming\GoIT Neoversity\Neoversity-algorythms-and-data-structures\goit-algo-hw-05\article2.txt"

# Підрядки для пошуку у тексті файлів
search_str1 = r"алгоритм"
search_str2 = r"круасан"

# Зчитування тексту з файлів
text1 = read_file(text_file1)
text2 = read_file(text_file2)


# Порівняння швидкості алгоритмів для текстів з файлів 
compare_algorithms(text1, text2, search_str1, search_str2)

"""
Результат виконання:

Пошук підрядка 'алгоритм':
Boyer-Moore:
Текст 1: 0.00002900 секунд
Текст 2: 0.00020920 секунд
KMP:
Текст 1: 0.00004040 секунд
Текст 2: 0.00049050 секунд
Rabin-Karp:
Текст 1: 0.00009640 секунд
Текст 2: 0.00268220 секунд

Найшвидший алгоритм для тексту 1: Boyer-Moore
Найшвидший алгоритм для тексту 2: Boyer-Moore

Пошук підрядка 'круасан':
Boyer-Moore:
Текст 1: 0.00103370 секунд
Текст 2: 0.00142660 секунд
KMP:
Текст 1: 0.00288310 секунд
Текст 2: 0.00329400 секунд
Rabin-Karp:
Текст 1: 0.00582600 секунд
Текст 2: 0.00806090 секунд

Найшвидший алгоритм для тексту 1: Boyer-Moore
Найшвидший алгоритм для тексту 2: Boyer-Moore
"""