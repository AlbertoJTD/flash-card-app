from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- GET A NEW WORD ------------------------------- #
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
finally:
    words_to_learn = data.to_dict(orient='records')

current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text=list(current_card.keys())[0], fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- FLIP THE CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(card_title, text=list(current_card.keys())[1], fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(background, image=card_back_image)

def is_known():
    words_to_learn.remove(current_card)
    unknown_words = pandas.DataFrame(words_to_learn)
    unknown_words.to_csv('data/words_to_learn.csv', index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Add image to the background
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))

canvas.grid(row=0, column=0, columnspan=2)

# Buttons
check_mark_image = PhotoImage(file="images/right.png")
known_button= Button(image=check_mark_image, highlightthickness=0, bg=BACKGROUND_COLOR, relief="flat", command=is_known)
known_button.grid(row=1, column=1)

cross_mark_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_mark_image, highlightthickness=0, bg=BACKGROUND_COLOR, relief="flat", command=next_card)
unknown_button.grid(row=1, column=0)

next_card()

window.mainloop()
