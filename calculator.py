from tkinter import *
from tkinter import messagebox
import math

# Global variables
root = Tk()
SIZE = 14
WEIGHT = "bold"
FONT = "yu gothic"

#creating the calculator class

class Calculator:
    global root,SIZE,FONT,WEIGHT
    def __init__(self,root):
        #app settings
        self.root=root
        self.app_width = 395
        self.app_height = 570
        self.root.title("Calculator")
        self.x = self.root.winfo_screenwidth()// 2 - self.app_width // 2
        self.y = self.root.winfo_screenheight()// 2 - self.app_height // 2
        self.root.geometry("{}x{}+{}+{}".format(self.app_width,self.app_height,self.x,self.y))
        self.font = (FONT,SIZE,WEIGHT)
        self.bg_secondary = "gray75"
        self.bg = "gray85"
        self.fg = "gray20"
        self.act_foreground = "gray70"
        self.act_background = "gray75"
        self.root["bg"] = "gray80"
        self.width = 7
        self.height = 2
        self.add_x = 100
        self.layout()
        self.input()
        self.buttons()
     
        self.firstNum = []
        self.secondNum = []
        self.pressed = ""
        self.arg_1 = ""
        self.arg_2 = ""
        self.x = ""
        self.operatorButtons = [self.button_add,self.button_minus,self.button_multiply,self.button_divide]
 
    #for deactivating background operator
    def deactive(self):       
        for x in range(len(self.operatorButtons)) :
            self.operatorButtons[x]["bg"] = self.bg
           
    #for all the basic arithemtic operator
    def operator(self,operator):
        for x in range(len(self.operatorButtons)) :
            self.operatorButtons[x]["bg"] = self.bg
            if operator == self.operatorButtons[x]["text"]:
                self.operatorButtons[x]["bg"] = "PowderBlue"  
        self.pressed  = self.pressed + operator
    #for getting the logarithm 
    def logs(self):
        try:
            num = math.log(int(self.pressed))
            self.var.set(num)
            self.pressed = str(num)
        except ValueError:
            self.var.set("Syntax Error")

    #getting the sqaure of the number           
    def square(self):
        try:
            num = math.sqrt(int(self.pressed))
            self.var.set(num) 
            self.pressed = str(num) 
        except ValueError:
            self.var.set("Syntax Error") 

    def pi(self):    
        try:
            num = math.pi
            self.var.set(num) 
            self.pressed = str(num) 
        except ValueError:
            self.var.set("Syntax Error") 
    def percent(self):
        try:
            num = int(self.pressed) / 100
            self.var.set(num) 
            self.pressed = str(num) 
        except ValueError:
            self.var.set("Syntax Error")  
    # power calculation   
    def power(self):
        try:  
            num = math.pow(int(self.pressed),2)   
            self.var.set(num)
            self.pressed = str(num)
        except ValueError:
            self.var.set("Syntax Error")
    
    #concatinating the string when they are pressed     
    def clicked(self,x):
        self.x = str(x)  
        self.pressed = self.pressed + self.x 
        self.var.set(self.pressed)
    #to clear or reset the app
    def clear(self):
        self.pressed = ""
        self.var.set("0")
        self.deactive()
    #sin,tan and cosine math
    def sine(self):
        try:
            num  = math.sin(int(self.pressed))
            self.var.set(num)
            self.pressed = str(num)
             
        except ValueError:
            self.var.set("Syntax Error")
    def cosine(self):
        try:
            num  = math.cos(int(self.pressed))
            self.var.set(num)
            self.pressed = str(num)
        except ValueError:
            self.var.set("Syntax Error")
    def tang(self):
        try:
            num  = math.tan(int(self.pressed))
            self.var.set(num)
            self.pressed = str(num)
        except ValueError:
            self.var.set("Syntax Error")
    def result(self):
       
        self.deactive()
        try:    
            self.answer = eval(self.pressed)
            self.var.set("0")
            self.var.set(self.answer)  
            self.pressed = str(self.answer)    
        except SyntaxError :
            self.var.set("Syntax Error")
        except TypeError as e:
            self.var.set("Stack Error")
        except ValueError :
            self.var.set("Syntax Error")
    def font(self,**args):
        return  (args[0],args[1],args[2])    
    def layout(self):
        #toggle bar grid
        grid_toggle = Label(text="➕",bg=self.root["bg"],font=("yu gothic",12,"bold"))
        grid_toggle.grid(padx=35,pady=5,row=0,column=0)

        #label gridx
        grid_label = Label(text="Standard Calculator",fg="gray20" ,bg=self.root["bg"],font=("yu gothic",12,"bold"))
        grid_label.grid(padx=10,pady=10,row=0,column=1)
    def input(self):
        #input Grid
        self.var = StringVar()
        calc_input =  Entry(width=25,relief="flat",highlightthickness=0,textvariable=self.var,bg=self.root["bg"],font=("yu gothic",20,"bold"),justify="right")
        calc_input.place(x=10,y=90)
        
         
    def buttons(self):
        #button Grid
        button_percent = Button(text="%",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg_secondary,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.percent())
        button_percent.place(x=10,y=150)
        button_ce = Button(text="pi",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg_secondary,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.pi())
        button_ce.place(x=105,y=150)
        button_clear = Button(text="X^2",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg_secondary,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.power())
        button_clear.place(x= 200,y=150)
        self.delete = Button(text="C",width=self.width,relief="flat",font=self.font,fg="red3",bg=self.bg_secondary,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.clear())
        self.delete.place(x=295,y=150)

        # ------- second row ---------
        button_sin = Button(text="Sin",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg_secondary,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.sine())
        button_sin.place(x=10,y=220)
        button_cos= Button(text="Cos",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg_secondary,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.cosine())
        button_cos.place(x=105,y=220)
        button_square = Button(text="Tan",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg_secondary,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.tang())
        button_square.place(x= 200,y=220)
        self.button_divide = Button(text="/",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg_secondary,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.operator("/"))
        self.button_divide.place(x=295,y=220)

        # -------- thrid row -------
        button_7 = Button(text="7",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.clicked("7"))
        button_7.place(x=10,y=290)
        button_8 = Button(text="8",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.clicked("8"))
        button_8.place(x=105,y=290)
        button_9 = Button(text="9",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.clicked("9"))
        button_9.place(x= 200,y=290)
        self.button_multiply = Button(text="x",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.operator("*"))
        self.button_multiply.place(x=295,y=290)

        # ------- fourth row ---------

        button_4 = Button(text="4",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.clicked("4"))
        button_4.place(x=10,y=360)
        button_5 = Button(text="5",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.clicked("5"))
        button_5.place(x=105,y=360)
        button_6 = Button(text="6",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.clicked("6"))
        button_6.place(x= 200,y=360)
        self.button_minus = Button(text="-",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.operator("-"))
        self.button_minus.place(x=295,y=360)

        #  -------- fifth row ----------
        button_1 = Button(text="1",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.clicked("1"))
        button_1.place(x=10,y=430)
        button_2 = Button(text="2",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.clicked("2"))
        button_2.place(x=105,y=430)
        button_3 = Button(text="3",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.clicked("3"))
        button_3.place(x= 200,y=430)
        self.button_add = Button(text="+",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.operator("+"))
        self.button_add.place(x=295,y=430)

        # -------- sixth row ------------
        button_log = Button(text="log",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.logs())
        button_log.place(x=10,y=500)
        button_zero = Button(text="0",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.clicked("0"))
        button_zero.place(x=105,y=500)
        button_dot = Button(text=".",width=self.width,relief="flat",font=self.font,fg=self.fg,bg=self.bg,activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.clicked("."))
        button_dot.place(x= 200,y=500)
        button_equal = Button(text="=",width=self.width,relief="flat",font=self.font,fg=self.fg,bg="cyan",activebackground=self.act_background,activeforeground=self.act_foreground,border=0,highlightthickness=0,height=self.height,command=lambda:self.result())
        button_equal.place(x=295,y=500)

    def loop(self):
        self.root.mainloop()
        
run = Calculator(root=root)
run.loop()






