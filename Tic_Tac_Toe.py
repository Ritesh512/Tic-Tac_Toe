from calendar import c
from pydoc import cli
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")

def disable_btns():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def Winner(text):
    global winner
  

    winner = False
    if b1["text"] == text and b2["text"] == text and b3["text"] == text:
        b1.config(bg = "red")
        b2.config(bg = "red")
        b3.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","Congratulations "+text+ " won!!!!")
        disable_btns()
    elif b4["text"] == text and b5["text"] == text and b6["text"] == text:
        b4.config(bg = "red")
        b5.config(bg = "red")
        b6.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","Congratulations "+text+ " won!!!")
        disable_btns()

    elif b7["text"] == text and b8["text"] == text and b9["text"] == text:
        b7.config(bg = "red")
        b8.config(bg = "red")
        b9.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","Congratulations "+text+ " won!!!!")
        disable_btns()

    elif b1["text"] == text and b4["text"] == text and b7["text"] == text:
        b1.config(bg = "red")
        b4.config(bg = "red")
        b7.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","Congratulations "+text+ " won!!!")
        disable_btns()

    elif b2["text"] == text and b5["text"] == text and b8["text"] == text:
        b2.config(bg = "red")
        b5.config(bg = "red")
        b8.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","Congratulations "+text+ " won!!!")
        disable_btns()

    elif b3["text"] == text and b6["text"] == text and b9["text"] == text:
        b3.config(bg = "red")
        b6.config(bg = "red")
        b9.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","Congratulations "+text+ " won!!!")
        disable_btns()
    
    elif b1["text"] == text and b5["text"] == text and b9["text"] == text:
        b1.config(bg = "red")
        b5.config(bg = "red")
        b9.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","Congratulations "+text+ " won!!!")
        disable_btns()

    elif b3["text"] == text and b5["text"] == text and b7["text"] == text:
        b3.config(bg = "red")
        b5.config(bg = "red")
        b7.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","Congratulations "+text+ " won!!!")
        disable_btns()


    if count == 9 and winner == False:
        messagebox.showinfo("Tic-Tac-Toe","Match is Tie!!\nNo one win!!")
        disable_btns()


click = True
count = 0
def btn_click(b):
    global click 
    global count

    if b["text"] == " " and click ==True:
        b["text"] = "X"
        click = False
        count+=1
        Winner("X") 
    
    elif b["text"] == " " and click ==False:
        b["text"] = "O"
        click  = True
        count+=1
        Winner("O") 
    
    else:
        messagebox.showerror("Tic-Tac-Toe","Its already click\nPlease choose another one.")

def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global click, count
    click = True
    count = 0
#Creating Buttons 
    b1 = Button(root,text = " ",height = 3,width=6,font=("Helvetica",20),bg="SystemButtonFace",command=lambda : btn_click(b1))
    b2 = Button(root,text = " ",height = 3,width=6,font=("Helvetica",20),bg="SystemButtonFace",command=lambda : btn_click(b2))
    b3 = Button(root,text = " ",height = 3,width=6,font=("Helvetica",20),bg="SystemButtonFace",command=lambda : btn_click(b3))
    b4 = Button(root,text = " ",height = 3,width=6,font=("Helvetica",20),bg="SystemButtonFace",command=lambda : btn_click(b4))
    b5 = Button(root,text = " ",height = 3,width=6,font=("Helvetica",20),bg="SystemButtonFace",command=lambda : btn_click(b5))
    b6 = Button(root,text = " ",height = 3,width=6,font=("Helvetica",20),bg="SystemButtonFace",command=lambda : btn_click(b6))
    b7 = Button(root,text = " ",height = 3,width=6,font=("Helvetica",20),bg="SystemButtonFace",command=lambda : btn_click(b7))
    b8 = Button(root,text = " ",height = 3,width=6,font=("Helvetica",20),bg="SystemButtonFace",command=lambda : btn_click(b8))
    b9 = Button(root,text = " ",height = 3,width=6,font=("Helvetica",20),bg="SystemButtonFace",command=lambda : btn_click(b9))

    #creating Grid of the buttons

    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)
    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)
    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)

my_menu = Menu(root)
root.config(menu=my_menu)

options_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Options",menu=options_menu)
options_menu.add_command(label="Reset Game",command=reset)
options_menu.add_command(label="Exit",command=root.destroy)
reset()

root.mainloop()