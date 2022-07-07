from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("601x430")
root.title("Tic_Tac_Toe")

c=1
def show(q):
  global c
  c+=1


  if(c%2==0):
    if((q["text"]=="")):
      q["text"]="O"
      q["bg"]="red"
      q["fg"]="white"
  else:
    if(q["text"]==""):
      q["text"]="X"
      q["bg"]="blue"
      q["fg"]="white"


  if((b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O") or (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O") or (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O") or (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O") or (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O") or (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O") or (b7["text"]=="O" and b5["text"]=="O" and b3["text"]=="O") or (b9["text"]=="O" and b5["text"]=="O" and b1["text"]=="O")):
      messagebox.showinfo("Tic_Tac_Toe Winner", "              ***   Win  User_1   ( O )  ***                ")
      root.destroy()
      
      
      
  elif((b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X") or (b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X")or (b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X")or (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X")or (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X")or (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X") or (b7["text"]=="X" and b5["text"]=="X" and b3["text"]=="X") or (b9["text"]=="X" and b5["text"]=="X" and b1["text"]=="X")):
    messagebox.showinfo("Tic_Tac_Toe Winner", "              ***   Win  User_2   ( X )  ***                ")
    root.destroy()
    




b1=Button(root,font=("arial",25),text="",width=10,height=3,command=lambda:show(b1))
b1.grid(row=0,column=0)
b2=Button(root,font=("arial",25),text="",width=10,height=3,command=lambda:show(b2))
b2.grid(row=0,column=1)
b3=Button(root,font=("arial",25),text="",width=10,height=3,command=lambda:show(b3))
b3.grid(row=0,column=2)


b4=Button(root,font=("arial",25),text="",width=10,height=3,command=lambda:show(b4))
b4.grid(row=1,column=0)
b5=Button(root,font=("arial",25),text="",width=10,height=3,command=lambda:show(b5))
b5.grid(row=1,column=1)
b6=Button(root,font=("arial",25),text="",width=10,height=3,command=lambda:show(b6))
b6.grid(row=1,column=2)


b7=Button(root,font=("arial",25),text="",width=10,height=3,command=lambda:show(b7))
b7.grid(row=2,column=0)
b8=Button(root,font=("arial",25),text="",width=10,height=3,command=lambda:show(b8))
b8.grid(row=2,column=1)
b9=Button(root,font=("arial",25),text="",width=10,height=3,command=lambda:show(b9))
b9.grid(row=2,column=2)



root.mainloop()
