#!/usr/bin/python3
#coding:utf-8

#===============================================================================
# 输入文本
# 对这个GUI程序改进一下，加入一个文本框，让用户可以输入文本，然后点按钮后，弹出消息对话框。
#===============================================================================
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Click', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get()+'萌萌哒!' or '初音很萌哟!'
        messagebox.showinfo('Message', '主人说了: %s' % name)
        # messagebox.showinfo('Message', 'Hello, Dog')

app = Application()
# 设置窗口标题
app.master.title('Hello World')
# 主消息循环
app.mainloop()

# 当用户点击按钮时，触发hello()，通过self.nameInput.get()获得用户输入的文本后，使用tkMessageBox.showinfo()可以弹出消息对话框。

#===============================================================================
# 小结
# 
# Python内置的Tkinter可以满足基本的GUI程序的要求，如果是非常复杂的GUI程序，建议用操作系统原生支持的语言和库来编写。
#===============================================================================
