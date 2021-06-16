from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk

class student:
  def __init__(self,root):

    self.root = root
    self.root.title("Attendance Manager")
    self.root.state('zoomed')
    # self.root.configure(bg="#cbf3f0")

    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()

    background_frame = Frame(self.root,bg = "#cbf3f0")
    background_frame.place(x=0,y=0,width=screen_width,height=screen_height)

    title_size = 70*screen_width
    title_size = int(title_size/1920)
    heading = Label(background_frame ,text = "STUDENT DETAILS",font = ("Berlin Sans FB",title_size),fg= "#2ec4b6",bg = "#cbf3f0")
    heading.place(x=0,y=20,width=screen_width)

    

if __name__=="__main__":
  root=Tk()
  obj=student(root)
  root.mainloop()