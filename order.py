import tkinter as tk
from tkinter import messagebox
import random

ID = '111'
passwd = '123456'

t = False

def homepage():
    window = tk.Tk()
    window.title('主页')
    window.geometry("400x200")
    label = tk.Label(text='欢迎来到食堂点餐系统！', font=('','20'))
    label.pack()
    button = tk.Button(window, text='进入', command=lambda: [window.destroy(), login()])
    button.place(x=180, y=120)
    window.mainloop()

def login():
    window = tk.Tk()
    window.title('登录')
    window.geometry("400x200")

    tk.Label(window, text='学号: ').place(x=50, y=40)
    tk.Label(window, text='密码: ').place(x=50, y=80)

    var_usr_ID = tk.StringVar()
    entry_usr_ID = tk.Entry(window, textvariable=var_usr_ID)
    entry_usr_ID.place(x=160, y=40)
    var_usr_pwd = tk.StringVar()
    entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
    entry_usr_pwd.place(x=160, y=80)

    def usr_login():
        global ID, passwd, t
        if var_usr_ID.get() == ID and var_usr_pwd.get() == passwd:
            window.destroy()
            t = True
        else:
            messagebox.showinfo('提示', '学号或密码错误')

    btn_login = tk.Button(window, text='登录', command=usr_login)
    btn_login.place(x=180, y=120)
    window.mainloop()

def order():
    menu_items = {
        "时蔬": [("有机花菜", 6), ("酸辣土豆丝",6), ("手撕包菜", 5), ("豆芽菜", 3)],
        "小炒菜": [("西红柿炒蛋", 6),("鱼香茄子",6),("金针菇烧日本豆腐",6)],
        "荤菜": [("鱼香肉丝", 8),("回锅肉",8),("蜜汁红烧肉",12),("手撕鸡",8),("烧鸭",8)],
        "主食": [("米饭", 2),("炒粉",4)]
    }
    order_items={}
    def checkout():
        checkout_window = tk.Tk()
        checkout_window.title("结算")
        total_price=0
        tk.Label(checkout_window, text="菜品").grid(row=0, column=0)
        tk.Label(checkout_window, text="单价(元）").grid(row=0, column=1)
        tk.Label(checkout_window, text="总数").grid(row=0, column=4)
        for index, (item, quantity) in enumerate(order_items.items()):

            item_label = tk.Label(checkout_window, text=item)
            item_label.grid(row=index+1, column=0)
            quantity_label = tk.Label(checkout_window, text=int(quantity))
            price =[price for menu_category in menu_items.values() for menu_item, price in menu_category if menu_item == item][0]
            price_label = tk.Label(checkout_window, text=int(price))
            price_label.grid(row=index+1, column=1)
            quantity_label.grid(row=index+1, column=2)
            total_price+=quantity*price
        total_price_label = tk.Label(checkout_window, text="总价：{}".format(total_price))
        total_price_label.grid(row=len(order_items)+1, column=0, columnspan=2)
        radio_var = tk.StringVar()
        tk.Label(checkout_window, text="请选择堂食/到店自取/外送").grid(row=len(order_items) + 2, column=0)
        radio_button1 = tk.Radiobutton(checkout_window, text="堂食", variable=radio_var, value="选项1").grid(row=len(order_items) + 3, column=1)
        radio_button2 = tk.Radiobutton(checkout_window, text="到店自取（+1元）", variable=radio_var, value="选项2").grid(row=len(order_items) + 3, column=2)
        radio_button3 = tk.Radiobutton(checkout_window, text="外送（+2元）", variable=radio_var, value="选项3").grid( row=len(order_items) + 3, column=3)
        def submit_order(total_price):
            if (total_price > 0):
                if radio_var.get() == "":
                    messagebox.showinfo("提示！", "您没有选择取餐方式！")
                    s = 0
                else:
                    s = 1
                if radio_var.get() == "选项2":
                    total_price += 1
                elif radio_var.get() == "选项3":
                    total_price += 2
                if s == 1:
                    messagebox.showinfo("订单详情", "您的订单已提交，总金额为{},感谢您的使用！".format(total_price))
                    checkout_window.destroy()
            else:
                messagebox.showinfo("提示", "您未选择任何商品！")

        tk.Button(checkout_window, text="提交订单", command=lambda: submit_order(total_price)).grid(row=len(order_items) + 4, column=1)
        tk.Button(checkout_window, text="返回菜单", command=lambda: [checkout_window.destroy(), menu()]).grid(row=len(order_items)+4 ,column=2)
        checkout_window.mainloop()
    def menu():
        root = tk.Tk()
        root.title("点餐")
        root.geometry("400x300")

        def get_random_menu_items():
            menu = []
            for category in menu_items:
                item = random.choice(menu_items[category])
                menu.append(item[0])
            return menu[:2]

        random_items = get_random_menu_items()

        label1 = tk.Label(root, text="今天的推荐菜品是：")
        label1.grid(row=0, column=0)

        label2 = tk.Label(root, text=random_items[0])
        label2.grid(row=0, column=1)
        label3 = tk.Label(root, text=random_items[1])
        label3.grid(row=0, column=2)
        tk.Label(root, text="菜品").grid(row=2, column=0)
        tk.Label(root, text="单价(元）").grid(row=2, column=1)
        tk.Label(root, text="总数").grid(row=2, column=4)
        button_frame = tk.Frame(root)
        button_frame.grid(row=1, column=0)
        menu_frame = tk.Frame(root)
        menu_frame.grid(row=3, column=0)
        order_frame = tk.Frame(root)
        order_frame.grid(row=4, column=0)
        def show_menu(category):
            for widget in menu_frame.winfo_children():
                widget.destroy()
            row_count = 0
            for item in menu_items[category]:
                item_label = tk.Label(menu_frame, text=item[0])
                item_label.grid(row=row_count, column=0)
                price_label = tk.Label(menu_frame, text=item[1])
                price_label.grid(row=row_count, column=1)
                add_button = tk.Button(menu_frame, text="添加", command=lambda item=item[0]: add_to_order(item))
                add_button.grid(row=row_count, column=2)
                delete_button = tk.Button(menu_frame, text="删除", command=lambda item=item[0]: delete_from_order(item))
                delete_button.grid(row=row_count, column=3)
                row_count += 1

        def add_to_order(item):
            if item in order_items:
                order_items[item] += 1
            else:
                order_items[item] = 1
            for widget in menu_frame.winfo_children():
                if isinstance(widget, tk.Label) and widget["text"] == item:
                    order_label = tk.Label(menu_frame, text="")
                    order_label.config(text=str(order_items[item]))
                    order_label.grid(row=widget.grid_info()["row"], column=4)
                    break

        def delete_from_order(item):
            if item in order_items:
                order_items[item] -= 1
            else:
                order_items[item] = 0
            if order_items[item] < 0:
                messagebox.showinfo("提示！", "您当前没有选择该菜品！")
                order_items[item] = 0
            for widget in menu_frame.winfo_children():
                if isinstance(widget, tk.Label) and widget["text"] == item:
                    order_label = tk.Label(menu_frame, text="")
                    order_label.config(text=str(order_items[item]))
                    order_label.grid(row=widget.grid_info()["row"], column=4)
                    break

        for idx, category in enumerate(menu_items.keys()):
            button = tk.Button(button_frame, text=category, command=lambda category=category: show_menu(category))
            button.grid(row=0, column=idx, sticky="ew")

        default_category = list(menu_items.keys())[0]
        show_menu(default_category)
        checkout_button = tk.Button(root, text="去结算", command=lambda: [root.destroy(), checkout()])
        checkout_button.grid(row=5, column=0, columnspan=len(menu_items))
        root.mainloop()
    menu()

homepage()
if t:
    order()