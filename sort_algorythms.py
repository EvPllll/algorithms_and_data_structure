# рекомендуется использовать встроенные алгоритмы сортироваки Python, т.к. они быстрее и проще

# ПУЗЫРЬКОВАЯ СОРТИРОВКА - стандартный случай O(n**2)

# def bubble_sort(some_list: list) -> list:
#     list_length = len(some_list) - 1
#     for i in range(list_length):
#         for j in range(list_length):
#             if some_list[j] > some_list[j + 1]:
#                 some_list[j], some_list[j + 1] = some_list[j + 1], some_list[j]
#     return some_list
#
# my_list = list(map(int, input().split()))
# print(bubble_sort(my_list))

# ПУЗЫРЬКОВАЯ СОРТИРОВКА - первое улучшение - O(n**2)
# мы можем добавить вычитание i во вложенном цикле, что бы каждую итерацию внешнего цикла
# последнее число не проверялось, т.к. заведомо известно, что после первой итерации последним числом
# будет наибольшее число

# def bubble_sort(some_list: list) -> list:
#     list_length = len(some_list) - 1
#     for i in range(list_length):
#         for j in range(list_length - i):
#             if some_list[j] > some_list[j + 1]:
#                 some_list[j], some_list[j + 1] = some_list[j + 1], some_list[j]
#     return some_list
#
# my_list = list(map(int, input().split()))
# print(bubble_sort(my_list))


# ПУЗЫРЬКОВАЯ СОРТИРОВКА - второе улучшение - O(n**2)
# добавляем переменную для отслеживания перемещений элементов в списке
# если перемещения были, то переходим к следующей итерации внешнего цикла,
# если перемещений не было, то значит список отсортирован и не имеет смысла больше проводить итерации

# def bubble_sort(some_list: list) -> list:
#     list_length = len(some_list) - 1
#     for i in range(list_length):
#         moving = False
#         for j in range(list_length - i):
#             if some_list[j] > some_list[j + 1]:
#                 some_list[j], some_list[j + 1] = some_list[j + 1], some_list[j]
#                 moving = True
#         if moving == False:
#             return some_list
#     return some_list
#
# # my_list = list(map(int, input().split()))
# my_string_list = list(input().split()) # работает и со строками
# print(bubble_sort(my_string_list))


# СОРТИРОВКА ВСТАВКАМИ O(n**2)
# Если данные почти отсортированы, то он превращается в O(n)

# def insertion_sort(some_list: list) -> list:
#     for i in range(1, len(some_list)):
#         value = some_list[i]
#         while i > 0 and some_list[i - 1] > value:
#             some_list[i] = some_list[i - 1]
#             i -= 1
#         some_list[i] = value
#     return some_list
#
# my_list = list(map(int, input().split()))
# print(insertion_sort(my_list))

# СОРТИРОВКА СЛИЯНИЕМ O(n * log(n))

# def merge_sort(some_list: list):
#     if len(some_list) > 1:
#         middle = len(some_list) // 2
#         left_half = some_list[:middle]
#         right_half = some_list[middle:]
#         merge_sort(left_half)
#         merge_sort(right_half)
#
#         left_ind = 0
#         right_ind = 0
#         some_list_ind = 0
#         while left_ind < len(left_half) and right_ind < len(right_half):
#             if left_half[left_ind] <= right_half[right_ind]:
#                 some_list[some_list_ind] = left_half[left_ind]
#                 left_ind += 1
#             else:
#                 some_list[some_list_ind] = right_half[right_ind]
#                 right_ind += 1
#             some_list_ind += 1
#
#         while left_ind < len(left_half):
#             some_list[some_list_ind] = left_half[left_ind]
#             left_ind += 1
#             some_list_ind += 1
#
#         while right_ind < len(right_half):
#             some_list[some_list_ind] = right_half[right_ind]
#             right_ind += 1
#             some_list_ind += 1
#
#
# my_list = list(map(int, input().split()))
# merge_sort(my_list)
# print(my_list)

# ВСТРОЕННЫЕ ФУНКЦИИ СОРТИРОВКИ - гибридная (слияние + вставка)

# sorted - возвращает новый список, работает с любыми итерируемыми объектами

# my_list = list(map(int, input().split()))
# print(sorted(my_list))
#
# print(sorted(my_list, reverse=True))
#
# my_string_list = ['edfsdf', 'gfgfgfd', 'r', '23425451234', 'ergb']
# # print(sorted(my_string_list, key=len))
# # print(sorted(my_string_list, key=len, reverse=True))
#
# # .sort - метод списка, меняет существующий список
#
# my_string_list.sort(reverse=True, key=len)
# print(my_string_list)