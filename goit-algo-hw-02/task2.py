from collections import deque


def is_palindrome(input_string):
    """Функція перевірки рядку на паліндромом за допомогою двосторонньої черги."""
    # Приводимо рядок до нижнього регістру та видаляємо пробіли
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())

    # Створюємо двосторонню чергу
    char_deque = deque(cleaned_string)

    # Порівнюємо символи з обох кінців черги за допомогою методів popleft() та pop() з модуля deque
    # Якщо на якомусь кроці символи не співпадають, то рядок не є паліндромом
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True


def main():
    input_string = input("Введіть рядок для перевірки: ")

    if is_palindrome(input_string):
        print("Рядок є паліндромом.")
    else:
        print("Рядок не є паліндромом.")


if __name__ == "__main__":
    main()