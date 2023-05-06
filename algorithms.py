# БАЗОВЫЕ ПОНЯТИЯ

from datetime import datetime # импортируем библиотеку datetime

def dec_test_time(func): # функция декоратор с параметром получаемой функции
    def wrapper(*args, **kwargs): # функция декоратор с множеством параметров
        start = datetime.now() # определяем время старта
        result = func(*args, **kwargs) # функция, которую декорируют с множеством параметров
        end = datetime.now() # время окончания
        delta_time = (end - start).total_seconds() * 10**3 # разница во времени в миллисекундах
        print(f'Time executing: {delta_time} ms') # вывод времени
        return result # если функция в параметре декоратора возвращает результат, то возвращаем результат и тут
    return wrapper # возвращаем декоратор

@dec_test_time # таким образом применяем декоратор к функции
def my_program(a, n):
    for i in range(n):
        a += i**100
    return a

res = my_program(0, 10000000)
print(res)

# определение эффективности алгоритма по времени выполнения - не самое лучшее решение
# лучше определять эффективность по кол-ву шагов до конца выполнения программы

for i in range(6):
    print(i)
    # 6 шагов

a = 0
for i in range(6):
    print(i)
    a += i
    # 11 шагов




