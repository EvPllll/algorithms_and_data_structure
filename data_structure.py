# Абстрактный тип данных — это характеристика структуры данных, тогда
# как структура данных — фактическая реализация.
#
# Линейная структура данных упорядочивает элементы данных последовательно, в то время как нелинейная
# структура данных связывает данные непоследовательно.
#
# Обход — проход от первого элемента в структуре данных к последнему

# У статической структуры данных фиксированный размер, в то время
# как динамическая структура данных может увеличиваться или уменьшаться в размерах.

# Массив - это структура данных, которая сохраняет элементы с индексами
# в непрерывном блоке памяти. Массивы часто однородны и статичны.
# Однородная структура данных — структура, которая может хранить элементы только
# одного типа данных, например целые числа (integer) или строки. Статическая
# структура данных — структура данных, размер которой нельзя изменить после
# ее создания.

# Список Python представляет собой неоднородный массив переменной длины.
# Массив переменной длины — этомассив, размер которогоможет измениться после создания.
# Гетерогенный массив — массив, содержащий разные типы данных.

import array # импортирование массива (встроенный модуль)

arr = array.array('f', (1.0, 1.5, 2.0, 2.5)) # f -float, далее в скобках перечисление элементов

# в массиве может храниться только один тип данных
# в библиотеке NumPy работа с массивами такая же быстрая как на низкоуровневых языках типа С

# перемещение нулей O(n)

zero_list = [8, 0, 12, 0, 3]

def zero_moving(some_list: list) -> list: # функция для перемещения нулей в конец списка
    zero_index = 0
    for index, element in enumerate(some_list):
        if element != 0:
            some_list[zero_index] = element
            if zero_index != index:
                some_list[index] = 0
            zero_index += 1
    return some_list

# Объединение списков

movie_list = [ "Interstellar", "Inception",
 "The Prestige", "Insomnia",
 "Batman Begins"
 ]

ratings_list = [1, 10, 10, 8, 6]

# Поиск дубликатов в списке

a_list = [
 "Susan Adams",
 "Kwame Goodall",
 "Jill Hampton",
 "Susan Adams"]

def return_dublicate(some_iterable: list) -> list:
    dublicates = []
    a_set = set()

    for item in some_iterable:
        first_length = len(a_set)
        a_set.add(item)
        second_length = len(a_set)
        if first_length == second_length:
            dublicates.append(item)

    return dublicates

# Пересечение множеств

list1 = [2, 43, 48, 62, 64, 28, 3]
list2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]

# первый вариант

def return_intersection_one(some_list_one: list, some_list_two: list) -> list:
    intersection_list = [item for item in list1 if item in list2]
    return intersection_list

# второй вариант

def return_intersection_two(some_list_one: list, some_list_two: list) -> list:
    set1 = set(some_list_one)
    set2 = set(some_list_two)
    return list(set1.intersection(set2))

# Homework

# У вас есть массив an_array, состоящий из неотрицательных целых чисел.
# Верните массив, в котором все нечетные элементы массива an_array следуют
# за всеми четными элементами an_array.

number_list = [value for value in range(25)]

def even_noteven(some_list: list) -> list:
    even_list = sorted([item for item in some_list if item % 2 == 0])
    noteven_list = sorted([item for item in some_list if item % 2 != 0])
    even_list.extend(noteven_list)
    return even_list

if __name__ == '__main__':
    print(arr) # вывод объекта
    print(*arr) # распаковка и вывод
    print(arr[1]) # вывод элемента массива по индексу

    print(zero_moving(zero_list)) # перемещение нулей в конец списка (массива)
    print(list(zip(movie_list, ratings_list))) # объединение списков встроенной функцией zip
    print(return_dublicate(a_list)) # вывод дубликатов из списка
    print(return_intersection_one(list1, list2)) # первый вариант поиска дубликатов
    print(return_intersection_two(list1, list2)) # второй вариант поиска дубликатов
    print(even_noteven(number_list)) # Homework completed




