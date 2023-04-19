from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- GET A NEW WORD ------------------------------- #
data = pandas.read_csv('data/french_words.csv')
data = data.to_dict(orient='records')

def next_card():
    global data
    new_word = random.choice(data)
    canvas.itemconfig(card_title, text=list(new_word.keys())[0])
    canvas.itemconfig(card_word, text=new_word['French'])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Add image to the background
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=image)

card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))

canvas.grid(row=0, column=0, columnspan=2)

# Buttons
check_mark_image = PhotoImage(file="images/right.png")
known_button= Button(image=check_mark_image, highlightthickness=0, bg=BACKGROUND_COLOR, relief="flat", command=next_card)
known_button.grid(row=1, column=1)

cross_mark_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_mark_image, highlightthickness=0, bg=BACKGROUND_COLOR, relief="flat", command=next_card)
unknown_button.grid(row=1, column=0)

next_card()

window.mainloop()
