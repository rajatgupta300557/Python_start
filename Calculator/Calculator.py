from tkinter import *
root = Tk()
root.title("Calculator")
gd1 = StringVar()
exp = ""

def press(n):
	global exp
	exp = exp + str(n)
	gd.set(exp)

def ep():
    global exp
    try:
        total = str(eval(exp))
        gd.set(total)
        exp=""
        print(total)
        # print(gd.get())
    except:
        gd.set(" LOL Syntax ERROR ")
        exp = ""

gd = StringVar()

e1= Entry(width = 20, textvariable = gd,bg="gray25",fg="white", bd=1,font='Helvetica 19')
e1.grid(columnspan=4)


b1 = Button(width =7,height = 3,activebackground = "grey",bg="grey15",fg="white",bd=1,font='comic',text = "7",command=lambda: press(7))
b1.grid(row = 2, column = 0)
b2 = Button(width =7,height = 3,activebackground = "grey",bg="grey15",fg="white",bd=1,font='comic',text = "8",command=lambda: press(8))
b2.grid(row = 2, column = 1)
b3 = Button(width =7,height = 3,activebackground = "grey",bg="gray15",fg="white",bd=1,font='comic',text = "9",command=lambda: press(9))
b3.grid(row = 2, column = 2)
b4 = Button(width =7,height = 3,activebackground = "grey",bg="gray15",fg="white",bd=1,font='comic',text = "4",command=lambda: press(4))
b4.grid(row = 3, column = 0)
b5 = Button(width =7,height = 3,activebackground = "grey",bg="gray15",fg="white",bd=1,font='comic',text = "5",command=lambda: press(5))
b5.grid(row = 3, column = 1)
b6 = Button(width =7,height = 3,activebackground = "grey",bg="gray15",fg="white",bd=1,font='comic',text = "6",command=lambda: press(6))
b6.grid(row = 3, column = 2)
b7 = Button(width =7,height = 3,activebackground = "grey",bg="gray15",fg="white",bd=1,font='comic',text = "1",command=lambda: press(1))
b7.grid(row = 4, column = 0)
b8 = Button(width =7,height = 3,activebackground = "grey",bg="gray15",fg="white",bd=1,font='comic',text = "2",command=lambda: press(2))
b8.grid(row = 4, column = 1)
b9 = Button(width =7,height = 3,activebackground = "grey",bg="gray15",fg="white",bd=1,font='comic',text = "3",command=lambda: press(3))
b9.grid(row = 4, column = 2)
b10 = Button(width =7,height = 3,activebackground = "grey",bg="gray15",fg="white",bd=1,font='comic',text = "0",command=lambda: press(0))
b10.grid(row = 5, column = 0)
b11 = Button(width =7,height = 3,activebackground = "grey",bg="gray15",fg="dodgerblue2",bd=1,font='comic',text = ".",command=lambda: press("."))
b11.grid(row = 5, column = 1)
b12 = Button(width =7,height = 3,activebackground = "grey",bg="gray15",fg="dodgerblue2",bd=1,font='comic',text = "/",command=lambda: press("."))
b12.grid(row = 2, column = 3)
b13 = Button(width =7,height = 3,activebackground = "grey",bg="gray15",fg="dodgerblue2",bd=1,font='comic',text = "*",command=lambda: press("*"))
b13.grid(row = 3, column = 3)
b14 = Button(width =7,height = 3,activebackground = "grey",bg="gray15",fg="dodgerblue2",bd=1,font='comic',text = "-",command=lambda: press("-"))
b14.grid(row = 4, column = 3)
b15 = Button(width =7,height = 3,activebackground = "grey",bg="gray15",fg="dodgerblue2",bd=1,font='comic',text = "+",command=lambda: press("+"))
b15.grid(row = 5, column = 2)
b16 = Button(width =7,height = 3,activebackground = "grey",bg="red3",fg="white",bd=1,font='comic',text = "=",command=ep)
b16.grid(row = 5, column = 3)

# b17 = Button(width =6,height = 3,activebackground = "grey",bg="black",fg="dodgerblue2",font='comic',text = "C")
# b17.grid(row = 2, column = 4)

root.mainloop()