#1

# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
# платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
# время выполнения расчёта для конкретных значений необходимо запускать скрипт с
# # параметрами.
#
import os

# Получаем значения параметров из аргументов командной строки
выработка_в_часах = int(os.sys.argv[1])
ставка_в_час = float(os.sys.argv[2])
премия = float(os.sys.argv[3])

# Рассчитываем заработную плату
заработная_плата = (выработка_в_часах * ставка_в_час) + премия

# Выводим результат
print(f'Заработная плата сотрудника: {заработная_плата}')

#2

# Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его
# формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

result = []
new_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
for el in range(1, len(new_list)):
    if new_list[el] > new_list[el - 1]:
        result.append(new_list[el])
print(f"Новый список: {result}")


#3

# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну
# строку.
# Подсказка: используйте функцию range() и генератор.


final = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(final)


#4

# Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию. Элементы выведите в
# порядке их следования в исходном списке. Для выполнения задания обязательно используйте
# генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
gen = []
for el in range(len(list)):
    if list[el] != list[el - 1]:
        gen.append(list[el])
print(f"Новый список: {gen}")


#5

# Реализовать формирование списка, используя функцию range() и возможности генератора. В
# список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить
# результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

nums = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(lambda x, y: x * y, nums))

#6

# Реализовать два небольших скрипта:
# ● итератор, генерирующий целые числа, начиная с указанного;
# ● итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
# создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
# завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором
# повторение элементов списка прекратится.

#6.1

from itertools import count
from itertools import cycle


for i in count(3):
    if i > 10:
        break
    else:
        print(i)

#7

# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное
# значение. При вызове функции должен создаваться объект-генератор. Функция вызывается
# следующим образом: for el in fact(n). Она отвечает за получение факториала числа. В цикле
# нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал
# четырёх 4! = 1 * 2 * 3 * 4 = 24.



#6.2


list = [1, 2, 3, 4, 4]
q = 0
for i in cycle(list):
    if q > 50:
        break
    print(i)
    q += 1

#7

# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное
# значение. При вызове функции должен создаваться объект-генератор. Функция вызывается
# следующим образом: for el in fact(n). Она отвечает за получение факториала числа. В цикле
# нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал
# четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact(n):
    """
    Генератор для факториала числа.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result

# Пример использования
n = 4
for el in fact(n):
    print(el)