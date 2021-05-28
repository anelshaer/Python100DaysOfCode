import tkinter as tk
import time
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


PASSWORDS_FILE = "secure.dat"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_password():
    entry_password.delete(0, tk.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)
    entry_password.insert(0, "".join(password_list))
    pyperclip.copy(entry_password.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Empty Website/Password",
            message="You need to fill in these fields."
        )
    else:
        new_data = {
            website.lower(): {
                "username": username,
                "password": password
            }
        }

        is_ok = messagebox.askokcancel(
                title=f"{website}",
                message=f"You have entered:\nUsername: {username}\nPassword:{password}\nDo you want to save?"
                )

        if is_ok:
            try:
                with open(PASSWORDS_FILE, mode="r") as pass_file:
                    data = json.load(pass_file)
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
            finally:
                with open(PASSWORDS_FILE, mode="w") as pass_file:
                    json.dump(data, pass_file, indent=4)
                    entry_website.delete(0, tk.END)
                    entry_password.delete(0, tk.END)


# ---------------------------- Search Password ----------------------- #
def find_password():
    website = entry_website.get().lower()
    try:
        with open(PASSWORDS_FILE, mode="r") as pass_file:
            data = json.load(pass_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Opps", message="No data found!")
    else:
        if data.get(website):
            entry_username.delete(0, tk.END)
            entry_username.insert(0, data[website]["username"])
            entry_password.delete(0, tk.END)
            entry_password.insert(0, data[website]["password"])
            pyperclip.copy(entry_password.get())
        else:
            messagebox.showinfo(title="Opps", message=f"{website} is not found!")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("MyPass Manager")
window.config(padx=50, pady=50)
img_mypass = tk.PhotoImage(file="logo.png")

canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img_mypass)
canvas.grid(column=1, row=0)

label_website = tk.Label(text="Website:")
label_website.grid(column=0, row=1, sticky=tk.W)

entry_website = tk.Entry(width=30)
entry_website.focus()
entry_website.grid(column=1, row=1, columnspan=2, sticky=tk.W)

button_search = tk.Button(text="Search", width=15, command=find_password)
button_search.grid(column=2, row=1, sticky=tk.E)

label_username = tk.Label(text="Email/Username:")
label_username.grid(column=0, row=2, sticky=tk.W)

entry_username = tk.Entry(width=30)
entry_username.grid(column=1, row=2, columnspan=2, sticky=tk.W)

label_password = tk.Label(text="Password:")
label_password.grid(column=0, row=3, sticky=tk.W)

entry_password = tk.Entry(width=30)
entry_password.grid(column=1, row=3, sticky=tk.W)

button_pass_gen = tk.Button(text="Generate Password", command=random_password)
button_pass_gen.grid(column=2, row=3, sticky=tk.E)

button_add = tk.Button(text="Add", width=45, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
