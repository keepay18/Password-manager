import tkinter
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='white')

canvas = tkinter.Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo_image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text='Website:', fg='black', bg='white')
website_label.grid(column=0, row=1)

website_entry = tkinter.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

username_label = tkinter.Label(text='Email/Username:', fg='black', bg='white')
username_label.grid(column=0, row=2)

username_entry = tkinter.Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)

password_label = tkinter.Label(text='Password:', fg='black', bg='white')
password_label.grid(column=0, row=3)

password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_button = tkinter.Button(text='Generate Password')
generate_password_button.grid(column=2, row=3)

add_button = tkinter.Button(text='Add', width=36)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
