# CRUD
# хранить задачи - ок
# добавить задачу - ок create
# печатать задачи - ок read
# Обновляем +- update
# удалить - ок delete

# менюшка
# общая функция с циклом внутри и тп


def create_task(max_id):
    auto_id = max_id + 1

    todo = input("todo:")
    completed = bool(input("completed (1 Для True, пустой ввод для False):"))
    userId = int(input("userId:"))
    priority = int(input("priority:"))
    
    new_task = {auto_id:{
                "todo": todo,
                "completed": completed,
                "userId": userId,
                "priority": priority,
            }
        }
    
    return new_task


def read_tasks(todos):
    for tk, tdi in todos.items():
        
        print("Task id:", tk)
        
        for k, v in tdi.items():
            print("    ", k, ":", v)
        print("__________________________________")


def read_task(tid, todos):
    res_task = todos.get(tid, -1)
    
    if res_task == -1:
        print("задача не найдена с id:", tid)
        return
        
    print("Task id:", tid)
        
    for k, v in res_task.items():
        print("    ", k, ":", v)
        
    print("__________________________________")


def delete_task(tid, todos):
    res_task = todos.get(tid, -1)
    
    if res_task == -1:
        print("задача не найдена с id:", tid)
        return
        
    print("Task id:", tid)
    todos.pop(tid)   
    
    print("задача с id:", tid, "удалена.")    
    print("__________________________________")

