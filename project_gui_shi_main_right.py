import sys

try:
    
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import project_gui_shi_main_right_support
import os.path
from tkinter import filedialog
from PIL import ImageTk,Image
from prediction import pred
from tkinter import messagebox
import tkinter as tk
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    project_gui_shi_main_right_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    project_gui_shi_main_right_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font12 = "-family Arimo -size 10 -weight bold -slant italic "  \
            "-underline 0 -overstrike 0"
        font13 = "-family Arimo -size 10 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font9 = "-family Arimo -size 10 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("996x638+360+52")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("PAVEMENT CONDITION DETECTOR")
        top.configure(background="#d6d8ab")
        top.configure(highlightcolor="#5e5e5e")

        self.menubar = tk.Menu(top,font=font9,bg='#cdd8d3',fg=_fgcolor)
        top.configure(menu = self.menubar)

        # import tkinter as tk
        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.0, rely=0.0, relheight=1.624, relwidth=2.268)
        self.photo=Image.open('C:\\Users\\KRITIK SHIVANSHU\\Desktop\\Pavement_condition_assessment-master\\main1-0.jpg')
        self.photo_=ImageTk.PhotoImage(self.photo)
        self.Canvas1.create_image(0,0,image=self.photo_,anchor='nw')

        # self.Canvas1=tk.Canvas(top)
        # self.Canvas1.place(relx=0.0,rely=0.0,relheight=1.624,relwidth=2.268)
        # self.photo=Image.open("C://Users//GOVINDA//Downloads//sih_main//main1-0.jpg")
        # self.photo_=ImageTk.PhotoImage(self.photo)
        # self.Canvas1.create_image(0,0,image=self.photo_,anchor=NW)

        # """self.Label1 = tk.Label(top)
        # self.Label1.place(relx=-0.01, rely=0.078, height=650, width=515)
        # self.Label1.configure(background="#d6d8ab")
        # photo_location = os.path.join(prog_location,"C:/Users/GOVINDA/Downloads/sih_main/main1-0.png")
        # global _img0
        # _img0 = tk.PhotoImage(file=photo_location)
        # self.Label1.configure(image=_img0)"""

        self.Label_insert_image = tk.Label(top)
        self.Label_insert_image .place(relx=0.422, rely=0.204, height=250, width=475)
        self.Label_insert_image .configure(activebackground="#ffffff")
        self.Label_insert_image .configure(background="#ffffff")
        self.Label_insert_image .configure(highlightbackground="#ffffff")

        self.Button_ok = tk.Button(top)
        self.Button_ok.place(relx=0.672, rely=0.643, height=30, width=96)
        self.Button_ok.configure(background="#beb323")
        self.Button_ok.configure(font=font12)
        self.Button_ok.configure(text='''Ok''')



        self.Button_add_image = tk.Button(top)
        self.Button_add_image .place(relx=0.472, rely=0.643, height=30, width=96)
        self.Button_add_image .configure(background="#beb323")
        self.Button_add_image .configure(font=font12)
        self.Button_add_image .configure(text='''Add Image''')

        self.Button_add_image.configure(command=self.add_image)
        self.Button_ok.configure(command=self.ok_button)

    def add_image(self):

        self.file_name=filedialog.askopenfilename(filetypes=(("JPG","*.jpg"),("All files","*.*")))
        self.path=self.file_name
        self.photo=Image.open(self.file_name).resize((475,250),Image.ANTIALIAS)
        self.photo_image=ImageTk.PhotoImage(self.photo)
        self.Label_insert_image.configure(image=self.photo_image)
    def ok_button(self):
        self.Label_predict=pred(self.path)
        self.x=self.Label_predict
        print(type(self.x))
        messagebox.showinfo("Prediction",self.Label_predict)

if __name__ == '__main__':
    vp_start_gui()





