import pickle
import tkinter as tk
from tkinter import messagebox

#with open("账号密码.pickle",'wb') as f:
#    pickle.dump({'110':'119'},f)

win = tk.Tk()
win.geometry('500x400')
win.iconbitmap('11.ico')
win.title('QQ')
win.resizable(0,0)#拉升0为不可拉伸
username_in = tk.StringVar()
password_in = tk.StringVar()
username_up = tk.StringVar()
password_up = tk.StringVar()
password2_up = tk.StringVar()
def in_it(win_in):#登录程序
    with open('账号密码.pickle','rb') as f:
        name_dict = pickle.load(f)
    name = username_in.get()
    word = password_in.get()
    if name in name_dict:
        if name_dict[name] == word:
            tk.messagebox.showinfo(title='成功', message='你好啊%s'%name)  # 就看看信息
            win_in.destroy()
        else:
            tk.messagebox.showwarning(title='警告', message='密码错误')
    else:
        tk.messagebox.showwarning(title='警告', message='用户%s不存在'%name)  # 感叹号的
def up_it(win_up):#注册程序
    name = username_up.get()
    word1 = password_up.get()
    word2 = password2_up.get()
    with open('账号密码.pickle','rb') as f:
        name_dict = pickle.load(f)
    if name in name_dict:
        tk.messagebox.showwarning(title='警告', message='此名称已被祖册请重新输入')
    elif name == '':
        tk.messagebox.showwarning(title='警告', message='用户名为空')
    else:
        if word1 == word2:
            if word1 != '':
                name_dict[name] = word1
                with open('账号密码.pickle','wb') as f:
                    pickle.dump(name_dict,f)
                    tk.messagebox.showinfo(title='成功', message='%s注册成功' % name)  # 就看看信息
                    win_up.destroy()
            else:
                tk.messagebox.showwarning(title='警告', message='密码为空')
        else:
            tk.messagebox.showwarning(title='警告', message='密码不一致')
def sign_in():#登录窗口
    win_in = tk.Toplevel(win)
    win_in.geometry('500x200')
    win.iconbitmap('11.ico')
    win_in.title('登录')
    win_in.resizable(0,0)
    #win_in.attributes('-topmost',True)
    win_in.grab_set()  # 窗口锁定在top上
    win_in.focus_set()  # 焦点锁定在top上
    username_in.set('@163.com')
    password_in.set('')
    lable_name = tk.Label(win_in, text='username:', font=('宋体', 25)).place(x=20, y=30)
    lable_word = tk.Label(win_in, text='password:', font=('宋体', 25)).place(x=20, y=100)
    name_txt = tk.Entry(win_in,textvariable=username_in, show=None,width=30)
    name_txt.place(x=200,y=40)
    pass_txt = tk.Entry(win_in,textvariable=password_in, show='*', width=30)
    pass_txt.place(x=200, y=110)
    button_entry = tk.Button(win_in,text='确定',relief='flat',
                             bg='#e16c96',font=('宋体', 25),command=lambda :in_it(win_in)).place(x=230,y=140)#lambda 匿名

def sign_up():#注册窗口
    win_up = tk.Toplevel(win)
    win_up.geometry('500x300')
    win.iconbitmap('11.ico')
    win_up.title('注册')
    win_up.resizable(0, 0)#防止调整大小
    win_up.grab_set()  # 窗口锁定在top上
    win_up.focus_set()  # 焦点锁定在top上
    username_up.set('')
    password_up.set('')
    password2_up.set('')
    lable_name = tk.Label(win_up,text='username:',font=('宋体',25)).place(x=20,y=30)
    lable_name = tk.Label(win_up, text='password:', font=('宋体', 25)).place(x=20,y=90)
    pass_again = tk.Label(win_up, text='putagain:', font=('宋体', 25)).place(x=20, y=150)
    name_txt = tk.Entry(win_up,show=None,textvariable=username_up,width=30).place(x=200,y=40)
    pass_txt = tk.Entry(win_up, show=None,textvariable=password_up, width=30).place(x=200, y=110)
    again_txt = tk.Entry(win_up, show=None,textvariable=password2_up, width=30).place(x=200, y=170)
    button_entry = tk.Button(win_up,text='确定',relief='flat',
                             bg='#66a9c9',font=('宋体', 25),command=lambda : up_it(win_up)).place(x=230,y=210)

canvas = tk.Canvas(win,bg='white',height=215,width=314)
image_file = tk.PhotoImage(file='sg.png')
image = canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack()

button1 = tk.Button(win, text='登录', font=('微软雅黑', 30),
                    relief='flat', bg='#e16c96', command=sign_in).place(x=100, y=250)
button2 = tk.Button(win, text='注册', font=('微软雅黑', 30),
                    relief='flat', bg='#66a9c9', command=sign_up).place(x=300, y=250)

win.mainloop()