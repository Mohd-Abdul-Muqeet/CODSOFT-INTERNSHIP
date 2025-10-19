import random
import tkinter as tk
from tkinter import messagebox

def start_game():
    choice=tk.Tk()
    choice.title("Rock,Paper,Scissor Game")

    entry=tk.Entry(choice,width=100,font=("Arial",16))
    entry.grid(row=0,column=0,columnspan=3)

    def clear():
        entry.delete(0,tk.END)

    def click_me(String):
        entry.insert(tk.END,String)   

    def winner(user_choice):
        
        new={"Rock":-1,"Paper":0,"Scissor":1}
        user_val=new[user_choice]
        computer_choice=random.choice(["Rock","Paper","Scissor"])
        computer_val = new[computer_choice] 
        if user_val == computer_val:
            entry.insert(tk.END,f"\nComputers Choice: {computer_choice}|| Yours choice:{user_choice}||")
            entry.insert(tk.END,"Match Tied")
        elif (user_val == -1 and computer_val == 1) or \
                (user_val == 0 and computer_val == -1) or \
                (user_val == 1 and computer_val == 0):
                entry.insert(tk.END,f"\nComputers Choice: {computer_choice}|| Yours choice:{user_choice}||")
                entry.insert(tk.END,"You Won")
        else:
            entry.insert(tk.END,f"\nComputers Choice:{computer_choice} || Yours choice:{user_choice}||")
            entry.insert(tk.END,"Computer Won")
        choice.update()    
    def ask_restart():
        answer = messagebox.askyesno("Play Again?", "Do you want to play again?")
        choice.destroy()
        if answer:  # If yes, restart the game
            start_game()

    choice.after(3000, ask_restart)

    buttons=[
        'Rock','Paper','Scissor','Wins'
    ]
    row,col=1,0
    for text in buttons:
        tk.Button(choice,text=text,width=25,height=10,command=lambda v=text: winner(v)).grid(row=row,column=col)
        col+=1

    tk.Button(choice,text="Clear",width=25,height=10,command=clear).grid(row=2,column=3)
    choice.mainloop()
start_game()