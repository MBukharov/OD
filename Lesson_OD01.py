# Алгоритм программы:
# 1) Ввод строки
# 2) Проверка на палиндром
# 3) Вывод итогового сообщения

stroka = input('Введите строку: ')
if stroka == stroka[::-1]:
    print('Строка является палиндромом')
else:
    print('Строка не является палиндромом')