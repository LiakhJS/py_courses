#calculator

a = int(input())
b = int(input())
print(a,"+",b,"=",a+b)
print(a,"-",b,"=",a-b)
print(a,"*",b,"=",a*b)
print(a,"/",b,"=",a/b)

a, b = int(input("a=")), int(input("b="))
print (a,b)

#строка-формата f-strings since python 3.6

first_number, second_number = int(
    input("Put First number:")), int(
        input("Put Second number:"))

print('\nResults of maths! + - * /')
print(f'{first_number} + {second_number} = {first_number + second_number}')
print(f'{first_number} - {second_number} = {first_number - second_number}')
print(f'{first_number} * {second_number} = {first_number * second_number}')
print(f'{first_number} / {second_number} = {first_number / second_number}')

# import this in console

import this
