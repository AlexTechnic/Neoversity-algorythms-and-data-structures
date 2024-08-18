""" Модуль для побудови дерева Піфагора за допомогою рекурсії """


import turtle
import math


# Функція для побудови гілки дерева Піфагора за допомогою рекурсії
def draw_pythagoras_tree(t, branch_length, angle, depth):
    if depth > 0:
        # Малюємо гілку
        t.forward(branch_length)
        
        # Поворот для малювання лівої гілки
        t.left(angle)
        
        # Рекурсивно малюємо ліву гілку
        draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, angle, depth - 1)
        
        # Поворот для малювання правої гілки
        t.right(angle * 2)
        
        # Рекурсивно малюємо праву гілку
        draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, angle, depth - 1)
        
        # Повертаємося до початкової позиції
        t.left(angle)
        t.backward(branch_length)

# Основна функція для налаштування екрану та запуску малювання дерева Піфагора
def main():
    # Створюємо екран та налаштовуємо параметри
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    # Створюємо "пензлика" та налаштовуємо його параметри
    t = turtle.Turtle()
    t.speed("fastest")
    
    # Початкова позиція та напрямок "пензлика"
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    
    # Запитуємо у користувача бажаний рівень рекурсії
    depth = int(input("Введіть рівень рекурсії для дерева Піфагора (наприклад, 6): "))
    
    # Параметри фрактала (довжина гілки та кут повороту)
    branch_length = 100  # Довжина початкової гілки
    angle = 45  # Кут повороту
    
    # Запускаємо рекурсивне малювання дерева
    draw_pythagoras_tree(t, branch_length, angle, depth)
    
    # Закриваємо екран по кліку користувача
    screen.exitonclick()

if __name__ == "__main__":
    main()


""" Результатом виконання буде вікно з малюнком дерева Піфагора, побудованого за допомогою рекурсії. """
