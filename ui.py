from tkinter import *
from controller import Controller

BACKGROUND_COLOR = "#B1DDC6"


class UI(Controller):
    def __init__(self):
        super().__init__()
        self.window = Tk()
        self.init_window()
        self.chosen_word = self.choose_random_french_word()
        self.canvas = Canvas(width=800, height=520, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.front_canvas_image = PhotoImage(file='./images/card_front.png')
        self.back_canvas_image = PhotoImage(file='./images/card_back.png')
        self.canvas_image = self.canvas.create_image(400, 260, image=self.front_canvas_image)
        self.language_word = self.canvas.create_text(400, 150, font="Ariel 40 italic", text="French")
        self.displayed_word = self.canvas.create_text(400, 263, font="Ariel 60 bold", text=self.chosen_word["French"])
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.wrong_button_image = PhotoImage(file="./images/wrong.png")
        self.wrong_button = Button(image=self.wrong_button_image, highlightthickness=0,
                                   command=lambda: self.set_new_word(False))
        self.wrong_button.grid(row=1, column=0)
        self.right_button_image = PhotoImage(file="./images/right.png")
        self.right_button = Button(image=self.right_button_image, highlightthickness=0,
                                   command=lambda: self.set_new_word(True))
        self.right_button.grid(row=1, column=1)
        self.flip_timer = self.window.after(3000, self.show_english)

    def init_window(self):
        self.window.title("Flashy")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.window.minsize(width=800, height=800)

    def set_new_word(self, cancel):
        print(cancel)
        self.window.after_cancel(self.flip_timer)
        if cancel:
            self.raw_dictionary_data.remove(self.chosen_word)
            self.cancel_data()
            print(self.raw_dictionary_data)
        self.chosen_word = self.choose_random_french_word()
        self.canvas.itemconfig(self.canvas_image, image=self.front_canvas_image)
        self.canvas.itemconfig(self.language_word, text="French", fill="black")
        self.canvas.itemconfig(self.displayed_word, text=self.chosen_word["French"], fill="black")
        self.flip_timer = self.window.after(3000, self.show_english)

    def show_english(self):
        self.canvas.itemconfig(self.canvas_image, image=self.back_canvas_image)
        self.canvas.itemconfig(self.displayed_word, text=self.chosen_word["English"], fill="white")
        self.canvas.itemconfig(self.language_word, text="English", fill="white")
