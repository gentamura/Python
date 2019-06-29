import tkinter as tk
base = tk.Tk()
topping = {0:'ノリ', 1:'煮玉子', 2:'もやし', 3:'チャーシュー'}
check_values = {}
for i in range(len(topping)):
    check_values[i] = tk.BooleanVar()
    tk.Checkbutton(base, variable = check_values[i], text =
            topping[i]).pack(anchor = tk.W)

def buy():
    for i in check_values:
        if check_values[i].get() == True:
            print(topping[i])

tk.Button(base, text = '注文', command = buy).pack()

