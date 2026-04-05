# # Lists
# li = [1, 2, 3, 4, 5]
# newLi = li.copy() # копирует 
# newLi[1] = 9999
# a = 1
# b = 1
# print(id(a))
# print(id(b))
# liNew = li # ссылка, будет отображение в первом списке, если изменить второй
# removedVal = li.pop()
# print(removedVal)
# li.pop(1)
# print(li)
# del li[-1]
# print(li)
# li.clear()
# print(len(li))

# # Task
# n = int(input('Сколкьо чисел хочешь ввести?'))
# print(type(n))
# userList = []
# for i in range(n) :
#     userList.append(5)              
# else :
#     results = sum(userList)
#     print('originals=', userList)
#     userList.sort()
#     print('sorted=', userList)
#     userList.reverse()
#     print('reverse', userList)
#     print('len=', len(userList))
#     print('sum=', results)

# # Task by value
# li = [1, 2, 4, 67868, 9, 56, 44, 6]
# for value in li:
#     print(value, end=" ")

# # Task by index
# li = [1, 2, 4, 67868, 9, 56, 44, 6]
# # range(x) - 0 before x is not included
# for index in range(len(li)) :
#     print('index', index)
#     print('value', li[index])

# # Enumerate
# li = ['блокнот', 'ручка', 'пальчик', 'арбузик']
# counter = 0
# for i in li :
#     print(i, end=' ')
#     counter += 1
# else :
#      print(counter)

# li = ['блокнот', 'ручка', 'пальчик', 'арбузик']
# for i, value in enumerate(li) :
#     print(i, value, end=' ')
    
# # Slices
# li = [3, 5, 6, 2, 8, 6, 4]
# # [index] не позволяет сделать срез
# # [startIndex:endIndex]
# print(li[2:5])
# print(li)
# print(li[:5], li[2:])

# # Task 
# print(3 in li)
# result = 0
# for val in li :
#     result +=val
# print(result)

# # Set type - множество, только уникальные ключи, нет индексов, изменяемый
# li = [3, 5, 6, 2, 8, 6, 4, 3, 5, 6, 2, 8, 6, 4]
# se = {3, 5, 6, 2, 8, 6, 4, 3, 5, 6, 2, 8, 6, 4}
# print(se)
# newSet = set(li)
# print(newSet)
# li = list(set(li))
# print(li)
# se = set() # type(se) - set
# # se = {} # type(se) - dict
# se.add(3333)
# print(se)
# se.add(8)
# #se.remove(2)
# #se.discard(1)

# # Lab 3.4
# my_list = [3, 5, 6, 2, 8, 6, 4, 3, 5, 6, 2, 8, 6, 4]
# my_list = list(set(my_list))
# print(my_list)

# #List comprehension
# st = "ersdkfjesojfseojosj"
# li = []
# for char in st :
#   if char in "aeoyuqi" :
#     li.append(char.upper())
#   else :
#     li.append(char*3)
    
# print(li)

# result = [char.upper() for char in st if char not in "aeoyuqi"  ]
# print(result)

# li2 = []
# for char in st :
#   if char not in "aeoyuqi" :
#     li2.append(char.upper())
# print(li2)

# # How many numbers do you wanna enter
# userlist = [int(input('-->')) for i in range(int(input('how many?')))]
# print(userlist)

# # Task
# sep = ' '
# numbers = input()
# numbers.split(sep)
# li = [int(val) for val in numbers.split(sep)]
# print(li)
# print(sum(li))
# print(len(li))

# # Froxenset type фиксированное значение - константа
# # List in list многомерные массивы
# li = [1, 2, 3, 4, 5]
# li[0]
# li = [[1,2,3],[2], [3,2], [4], [5]]
# print(li[0][1])

# #   2
# #   1
# #   Z
# # 0
# # Y
# # 0
# # 1
# # 2 X 0 1 2

# # Inside list - запятая [a, b, s ,]

# # Shorts
# # Можно пропустить, ничего не делать, чтобы не было ошибки
# for i in range(100) :
#   pass

