# # AVG SCORE
# def writingOfTheResultsOfTheGame(student_class):

#     we_are_active = True
#     while we_are_active :
#         name = input("Имя студента -->")

#         mark = int(input("Его/её оценка -->"))

#         if name in student_class :
#             student_class.update(
#                 {
#                 name: student_class.get(name)+(mark,)
#                 }
#             )
#         else :
#             student_class.update(
#                 {
#                 name:(mark,)
#                 }
#             )
#         if input('+ или stop -->').strip() == 'stop':
#             we_are_active = False
        
            
#     print(student_class)
#     print('Загрузка среднего счёта ..')

# def main():
#     student_class = {}
#     writingOfTheResultsOfTheGame(student_class)

#     for name in student_class.keys():
#         print(name, '--СРЕДНИЙ СЧЁТ--', \
#         sum(student_class.get(name))/\
#         len(student_class.get(name))
#                 )
# main()

