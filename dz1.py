#DZ2
# chas = int(input("vvdi chas - "))
# min = int(input("vvedi min - "))
# sec = int(input("vvedi sec - "))
# if chas <= 10:
#     chas = str("0" + str(chas))
# if min < 10:
#     min = str("0" + str(min))
# if sec < 10:
#     sec = str("0" + str(sec))
# print(chas, ":", min, ":", sec)
#Решение из разбора
time = int(input("Введите время в секундах - "))
hours = time // 3600
minutes = (time // 60) - (hours * 60)
seconds = time % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')

#DZ3
# a = int(input('vvedi chislo - '))
# b = a + a
# c = a + a + a
# print(a + b + c)

#DZ4
# i = number = int(input('Введите целое число: '))
# r = -1
# while i > 10:
#     d = i % 10
#     i //= 10
#     if d > r:
#         r = d
# print(r)

#DZ5
# vir = int(input('Введите выручку - '))
# izd = int(input('Введите издержки - '))
# r = int(vir) / int(izd)
# if vir < izd:
#     print('У вас убытки')
# else:
#     ludi = input('Введите число сотрудников - ')
#     n = int(r) / int(ludi)
#     print(f'У вас прибыль в размере {r}, на одного сотрудника это получается {n} рублей')

#DZ6
# day_one_km = int(input('Километров пробежал в первый день - '))
# last_day = int(input('Лимит километров - '))
# day = 1
# while day_one_km < last_day:
#     day_one_km = (day_one_km / 10) + day_one_km
#     day = day + 1
# print(f'на {day} день спортсмен пробежал не менее {last_day} км')