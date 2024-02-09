from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
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
    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='You can\'t keep any fields empty.')
    else:
        is_ok =  messagebox.askokcancel(title=web, message=f"These are the details entered \nEmail: {email} \nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open('data.txt',mode='a') as data:
                data.write(f"{web} | {email} | {password}\n")
            web_entry.delete(0,END)
            pass_entry.delete(0,END)

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



window.mainloop()