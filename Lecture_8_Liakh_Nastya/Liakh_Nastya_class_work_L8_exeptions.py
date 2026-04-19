# for i in range(5):
#     try:
#         # ZeroDivisionError ValueError 
#         cash = int(input("Сумму которую хочешь накопить?"))
#         m = int(input("Количество месяцев за которые хочешь накопить сумму?"))
#         res = cash / m
#         print(f"Тебе нужно откладывать {res} в месяц, чтобы за {m} месяцев накопить {cash}")
#     except ZeroDivisionError:
#         print("делить на ноль нельзя")
#     except ValueError:
#         print("не пытайся конвертировать строку из букв в int")
#     except:
#         print("Возникла ошибка, попробуй ещё раз")

# try:
#     # ZeroDivisionError ValueError 
#     cash = int(input("Сумму которую хочешь накопить?"))
#     m = int(input("Количество месяцев за которые хочешь накопить сумму?"))
#     res = cash / m
#     print(f"Тебе нужно откладывать {res} в месяц, чтобы за {m} месяцев накопить {cash}")
# except ZeroDivisionError as e:
#     print("делить на ноль нельзя")
#     print(e)
#     print(e.args)
# except ValueError as e:
#     print("не пытайся конвертировать строку из букв в int")
#     print(e)
#     print(e.args)
# except BaseException as e:
#     print("base")
# except:
#     print("Возникла ошибка, попробуй ещё раз")

# # AssertionError
# # если ни ноль, ни false, ни пустая строка и т.п., тогда ок, иначе ошибка
# assert 1
# # assert 0

# # Raise - помощник для проверки работы try/exept как задумано
# raise ZeroDivisionError('Делить на ноль нельзя')

