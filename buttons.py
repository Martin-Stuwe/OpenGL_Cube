from tkinter import*
import glfwtest

root =Tk()

def clicked():
    label = Label(root, text="WHY CLICKED?!")
    label.pack()
    glfwtest.test = 1

button1 = Button(root,text="click it",padx=50,pady=50, command=clicked, fg="blue", bg="black")  #state = DISABLED/?
button1.pack()



root.mainloop()