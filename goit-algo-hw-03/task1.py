""" Щоб запустити програму, використовуйте командний рядок: 
python task1.py <src_dir> <dest_dir> 
де 
<src_dir> - шлях до вихідної директорії, 
<dest_dir> - шлях до директорії призначення (необов'язковий параметр, за замовчуванням 'dist'). 

Програма рекурсивно копіює файли з вихідної директорії та сортує їх у піддиректорії за розширенням файлів."""


import os
import shutil
import argparse

def parse_arguments():
    """Парсить аргументи командного рядка."""
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання і сортування файлів за розширенням.")
    parser.add_argument('src_dir', help="Шлях до вихідної директорії")
    parser.add_argument('dest_dir', nargs='?', default='dist', help="Шлях до директорії призначення (за замовчуванням 'dist')")
    return parser.parse_args()

def copy_and_sort_files(src_dir, dest_dir):
    """Рекурсивно копіює файли і сортує їх у піддиректорії на основі розширення файлів."""
    try:
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            if os.path.isdir(item_path):
                # Якщо елемент є директорією, рекурсивно обробляємо її
                copy_and_sort_files(item_path, dest_dir)
            elif os.path.isfile(item_path):
                # Якщо елемент є файлом, копіюємо його у відповідну піддиректорію
                file_extension = os.path.splitext(item)[1].lstrip('.').lower()
                if not file_extension:
                    file_extension = 'no_extension'  # Для файлів без розширення

                target_dir = os.path.join(dest_dir, file_extension)

                # Створюємо піддиректорію, якщо вона не існує
                os.makedirs(target_dir, exist_ok=True)

                # Копіюємо файл до відповідної піддиректорії
                shutil.copy2(item_path, target_dir)
                print(f"Файл {item} скопійовано до {target_dir}")

    except Exception as e:
        print(f"Виникла помилка: {e}")

def main():
    """Головна функція, яка виконує копіювання файлів."""
    args = parse_arguments()

    # Перевіряємо, чи існує вихідна директорія
    if not os.path.exists(args.src_dir):
        print(f"Вихідна директорія {args.src_dir} не існує.")
        return

    # Створюємо директорію призначення, якщо вона не існує
    os.makedirs(args.dest_dir, exist_ok=True)

    # Виконуємо рекурсивне копіювання та сортування файлів
    copy_and_sort_files(args.src_dir, args.dest_dir)

    print(f"Копіювання та сортування файлів завершено. Файли збережено у {args.dest_dir}.")

if __name__ == "__main__":
    main()

""" Результати виконання програми:

Файл README.md скопійовано до dist\md
Файл task1.py скопійовано до dist\py
Файл task2.py скопійовано до dist\py
Копіювання та сортування файлів завершено. Файли збережено у dist.

"""