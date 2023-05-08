# numbers = [1, 8, 32, 91, 5, 15, 9, 100, 3]

# линейный поиск, 4 варианта:

# def check_number(some_list: list, some_number: int) -> bool:
#     if some_number in some_list: return True
#     else: return False

# def check_number_2(some_list: list, some_number: int) -> bool:
#     for i in some_list:
#         if i == some_number: return True
#     return False
# #
# print(9 in numbers) # вернётся булевое значение
#
# print('a' in 'apple') # можно даже символы в слове проверять

# print(check_number_2(numbers, 9))

# это метод пербора элементов, мы проходим по каждому элементу списка и проверяем значения.
# сложность алгоритма в данном случае О(n), в лучшем случае О(1) - если нужный нам элемент первый в списке,
# средняя сложность О(n/2)
# линейный поиск используется если данные не отсортированы.
# если данные отсортированы, то используем...

# двоичный (бинарный) поиск:

# def binary_search(some_list: list, some_number: int) -> bool:
#     first = 0
#     last = len(some_list) - 1
#     while last >=first:
#         middle_number = (first + last) // 2
#         if some_number == some_list[middle_number]:
#             return True
#         else:
#             if some_number > some_list[middle_number]:
#                 first = middle_number + 1
#             else:
#                 last = middle_number - 1
#     return False
#
# print(sorted(numbers))
#
# print(binary_search(numbers, 9))
#
# мы берём отсортированный список, определяем начало и конец списка (-1),
# затем начинаем цикл до тех пор, пока в списке еще есть элементы
# в цикле находим середину списка, проверяем, является ли середина искомым числом,
# если да, то возвращаем истину, если нет, то продолжаем цикл с условием
# если искомое число больше центрального, то первое число становится первым числом после середины,
# а если искомое число меньше середины, то последнее число становится числом перед серединой
# таким образом мы уменьшаем список до тех пор, пока не найдётся наше число
# если числа нет, то возвращается ложь
# сложность алгоритма О(log(n))
#
# у питона есть встроенные средства двоичного поиска

# from bisect import bisect_left # библиотека для двоичного поиска
#
# sorted_fruits = ['apple', 'banana', 'orange', 'plum']
# print(bisect_left(sorted_fruits, 'banana')) # показывает индекс искомого элемента
# print(bisect_left(sorted_fruits, 'kiwi')) # показывает индекс где мог бы быть искомый элемент если его нет в списке

# для проверки вхождения элемента используем функцию

# def binary_search(some_list: list, some_element: str) -> bool:
#     index = bisect_left(some_list, some_element)
#     if index <= len(some_list) and some_list[index] == some_element:
#         return True
#     return False
#
# # получаем индекс элемента и проверяем имеется ли этот индекс в списке
# # и если элемент списка по этому индексу равен искомому элементу, то истина
# # в противном случае ложь
#
# print(binary_search(sorted_fruits, 'banana'))


# print(ord('@')) # определение юникода символа (может быть полезно при поиске символов)

# names = ['Ann', 'Bob', 'Mary', 'Zoltan']
#
# def new_search(some_list: list, some_element: str) -> bool:
#     index = bisect_left(some_list, some_element)
#     if index <= len(some_list) and some_list[index] == some_element:
#         return True
#     return False
#
# print(new_search(names, 'Ann'))