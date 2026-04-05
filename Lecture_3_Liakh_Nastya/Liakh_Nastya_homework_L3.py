# # 3.1 Замена центрального элемента
# list = [1, 2, 3, 4, 5]
# list[2] = int(input())
# del list[-1]
# print(list)
# print(len(list))

# # 3.3
# # Creating of list
# sortList = []
# howManyNumbers = int(input('How many mumbers?'))
# print(sortList)
# for i in range(howManyNumbers) :
#     sortList.append(int(input('Enter number to add:')))
# print(sortList)

# # Bubble Sort
# swap = True
# while swap:
#     swap = False
#     for i in range(len(sortList) - 1) :
#         if sortList[i] > sortList[i+1] :
#             sortList[i], sortList[i+1] = sortList[i+1], sortList[i]
#             swap = True
# print(sortList)
# sortList.reverse()
# print(sortList)

# # 3.5
# strOfNum = input('Enter numbers with spaces:')
# listOfInt = [int(el) for el in strOfNum.split()]
# print('Sum:', sum(listOfInt))

