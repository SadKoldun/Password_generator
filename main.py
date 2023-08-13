import json
from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_entry.delete(0, END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letters = [random.choice(letters) for _ in range(nr_letters)]
    pass_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pass_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = pass_letters + pass_numbers + pass_symbols

    random.shuffle(password_list)

    password = ''.join(password_list)

    password_entry.insert(0, password)
    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    new_web = web_entry.get()
    new_email = email_entry.get()
    new_password = password_entry.get()
    new_data = {
        new_web: {
            'email': new_email,
            'password': new_password,
        }
                }
    if new_password == '' or new_email == '' or new_web == '':
        messagebox.showerror(title='Whoops', message='Missing information')
    else:
        try:
            with open('password_files.json', 'r') as pass_file:
                json_data = json.load(pass_file)
        except FileNotFoundError:
            with open('password_files.json', 'w') as pass_file:
                json.dump(new_data, pass_file, indent=4)
        else:
            json_data.update(new_data)
            with open('password_files.json', 'w') as pass_file:
                json.dump(json_data, pass_file, indent=4)

        finally:
            web_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            web_entry.focus()


def search_website():
    search_web = web_entry.get()
    try:
        with open('password_files.json', 'r') as pass_file:
            json_load = json.load(pass_file)
    except FileNotFoundError:
        messagebox.showerror(message='File not existed lol')
    else:
        if search_web in json_load:
            search_email = json_load[search_web]['email']
            search_pass = json_load[search_web]['password']
            messagebox.showinfo(title=search_web, message=f'Email: {search_email}\nPassword: {search_pass}')
        else:
            messagebox.showerror(title='Missing', message=f'Cant found info about {search_web}')
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

new_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=new_img)
canvas.grid(row=0, column=1)

web_label = Label(text='Website')
web_label.grid(row=1, column=0)

web_entry = Entry(width=33)
web_entry.grid(row=1, column=1)
web_entry.focus()

web_search = Button(text='Search', command=search_website)
web_search.grid(row=1,column=2)

email_label = Label(text='Email')
email_label.grid(row=2, column=0)

email_entry = Entry(width=43)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text='Password')
password_label.grid(row=3, column=0)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate_button = Button(text='Generate', command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='ADD', width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
