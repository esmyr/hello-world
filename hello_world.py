from  tkinter import *

def centre(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    root.update_idletasks()

if __name__ == '__main__':
    root = Tk()
    root.title('Test')
    Label(root, text='Hello world! This is a git test.').pack()
    centre(root)
    mainloop()
    
# A comment
