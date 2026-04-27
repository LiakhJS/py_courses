import tkinter as tk
from comment_pkg import comments_funcs as cf

comments = {
    1:{"body":"This is some awesome thinking!","likes":3,
     "user":{"username":"emmac","fullName":"Emma Wilson"}},
    2:{"body":"What terrific math skills you're showing!","postId":46,"likes":4,
     "user":{"username":"cameronp","fullName":"Cameron Perez"}},
    3:{"body":"You are an amazing writer!","likes":2,
     "user":{"username":"emilys","fullName":"Emily Johnson"}},
    4:{"body":"Wow! You have improved so much!","likes":1,
     "user":{"username":"braydenf","fullName":"Brayden Fleming"}},
    5:{"body":"Nice idea!","likes":1,
     "user":{"username":"wyattp","fullName":"Wyatt Perry"}},
    6:{"body":"You are showing excellent understanding!","likes":5,
     "user":{"username":"danielt","fullName":"Daniel Taylor"}},
    7:{"body":"This is clear, concise, and complete!","likes":1,
     "user":{"username":"jamesd","fullName":"James Davis"}},
    8:{"body":"What a powerful argument!","likes":0,
     "user":{"username":"lukec","fullName":"Luke Cooper"}},
    9:{"body":"I knew you could do it!","likes":3,
     "user":{"username":"jaces","fullName":"Jace Smith"}},
    10:{"body":"Wonderful ideas!","likes":0,
     "user":{"username":"noram","fullName":"Nora Mills"}},
    11:{"body":"It was a pleasure to grade this!","likes":8,
     "user":{"username":"mateob","fullName":"Mateo Bennett"}},
    12:{"body":"Keep up the incredible work!","likes":10,
     "user":{"username":"scarlettb","fullName":"Scarlett Bowman"}},
    13:{"body":"My goodness, how impressive!","likes":10,
     "user":{"username":"hunterg","fullName":"Hunter Gordon"}},
    14:{"body":"You're showing inventive ideas!","likes":8,
     "user":{"username":"jonathanp","fullName":"Jonathan Pierce"}},
    15:{"body":"You've shown so much growth!","likes":2,
     "user":{"username":"evelyns","fullName":"Evelyn Sanchez"}},
    16:{"body":"Interesting thoughts!","likes":5,
     "user":{"username":"viviang","fullName":"Vivian Carter"}},
    17:{"body":"I love your neat work!","likes":7,
     "user":{"username":"nicholase","fullName":"Nicholas Edwards"}},
    18:{"body":"Doesn't it feel good to do such great work?","likes":6,
     "user":{"username":"noramx","fullName":"Nora Russell"}},
    19:{"body":"First-rate work!","likes":1,
     "user":{"username":"novab","fullName":"Nova Cooper"}},
    20:{"body":"This is fascinating information!","likes":4,
     "user":{"username":"lucasg","fullName":"Lucas Gray"}},
    21:{"body":"You inspire me!","likes":0,
     "user":{"username":"miam","fullName":"Mia Miller"}},
    22:{"body":"This is right on target!","likes":5,
     "user":{"username":"miam","fullName":"Mia Miller"}},
    23:{"body":"What an astounding observation!","likes":1,
     "user":{"username":"nicholase","fullName":"Nicholas Edwards"}},
    24:{"body":"This is very well thought out!","likes":1,
     "user":{"username":"jaxonb","fullName":"Jaxon Barnes"}},
    25:{"body":"I can tell you've been practicing!","likes":9,
     "user":{"username":"claires","fullName":"Claire Foster"}},
    26:{"body":"You've come a long way!","likes":7,
     "user":{"username":"ethanf","fullName":"Ethan Fletcher"}},
    27:{"body":"I can tell you've been paying attention!","likes":9,
     "user":{"username":"nathand","fullName":"Nathan Dixon"}},
    28:{"body":"Reading this made my day!","likes":8,
     "user":{"username":"xavierw","fullName":"Xavier Wright"}},
    29:{"body":"This is very perceptive!","likes":2,
     "user":{"username":"lunah","fullName":"Luna Perez"}},
    30:{"body":"What an accomplishment!","likes":8,
     "user":{"username":"braydenf","fullName":"Brayden Fleming"}}
    }

menu_doc = """
  ╔══════════════════════════════════════╗
  ║           МЕНЮ КОММЕНТАРИЕВ          ║
  ╠══════════════════════════════════════╣
  ║ 1 - напиши свой коммент              ║
  ║ 2 - прочитать коммент по его номеру  ║
  ║ 3 - прочитать все комменты           ║
  ║ 4 - удалить коммент по его номеру    ║
  ║ 5 - самые популярные комменты        ║
  ║ 0 - достаточно                       ║
  ╚══════════════════════════════════════╝
"""

rotated_heavy_black = """❥ ❥ ❥ ❥ ❥ ❥ ❥ ❥ ❥ ❥ ❥ ❥ ❥ ❥ ❥ ❥ ❥"""
rotated_heavy_black_short = """❥"""

def main():

    root = tk.Tk()
    label = tk.Label(root, text=menu_doc, justify=tk.LEFT, font=("Courier", 10))
    label.pack(pady=20)
    root.after(2000, root.destroy)
    print(menu_doc)
    operation = int(input("-->"))
    
    while operation != 0:
        if operation == 1:
            comment = cf.create_comment(max(comments.keys()))
            comments.update(comment)
        elif operation == 2:
            tid = int(input("Введи comment id:"))
            cf.read_comment(tid, comments)
        elif operation == 3:
            cf.read_comments(comments)
        elif operation == 4:
            tid = int(input("Введи коммент id:"))
            cf.delete_comment(tid, comments)
        elif operation == 5:
            cf.max_likes_comments(comments, rotated_heavy_black, rotated_heavy_black_short)
        else:
            print("Я не понял, попробуй ещё раз.")

        root = tk.Tk()
        label = tk.Label(root, text=menu_doc, justify=tk.LEFT, font=("Courier", 10))
        label.pack(pady=20)
        root.after(2000, root.destroy)
        print(menu_doc)
        operation = int(input("-->"))
       
    
    print("Достаточно, так достаточно..")


main()

