import tkinter
from tkinter import Label, PhotoImage, simpledialog


window=tkinter.Tk() # gui open
window.title("Door Lock")
window.geometry("800x400+100+100")
window.option_add("*Font", "궁서 20")
window.resizable(1, 1)


door_password = input("초기 패스워드(5자리) : ")
password =""

while len(door_password) != 5 : # check password
    print("비밀번호는 4자리만 입력하여주시기 바랍니다.")
    door_password = ("초기 패스워드 재입력(5자리) : ")
    

def command_args(pad): #input value and action
    global password
    global door_password
    password += str(pad)
    label.config(text=str(password))

    if len(password) == 5 : #if password is 5 suc/fail button disabled
        button_suc.config(state="disabled")
        button_fail.config(state="disabled")

    if len(password) == 5 and door_password == password: # if password 5 and matched suc activate
        button_suc.config(state="active",activebackground="blue")
        password = ""
    elif len(password) == 5 and door_password != password: # if password is not matched fail activate
        button_fail.config(state="active")
        password = ""

#gui layout
lbl = tkinter.Label(window, text="입력값")
label = tkinter.Label(window, text="0")

lbl.place(x=20, y=20, width=50, height=50)
label.place(x=80, y=20, width=50, height=50)

#button setting
button1_1 = tkinter.Button(window, text="1", command=lambda: command_args("1"))
button1_2 = tkinter.Button(window, text="2", command=lambda: command_args("2"))
button1_3 = tkinter.Button(window, text="3", command=lambda: command_args("3"))

button2_1 = tkinter.Button(window, text="4", command=lambda: command_args("4"))
button2_2 = tkinter.Button(window, text="5", command=lambda: command_args("5"))
button2_3 = tkinter.Button(window, text="6", command=lambda: command_args("6"))

button3_1 = tkinter.Button(window, text="7", command=lambda: command_args("7"))
button3_2 = tkinter.Button(window, text="8", command=lambda: command_args("8"))
button3_3 = tkinter.Button(window, text="9", command=lambda: command_args("9"))

button4_1 = tkinter.Button(window, text="*", command=lambda: command_args("*"))
button4_2 = tkinter.Button(window, text="0", command=lambda: command_args("0"))
button4_3 = tkinter.Button(window, text="#", command=lambda: command_args("#"))

#button location
button1_1.place(x=20, y=90, width=50, height=50)
button1_2.place(x=80, y=90, width=50, height=50)
button1_3.place(x=140, y=90, width=50, height=50)

button2_1.place(x=20, y=150, width=50, height=50)
button2_2.place(x=80, y=150, width=50, height=50)
button2_3.place(x=140, y=150, width=50, height=50)

button3_1.place(x=20, y=210, width=50, height=50)
button3_2.place(x=80, y=210, width=50, height=50)
button3_3.place(x=140, y=210, width=50, height=50)

button4_1.place(x=20, y=270, width=50, height=50)
button4_2.place(x=80, y=270, width=50, height=50)
button4_3.place(x=140, y=270, width=50, height=50)

button_suc = tkinter.Button(window, state="disabled", text="성공")
button_fail = tkinter.Button(window, state="disabled", text="실패")
button_suc.place(x=200, y=90, width=70, height=30)
button_fail.place(x=280, y=90, width=70, height=30)

window.mainloop()