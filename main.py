import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


def add_details():
    if entry1.get() and entry2.get() and entry3.get():
        choice = messagebox.askokcancel(title="Confirmation", message=f"Are you sure the details are correct?\nWebsite: {entry1.get().title()}\nEmail: {entry2.get()}\nPassword: {entry3.get()}")

        if choice:
            # Updating this code to JSON
            # with open("password.txt", mode="a") as file:
            #     new_line = f"{entry1.get()}: {entry2.get()}(email), {entry3.get()}(password)\n"
            #     file.write(new_line)
            new_data = {
                entry1.get().title(): {
                    "email": entry2.get(),
                    "password": entry3.get()
                }
            }
            try:
                with open("password.json", mode="r") as file:
                    data = json.load(file)
            except json.decoder.JSONDecodeError:
                data = {}
                data.update(new_data)
                with open("password.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            except FileNotFoundError:
                with open("password.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("password.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                entry1.delete(0, tkinter.END)
                entry3.delete(0, tkinter.END)
    else:
        messagebox.showerror("Missing Credentials", message="Please fill all three fields (website, email, password)")


def generate_password():
    entry3.delete(0, tkinter.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    entry3.insert(tkinter.END, password)
    # pyperclip.copy(entry3.get())
    window.clipboard_clear()
    window.clipboard_append(entry3.get())


def search_details():
    try:
        with open("password.json", mode="r") as file:
            data = json.load(file)
        details = data[entry1.get().title()]
        messagebox.showinfo(entry1.get().title(), f"Email: {details['email']}\nPassword: {details['password']}")
    except json.decoder.JSONDecodeError:
        messagebox.showerror("Empty File", "Sorry, the file is empty.")
    except FileNotFoundError:
        messagebox.showerror("Not Found", "Sorry, the file could not be found.")
    except KeyError as error_message:
        if not entry1.get():
            messagebox.showerror("Not Found", "Please enter something inside of the website field.")
        else:
            messagebox.showerror("Not Found", f"Sorry, no data exits under the website '{error_message}'.")


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
photo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

label1 = tkinter.Label(text="Website:", width=15)
label1.grid(column=0, row=1)

label2 = tkinter.Label(text="Email/Username:")
label2.grid(column=0, row=2)

label3 = tkinter.Label(text="Password:")
label3.grid(column=0, row=3)

entry1 = tkinter.Entry()
entry1.focus()
entry1.grid(column=1, row=1, sticky="EW")

entry2 = tkinter.Entry()
entry2.insert(tkinter.END, "farhantcs13@gmail.com")
entry2.grid(column=1, row=2, columnspan=2, sticky="EW")

entry3 = tkinter.Entry(width=21)
entry3.grid(column=1, row=3, sticky="EW")

button1 = tkinter.Button(text="Generate Password", command=generate_password)
button1.grid(column=2, row=3, sticky="EW")

button2 = tkinter.Button(text="Add", command=add_details)
button2.grid(column=1, row=4, columnspan=2, sticky="EW")

button3 = tkinter.Button(text="Search", command=search_details)
button3.grid(column=2, row=1, sticky="EW")

window.mainloop()
