import tkinter as tk
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

words = []

def change_image_to_front():
    canvas.create_image(400, 263, image=card_front)

def change_image_to_back():
    canvas.create_image(400, 263, image=card_back)

def new_card():
    global words, id
    window.after_cancel(id)
    words = random.choice(data)
    canvas.selection_clear()
    canvas.itemconfig(card_title, text=list(data[0].keys())[-2], fill="black")
    canvas.itemconfig(card_word, text=words[list(data[0].keys())[-2]], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    id = window.after(ms=3000, func=flip_card)

def flip_card():
    global words
    canvas.itemconfig(card_word, text=words[list(data[0].keys())[-1]], fill="white")
    canvas.itemconfig(card_title, text=list(data[0].keys())[-1], fill="white", )
    canvas.itemconfig(card_image, image=card_back)

def right_button():
    try:
        data.remove(words)
        new_card()
    except IndexError:
        finish()
    else:
        data1 = pandas.DataFrame(data)
        data1.to_csv("data/words_to_learn.csv", index=False)

def wrong_button():
    new_card()
def finish():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text="Brawo!", fill="white")
    canvas.itemconfig(card_word, text="Wszystko umiesz :)", fill="white")


try:
    data = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/polang.csv", sep=';').to_dict(orient="records")



window = tk.Tk()
window.title("flashcard")
window.config(padx=50,  pady=50, bg=BACKGROUND_COLOR)

card_back = tk.PhotoImage(file="images/card_back.png")
card_front = tk.PhotoImage(file="images/card_front.png")
right = tk.PhotoImage(file="images/right.png")
wrong = tk.PhotoImage(file="images/wrong.png")

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400,263, image=card_front)
card_title = canvas.create_text(400, 150, text="Tittle", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), fill="black", width=800, anchor=tk.N)

canvas.grid(row=0, column=0, columnspan=2)

right_button = tk.Button(image=right, bg=BACKGROUND_COLOR, highlightthickness=0, command=right_button)
right_button.grid(row=1, column=1)

wrong_button = tk.Button(image=wrong, bg=BACKGROUND_COLOR, highlightthickness=0, command=wrong_button)
wrong_button.grid(row=1, column=0)

id = window.after(ms=3000, func=flip_card)
new_card()


window.mainloop()




