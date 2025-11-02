#to create an empty window

# #import tkinter module
# import tkinter as tk
# #create empty root window
# root=tk.Tk()  #Tk is inbuilt class
# root.title("hello world")
# root.geometry("500x200")   #width and height of window
# #making root window visible
# root.mainloop()









import tkinter as tk
from tkinter import ttk 
root=tk.Tk()  
root.title("hello world")
root.geometry("500x200")

frame=ttk.Frame(root,padding="10 10 10 10")
frame.pack(fill=tk.BOTH,expand=True)

#call back functions
def hello():
    root.title("hello page")   #by clicking button1, title changes to hello page
def india():
    #root.title("indian page")   #by clicking button2, title changes to indian page 
    root.destroy()             #it exit from window or remove window
#for using call back function use command argument for Button constructor
button1=ttk.Button(frame,text="click me",command=hello)  #for adding buttons
button2=ttk.Button(frame,text="exit",command=india )
button1.pack()   #to display the buttons
button2.pack()

#input=ttk.Label(frame,text="name")
#input.pack()
#or......
ttk.Label(frame,text="name").pack()

#inname=tk.StringVar()
#innname=ttk.Entry(frame,width=25,textvariable=inname)
#innname.pack()
# or......
ttk.Entry(frame,width=25,textvariable=tk.StringVar()).pack()
 
root.mainloop()





#The grid geometry manager and the pack geometry manager are mutually exclusive in Tkinter.
#You cannot use both of them for the same container (frame) at the same time. 
#frame.pack(fill=tk.BOTH, expand=True)  # Using pack here with this we cannot use grid therefore just use frame.pack()
""" 
import tkinter as tk
from tkinter import ttk 
root=tk.Tk()  
root.title("hello world")
root.geometry("500x200")
frame = ttk.Frame(root, padding = "30 50 50 50")
frame.pack()
#lay out in grid-->grid method not present in frame  class only available in Tk() classs
ttk.Label(frame,text="name").grid(column=0,row=0)
ttk.Entry(frame,width=25,textvariable=tk.StringVar()).grid(column=1,row=0)
root.mainloop() """






""" 
import tkinter as tk
from tkinter import ttk
# create the root window
root = tk.Tk()
# modify the window
root.title("Simple Calculator")
root.geometry("600x500")
# create a frame in the window to hold other widgets
Calci = ttk.Frame(root, padding = "50 50 50 50")
Calci.pack()
# create a label for no1 in the frame
no1Label = ttk.Label(Calci, text = "Enter first no: ")
no1Label.grid(column=0,row=0)             #if we put grid then we cannot use pack()
# create textbox for no1 in the frame
no1 = tk.StringVar()
ttk.Entry(Calci, width=25, textvariable=no1,state="readonly").grid(column=1,row=0)   #we cannot enter any value adter it is in readonly state 
no1.set("5000")    #if we set value then we can enter after that value if readonly state present in entry then we cannot enter after set value in that entry box
# create a label for no2 in the frame
no2Label = ttk.Label(Calci, text = "Enter second no: ")
no2Label.grid(column=0,row=1)

# create textbox for no2 in the frame
no2 = tk.StringVar()
ttk.Entry(Calci, width=25, textvariable=no2).grid(column=1,row=1)
#no2.get() we use it when we get value from an input and doing operations
root.mainloop() """




# #to perform 
# import tkinter as tk
# from tkinter import ttk 
# root=tk.Tk()  
# root.title("hello world")
# root.geometry("500x200")
# frame = ttk.Frame(root, padding = "30 50 50 50")
# frame.pack()
# ttk.Label(frame,text="a:").grid(column=0,row=0)
# n1=tk.StringVar()
# ttk.Entry(frame,width=25,textvariable=n1).grid(column=1,row=0)
# ttk.Label(frame,text="b:").grid(column=0,row=1)
# n2=tk.StringVar()
# ttk.Entry(frame,width=25,textvariable=n2).grid(column=1,row=1)
# def sum():
#     num1=float(n1.get())
#     num2=float(n2.get())
#     res.set(num1+num2)
# def clear():
#     n1.set("")
#     n2.set("")
#     res.set("")
# button1=ttk.Button(frame,text="sum",command=sum).grid(column=0,row=2)
# res=tk.StringVar()
# ttk.Entry(frame,width=25,textvariable=res,state="readonly").grid(column=1,row=2)
# button2=ttk.Button(frame,text="clear",command=clear).grid(column=0,row=3,sticky=tk.W,pady=5)
# root.mainloop()