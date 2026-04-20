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

# class Terrier(Dog):
#     def __init__(self, name, age, color):
#         self.color = color
#         super().__init__(name, age)
#     def __repr__(self):
#         return super().__repr__() + f" |color:{self.color}"
   
# kelly = Terrier("Kelly", 5, "black")
# kelly.speak("HI")


# storage = []

# n = int(input("Сколько хочешь создать собак:"))

# for i in range(n):
#     dog_type = int(input("1 Bulldog 2 Terrier:"))
#     if dog_type == 1:
#         name = input("name:")
#         age = input("age:")
#         dog_bulldog = Bulldog(name, age)
#         storage.append(dog_bulldog)
        
#     elif dog_type == 2:
#         name = input("name:")
#         age = input("age:")
#         color = input("color:")
#         dog_terrier = Terrier(name, age, color)
#         storage.append(dog_terrier)
        
#     else:
#         print("не понимаю операцию")

#     storage[i].name
#     storage[i].age

# for dog in storage:
#     print(dog.name)
#     print(dog.age)

# # Инкапсуляция

# class Dog:
#     def __init__(self, name, age, password):
#         self.name = name
#         self.age = age
#         self.__password = password
#         self._olddata = "sfasfsfa"

#     def __repr__(self):
#         return f"repr: name:{self.name} |age:{self.age}"    
    
#     def speak(self, sound):
#         return f"{self.name} says {sound}"

# # Полиморфизм
#     def __add__(self, another_dog):
#         return self.age + another_dog.age

# d = Dog("D", 212, 124124124)
# d.__dict__
# d1 = Dog("D1", 11, 1232312)
# d2 = Dog("D2", 22, 234235235)
# print(d1 + d2)

