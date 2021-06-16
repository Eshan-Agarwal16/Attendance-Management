from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk

class student:
  def __init__(self,root):
    self.root = root
    self.root.title("Attendance Manager")
    self.root.state('zoomed')
    self.root['background'] = "#cbf3f0"





if __name__=="__main__":
  root=Tk()
  obj=student(root)
  root.mainloop()