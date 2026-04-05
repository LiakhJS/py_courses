# # 25-03-2026
# print(1,2,3,4,5, sep=')')
# age = 9999
# print(age)
# type(age)
# isinstance(age, str)
# number = input('введи число')
# type(number)
# number = int(number)
# print(type(number))
# number2 = number / 9
# print(number2)
# name = 'nastya'
# print(name*7)
# a = 'vasya'
# print(name + a)
# print(a + name)

# # Lection 2_2
# # If-else (1 tab - important!!!)
# password = '12345'
# password = '12345*'
# if password == "12345":
#     print('ok')
# else:
#     print('ne ok')

# # If-elif-else (if else-if else) 
# age = 16
# age = 13
# if age <= 6:
#     print('small')
# elif age <= 14:
#     print('average')
# elif age <= 15:
#     print('average2')
# else:
#     print('adult')

# # Однострочник
# key = '777'
# if key == '777':
#     print(1)
# else:
#     print(2)

# check = True if key == '777' else False
# print(check)

# # Find the largest of several numbers and print it out
# number1, number2 = int(input('num1:')), int(input('num2:'))
# print(number1, number2)
# if number1 > number2:
#     print('number1 is bigger than number2')
# elif number1 == number2 :
#     print('numbers are equal')
# elif number1 < number2 :
#     print('number1 is smaller than number2')
# else :
#     print('task is finished!')

# # Second variant
# number1, number2 = int(input('num1:')), int(input('num2:'))
# print(number1, number2)
# result = 0;
# if number1 > number2 :
#     result = number1
# else :
#     result = number2
# print(result)

# # Third variant
# number1, number2 = int(input('num1:')), int(input('num2:'))
# print(number1, number2)
# print(number1 if number1 > number2 else number2)

# # Match case
# age = int(input('write the number:'))
# match age :
#     case 16:
#         print('average')
#     case 18:
#         print('adult')
#     case 5:
#         print('small')

# # While (must be ending loop)
# text = 'hello'
# counter = 1
# while counter <= 5 :
#     print(text)
#     print(counter)
#     counter += 1

# # Odd, even Чётные нечетные числа 
# odd, even = 0, 0
# number = int(input('enter the number or zero to stop it'))
# while number != 0 :
#     if number % 2 == 0:
#         print('this is even number')
#         even += 1
#     else :
#         print('this is odd number')
#         odd += 1
#     number = int(input('enter the number or zero to stop it'))
# print(odd , even)
# print(
#       'odd > even' if odd > even else 'even > odd')

# # Range

# for number in range(1, 10) :
#     print(number, end=' ')
# print('\n')
# for number in range(10) :
#     print(number, end=' ')
# print('\n')
# for number in range(1, 10, 2) :
#     print(number, end=' ')
# print('\n')
# for i in range(1, 11) :
#     print(i**2 + (i+i)**2 + i*(i+i+i))

# # Time.sleep - first of all - import time
# import time
# for i in range(5) :
#     time.sleep(1)
#     print('hello, Sonya', i)

# # Break continue - only inside loop
# for i in range(5) :
#     if i == 3:
#         break       
#     time.sleep(1)
#     print('hello, Sonya', i)

#     for i in range(5) :
#         if i == 3:
#             continue  
#     time.sleep(1)
#     print('hello, Sonya', i)

# # Task
# HP = 100
# time_limit = 60
# while time_limit >= 0 :
#     if HP <= 0 :
#         break
#     print('time limit', time_limit)
#     print('осталось HP', HP)
#     if time_limit % 2 == 0 :
#         HP -= 15
#         print('вы потеряли от удара в голову 15 HP')
#     if time_limit % 2 != 0 :
#         HP -= 5
#         print('вы потеряли от удара 5 HP')
    
#     time_limit -=1
# print('game over')

# # In - not in - for strings
# word = 'word'
# print('d' in word)
# print('r' in word)


# file = """ergrerereh
# ergerghreg
# rdgergtru56uhb
# sdfdsfwreweyryi
# """
# if 'erg' in file :
#     print('da')
# else :
#     print('net')

# # AND OR NOT
# name = 'X'
# phone = '123'
# age = 18
# if name == 'X' and phone == '123' and age == 18:
#     print('все 3 совпали')

# if name == 'x' or phone == '123' or age == 18:
#     print('что-то')

