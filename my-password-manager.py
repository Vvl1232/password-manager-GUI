# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    import random as rd
    import string
    password=""
    for _ in range(10):
        password += rd.choice(string.ascii_letters + string.digits + string.punctuation)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!!!", text="Make sure you haven't left any fields empty.")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"Is it okay to save?")
    if is_ok:
        with open("passwords.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        message_label.config(text="Password Saved")

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, pady=2)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, pady=2)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, pady=2)
message_label = Label(text="")
message_label.grid(row=5, column=1, columnspan=2, pady=2)

# entries
website_entry = Entry(width=55)
website_entry.grid(row=1, column=1, columnspan=2, pady=2)
website_entry.focus()
email_entry = Entry(width=55)
email_entry.grid(row=2, column=1, columnspan=2, pady=2)
email_entry.insert(0, "@gmail.com")
password_entry = Entry(width=37)
password_entry.grid(row=3, column=1, pady=2)
password_entry.config(show="*")

# buttons
generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(row=3, column=2, pady=2)
add_button = Button(text="Add", width=47, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=2)

window.mainloop()