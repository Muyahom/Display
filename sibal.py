import time
from ttkwidgets import Calendar

try:
    import Tkinter as tk
except:
    import tkinter as tk
import tkinter.font as font



class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Frame Window Size Frozen")
        self.geometry('350x350')
        self.configure(bg='black')

        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()


class StartPage(tk.Frame):
    def __init__(self, master):

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='black')
        myFont = font.Font(family='Helvetica', size=15, weight='bold')

        def clock():
            clock_time = time.strftime('%H:%M:%S %p')
            curr_time.config(text=clock_time)
            curr_time.after(1000, clock)

        tk.Label(self, text="Main", font = myFont, fg ='white', bg='black').grid(column=4, row=0)

        empty_label = tk.Label(self, text="", font = myFont,  bg='black')
        empty_label.grid(column=0, row=1)

        curr_time = tk.Label(self, font = myFont, fg ='white', bg='black')
        curr_time.grid(column=4, row=1)
        clock()

        empty_label = tk.Label(self, text="", font=myFont, bg='black')
        empty_label.grid(column=0, row=2)

        tk.Button(self, text="1번 화면",
                  command=lambda: master.switch_frame(PageOne)).grid(column=3, row=3)
        empty_label = tk.Label(self, text="", font = myFont, fg ='white', bg='black')
        empty_label.grid(column=2, row=3)
        tk.Button(self, text="2번 화면",
                  command=lambda: master.switch_frame(PageTwo)).grid(column=5, row=3)


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='black')
        myFont = font.Font(family='Helvetica', size=15, weight='bold')

        title_label = tk.Label(self, text="1번화면", font = myFont, fg ='white', bg='black')
        title_label.grid(column=1, row=0)

        empty_label = tk.Label(self, text="", font = myFont,  bg='black')
        empty_label.grid(column=0, row=1)


        cal = Calendar(self)
        cal.grid(row=2, column=1, padx=20, columnspan=2)

        empty_label = tk.Label(self, text="", font = myFont,  bg='black')
        empty_label.grid(column=0, row=3)

        button1 = tk.Button(self, text="btn1", width = 6)
        button1.grid(row=4, column=1, padx = 3, pady = 3)
        button2 = tk.Button(self, text="btn2", width = 6)
        button2.grid(row=4, column=2, padx = 3, pady = 3)

        empty_label = tk.Label(self, text="", font = myFont,  bg='black')
        empty_label.grid(column=0, row=5)

        tk.Button(self, text="back",
                  command=lambda: master.switch_frame(StartPage), width = 6).grid(row=6, column=2)


class PageTwo(tk.Frame):
    def __init__(self, master):
        # define font
        myFont = font.Font(family='Helvetica', size=15, weight='bold')

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='black')
        tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).grid

        def button_pressed(value):
            number_entry.insert("end", value)
            print(value, "pressed")

        def math_button_pressed(value):
            print(value, "pressed")

        def equal_button_pressed():
            print("equal pressed")

        title_label = tk.Label(self, text="2번화면", font = myFont, fg ='white', bg='black')
        title_label.grid(column=2, row=0)

        empty_label = tk.Label(self, text="", font = myFont,  bg='black')
        empty_label.grid(column=0, row=1)


        a_label = tk.Label(self, text="입력창", font = myFont, fg ='white', bg='black')
        a_label.grid(column=0, row=2)

        entry_value = tk.StringVar(self, value='')
        number_entry = tk.Entry(self, textvariable=entry_value, width=20)
        number_entry.grid(row=2, column = 1, columnspan=3)

        button7 = tk.Button(self, text="7", command=lambda: button_pressed('7'), width = 4)
        button7.grid(row=6, column=0, padx = 3, pady = 10)
        button8 = tk.Button(self, text="8", command=lambda: button_pressed('8'), width = 4)
        button8.grid(row=6, column=1, padx = 3, pady = 10)
        button9 = tk.Button(self, text="9", command=lambda: button_pressed('9'), width = 4)
        button9.grid(row=6, column=2, padx = 3, pady = 10)

        button4 = tk.Button(self, text="4", command=lambda: button_pressed('4'), width = 4)
        button4.grid(row=5, column=0, padx = 3, pady = 10)
        button5 = tk.Button(self, text="5", command=lambda: button_pressed('5'), width = 4)
        button5.grid(row=5, column=1, padx = 3, pady = 10)
        button6 = tk.Button(self, text="6", command=lambda: button_pressed('6'), width = 4)
        button6.grid(row=5, column=2, padx = 3, pady = 10)

        button1 = tk.Button(self, text="1", command=lambda: button_pressed('1'), width = 4)
        button1.grid(row=4, column=0, padx = 3, pady = 3)
        button2 = tk.Button(self, text="2", command=lambda: button_pressed('2'), width = 4)
        button2.grid(row=4, column=1, padx = 3, pady = 3)
        button3 = tk.Button(self, text="3", command=lambda: button_pressed('3'), width = 4)
        button3.grid(row=4, column=2, padx = 3, pady = 3)


        button_ac = tk.Button(self, text="확인", command=lambda:equal_button_pressed(), width = 4)
        button_ac.grid(row=7, column=0, padx = 3, pady = 10)
        button0 = tk.Button(self, text="0", command=lambda: button_pressed('0'), width = 4)
        button0.grid(row=7, column=1, padx = 3, pady = 10)
        button_equal = tk.Button(self, text="취소", command=lambda: button_pressed('AC'), width = 4)
        button_equal.grid(row=7, column=2, padx = 3, pady = 10)

        button_ac = tk.Button(self, text="성공", command=lambda:equal_button_pressed(), width = 6, height = 3)
        button_ac.grid(row=4, column=4, padx = 3, pady = 3)
        button_equal = tk.Button(self, text="실패", command=lambda: button_pressed('AC'), width = 6, height = 3)
        button_equal.grid(row=4, column=5, padx = 3, pady = 3)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop() 