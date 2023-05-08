# print(bin(16)) # функция, представляющая число в двоичной системе счисления
#
# print(0b10 & 0b11) # & - это побитовое И
# print(0b10 | 0b11) # | - эжто побитовой ИЛИ

# проверка на чётность

# def is_even(some_number: int) -> bool:
#     return not some_number & 1
#
# print(is_even(4235345345435))

# проверка - является ли число степенью 2
#
# def is_power(some_number:int) -> bool:
#     if some_number & (some_number - 1) == 0:
#         return True
#     return False
#
# print(is_power(256))

# Задача FizzBuzz O(n)

# def fizzbuzz():
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print('FizzBuzz')
#         elif i % 5 == 0:
#             print('Buzz')
#         elif i % 3 == 0:
#             print('Fizz')
#         else:
#             print(i)
#
# fizzbuzz()

# Наибольший общий делитель O(n)

# def get_big_del() -> int:
#
#     big_del = 0
#
#     while True:
#
#         some_number_one = int(input("Enter first number: "))
#         some_number_two = int(input("Enter second number: "))
#
#         if some_number_one < 0 or some_number_two < 0:
#             print('Numbers must be positive!')
#             continue
#         if some_number_one == 0:
#             return some_number_two
#         if some_number_two == 0:
#             return some_number_one
#
#         if some_number_one > some_number_two:
#             smaller = some_number_two
#         else:
#             smaller = some_number_one
#         for i in range(1, smaller + 1):
#             if some_number_one % i == 0 and some_number_two % i == 0:
#                 big_del = i
#         return big_del
#
# print(get_big_del())

# Алгоритм Евклида

# def evclid() -> int:
#     while True:
#         some_number_one = int(input("Enter first number: "))
#         some_number_two = int(input("Enter second number: "))
#         if some_number_two == 0:
#             some_number_one, some_number_two = some_number_two, some_number_one
#         while some_number_two != 0:
#             some_number_one, some_number_two = some_number_two, some_number_one % some_number_two
#         return some_number_one
#
# print(evclid())

# простые числа O(n)
#
# def is_prime(some_number: int) -> int:
#     for i in range(2, some_number):
#         if some_number % i == 0:
#             return False
#     return True
#
# print(is_prime(7))

