# #Дан список: 
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
#  кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
#  и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? 
# Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его 
# реализации позже. Главное: дополнить числа до двух разрядов нулём!

# list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градуов']
# list2 = []
# for i in range(len(list)):
#     if list[i].isdigit():
#         list2.append('"')
#         list2.append(f'{int(list[i]):02d}')
#         list2.append('"')
#     elif list[i][0] == '+':
#         list2.append('"')
#         list2.append(f'+{int(list[i]):02d}')
#         list2.append('"')
#     else:
#         list2.append(list[i])
# print('Список до обработки: ')
# print(list2)
# print('Список после обработки: ')
# print(' '.join(list2))


# Дан список, содержащий искажённые данные с должностями и именами сотрудников: 
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. 
# Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' 
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному 
# виду. Можно ли при этом не создавать новый список?

# list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# for i in range(len(list)):
#     list[i] = list[i].split()
#     print(f'Привет, {(list[i][-1]).capitalize()}!')

# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде 
# <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, 
# как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать 
# (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, 
# написав минимум кода?
# list = [5, 3.05, 2.20, 4.55, 7.4, 5.45, 8.33, 7.90, 3.45, 6.25]
# store_id = id(list)
# a = ','
# print(f'Исходный список: {list}')
# print(f'Добавили рубли и копейки: ') 
# for i in range(len(list)):
#     temp = str(f"{float(list[i]):.2f}").split(".")
#     list[i] = f'{temp[0]} руб {temp[1]} коп'
#     if i == len(list) - 1:
#         a = "\n"
#     print(list[i],end=a)

# print(f'Сортировка по возрастанию:')
# print(f"id перед сортировкой {store_id}")
# list.sort()
# print(list)
# print(f"id после сортировки {id(list)}")

# print(f'Сортировка по убыванию:')
# list2 = list.copy()
# list2.sort(reverse=True)
# print(list2)

# print('Цены пяти самых дорогих товаров')
# list_5_max = []
# for i in range(0,5):
#     list_5_max.append(list2[i])
# print(list_5_max)