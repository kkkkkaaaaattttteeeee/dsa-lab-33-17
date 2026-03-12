import requests
import random

# Базовый URL сервера
BASE_URL = 'http://127.0.0.1:5000'

print("=" * 50)
print("Лабораторная работа №3")
print("=" * 50)

# 1. GET запрос
param = random.randint(1, 10)
response_get = requests.get(f'{BASE_URL}/number/', params={'param': param})
data_get = response_get.json()
print(f"\n1. GET запрос:")
print(f"   Параметр: param={param}")
print(f"   Ответ: {data_get}")

# 2. POST запрос
json_param = random.randint(1, 10)
headers = {'Content-Type': 'application/json'}
response_post = requests.post(
    f'{BASE_URL}/number/', 
    json={'jsonParam': json_param},
    headers=headers
)
data_post = response_post.json()
print(f"\n2. POST запрос:")
print(f"   Тело: {{'jsonParam': {json_param}}}")
print(f"   Ответ: {data_post}")

# 3. DELETE запрос
response_delete = requests.delete(f'{BASE_URL}/number/')
data_delete = response_delete.json()
print(f"\n3. DELETE запрос:")
print(f"   Ответ: {data_delete}")

# 4. Вычисление выражения
print(f"\n" + "=" * 50)
print("Вычисление выражения:")

# Начинаем с первого числа
result = data_get['number']
expression = f"{data_get['number']}"

# Применяем первую операцию (из GET)
if data_get['operation'] == 'sum':
    result = result + data_post['number']
    expression += f" + {data_post['number']}"
elif data_get['operation'] == 'sub':
    result = result - data_post['number']
    expression += f" - {data_post['number']}"
elif data_get['operation'] == 'mul':
    result = result * data_post['number']
    expression += f" * {data_post['number']}"
elif data_get['operation'] == 'div':
    result = result / data_post['number']
    expression += f" / {data_post['number']}"

print(f"После операции {data_get['operation']}: {expression} = {result}")

# Применяем вторую операцию (из POST)
if data_post['operation'] == 'sum':
    result = result + data_delete['number']
    expression += f" + {data_delete['number']}"
elif data_post['operation'] == 'sub':
    result = result - data_delete['number']
    expression += f" - {data_delete['number']}"
elif data_post['operation'] == 'mul':
    result = result * data_delete['number']
    expression += f" * {data_delete['number']}"
elif data_post['operation'] == 'div':
    result = result / data_delete['number']
    expression += f" / {data_delete['number']}"

print(f"После операции {data_post['operation']}: {expression} = {result}")

# Последняя операция (из DELETE) - не применяется
print(f"Операция из DELETE ({data_delete['operation']}) не применяется")

# Приводим к int
final_result = int(result)
print(f"\nИТОГ: {expression} = {final_result} (int)")
print("=" * 50)