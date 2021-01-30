
import tkinter as tk
from gradient import GradientFrame


class page_displayer:

    def __init__(self):
        # self.BACKGROUND_COLOR = "#add8e6" #The background color
        self.HEIGHT = 500 #This is the initial window size, everything will be resized if you change the size of the
        # window
        self.WIDTH = 800

        self.root = tk.Tk()  # Initializing root
        self.root.title("Something")  # setting window title name

        #initializing background:


        self.screen = tk.Canvas(self.root, width=self.WIDTH, height=self.HEIGHT)
        self.screen.pack()


        self.main_frame = GradientFrame(self.root, from_color="#000000", to_color="#E74C3C", height=1000)

        # Placing the background:
        self.main_frame.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor="n")

        self.main_frame.create_text(100,100,text="Click",fill="white")
        # PLACE HOLDER VALUES:
        self.root.bind("<Configure>", self.on_resize)

        self.list_of_objects = []  # we will store a list of objects so that we can delete things on the screen

    def on_resize(self):
        self.WIDTH = self.root.winfo_screenwidth()
        self.HEIGHT = self.root.winfo_screenheight()

        print("Working")
    def clear_page(self):
        # This function deletes every object on the page. It will be used when transitioning between pages.
        for object in self.list_of_objects:
            object.destroy()

        self.list_of_objects = []  # Just to make sure everything is fully wiped from memory
from gradient import GradientFrame
self=page_displayer()

self.screen.create_text(10,10,text="Click")
self.screen.update()
self.screen.mainloop()
