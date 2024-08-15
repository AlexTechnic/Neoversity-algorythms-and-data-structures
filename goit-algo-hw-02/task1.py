import queue
import time

# Черга для заявок
request_queue = queue.Queue()

def generate_request(request_counter):
    """Функція генерує заявку та додає її до черги."""
    request_id = f"#{request_counter}"
    request_queue.put(request_id)
    print(f"Заявку {request_id} додано до черги.")

def process_request():
    """Обробляє заявку з черги."""
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Обробка заявки {request_id}...")
        time.sleep(1)  # Пауза обробки заявок на 1 секунду
        print(f"Заявку {request_id} оброблено.")
    else:
        print("Черга пуста. Немає заявок для обробки.")

def main():
    request_counter = 1  # Лічильник заявок

    max_requests = 5  # Максимальна кількість заявок

    while request_counter <= max_requests:
        # Генеруємо заявки, у цьому варіанті заявки генеруються автоматично, тому черга ніколи не буде пустою
        # Але якщо лічильник заявок буде більше ніж 'max_requests', то програма завершиться
        generate_request(request_counter)

        # Обробляємо заявку
        process_request()

        # Пауза між заявками
        time.sleep(1)
        
        request_counter += 1  # Збільшуємо лічильник після обробки заявки

    print("Досягнуто максимальну кількість заявок. Програма завершена.")

if __name__ == "__main__":
    main()