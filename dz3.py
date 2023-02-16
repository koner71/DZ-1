# 1

# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль.

def i_func(numb1, numb2):
    try:
        rezult = numb1 / numb2
    except ZeroDivisionError:
        return 'Деление на ноль'
    return rezult
print(i_func(int(input('Введи первое число: ')), int(input('Введи второе число: '))))

# 2

# Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.

def i_finc(name, second_name, year, city, email, tel):
     return (f'{name} {second_name}, {year}, {city}, {email}, {tel}')
print(i_finc(name='Artem', second_name='Kuznetsov', year=1996, city='Moscow', email='ak@mail.ru', tel='+7-495-777-77-77'))

# 3

# Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(num1=5, num2=4, num3=3):
    if num1 < num2 and num1 < num3:
        sum1 = num2 + num3
        return(f'Сумма наибольших чисел = {sum1}')
    elif num2 < num1 and num2 < num3:
        sum2 = num1 + num3
        return(f'Сумма наибольших числе = {sum2}')
    elif num3 < num1 and num3 < num2:
        sum3 = num1 + num2
        return (f'Сумма наибольших числе = {sum3}')
print(my_func())

# 4

# Программа принимает действительное положительное число x и целое отрицательное число
# y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции
# my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения
# числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
# помощью оператора **. Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.

# Решение 1
def my_func(x, y):
    step = x ** abs(y)
    return step
print(my_func(5, -3))

# Решение 2
def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y < 0:
        result = 1 / result
    return result
print(my_func(5, -3))

# 5

# Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
# Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
# добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.

def i_func():
    sum = 0
    while True:
        user_input = input('Введи числа через пробел (для выхода нажми "q"): ')
        if user_input == 'q':
            print('Выход')
            break
        numbers = user_input.split()
        for el in numbers:
            if el == 'q':
                print('выход')
                break
            else:
                sum += int(el)
        print('Сумма: ', sum)
    return
print(i_func())

#6

# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

#1 решение
def int_func():
    user_text = str(input('Введи слово с маленькой буквы: '))
    user_textprint = user_text.capitalize()
    return user_textprint
print(int_func())

#Ниже наброски кода до того, как нашел capitalize (не рабочий)

def int_func():
    user_text = str(input('Введи слово с маленькой буквы: '))
    user_textprint = user_text.capitalize()
    text = str(user_text.split())
    for el in text:
        if el[0].isupper() == True:
            print(f'{el[0]}{el[1:].lower}')
        else:
            print(f'{el[0].upper}{el[1:].lower}')
    return user_textprint
print(int_func())