import tkinter as tk
from pandas  import read_csv, DataFrame, errors
import random
from tkinter import messagebox


BACKGROUND_COLOR = "#B1DDC6"
window_flip_countdown = None
current_card = {}


def get_random_word_pair():
    global window_flip_countdown, current_card
    if window_flip_countdown:
        cancle_translation()
    if len(french_english_list) > 0:
        current_card = random.choice(french_english_list)
        french_word, english_word = current_card.values()
        canvas.itemconfig(canvas_image, image=img_card_front)
        canvas.itemconfig(canvas_language, text="French", fill="black")
        canvas.itemconfig(canvas_word, text=french_word, fill="black")
        window_flip_countdown = window.after(3000, flip_card, english_word)
        return french_word, english_word
    return None, None


def mark_known_word():
    global french_english_list
    french_word, english_word = get_random_word_pair()
    if french_word or english_word:
        french_english_list.remove(current_card)
        save_progress()
    else:
        messagebox.showinfo(title="WOW", message="You nailed it, no more words to learn!")
        exit()


def flip_card(word):
    canvas.itemconfig(canvas_image, image=img_card_back)
    canvas.itemconfig(canvas_language, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=word, fill="white")
    cancle_translation()


def cancle_translation():
    window.after_cancel(window_flip_countdown)


def save_progress():
    df = DataFrame(french_english_list)
    df.to_csv("data/words_to_learn.csv", index=False)


try:
    df_csv = read_csv("data/words_to_learn.csv")
    if len(df_csv) == 0:
        raise errors.EmptyDataError
except (FileNotFoundError, errors.EmptyDataError):
    try:
        df_csv = read_csv("data/french_words.csv")
    except FileNotFoundError:
        messagebox.showerror(title="Opps", message="Words file not found!")
        exit()


french_english_list = df_csv.to_dict(orient="records")

window = tk.Tk()
window.title("Language Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

img_card_front = tk.PhotoImage(file="images/card_front.png")
img_card_back = tk.PhotoImage(file="images/card_back.png")
img_button_right = tk.PhotoImage(file="images/right.png")
img_button_wrong = tk.PhotoImage(file="images/wrong.png")

canvas = tk.Canvas(width=820, height=540, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(410, 270, image=img_card_front)
canvas_language = canvas.create_text(410, 130, font=('Arial', 40, 'italic'))
canvas_word = canvas.create_text(410, 280, font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)
get_random_word_pair()

button_wrong = tk.Button(image=img_button_wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=get_random_word_pair)
button_wrong.grid(column=0, row=1, sticky=tk.W)

button_right = tk.Button(image=img_button_right, highlightthickness=0, bg=BACKGROUND_COLOR, command=mark_known_word)
button_right.grid(column=1, row=1, sticky=tk.E)


window.mainloop()
