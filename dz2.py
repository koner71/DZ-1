# 1
# my_list = [2, 'dva', False, 83.11]
# my_type = type(my_list)
#
#     for el in my_list:
#         type(my_list[el])
#     print(my_type)
# 2
# my_list = list(input("Введите количество элементов списка "))
# for el in range(1, len(my_list), 2):
#     my_list[el], my_list[el - 1] = my_list[el - 1], my_list[el]
#     el += 2
# print(my_list)
# 3
# vvod = int(input('Введите число от 1 до 12 - '))
# my_dict = {1: 'zima', 2: 'vesna', 3: 'leto', 4: 'osenb'}
# my_list = ('zima', 'vesna', 'leto', 'osenb')
# if vvod == 1 or vvod == 2 or vvod == 12:
#     print(my_dict.get(1))
#     print(my_list[0])
# elif vvod == 3 or vvod == 4 or vvod == 5:
#     print(my_dict.get(2))
#     print(my_list[1])
# elif vvod == 6 or vvod == 7 or vvod == 8:
#     print(my_dict.get(3))
#     print(my_list[2])
# elif vvod == 9 or vvod == 10 or vvod == 11:
#     print(my_dict.get(4))
#     print(my_list[3])
# else:
#     print('число не вошло в интервал')
# 4
# my_str = input('vvedi stroku: ')
# my_word = []
# num = 1
# for el in range(my_str.count(' ') + 1):
#     my_word = my_str.split()
#     if len(str(my_word)) <= 10:
#         print(f'{num} {my_word [el]}')
#         num += 1
#     else:
#         print(f'{num} {my_word [el] [0:10]}')
#         num += 1
# 5
# list = [7, 5, 3, 3, 2]
# # print(list)
# number = int(input('Введите любое число: '))
# # while number != 100:
# for i in range(len(list)):
#     if list[i] == number:
#         list.insert(i + 1, number)
#         # print(list)
#         break
#     elif list[0] < number:
#         list.insert(0, number)
#     elif list[-1] > number:
#         list.append(number)
#     elif list[i] > number and list[i + 1] < number:
#         list.insert(i + 1, number)
# print(f'Новый список - {list}')
# # break
#6
goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 0
feature_ = None
control = None
while True:
    control = input("For quit press 'Q', for continue press 'Enter', for analytics press 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Input feature "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))


# goods = int(input("Введите количество товара "))
# n = 1
# my_dict = []
# my_list = []
# my_analys = {}
# while n <= goods:
#     my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
#                     'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
#     my_list.append((n, my_dict))
#     n += 1
#     my_analys = dict(
#         {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
#          'ед': my_dict.get('ед')})
# print(my_list)
# print(my_analys)