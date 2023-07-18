import tkinter


class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("GAME")  # window title
        self.main_window.geometry('420x420')  # window geometry(size)

        self.image = tkinter.PhotoImage(file='blair2.png')  # loads photo/image
        self.main_window.iconphoto(True, self.image)  # Icon image of window
        self.main_window.config(background='green')  # background color

        self.photo = tkinter.PhotoImage(file='blair2.png')
        # Labels
        self.label = tkinter.Label(self.main_window,
                                   text='Ghana',
                                   font=('Arial', 40, 'bold'),  # font(font-family,font-size, font-style)
                                   fg='red',  # fg(foreground) for text color
                                   bg='yellow',  # background color
                                   relief=tkinter.RAISED,  # label border
                                   bd=10,  # border width
                                   padx=20,  # padding X-axis
                                   pady=20,  # padding y-axis
                                   # image=self.photo,# adding image to text
                                   compound='bottom'  # separating image from text
                                   )

        self.label.place(x=0, y=0)  # place object(In place of pack )
        # self.label.pack(side='left')

        # Button
        self.button = tkinter.Button(self.main_window,
                                     text='Click Me!',
                                     command=self.push,
                                     font=('Comic sans', 30),
                                     fg='green',
                                     bg='black',
                                     activeforeground='red',  # foreground when clicked
                                     activebackground='blue',  # background when clicked
                                     #  state=tkinter.DISABLED  # disable button
                                     # image=self.photo
                                     )
        self.button.pack(side='left')

        tkinter.mainloop()

    def push(self):
        print('dem')


# Entry(Button for delete, backspace and submit)

class Interface:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.entry = tkinter.Entry(self.main_window,
                                   width=10,
                                   show='*'  # Entry should show specific characters (like password)
                                   )
        # self.entry.insert(0, 'Blairnation') # Default text in entry box
        self.entry.pack(side='left')

        self.button1 = tkinter.Button(self.main_window, text='submit', command=self.submit)
        self.button2 = tkinter.Button(self.main_window, text='backspace', command=self.backspace)
        self.button3 = tkinter.Button(self.main_window, text='delete', command=self.delete)

        self.button1.pack(side='left')
        self.button2.pack(side='left')
        self.button3.pack(side='left')

        tkinter.mainloop()

    def submit(self):
        name = self.entry.get()
        print('Hello ', name)
        # self.entry.config(state=tkinter.DISABLED) # disable entry box after
        # after clicking button

    def delete(self):
        self.entry.delete(0, tkinter.END)

    def backspace(self):
        self.entry.delete(len(self.entry.get()) - 1, tkinter.END)


window = Interface()


# script tkinter
import tkinter

main_window = tkinter.Tk()
main_window.title("GAME")  # window title
main_window.geometry('420x420')  # window geometry(size)

image = tkinter.PhotoImage(file='blair2.png')  # loads photo/image
main_window.iconphoto(True, image)  # Icon image of window
main_window.config(background='green')  # background color

label = tkinter.Label(main_window,
                      text='Ghana',
                      font=('Arial', 40, 'bold'),  # font(font-family,font-size, font-style)
                      fg='red',  # fg(foreground) for text color
                      bg='yellow',  # background color
                      relief=tkinter.RAISED,  # label border
                      bd=10,  # border width
                      padx=20,  # padding X-axis
                      pady=20,  # padding y-axis
                      # image=image,  # adding image to text
                      compound='bottom'  # seperating image from text
                      )

# self.label.place(x=0, y=0) #  place object(In place of pack )
label.pack()
tkinter.mainloop()

