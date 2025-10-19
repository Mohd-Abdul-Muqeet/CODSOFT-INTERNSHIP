import tkinter as tk

win=tk.Tk()
win.title("Simple Calculator")

entry=tk.Entry(win,width=50,font=("Arial",16))
entry.grid(row=0,column=0,columnspan=4)

def click_me(num):
    entry.insert(tk.END,num)
def clear():
    entry.delete(0,tk.END)
def equal():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(tk.END,"Error")
buttons=[
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','+','='
]
row,col=1,0
for b in buttons:
    cmd=lambda x=b: click_me(x) if x != '=' else equal()
    tk.Button(win,text=b,height=5,width=15,command=cmd).grid(row=row,column=col)
    col+=1
    if col > 3:
        col=0
        row+=1

tk.Button(win,text="C",height=5,width=15,command=clear).grid(row=row,column=col)
win.mainloop()