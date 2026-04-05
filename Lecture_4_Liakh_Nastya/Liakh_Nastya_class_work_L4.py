# L4
a = 4
b, c, d, = 3, 6, 9
z = x = v = 9
st = 'rgergreg'
len(st)
li = []
li =[1, ]
print()
li.append(666)
print(li)
print(id(li))
li1 = li
print(li1)
li1[1] = 88
print(li, li1)
print(id(li1), id(li))
li2 = li.copy()
print(id(li2))
li3 = li[:]
print((li3))
#deepcopy
inner_list = [4, 3, 2]
outer_list = [1, 2, 3, inner_list, 5]
c1 = outer_list.copy()
print(c1)
inner_list[1] = 919
print(c1)
print(id(outer_list))
print(id(c1))
import copy
c2 = copy.deepcopy(outer_list)
inner_list[1] = 88888
print(outer_list, inner_list, c1, c2)
import calendar
print(calendar.isleap(2017)) #високосный нет
#строки ASCII - AMERICAN STANDART CODE FOR INFORMATION INTERCHANGE
st = 'strhgy'
for ch in st :
    print(ch, end =' ')

for index in range(len(st) ) :
    print(index, st[index])

# Ord - номер
alf = 'ahndbscahk"-+'
for char in alf :
    print(char, ord(char))
# Chr - символ
for i in range(100, 450) :
    print(chr(i), end=' ')

# Шифр сдвига - цезарь
m = 'ssdgsgdsgsg'
for i in m :
    print(i, ord(i), " | ", chr(ord(i)+5), ord(i)+5)

# Зашшифрованное письмо и дешифровка
message = 'Привет! Это послание из прошлого!'
key = 5
print(message)
secured_message = ''
for i in message :
    secured_message += chr(ord(i)+5)
print(secured_message)
print('Дешифровка...')
for i in secured_message :
    print(chr(ord(i)-key), end = ' ')

# Task
s = 'hello'
text = 'HELLO'
newHello = s[:2] + text + s[4:]
print(newHello)

# In not in
name = 'ldskldsihsil'
name.capitalize()
name.upper()
name.title()
c = 'c'
c.isalpha()
c.isalnum()

# Add postfix to the email
url = 'hotmail.*'
li = ['com', 'ru', 'by', 'tech']
urlList = []
for postfix in li :
    urlList.append(url.replace('*', postfix))
print(urlList)

# Удаление пробелов в строке
s = '     sdgssh                '
resultS = s.strip()
print(resultS)
print(s.split('d'))
#01.04.26