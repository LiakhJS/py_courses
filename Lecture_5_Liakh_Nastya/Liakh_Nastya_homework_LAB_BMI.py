# from time import sleep

# BANNER = """
# ██████╗  ██████╗ ██████╗ ██╗   ██╗    ███╗   ███╗ █████╗ ███████╗███████╗
# ██╔══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝    ████╗ ████║██╔══██╗██╔════╝██╔════╝
# ██████╔╝██║   ██║██║  ██║ ╚████╔╝     ██╔████╔██║███████║███████╗███████╗
# ██╔══██╗██║   ██║██║  ██║  ╚██╔╝      ██║╚██╔╝██║██╔══██║╚════██║╚════██║
# ██████╔╝╚██████╔╝██████╔╝   ██║       ██║ ╚═╝ ██║██║  ██║███████║███████║
# ╚═════╝  ╚═════╝ ╚═════╝    ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝

#                 ██╗███╗   ██╗██████╗ ███████╗██╗  ██╗
#                 ██║████╗  ██║██╔══██╗██╔════╝╚██╗██╔╝
#                 ██║██╔██╗ ██║██║  ██║█████╗   ╚███╔╝ 
#                 ██║██║╚██╗██║██║  ██║██╔══╝   ██╔██╗ 
#                 ██║██║ ╚████║██████╔╝███████╗██╔╝ ██╗
#                 ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
# """

# #Функция определения BMI с введёнными от пользователя значениями
# def BMI(weight, height) :
#     if float(weight) < +1 or float(weight) <= 0 :
#         print('Неправильные значения')

#     return float(weight) / (float(height)/100)**2


# # Вывод текста
# def text(text=''):
#     sleep(2)
#     print(text)
#     sleep(2)

# # Логика для нахождения BMI
# def logicBMI(result) :
#     if result < 18.5 :
#         return "Ваш вес ниже нормального"
#     elif 18.5 <= result < 25. :
#         return "У Вас нормальный вес"
#     elif 25 <= result < 30. :
#         return "У Вас избыточный вес"
#     elif 30 <= result < 35. :
#         return "У Вас ожирение 1-й степени"
#     elif 35 <= result < 40. :
#         return "У Вас ожирение 2-й степени"
#     elif result >= 40. :
#         return "У Вас ожирение 3-й степени"
    

# # Функция нахождения BMI
# def BmiFunction():
#     print(BANNER)
#     text('Find your BMI! Dont wait! Right now!\nJust enter your height and weight! Lets do it!')
    
#     userName = input('Введите Ваше имя:')
#     userWeight = input('Введите Ваш вес:')
#     userHeight = input('Введите Ваш рост:')

#     userBmi = BMI(userWeight, userHeight)
#     print(userName + ",", "Ваш индекс массы тела равен ", round(userBmi, 2))

#     print(logicBMI(userBmi))

#     text('=BYE=')

# BmiFunction()

