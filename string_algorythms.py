# import string

# выявление анаграмм (разные слова, содержащие одинаковые буквы)
# O(n * log(n)), потому что использует встроенную функцию сортировки
# которая как раз таки O(n * log(n))

# def check_anagram(some_string_one: str, some_string_two: str) -> bool:
#     some_string_one = some_string_one.replace(' ', '').lower()
#     some_string_two = some_string_two.replace(' ', '').lower()
#     if sorted(some_string_one) == sorted(some_string_two):
#         return True
#     else:
#         return False
#
# s1 = 'Emperor Octavian'
# s2 = 'Captain over Rome'
# print(check_anagram(s1, s2))

# Выявление палиндромов

# def check_palindrom(some_string_one: str, some_string_two: str) -> bool:
#     if some_string_one.lower() == some_string_two[::-1].lower():
#         return True
#     else:
#         return False
#
# s1 = 'Шалаш'
# s2 = 'шалаш'
# print(check_palindrom(s1, s2))

# поиск последней цифры в строке O(n)

# def last_digit_in_string(some_string: str) -> str:
#     digit = [symbol for symbol in some_string if symbol.isdigit()][-1]
#     return digit
#
# print(last_digit_in_string('Я 4 куска говна съел, 3 из них были полнейшим дерьмом, лишь 1 вкусный.'))

# Шифр Цезаря O(n)

# def ceasar(some_string: str, key: int) -> str:
#     uppercase = string.ascii_uppercase
#     lowercase = string.ascii_lowercase
#     encrypt = ''
#     for char in some_string:
#         if char in uppercase:
#             new = (uppercase.index(char) + key) % 26
#             encrypt += uppercase[new]
#         elif char in lowercase:
#             new = (lowercase.index(char) + key) % 26
#             encrypt += lowercase[new]
#         else:
#             encrypt += char
#     return encrypt
#
# print(ceasar('Munchkin', 3))

# Используйте списковое включение, чтобы из следующего списка вернуть
# список всех слов, содержащих более четырех символов: ["selftaught",
# "code", "sit", "eat", "programming", "dinner", "one", "two", "coding",
# "a", "tech"].

# def return_words(some_list: list, count_of_symbols_in_word: int) -> list:
#     words = [word for word in some_list if len(word) > count_of_symbols_in_word]
#     return words
#
# list_of_words = ["selftaught", "code", "sit", "eat", "programming", "dinner", "one", "two", "coding", "a", "tech"]
# print(return_words(list_of_words, 4))


