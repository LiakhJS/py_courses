# #15.04

# class Car:
#     pass

# class Wallet:
#     pass

# class User:
#     pass

# class Animal:
#     pass

# mycar = Car()
# print(mycar)

# type(mycar)
# #__main__.Car

# mywal = Wallet()
# #<__main__.Wallet at 0x27e8fbea510>

# type(mywal)
# #type(mywal)

# # # у каждого кользователя
# # есть своё собственное
# # имя
# # телефон
# # почта

# class User:
#     def __init__(self, user_name, user_phone, user_email):
#         self.name = user_name
#         self.phone = user_phone
#         self.email = user_email

# stas = User("Stas", "232424234", "sdfsd@sfas.com")
# dima = User("Dima","3424234234234","dima@dima.com")

# print(dima.name, dima.phone)

# # 17.04
# class User:
#     def __init__(self, user_name, user_phone, user_email=""):
#         self.name = user_name
#         self.phone = user_phone
#         self.email = user_email

# u1 = User("Stas", "232424234", "sdfsd@sfas.com")
# u2 = User("Stas", "232424234")


# # переменная экземпляра
# self.name = 9999 

# class User:
#     counter = 0
#     def __init__(self, user_name, user_phone, user_email=""):
#         self.name = user_name
#         self.phone = user_phone
#         self.email = user_email
#         User.counter += 1

# class User:
#     counter = 0
#     def __init__(self, user_name, user_phone, age, user_email=""):
#         self.name = user_name
#         self.phone = user_phone
#         self.email = user_email
#         self.age = age
#         User.counter += 1
        
#     def get_name(self):
#         return self.name
        
#     def get_phone(self):
#         return self.phone
        
#     def get_email(self):
#         return self.email

#     def __len__(self):
#         return self.age
    
#     def __str__(self):
#         return f"name:{self.name} |phone:{self.phone} | age:{self.age} |email:{self.email}"

#     def __repr__(self):
#         return f"repr: name:{self.name} |phone:{self.phone} | age:{self.age} |email:{self.email}"
    
# u1 = User("Stas", "232424234", "sdfsd@sfas.com")
# print(u1)

# User.__dict__
# u1.__dict__

# # Наследование
# # Собака

# # Свойства
# # имя
# # возраст
# # вес

# # Методы
# # ходить
# # лежать
# # лаять
# # спать
# # есть

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"repr: name:{self.name} |age:{self.age}"    
    
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
    
# class Bulldog(Dog):
#     def walk(self, steps):
#         return f"{self.name} ходит {steps} шагов"

#     def speak(self, sound):
#         par_speak = super().speak(sound)
#         par_speak = par_speak.upper()
#         return "Bulldog speak\n" + par_speak 
        
#         # return "Bulldog speak\n" + super().speak(sound) 

# jimmy = Bulldog("Jim", 6)
# print(jimmy.speak('UFD'))

# class BlackCat(Dog):
#     pass

# petr = BlackCat("Petr", 77)
# BlackCat.__dict__
# Dog.__dict__
# petr.__dict__

