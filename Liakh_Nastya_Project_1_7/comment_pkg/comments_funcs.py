
def create_comment(max_id):
    auto_id = max_id + 1

    body = input("Напишшите свой комент:")
    username = input("Введи имя пользователя:")
    fullname = input("Введи фамилию пользователя или ник:")
    
    new_comment = {auto_id:{
        "body":body,
        "likes":1,
        "user":{
            "username":username,
            "fullName":fullname
            }
            }
            }
    
    return new_comment


def read_comments(comments):
    for comment_key, comment_di in comments.items():

        print("\n║ Коммент id:", comment_key) 
        print("║ Количество лайков:", comment_di['likes'])     
        print("║ Коммент:", comment_di['body'])      
        print("║ Пользователь:", comment_di['user']['username']
                        + '  ' + 
                    comment_di['user']['fullName'])
        
        print("__________________________________")


def read_comment(comment_id, comments):
    res_comment = comments.get(comment_id, -1)
    
    if res_comment == -1:
        print("Коммент с id:", comment_id, "не найден.")
        return     
       
    print("__________________________________")
    
    print("\n║ Количество лайков:", res_comment['likes'])     
    print("║ Сам коммент:", res_comment['body'])      
    print("║ Пользователь:", res_comment['user']['username']
                        + '  ' + 
                    res_comment['user']['fullName'])    
        
    print("__________________________________")


def delete_comment(cid, comments):
    res_comment = comments.get(cid, -1)
    
    if res_comment == -1:
        print("Коммент с id", cid, "не найден.")
        return
        
    comments.pop(cid)   
    
    print("Коммент с id", cid, "удален.") 

    print("__________________________________")


def max_likes_comments(comments, rotated_heavy_black, rotated_heavy_black_short):
    massive = []
    for comment_key, comment_di in comments.items():
        for k, v in comment_di.items():
            if k == 'likes':
                massive.append(v)        
        largest = max(massive)
        indices = [i for i, x in enumerate(massive) if x == largest]
        
    for comment_id, comment_key in comments.items(): 
       for i in indices:
            if comment_id == i + 1 :
                print( rotated_heavy_black_short, "Максимальное количество лайков:", 
                      comments[comment_id]['likes'], rotated_heavy_black_short
                      )
                print(rotated_heavy_black_short, "Сам коммент:", 
                      comments[comment_id]['body'], rotated_heavy_black_short)
                print(rotated_heavy_black_short, "Пользователь:", 
                    comments[comment_id]['user']['username']
                        + '  ' + 
                    comments[comment_id]['user']['fullName'], rotated_heavy_black_short)
                print(rotated_heavy_black, """
""")

