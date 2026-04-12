# Todo List Lab 6 release
todos = {
    1:{
        "todo":"Do something nice for someone you care about",
        "completed":False,
        "userId":152,
        "priority":5,
      },
    2:{
        "todo":"Memorize a poem",
        "completed":True,
        "userId":13,
        "priority":5,
      },
    3:{
        "todo":"Watch a classic movie",
        "completed":True,
        "userId":68,
        "priority":5,
      },
        }

# CRUD
# Хранить задачи
# добавить задачу
# печатать задачи
# обновлять
# удалить
# менюшка
# общая функция с циклом внутри

task = {
        "id":1,
        "todo":"Do something nice for someone you care about",
        "completed":False,
        "userId":152,
        "priority":5,
        }
def create_task(max_id):
    #auto_id = (max(todos.keys()) + 1)
    auto_id = max_id + 1
    new_task = {
        "todo":0,
        "completed":0,
        "userId":0,
        "priority":0,
        }

    todo = input("todo:")
    completed = bool(input("completed (1 для true или пустой ввод false):"))
    userId = int(input("userId:"))
    priority = int(input("priority:"))
  
    new_task = {
        auto_id:{
              "todo":todo,
              "completed":completed,
              "userId":userId,
              "priority":priority,
        }
        }
    
    return new_task

print(create_task(max(todos.keys())))

def read_tasks():
      for t_key, t_dict in todos.items():
            print("Task id:", t_key)
            for key, value in t_dict.items():
                  print("    ",key, ":", value)
            print("____________________________")

def read_task(t_id):
      res_task = todos.get(t_id, -1)
      if res_task == -1 :
            print("Задача не найдена с id:", t_id)
            return
      print("Task id:", t_id)

      for key, value in res_task.items():
          print("    ",key, ":", value)
      print("____________________________")

def delete_task(t_id):
      res_task = todos.get(t_id, -1)
      if res_task == -1 :
            print("Задача не найдена с id:", t_id)
            return
      print("Task id:", t_id)

      todos.pop(t_id)
      print("Задача с id:", t_id, "удалена")
      print("____________________________")


def main():
      print("1: create, " \
            "2: read task by id, " \
            "3: read all tasks, " \
            "4: delete task by id, 5: exit "
            )
      operation = int(input("-->"))
      while operation != 5:
          if operation == 1:
            task = create_task(max(todos.keys()))
            todos.update(task)
          elif operation == 2:
            t_id = int(input("Введи t_id:"))
            read_task(t_id)
          elif operation == 3:
            read_tasks()
          elif operation == 4:
            t_id = int(input("Введи t_id:"))
            delete_task(t_id)
          else:
            print("Я не понял, попробуй ещё раз")
          

          print("1: create, " \
            "2: read task by id, " \
            "3: read all tasks, " \
            "4: delete task by id, 5: exit "
            )
          operation = int(input("-->"))

      print("Пока-пока")

main()      

# print(todos)
# print(todos.get(2))
# print(todos.keys())
# print(max(todos.keys()))

# #id для следующей задачи
# auto_id = (max(todos.keys()) + 1)
# print(auto_id)

# res = todos.get(1)
# for k, v in res.items() :
#     print(k, v)

# print(str(todos.get(1)))
    
      



    