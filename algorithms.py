from datetime import datetime # импорт библиотеки datetime

start = datetime.now() # время старта (время прямо сейчас)
a = 0
for i in range(1000):
    a += i**100
end = datetime.now() # время окончания (время прямо сейчас)
td = (end - start).total_seconds() * 10**3 # разница времени в миллисекундах
print(f'{td:.03f}ms') # вывод времени в миллисекундах с тремя знаками после запятой

