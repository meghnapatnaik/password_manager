from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
FONT = ("Arial", 10, "bold")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web_entry = website_entry.get()
    em_entry = email_entry.get()
    pass_entry = password_entry.get()
    if len(web_entry) == 0 or len(pass_entry) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="Details Entered", message=f"Website: {web_entry}\nEmail: {em_entry}\n"
                                                                     f"Password: {pass_entry}\nIs It fine to save?\n")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{web_entry} || {em_entry} || {pass_entry}\n")
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website = Label(text="Website:", font=FONT)
website.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")

email = Label(text="Email/Username:", font=FONT)
email.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.insert(0, "meghnapatnaik@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

password = Label(text="Password:", font=FONT)
password.grid(row=3, column=0)

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1, columnspan=1, sticky="EW")

password_button = Button(text="Generate Password", command=password_generator)
password_button.grid(row=3, column=2)

add_button = Button(text="   ADD", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
