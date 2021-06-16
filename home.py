from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
global screen_width 

#cbf3f0
#2ec4b6
class student_attendance_system:
    def __init__(self,root):
        self.root = root
        self.root.title("Attendance Manager")
        self.root.state('zoomed')
        self.root['background'] = "#cbf3f0"
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        print(screen_height,screen_width)
        
        
        main_frame = Frame(self.root,bg = "#cbf3f0")
        main_frame.place(x=0,y=0,width=screen_width,height=screen_height)
        
        #ADDING MAIN LABEL
        title_size = 70*screen_width
        title_size = int(title_size/1920)
        heading = Label(main_frame,text = "ATTENDANCE MANAGEMENT SYSTEM",font = ("times new roman",title_size),fg= "#2ec4b6",bg = "#cbf3f0")
        heading.place(x=0,y=0,width=screen_width)

        #BUTTON FRAME
        button_frame = Frame(main_frame,bg = "#cbf3f0")
        x_but_frame = screen_width-800
        x_but_frame = int(x_but_frame/2)
        button_frame.place(x = x_but_frame,y = 300,height = 450,width = 800)
        #250*240
        frame_check1 = Frame(button_frame,bg = "yellow")
        frame_check1.place(x=0,y=0,width = 250,height = 212.5)

        frame_check2 = Frame(button_frame,bg = "yellow")
        frame_check2.place(x=275,y=0,width = 250,height = 212.5)

        frame_check3 = Frame(button_frame,bg = "yellow")
        frame_check3.place(x=550,y=0,width = 250,height = 212.5)
        
        frame_check4 = Frame(button_frame,bg = "yellow")
        frame_check4.place(x=0,y=237.5,width = 250,height = 212.5)
        
        frame_check5 = Frame(button_frame,bg = "yellow")
        frame_check5.place(x=275,y=237.5,width = 250,height = 212.5)
        
        frame_check6 = Frame(button_frame,bg = "yellow")
        frame_check6.place(x=550,y=237.5,width = 250,height = 212.5)

        #ADDING BUTTONS OF MENU



root = Tk()
obj = student_attendance_system(root)
root.mainloop()
