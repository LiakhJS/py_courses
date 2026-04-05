# # 5.1 Високосный год
# def isLeapYear (year) :
#     """...Is year is leap --> """
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# yearsExamples = [1876, 2000, 2016, 1987]
# results = [False, True, True, False]
# for i in range(len(yearsExamples)) :
#     year = yearsExamples[i]
#     print(year, '-->', end=' ')
#     result = isLeapYear(year)
#     if result == results[i] :
#         print('Success')
#     else :
#         print('Failure')

# # 5.3 Factorial
# def func(num):
#     factorial = 1
#     if num < 0 :
#         return
#     if num <= 1 :
#         return 1

#     for i in range(1, num + 1) :
#         factorial *= i
#     return factorial


# print('Factorial is:', 
#       func(num = int(input('Enter a number:'))))

# # 5.4 Fibonacci numbers
# def fibonacci(num):
  
#     if num < 1 :
#         return None
#     if num < 3 :
#         return 1
    
#     firstNum = secondNum = 1

#     for i in range(2, num) :
#             firstNum, secondNum = secondNum, firstNum + secondNum
#     return secondNum

# for i in range(-1, 25):
#     print(fibonacci(i))

