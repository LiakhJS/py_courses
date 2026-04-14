# # Lecture 7
# # Tuple кортежи () еизменяемые

# li = [1, 2, 3, 4, 5]
# se = (1,2,3,4,1,2,3,4)
# tp = (1,2,3,4,5)
# print(type(li))
# print(type(se))
# print(type(tp))

# a = 1
# aa = 1.
# tp1 = 1,
# tp = 1,2,3,4,5
# print(tp)
# tp = .0, 1., 4, 5., .9
# print(tp)

# print(tp[-1])

# for val in tp :
#   print(val)
  
# for index in range(len(tp)) :
#     print(tp[index])

# tp = (777,) + tp[1:]
# print(tp)

# tp = list(tp)
# print(tp)

# tp[1] = 88888
# print(tp)

# tp = tuple(tp)
# print(tp)

# tp = 1,1,1,1,1
# print(tp)

# def useful(n) :
#   tt = ()
#   for i in range(n) :
#     # Error tt = tt + i
#     tt = tt + (i, )
    
#   return tt
    
# result = useful(4)

# # Task 2
# # Распаковка кортежа
# a, b, c, d = useful(4)
# print(a, b, c, d)

# # Task 3
# # Распакавать часть
# a, b, *c = useful(4)
# print(a, b, c)

# # Распаковать элементы , которые нужны
# # Заменить ненужный элемент нижним подч _

#  _, b, c, _ = useful(4)

