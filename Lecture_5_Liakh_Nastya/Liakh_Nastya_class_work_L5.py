# # Simple functions
# # def - определить
# def GiveMeTheMessage(text) :
#     message = input(text)

#     return message

# result = GiveMeTheMessage('give me text')

# # Зашшифрованное письмо и дешифровка  с помощью функции
# message = 'Привет! Это послание из прошлого!'
# key = 5
# print(message)
# secured_message = ''
# for i in message :
#     secured_message += chr(ord(i)+5)
# print(secured_message)
# print('Дешифровка...')
# for i in secured_message :
#     print(chr(ord(i)-key), end = ' ')