# frames and labels

import tkinter


class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text='Tony Blair')
        self.label2 = tkinter.Label(self.top_frame, text='Kwaku Yeboah')
        self.label3 = tkinter.Label(self.top_frame, text='Blair nation')

        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        self.label4 = tkinter.Label(self.bottom_frame, text='Tony Blair')
        self.label5 = tkinter.Label(self.bottom_frame, text='Kwaku Yeboah')
        self.label6 = tkinter.Label(self.bottom_frame, text='Blair nation')

        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


window = GUI()



# create button(action and quit)

import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.button = tkinter.Button(self.main_window, text='Main window', command=self.do_something)
        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        self.button.pack()
        self.quit_button.pack()

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Message Box',
                                    'Welcome To Main Window')


interface = GUI()

# converter(taking entry) using message box

import tkinter
import tkinter.messagebox


class Converter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label = tkinter.Label(self.top_frame, text='Enter distance in kilometers')
        self.entry = tkinter.Entry(self.top_frame, width=20)

        self.label.pack(side='left')
        self.entry.pack(side='left')

        self.convert_button = tkinter.Button(self.bottom_frame, text='convert', command=self.converter)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.convert_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def converter(self):
        kilo = float(self.entry.get())

        miles = 0.6 * kilo

        tkinter.messagebox.showinfo('Results',
                                    f'{str(kilo)} kilometers is equal to {str(miles)} miles')


converter = Converter()

# converter using StringVar

import tkinter


class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label = tkinter.Label(self.top_frame, text='Enter distance in kilometers')
        self.entry = tkinter.Entry(self.top_frame, width=10)

        self.label.pack(side='left')
        self.entry.pack(side='left')

        self.result_label = tkinter.Label(self.middle_frame, text='Distance in miles: ')
        self.value = tkinter.StringVar()
        self.result_text = tkinter.Label(self.middle_frame, textvariable=self.value)

        self.result_label.pack(side='left')
        self.result_text.pack(side='left')

        self.convert_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.convert_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.entry.get())
        mile = 0.64 * kilo
        self.value.set(str(mile))


converter = GUI()


# calculate Average

import tkinter


class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_top_frame = tkinter.Frame(self.main_window)
        self.middle_mid_frame = tkinter.Frame(self.main_window)
        self.middle_down_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text='Enter the score for test 1:')
        self.entry1 = tkinter.Entry(self.top_frame, width=10)

        self.label1.pack(side='left')
        self.entry1.pack(side='left')

        self.label2 = tkinter.Label(self.middle_top_frame, text='Enter the score for test 2:')
        self.entry2 = tkinter.Entry(self.middle_top_frame, width=10)

        self.label2.pack(side='left')
        self.entry2.pack(side='left')

        self.label3 = tkinter.Label(self.middle_mid_frame, text='Enter the score for test 3:')
        self.entry3 = tkinter.Entry(self.middle_mid_frame, width=10)

        self.label3.pack(side='left')
        self.entry3.pack(side='left')

        self.label4 = tkinter.Label(self.middle_down_frame, text='Average')
        self.answer = tkinter.StringVar()
        self.display_ans = tkinter.Label(self.middle_down_frame, textvariable=self.answer)

        self.label4.pack(side='left')
        self.display_ans.pack(side='left')

        self.average_button = tkinter.Button(self.bottom_frame, text='Average', command=self.average)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.average_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_top_frame.pack()
        self.middle_mid_frame.pack()
        self.middle_down_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def average(self):
        test1 = float(self.entry1.get())
        test2 = float(self.entry2.get())
        test3 = float(self.entry3.get())

        average_score = (test1 + test2 + test3) / 3
        self.answer.set(str(average_score))


average = GUI()

# radio button

import tkinter
import tkinter.messagebox


class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)
        self.r1 = tkinter.Radiobutton(self.top_frame, text='Option 1', variable=self.radio_var,
                                      value=1)
        self.r2 = tkinter.Radiobutton(self.top_frame, text='Option 2', variable=self.radio_var,
                                      value=2)
        self.r3 = tkinter.Radiobutton(self.top_frame, text='Option 3', variable=self.radio_var,
                                      value=3, command=self.display)

        self.r1.pack()
        self.r2.pack()
        self.r3.pack()

        self.display_button = tkinter.Button(self.bottom_frame, text='Display',command=self.display)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.display_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def display(self):
        tkinter.messagebox.showinfo('Result',
                                    f'{self.radio_var.get()} is selected')


window = GUI()


# check box

import tkinter
import tkinter.messagebox


class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.cb1 = tkinter.IntVar()
        self.cb2 = tkinter.IntVar()
        self.cb3 = tkinter.IntVar()

        self.cb1.set(0)
        self.cb2.set(0)
        self.cb3.set(0)

        self.check1 = tkinter.Checkbutton(self.top_frame,
                                          text='Option 1',
                                          variable=self.cb1)
        self.check2 = tkinter.Checkbutton(self.top_frame,
                                          text='Option 2',
                                          variable=self.cb2)
        self.check3 = tkinter.Checkbutton(self.top_frame,
                                          text='Option 3',
                                          variable=self.cb3)

        self.check1.pack()
        self.check2.pack()
        self.check3.pack()

        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text="OK",
                                        command=self.display)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def display(self):
        self.show = "You selected:\n"

        if self.cb1.get() == 1:
            self.show = self.show + 'Option1\n'
        if self.cb2.get() == 1:
            self.show = self.show + 'Option2\n'
        if self.cb3.get() == 1:
            self.show = self.show + 'Option3\n'

        tkinter.messagebox.showinfo('Display',
                                    self.show)


window = GUI()

