import customtkinter as ctk
import pyautogui as pygui
import random
import time
from threading import Thread



ctk.set_appearance_mode("dark")       
ctk.set_default_color_theme("green")


def validate_numeric_input(text):
    return text.isdigit() or text == ""

def limitation(text: str):
    if text.isdigit():
        return 0 < int(text) <= 100
    elif not text:
        return True
    
    return False



class app(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Mouse Pointer")   
        self.geometry('400x500')
        self.resizable(False, False)
        numeric_validation = self.register(validate_numeric_input)
        limit = self.register(limitation)
        
        
        self.s = pygui.size()
        self.resolution = ctk.CTkLabel(self, text=f'System Resolution : {self.s.width} x {self.s.height}', font=("Arial", 15))
        self.resolution.grid(row=1, columnspan=8,
                             pady=(2,5), sticky='ew')
        
        
        self.current = ctk.CTkLabel(self, text=f'Current Position', font=("Arial", 25))
        self.current.grid(row=2, columnspan=8,
                             pady=(5,10), sticky='ew')
        
        
        self.currentpos = ctk.CTkLabel(self, text=f'', font=("Arial", 40), text_color='#1CFAD5')
        self.currentpos.grid(row=3, columnspan=8,
                             pady=(5,30), sticky='ew')
        self.update()
        
        
        self.seperate = ctk.CTkLabel(self, text = '', height=1, width=400, bg_color='#000000', font=('Aerial', 1))
        self.seperate.place(in_= self.currentpos, relx=0, rely=1.5)
        
        
        
        self.Label = ctk.CTkLabel(self, width=340,
                                  text= 'Enter Co-ordinates', font=("Arial", 25))
        self.Label.grid(row=4, columnspan=8,
                           padx=30, pady=(20,5),
                           sticky="ew")
        
        
        self.XLabel = ctk.CTkLabel(self, text="X   - ")
        self.XLabel.grid(row=5, column=0,
                           padx=(30, 10), pady=20,
                           sticky="ew")
 
        # X Entry Field
        self.XEntry = ctk.CTkEntry(self, width=100, 
                            placeholder_text="",
                            validate="key", validatecommand=(numeric_validation, "%P"))
        self.XEntry.grid(row=5, column=1, sticky="ew")
        
        
        self.YLabel = ctk.CTkLabel(self, text="Y   - ")
        self.YLabel.grid(row=5, column=2,
                           padx=(30, 10), pady=20,
                           sticky="ew")
 
        # Y Entry Field
        self.YEntry = ctk.CTkEntry(self, width=100, 
                            placeholder_text="",
                            validate="key", validatecommand=(numeric_validation, "%P"))
        self.YEntry.grid(row=5, column=3, sticky="ew")
        
        
        # button
        self.mouse = ctk.CTkButton(self, text='Get Mouse', command=self.move_mouse)
        self.mouse.grid(row=6, columnspan=8, pady=(15, 0))
        
        
        
        self.seperate = ctk.CTkLabel(self, text = '', height=1, width=450, bg_color='#000000', font=('Aerial', 1))
        self.seperate.place(in_= self.mouse, relx=-1, rely=2)
        
        
        self.random = ctk.CTkLabel(self, text='Get Random Positions', font=('Arial', 20))
        self.random.grid(row=7, columnspan=8,
                         pady=(50, 30))
        
        
        self.randomentry = ctk.CTkEntry(self, width=100,
                            placeholder_text="times",
                            validate="key", validatecommand=(limit, "%P"))
        self.randomentry.grid_forget()
        # self.randomentry.pack()
        self.randomentry.place(in_=self.random, relx=-0.05, rely=1.2)
        
        self.randbutton = ctk.CTkButton(self, width= 100, text='Get Randoms', command=self.get_randoms)
        self.randbutton.grid_forget()
        # self.randbutton.pack()
        self.randbutton.place(in_=self.randomentry, relx=1.1, rely=0)
        
        self.randomtimes = ctk.CTkLabel(self, text='Max : 100 times', font=('Arial', 10))
        self.randomtimes.grid_forget()
        self.randomtimes.place(in_=self.random, relx=0.3, rely=2.2)
        
        
        
    
    def get_xy(self):
        x = self.XEntry.get()
        y = self.YEntry.get()
        
        return int(x), int(y)
    
    def move_mouse(self):
        x, y = self.get_xy()
        pygui.moveTo(x, y)
        
    def get_randoms(self):
        limit = int(self.randomentry.get())
        
        def rand(limit):
            for _ in range(limit):
                x, y = random.randint(0, self.s.width), random.randint(0, self.s.height)
                pygui.moveTo(x,y)
                time.sleep(.2)
                
        Thread(target=rand, args=(limit,)).start()
        
    def update(self):
        x, y = pygui.mouseinfo.position()
        self.currentpos.configure(text=f'{x:4} x {y:<4}')
        
        self.after(25, self.update)
        
        
        
if __name__ == '__main__' :
    app = app()
    app.mainloop()