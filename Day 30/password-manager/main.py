from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)] + [chr(i) for i in range(ord('a'), ord('z')+1)]
    number = [str(i) for i in range(10)]
    symbols = ['!', '@', '#', '$', '%', '&', '*', '+','(',')']

    num_alphabets = randint(8,10)
    num_numbers = randint(2,4)
    num_special =randint(2,4)

    pass_letters = [choice(alphabet) for _ in range(num_alphabets)]
    pass_number = [choice(number) for _ in range(num_numbers)]
    pass_symbol = [choice(symbols) for _ in range(num_special)]
    password_list = pass_letters + pass_number + pass_symbol
    shuffle(password_list)
    pass_word = "".join(password_list)
    pass_entry.insert(0,pass_word)
    pyperclip.copy(pass_word)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    web = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        web:{
            'email':email,
            'password':password,
        }
    }
    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='You can\'t keep any fields empty.')
    else:
        try:
            with open('data.json',mode='r') as data:
                file = json.load(data)
                file.update(new_data)
        except FileNotFoundError:
            with open('data.json','w') as data:
                json.dump(new_data,data,indent=4)
        else:
            with open('data.json','w') as data:
                json.dump(file,data,indent=4)
        finally:
            web_entry.delete(0,END)
            pass_entry.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_pass():
    web = web_entry.get()
    try:
        with open('data.json') as data:
            file = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message = 'No data file found')
    else:
        if web in file:
                email = file[web]["email"]
                password = file[web]['password']
                messagebox.showinfo(title=web, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title='Error',message=f'There is no entry for {web}')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

canvas = Canvas(width = 200, height = 200)
photo = PhotoImage(file='logo.png')
canvas.create_image(100,100,image = photo)
canvas.grid(column=1,row=0)

web_label = Label(text='Website:')
web_label.grid(row=1,column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2,column=0)

pass_label = Label(text='Password:')
pass_label.grid(column=0,row=3)

web_entry = Entry(width=39)
web_entry.grid(column=1,row=1,columnspan=2)
web_entry.focus()

email_entry = Entry(width=39)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,'harsh@gmail.com')

pass_entry = Entry(width=21)
pass_entry.grid(column=1,row=3)

pass_button = Button(text="Generate Password",command=pass_generator)
pass_button.grid(column=2,row=3)

add_button = Button(text="Add",width=33,command=save_details)
add_button.grid(column=1,row=4,columnspan=2)

search_button = Button(text='Search',width=13,command=find_pass)
search_button.grid(column=2,row=1)

window.mainloop()