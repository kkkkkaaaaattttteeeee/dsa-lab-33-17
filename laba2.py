# Задание 1.1. Работа с математическими операциями в Python

print("=== Задание 1.1: Работа с математическими операциями ===")
print()

# 1. Считать с клавиатуры три произвольных числа, найти минимальное среди них и вывести на экран
print("--- Задание 1: Минимальное из трех чисел ---")
print("Введите три произвольных числа:")

# Вводим три числа
num1_input = input("Введите первое число: ")
num2_input = input("Введите второе число: ")
num3_input = input("Введите третье число: ")

# Преобразуем в числа с плавающей точкой (для поддержки любых чисел)
num1 = float(num1_input)
num2 = float(num2_input)
num3 = float(num3_input)

# Находим минимальное (без использования min())
min_number = num1
if num2 < min_number:
    min_number = num2
if num3 < min_number:
    min_number = num3

print(f"Минимальное число: {min_number}")
print()

# 2. Считать с клавиатуры три произвольных числа, вывести в консоль те числа, которые попадают в интервал [1, 50]
print("--- Задание 2: Числа в интервале [1, 50] ---")
print("Введите три произвольных числа:")

# Вводим три числа
a_input = input("Введите первое число: ")
b_input = input("Введите второе число: ")
c_input = input("Введите третье число: ")

# Преобразуем в числа
a = float(a_input)
b = float(b_input)
c = float(c_input)

print("Числа, попадающие в интервал [1, 50]:", end=" ")
found = False

# Проверяем каждое число
if 1 <= a <= 50:
    print(a, end=" ")
    found = True
if 1 <= b <= 50:
    print(b, end=" ")
    found = True
if 1 <= c <= 50:
    print(c, end=" ")
    found = True

if not found:
    print("нет чисел в указанном интервале", end="")
print("\n")

# 3. Считать с клавиатуры вещественное число m. Посчитать и вывести каждый член последовательности
print("--- Задание 3: Последовательность [(1 * m), (2 * m), ..., (10 * m)] ---")

m_input = input("Введите вещественное число m: ")
m = float(m_input)

print(f"Последовательность для m = {m}:")
for i in range(1, 11):
    result = i * m
    print(f"{i} * {m} = {result}")
print()

# 4. Считать с клавиатуры непустую произвольную последовательность целых чисел
print("--- Задание 4: Работа с последовательностью целых чисел ---")
print("Введите последовательность целых чисел.")
print("Для завершения ввода введите 'stop' или оставьте строку пустой:")

# Создаем список для хранения чисел
numbers = []

# Вводим числа до тех пор, пока пользователь не введет 'stop' или пустую строку
while True:
    user_input = input("Введите целое число (или 'stop' для завершения): ")
    
    # Проверка на завершение ввода
    if user_input == "" or user_input.lower() == "stop":
        # Проверяем, что последовательность не пустая
        if len(numbers) == 0:
            print("Ошибка: последовательность не может быть пустой. Введите хотя бы одно число.")
            continue
        else:
            break
    
    # Проверяем, является ли введенная строка целым числом
    is_negative = False
    start_idx = 0
    
    # Проверяем первый символ на знак минус
    if user_input[0] == '-':
        is_negative = True
        start_idx = 1
    
    # Проверяем, что все остальные символы - цифры
    is_valid = True
    if start_idx == 0 and len(user_input) == 0:
        is_valid = False
    else:
        for i in range(start_idx, len(user_input)):
            if user_input[i] < '0' or user_input[i] > '9':
                is_valid = False
                break
    
    if is_valid and len(user_input) > start_idx:
        # Преобразуем строку в число вручную
        num = 0
        for i in range(start_idx, len(user_input)):
            digit = ord(user_input[i]) - ord('0')
            num = num * 10 + digit
        
        if is_negative:
            num = -num
        
        numbers.append(num)
    else:
        print("Ошибка: введите целое число или 'stop' для завершения")

# Выводим введенную последовательность
print(f"\nВведенная последовательность:", end=" ")
for i in range(len(numbers)):
    print(numbers[i], end=" ")
print()
print(f"Длина последовательности: {len(numbers)}")
print()

# i. Сумма всех чисел последовательности (используя while)
print("--- i.Сумма всех чисел (while) ---")
sum_numbers = 0
index = 0

while index < len(numbers):
    sum_numbers += numbers[index]
    index += 1

print(f"Сумма всех чисел: {sum_numbers}")
print()

# ii. Количество всех чисел последовательности (используя while)
print("--- ii. Количество всех чисел (while) ---")
count_numbers = 0
index = 0

while index < len(numbers):
    count_numbers += 1
    index += 1

print(f"Количество всех чисел: {count_numbers}")

#Задание 2.13 Кучерова
#1. Считать с клавиатуры произвольную строку, в которой есть одна открывающаяся и одна закрывающаяся скобки.
#2. Вывести на экран все символы, расположенные внутри этих скобок

print("=== Задание 2.13: Символы внутри скобок ===")

# 1. Считываем строку с клавиатуры
text = input("Введите строку с одной открывающей и одной закрывающей скобкой: ")

# Находим позиции открывающей и закрывающей скобок
open_index = -1
close_index = -1

# Ищем открывающую скобку '('
i = 0
while i < len(text):
    if text[i] == '(':
        open_index = i
        break
    i += 1

# Если нашли открывающую скобку, ищем закрывающую ')'
if open_index != -1:
    i = open_index + 1
    while i < len(text):
        if text[i] == ')':
            close_index = i
            break
        i += 1

# Проверяем, что обе скобки найдены и расположены корректно
if open_index != -1 and close_index != -1 and close_index > open_index:
    print("Символы внутри скобок:", end=" ")
    
    # Выводим все символы между скобками
    i = open_index + 1
    while i < close_index:
        print(text[i], end="")
        i += 1
    print()  # Переход на новую строку
    
    # Дополнительно можно вывести информацию о количестве символов
    count_inside = close_index - open_index - 1
    print(f"Количество символов внутри скобок: {count_inside}")
    
else:
    print("В строке нет корректно расположенных скобок (одна открывающая и одна закрывающая)")

# Задание 3.2 Обедина 
# 1. Считать из параметров командной строки одномерный массив, состоящий из N целочисленных элементов.
# 2. Найти минимальный элемент.
# 3. Вывести индекс минимального элемента на экран.
# 4. Вывести в одну строку все положительные числа массива.
# 5. Вывести в одну строку все отрицательные числа массива.
import sys

print("=== Задание 3.2: Работа с одномерным массивом ===")

# Функция для безопасного получения аргументов командной строки
def get_command_line_args():
    """
    Получает аргументы командной строки, игнорируя аргументы IPython/Jupyter
    """
    args = []
    
    # Пропускаем первый аргумент (имя скрипта)
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        # Пропускаем аргументы, которые начинаются с '-' (это опции интерпретатора)
        if arg.startswith('-'):
            continue
        try:
            # Пробуем преобразовать в целое число
            num = int(arg)
            args.append(num)
        except ValueError:
            # Если не число, пропускаем
            continue
    
    return args

# 1. Считываем параметры командной строки
array = get_command_line_args()

# Если аргументы не найдены, предлагаем ввести их вручную
if len(array) == 0:
    print("Аргументы командной строки не найдены или содержат нечисловые значения.")
    print("Введите целые числа через пробел:")
    user_input = input()
    
    # Ручной парсинг введенной строки без использования split
    temp_array = []
    current_number = ""
    
    for char in user_input:
        if char != ' ':
            current_number += char
        else:
            if current_number:
                try:
                    temp_array.append(int(current_number))
                except ValueError:
                    print(f"Предупреждение: '{current_number}' не является целым числом и будет пропущено")
                current_number = ""
    
    # Добавляем последнее число
    if current_number:
        try:
            temp_array.append(int(current_number))
        except ValueError:
            print(f"Предупреждение: '{current_number}' не является целым числом и будет пропущено")
    
    array = temp_array

# Проверяем, что массив не пустой
if len(array) == 0:
    print("Ошибка: массив не может быть пустым. Программа завершена.")
    sys.exit(1)

# Выводим исходный массив
print(f"Исходный массив: {array}")
print(f"Размер массива N = {len(array)}")
print()

# 2. Находим минимальный элемент
min_element = array[0]
min_index = 0

for i in range(1, len(array)):
    if array[i] < min_element:
        min_element = array[i]
        min_index = i

# 3. Выводим индекс минимального элемента
print(f"Минимальный элемент: {min_element}")
print(f"Индекс минимального элемента: {min_index}")
print()

# 4. Выводим в одну строку все положительные числа
print("Положительные числа:", end=" ")
positive_exists = False
for i in range(len(array)):
    if array[i] > 0:
        print(array[i], end=" ")
        positive_exists = True

if not positive_exists:
    print("(нет положительных чисел)", end="")
print()  # Переход на новую строку

# 5. Выводим в одну строку все отрицательные числа
print("Отрицательные числа:", end=" ")
negative_exists = False
for i in range(len(array)):
    if array[i] < 0:
        print(array[i], end=" ")
        negative_exists = True

if not negative_exists:
    print("(нет отрицательных чисел)", end="")
print()

# Дополнительно: выводим нули
print("Нулевые элементы:", end=" ")
zero_exists = False
for i in range(len(array)):
    if array[i] == 0:
        print(array[i], end=" ")
        zero_exists = True

if not zero_exists:
    print("(нет нулевых элементов)", end="")
print()
