from tkinter import Tk,Button,Label,Frame
cliker=0
cpc=1
def Checker():
    if cliker>=200:
        U1.config(state="normal")
    else:
        U1.config(state="disabled")
    if cliker>=1000:
        U2.config(state="normal")
    else:
        U2.config(state="disabled")
def Implaman(Cost,cpcadd):
    global cpc 
    global cliker 
    cpc=cpc+cpcadd
    cliker=cliker-Cost
    label.config(text=cliker)
    Checker()
def nuber():
    global cliker
    cliker=cliker+cpc
    label.config(text=cliker)
    Checker()
    
window=Tk()
window.title("Brownie Cliker By Calvin Shalov")
window.geometry("1920x1080")
button=Button(window,text="make a brownie",command=nuber)
button.grid(row=0,column=0)
label=Label(window,text="Click Count")
label.grid(row=1,column=0)
Upgradeframe=Frame(window)
U1=Button(Upgradeframe,text="Coca powder $200 gives 10 cpc",state="disabled",command=lambda:Implaman(200,10))
U1.grid(row=0, column=0)
U2=Button(Upgradeframe,text="Eggs $1000 gives 35 cpc",state="disabled",command=lambda:Implaman(1000,35))
U2.grid(row=1, column=0)
Upgradeframe.grid(row=5, column=5)
window.mainloop()