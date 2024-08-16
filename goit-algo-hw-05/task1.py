""" хеш-таблиця з доданим методом видалення delete для видалення пар ключ-значення """

class HashTable:
    def __init__(self, size):
        """
        Ініціалізація хеш-таблиці.
        
        :param size: Розмір хеш-таблиці (кількість слотів у таблиці).
        """
        self.size = size
        # Створення таблиці як списку списків. Кожен слот в таблиці буде містити список для розв'язання колізій методом ланцюгів.
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        """
        Хеш-функція для обчислення індексу в таблиці на основі ключа.
        
        :param key: Ключ для обчислення хешу.
        :return: Індекс в хеш-таблиці для зберігання значення.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Вставка пари ключ-значення в хеш-таблицю.
        
        :param key: Ключ для ідентифікації значення.
        :param value: Значення, яке буде зберігатися у таблиці.
        :return: True, якщо вставка пройшла успішно.
        """
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            # Якщо слот порожній, створюємо новий список і додаємо пару ключ-значення.
            self.table[key_hash] = list([key_value])
            return True
        else:
            # Перевірка, чи ключ вже існує в списку (у випадку колізії).
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    # Якщо ключ існує, оновлюємо його значення.
                    pair[1] = value
                    return True
            # Якщо ключ не знайдений, додаємо нову пару ключ-значення.
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        """
        Отримання значення за ключем із хеш-таблиці.
        
        :param key: Ключ для пошуку значення.
        :return: Значення, що відповідає ключу, або None, якщо ключ не знайдено.
        """
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            # Пошук ключа в списку, якщо він існує.
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        """
        Видалення пари ключ-значення з хеш-таблиці.
        
        :param key: Ключ, що потрібно видалити разом зі значенням.
        :return: True, якщо видалення пройшло успішно, або False, якщо ключ не знайдено.
        """
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for i in range(len(self.table[key_hash])):
                if self.table[key_hash][i][0] == key:
                    # Видаляємо пару ключ-значення зі списку
                    self.table[key_hash].pop(i)
                    return True
        return False

# Тестуємо хеш-таблицю:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print(H.get("apple"))   # Виведе: 10
print(H.get("orange"))  # Виведе: 20
print(H.get("banana"))  # Виведе: 30

# Тестуємо видалення:
H.delete("orange")
print(H.get("orange"))  # Виведе: None, оскільки ключ "orange" був видалений