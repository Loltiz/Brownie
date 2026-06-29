from tkinter import Tk,Button,Label
cliker=0
def nuber():
    global cliker
    cliker=cliker+1
    label.config(text=cliker)
window=Tk()
window.title("Brownie Cliker By Calvin Shalov ")
window.geometry("1920x1080")
button=Button(window,text="make a brownie",command=nuber)
button.pack(pady=500)
label=Label(window,text="Click Count")
label.pack()
window.mainloop()
