#input

name = input("What is your name?")
print(name)

a=input()
#result: 'Nastya'

#type casting - приведение типов
#int(x) float(x) str(x)

a = 'hello'
b = 100
c = 3.14
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

#in console, but we use print()

age = input('How old are you?')
print(age)
numberAge = int(age)
print(numberAge/2)


#isinstance - checking of type

a = 'string'
print(isinstance(a, int))

#exponentiation(power)
#если участников в выражении больше 2-х, справа налево расчёт
#first one 3 ** 2 = 9, second one 2 ** 9 = 512

print(2 ** 3 ** 2)

#на ноль делить нельзя, ноль делить на всё что хочешь можно

#string's concatenation

name = 'Nastya'
age = '32'
phone = '+3751111111'
userData = name + age + phone
separator = " | "
userData1 = name + separator + age  + separator + phone

# string's replication - умножение строки на число

'cat' * 99
99 * 'cat'

name = '5'
age = '34'
phone = '+3674444444'
sep = ', '
userData2 = f'{name}{sep} {age}{sep} {phone}'
print(userData2)

#keywords

import keyword
keyword.kwlist


