import tkinter as tk
from tkinter import *
from sys import exit
from PIL import Image, ImageTk
import os as os
import pygame
os.chdir('jqimages')
LARGE_FONT = ("Arial", 14)
BUTTON_FONT = ("Arial", 9)
scorecount = 0

class NAME_HEREQuiz(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        pygame.mixer.init()
        pygame.mixer.music.load("MUSIC_FILE_HERE")
        pygame.mixer.music.play(loops=-1) # Replays music

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # menubar = tk.Menu(container)
        # filemenu = tk.Menu(menubar, tearoff=0)
        # filemenu.add_separator()
        # filemenu.add_command(label="Exit", command=exit)
        # menubar.add_cascade(label="File", menu=filemenu)

        # tk.Tk.config(self, menu=menubar)
        tk.Tk.config(self)
        self.frames = {}

        for F in (StartPage, EndPage0, EndPage1, EndPage2, EndPage3, EndPage4,
                  EndPage5, EndPage6, EndPage7, EndPage8, EndPage9, EndPage10, Credits):
            frame = F(parent=container, controller=self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frameStart()

    def show_frameStart(self):
        frame = self.frames[StartPage]
        frame.tkraise()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def show_frameQ1(self, container):
        global scorecount
        scorecount = 0
        frame = PageOne(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

    def show_frameQ2(self, container, correct):
        global scorecount
        if correct == 1:
            scorecount += 1
        frame = PageTwo(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

    def show_frameQ3(self, container, correct):
        global scorecount
        if correct == 1:
            scorecount += 1
        frame = PageThree(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

    def show_frameQ4(self, container, correct):
        global scorecount
        if correct == 1:
            scorecount += 1
        frame = PageFour(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

    def show_frameQ5(self, container, correct):
        global scorecount
        if correct == 1:
            scorecount += 1
        frame = PageFive(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

    def show_frameQ6(self, container, correct):
        global scorecount
        if correct == 1:
            scorecount += 1
        frame = PageSix(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

    def show_frameQ7(self, container, correct):
        global scorecount
        if correct == 1:
            scorecount += 1
        frame = PageSeven(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

    def show_frameQ8(self, container, correct):
        global scorecount
        if correct == 1:
            scorecount += 1
        frame = PageEight(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

    def show_frameQ9(self, container, correct):
        global scorecount
        if correct == 1:
            scorecount += 1
        frame = PageNine(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

    def show_frameQ10(self, container, correct):
        global scorecount
        if correct == 1:
            scorecount += 1
        frame = PageTen(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

    def show_endframe(self, correct):
        global scorecount
        if correct == 1:
            scorecount += 1
        if (scorecount == 0):
            frame = self.frames[EndPage1]
            frame.tkraise()
        elif (scorecount == 1):
            frame = self.frames[EndPage1]
            frame.tkraise()
        elif (scorecount == 2):
            frame = self.frames[EndPage2]
            frame.tkraise()
        elif (scorecount == 3):
            frame = self.frames[EndPage3]
            frame.tkraise()
        elif (scorecount == 4):
            frame = self.frames[EndPage4]
            frame.tkraise()
        elif (scorecount == 5):
            frame = self.frames[EndPage5]
            frame.tkraise()
        elif (scorecount == 6):
            frame = self.frames[EndPage6]
            frame.tkraise()
        elif (scorecount == 7):
            frame = self.frames[EndPage7]
            frame.tkraise()
        elif (scorecount == 8):
            frame = self.frames[EndPage8]
            frame.tkraise()
        elif (scorecount == 9):
            frame = self.frames[EndPage9]
            frame.tkraise()
        else:
            frame = self.frames[EndPage10]
            frame.tkraise()


class StartPage(tk.Frame):
    # ttk is different to tk
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('startbg.png')
        background_image = ImageTk.PhotoImage(bgload)
        # bgload.resize((768,5760), Image.ANTIALIAS)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # load = Image.open("sleepy_NAME_HERE.jpg")
        # load = load.resize((150,250), Image.ANTIALIAS)
        # render = ImageTk.PhotoImage(load)
        # label2 = tk.Label(self, image=render)
        # label2.image = render
        # label2.pack()
        button = tk.Button(self, text="START",
                           command=lambda: controller.show_frameQ1(parent),
                           font=("Arial", 12), fg='white')
        button.config(bg='#33FF5A', activebackground='blue', relief='raised', height=2, width=20)
        button.place(x=230, y=300)


######################################### PAGE ONE
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('NAME_HERE_q1.png')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        load1 = Image.open("q1.png")
        load1 = load1.resize((400, 300), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.place(x=210, y=120)
        button1 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=1))
        button1.place(x=10, y=125)
        button2 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button2.place(x=10, y=189)
        button3 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button3.place(x=10, y=253)
        button4 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button4.place(x=10, y=317)
        button5 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                            command=lambda: controller.show_endframe(correct=0))
        button5.place(x=10, y=381)


######################################## QUESTION TWO
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('NAME_HERE_q2.png')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        load1 = Image.open("q2.png")
        # load1 = load1.resize((100, 125), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.place(x=210, y=120)

        button1 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=1))
        button1.place(x=10, y=125)
        button2 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button2.place(x=10, y=189)
        button3 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button3.place(x=10, y=253)
        button4 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button4.place(x=10, y=317)
        button5 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                            command=lambda: controller.show_endframe(correct=0))
        button5.place(x=10, y=381)


###################################### QUESTION THREE
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('NAME_HERE_q3.png')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        load1 = Image.open("q3.png")
        load1 = load1.resize((400, 300), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.place(x=210, y=120)

        button1 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=1))
        button1.place(x=10, y=125)
        button2 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button2.place(x=10, y=189)
        button3 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button3.place(x=10, y=253)
        button4 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button4.place(x=10, y=317)
        button5 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                            command=lambda: controller.show_endframe(correct=0))
        button5.place(x=10, y=381)


###################################### QUESTION FOUR
class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('NAME_HERE_q4.png')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        load1 = Image.open("q4.png")
        # load1 = load1.resize((100, 125), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.place(x=210, y=120)

        button1 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=1))
        button1.place(x=10, y=125)
        button2 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button2.place(x=10, y=189)
        button3 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button3.place(x=10, y=253)
        button4 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button4.place(x=10, y=317)
        button5 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                            command=lambda: controller.show_endframe(correct=0))
        button5.place(x=10, y=381)


###################################### QUESTION FIVE
class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('NAME_HERE_q5.png')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        load1 = Image.open("q5.png")
        # load1 = load1.resize((100, 125), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.place(x=210, y=120)
        button1 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=1))
        button1.place(x=10, y=125)
        button2 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button2.place(x=10, y=189)
        button3 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button3.place(x=10, y=253)
        button4 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button4.place(x=10, y=317)
        button5 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                            command=lambda: controller.show_endframe(correct=0))
        button5.place(x=10, y=381)


###################################### QUESTION SIX
class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('NAME_HERE_q6.png')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        load1 = Image.open("q6.png")
        load1 = load1.resize((400, 300), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.place(x=210, y=120)

        button1 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=1))
        button1.place(x=10, y=125)
        button2 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button2.place(x=10, y=189)
        button3 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button3.place(x=10, y=253)
        button4 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button4.place(x=10, y=317)
        button5 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                            command=lambda: controller.show_endframe(correct=0))
        button5.place(x=10, y=381)


###################################### QUESTION SEVEN
class PageSeven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('NAME_HERE_q7.png')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        load1 = Image.open("q7.png")
        # load1 = load1.resize((100, 125), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.place(x=210, y=120)
        button1 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=1))
        button1.place(x=10, y=125)
        button2 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button2.place(x=10, y=189)
        button3 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button3.place(x=10, y=253)
        button4 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button4.place(x=10, y=317)
        button5 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                            command=lambda: controller.show_endframe(correct=0))
        button5.place(x=10, y=381)


###################################### QUESTION 8
class PageEight(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('NAME_HERE_q8.png')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        load1 = Image.open("q8.png")
        # load1 = load1.resize((100, 125), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.place(x=210, y=120)

        button1 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=1))
        button1.place(x=10, y=125)
        button2 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button2.place(x=10, y=189)
        button3 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button3.place(x=10, y=253)
        button4 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button4.place(x=10, y=317)
        button5 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                            command=lambda: controller.show_endframe(correct=0))
        button5.place(x=10, y=381)


###################################### RESULTS
class PageNine(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('NAME_HERE_q9.png')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        load1 = Image.open("q9.png")
        # load1 = load1.resize((100, 125), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.place(x=210, y=120)
        button1 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=1))
        button1.place(x=10, y=125)
        button2 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button2.place(x=10, y=189)
        button3 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button3.place(x=10, y=253)
        button4 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button4.place(x=10, y=317)
        button5 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                            command=lambda: controller.show_endframe(correct=0))
        button5.place(x=10, y=381)


###################################### QUESTION TEN
class PageTen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('NAME_HERE_q10.png')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        load1 = Image.open("q10.png")
        load1 = load1.resize((400, 300), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.place(x=210, y=120)
        button1 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=1))
        button1.place(x=10, y=125)
        button2 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button2.place(x=10, y=189)
        button3 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button3.place(x=10, y=253)
        button4 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                                    command=lambda: controller.show_endframe(correct=0))
        button4.place(x=10, y=317)
        button5 = tk.Button(self, text='ANSWER CHOICE',  font=BUTTON_FONT, height=2, width=20,
                            command=lambda: controller.show_endframe(correct=0))
        button5.place(x=10, y=381)

###################################### RESULTS
class EndPage0(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('backgroundnar.jpg')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text='0%',font=LARGE_FONT, bg='#935116', fg='white')
        label.pack(pady=10, padx=10)
        load1 = Image.open("end0.JPG")
        load1 = load1. resize((177, 236), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.pack()
        button1 = tk.Button(self, text='Try again', font=('Arial', 12), bg='#95A5A6',
                            command=lambda: controller.show_frameQ1(parent))
        button1.pack(pady=10)
        button2 = tk.Button(self, text='Exit', font=('Arial', 12),
                            command=exit)
        button2.config(bg='red')
        button2.pack(pady=10)

class EndPage1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('backgroundnar.jpg')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text='10%',
                         font=LARGE_FONT, bg='#935116', fg='white')
        label.pack(pady=10, padx=10)
        load1 = Image.open("end1.JPG")
        load1 = load1. resize((128, 263), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.pack()
        button1 = tk.Button(self, text='Try again', font=('Arial', 12), bg='#95A5A6',
                            command=lambda: controller.show_frameQ1(parent))
        button1.pack(pady=10)
        button2 = tk.Button(self, text='Exit', font=('Arial', 12),
                            command=exit)
        button2.config(bg='red')
        button2.pack(pady=10)

class EndPage2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('backgroundnar.jpg')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text='20%',
                         font=LARGE_FONT, bg='#935116', fg='white')
        label.pack(pady=10, padx=10)
        load1 = Image.open("end2.JPG")
        load1 = load1. resize((171, 320), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.pack()
        button1 = tk.Button(self, text='Try again', font=('Arial', 12), bg='#95A5A6',
                            command=lambda: controller.show_frameQ1(parent))
        button1.pack(pady=10)
        button2 = tk.Button(self, text='Exit', font=('Arial', 12),
                            command=exit)
        button2.config(bg='red')
        button2.pack(pady=10)

class EndPage3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('backgroundnar.jpg')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text='30%',font=LARGE_FONT, bg='#935116', fg='white')
        label.pack(pady=10, padx=10)
        load1 = Image.open("end3.JPG")
        load1 = load1. resize((176, 293), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.pack()
        button1 = tk.Button(self, text='Try again', font=('Arial', 12), bg='#95A5A6',
                            command=lambda: controller.show_frameQ1(parent))
        button1.pack(pady=10)
        button2 = tk.Button(self, text='Exit', font=('Arial', 12),
                            command=exit)
        button2.config(bg='red')
        button2.pack(pady=10)

class EndPage4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('backgroundnar.jpg')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text='40%',
                         font=LARGE_FONT, bg='#935116', fg='white')
        label.pack(pady=10, padx=10)
        load1 = Image.open("end4.JPG")
        load1 = load1. resize((220, 293), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.pack()
        button1 = tk.Button(self, text='Try again', font=('Arial', 12), bg='#95A5A6',
                            command=lambda: controller.show_frameQ1(parent))
        button1.pack(pady=10)
        button2 = tk.Button(self, text='Exit', font=('Arial', 12),
                            command=exit)
        button2.config(bg='red')
        button2.pack(pady=10)

class EndPage5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('backgroundnar.jpg')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text='50%',font=LARGE_FONT, bg='#935116', fg='white')
        label.pack(pady=10, padx=10)
        load1 = Image.open("end5.png")
        load1 = load1. resize((202, 234), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.pack()
        button1 = tk.Button(self, text='Try again', font=('Arial', 12), bg='#95A5A6',
                            command=lambda: controller.show_frameQ1(parent))
        button1.pack(pady=10)
        button2 = tk.Button(self, text='Exit', font=('Arial', 12),
                            command=exit)
        button2.config(bg='red')
        button2.pack(pady=10)

class EndPage6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('backgroundnar.jpg')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text='60%',font=LARGE_FONT, bg='#935116', fg='white')
        label.pack(pady=10, padx=10)
        load1 = Image.open("end6.png")
        load1 = load1. resize((300, 300), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.pack()
        button1 = tk.Button(self, text='Try again', font=('Arial', 12), bg='#95A5A6',
                            command=lambda: controller.show_frameQ1(parent))
        button1.pack(pady=10)
        button2 = tk.Button(self, text='Exit', font=('Arial', 12),
                            command=exit)
        button2.config(bg='red')
        button2.pack(pady=10)

class EndPage7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('backgroundnar.jpg')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text='70%',font=LARGE_FONT, bg='#935116', fg='white')
        label.pack(pady=10, padx=10)
        load1 = Image.open("end7.JPG")
        load1 = load1. resize((302, 170), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.pack()
        button1 = tk.Button(self, text='Try again', font=('Arial', 12), bg='#95A5A6',
                            command=lambda: controller.show_frameQ1(parent))
        button1.pack(pady=10)
        button2 = tk.Button(self, text='Exit', font=('Arial', 12),
                            command=exit)
        button2.config(bg='red')
        button2.pack(pady=10)

class EndPage8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('backgroundnar.jpg')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text='80%',font=LARGE_FONT, bg='#935116', fg='white')
        label.pack(pady=10, padx=10)
        load1 = Image.open("end8.JPG")
        load1 = load1. resize((240, 320), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.pack()
        button1 = tk.Button(self, text='Try again', font=('Arial', 12), bg='#95A5A6',
                            command=lambda: controller.show_frameQ1(parent))
        button1.pack(pady=10)
        button2 = tk.Button(self, text='Exit', font=('Arial', 12),
                            command=exit)
        button2.config(bg='red')
        button2.pack(pady=10)

class EndPage9(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('backgroundnar.jpg')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text='90%',font=LARGE_FONT, bg='#935116', fg='white')
        label.pack(pady=10, padx=10)
        load1 = Image.open("end9.png")
        load1 = load1. resize((300, 300), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.pack()
        button1 = tk.Button(self, text='Try again', font=('Arial', 12), bg='#95A5A6',
                            command=lambda: controller.show_frameQ1(parent))
        button1.pack(pady=10)
        button2 = tk.Button(self, text='Exit', font=('Arial', 12),
                            command=exit)
        button2.config(bg='red')
        button2.pack(pady=10)

class EndPage10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('backgroundnar.jpg')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text='100%',font=LARGE_FONT, bg='#935116', fg='white')
        label.pack(pady=10, padx=10)
        load1 = Image.open("end10.jpg")
        load1 = load1. resize((300, 300), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.pack()

        button2 = tk.Button(self, text='Exit', font=('Arial', 12),
                            command=exit)
        button2.config(bg='red')
        button2.pack(pady=10)
        button3 = tk.Button(self, text='Credits [BONUS]', font=('Arial', 12),
                            command=lambda: controller.show_frame(Credits))
        button3.config(bg='green', fg='white')
        button3.pack(pady=10)


class EndPage10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('backgroundnar.jpg')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text='100%: Happy birthday!',
                         font=LARGE_FONT, bg='#935116', fg='white')
        label.pack(pady=10, padx=10)
        load1 = Image.open("end10.jpg")
        load1 = load1.resize((216, 216), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.pack()

        button2 = tk.Button(self, text='Exit', font=('Arial', 12),
                            command=exit)
        button2.config(bg='red')
        button2.pack(pady=10)
        button3 = tk.Button(self, text='BONUS', font=('Arial', 12),
                            command=lambda: controller.show_frame(Credits))
        button3.config(bg='lightblue', fg='white')
        button3.pack(pady=10)

class Credits(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        bgload = Image.open('backgroundnar.jpg')
        background_image = ImageTk.PhotoImage(bgload)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text='Happy birthday!',font=('Vladimir Script',18))
        label.pack(pady=10, padx=10)
        load1 = Image.open("credits.jpg")
        load1 = load1. resize((232, 300), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        label2 = tk.Label(self, image=render1)
        label2.image = render1
        label2.pack()
        button1 = tk.Button(self, text='Do it again', font=('Arial', 12), bg='#95A5A6',
                            command=lambda: controller.show_frameStart())
        button1.pack(pady=10)
        button2 = tk.Button(self, text='Exit', font=('Arial', 12),
                            command=exit)
        button2.config(bg='red')
        button2.pack(pady=10)

app = NAME_HEREQuiz()
app.geometry('640x480+400+200')
app.title("NAME_HERE Quiz")
app.resizable(False, False)
app.mainloop()