# # List
# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)
# stack.append(5)
# stack.pop()
# stack.pop()
# print(stack)

# # STACK
# # касса 1 2 3 4 5 6
# # 
# # выходить 1 2 3 4 5 6

# class Stack:
#     def __init__(self):
#         self.__storage = []
#     def push(self, value):
#         self.__storage.append(value)
#         print("добавляю:", value)
#     def pop(self):
#         try:
#             res = self.__storage.pop()
#             print("удалил:", res)
#         except IndexError:
#             print("Твой склад пуст")
#         except:
#             print("какая то ошибка.")
#     def get_stack(self):
#         return self.__storage


# sklad1 = Stack()
# sklad1.push(2)
# sklad1.push(3)
# sklad1.push(66666)
# sklad1.pop()
# sklad1.pop()
# sklad1.pop()
# sklad1.pop()
# print(sklad1.get_stack())
# sklad1.pop()
# sklad1.push(5453)
# print(sklad1.get_stack())
# sklad1.push(232)
# print(sklad1.get_stack())
# sklad1.pop()
# sklad1.pop()
# sklad1.pop()

# # Stack - склады

# class Storage:
#     def __init__(self):
#         self.__items = []
#     def priemka(self, value):
#         self.__items.append(value)
#         print("Приемка товара на склад:", value)
#     def otgruzka(self):
#         try:
#             res = self.__items.pop()
#             print("Отгрузка товара со склада:", res)
#         except IndexError:
#             print("Твой склад пуст")
#         except:
#             print("какая то ошибка отгрузки на складе.")
#     def get_items(self):
#         return self.__items
    
# skladik = Storage()
# print(skladik.get_items())
# skladik.priemka("Стиралка")
# skladik.priemka("холодос")
# skladik.priemka("Комп")
# print(skladik.get_items())
# skladik.otgruzka()
# skladik.otgruzka()
# skladik.otgruzka()
# skladik.otgruzka()

