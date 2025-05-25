import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import databaseConnection
from insert import insertValue
from utils import add_to_treeview, clear  # Import from utils.py

def insert_button_clicked():
    from insert import insertValue  # Move the import here to avoid circular import
    insertValue(id_entry, name_entry, des_entry, variable1, status_entry)

app = customtkinter.CTk()

app = customtkinter.CTk()
app.title('Employee Management System')
app.geometry('900x420')
app.config(bg='#161C25')
app.resizable(False, False)

font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 12, 'bold')


def add_to_treeview():
    employees = databaseConnection.fetch_data()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('', END, values=employee)

'''
def insert():
    id = id_entry.get()
    name = name_entry.get()
    des = des_entry.get()
    gender = variable1.get()
    status = status_entry.get()
    if not (id and name and des and gender and status):
        messagebox.showerror('Error', 'Enter all fields.')
    elif databaseConnection.id_exists(id):
        messagebox.showerror('Error', 'ID already exists.')
    else:
        databaseConnection.insert_data(id, name, des, gender, status)
        add_to_treeview()
        messagebox.showinfo('Success', 'Data has been inserted.')
'''

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    des_entry.delete(0, END)
    variable1.set('Male')
    status_entry.delete(0, END)


def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        id_entry.insert(0, row[0])
        name_entry.insert(0, row[1])
        des_entry.insert(0, row[2])
        variable1.set(row[3])
        status_entry.insert(0, row[4])
    else:
        pass


def update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Choose an employee to update.')
    else:
        id = id_entry.get()
        name = name_entry.get()
        des = des_entry.get()
        gender = variable1.get()
        status = status_entry.get()
        databaseConnection.update_data(name, des, gender, status, id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success', 'data has been updated.')

def delete():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Choose an employee to delete.')
    else:
        id = id_entry.get()
        databaseConnection.delete_data(id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success', 'Data has been deleted.')


id_label = customtkinter.CTkLabel(app, font=font1, text='ID:', text_color='#fff', bg_color='#161C25')
id_label.place(x=20, y=20)

id_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295',
                                  width=180)
id_entry.place(x=150, y=20)

name_label = customtkinter.CTkLabel(app, font=font1, text='Name:', text_color='#fff', bg_color='#161C25')
name_label.place(x=20, y=80)

name_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295',
                                    width=180)
name_entry.place(x=150, y=80)

des_label = customtkinter.CTkLabel(app, font=font1, text='Designation:', text_color='#fff', bg_color='#161C25')
des_label.place(x=20, y=140)

des_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295',
                                   width=180)
des_entry.place(x=150, y=140)

gender_label = customtkinter.CTkLabel(app, font=font1, text='Gender:', text_color='#fff', bg_color='#161C25')
gender_label.place(x=20, y=200)

options = ['Male', 'Female']
variable1 = StringVar()

gender_options = customtkinter.CTkComboBox(app, font=font1, text_color='#000', fg_color='#fff',
                                           dropdown_hover_color='#0C9295', button_hover_color='#0C9295',
                                           border_color='#0C9295', width=180, variable=variable1, values=options,
                                           state='readonly')
gender_options.set('Male')
gender_options.place(x=150, y=200)

status_label = customtkinter.CTkLabel(app, font=font1, text='Status:', text_color='#fff', bg_color='#161C25')
status_label.place(x=20, y=260)

status_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295',
                                      width=180)
status_entry.place(x=150, y=260)



# add_button = customtkinter.CTkButton(app, command=insert, font=font1, text='ADD Employee', text_color='#fff',
#                                      fg_color='#05A312', bg_color='#161C25', cursor='hand2', corner_radius=15,
#                                      width=260, hover_color='#00850B')
# add_button.place(x=20, y=310)


add_button = customtkinter.CTkButton(app, command=lambda: insertValue(id_entry, name_entry, des_entry, variable1, status_entry),
                                     font=font1, text='ADD Employee', text_color='#fff',
                                     fg_color='#05A312', bg_color='#161C25', cursor='hand2', corner_radius=15,
                                     width=260, hover_color='#00850B')

add_button.place(x=20, y=310)


clear_button = customtkinter.CTkButton(app, command=lambda: clear(True), font=font1, text='NEW Employee',
                                       text_color='#fff', fg_color='#161C25', bg_color='#161C25', cursor='hand2',
                                       corner_radius=15, width=260, hover_color='#FF5002', border_color='#F15704',
                                       border_width=2)
clear_button.place(x=20, y=360)

update_button = customtkinter.CTkButton(app, command=update, font=font1, text='UPDATE Employee', text_color='#fff',
                                        fg_color='#161C25', bg_color='#161C25', cursor='hand2', corner_radius=15,
                                        width=260, hover_color='#FF5002', border_color='#F15704', border_width=2)
update_button.place(x=300, y=360)

delete_button = customtkinter.CTkButton(app, command=delete, font=font1, text='DELETE Employee', text_color='#fff',
                                        fg_color='#FF0000', bg_color='#161C25', cursor='hand2', corner_radius=15,
                                        width=260, hover_color='#FA5F55', border_width=2)
delete_button.place(x=580, y=360)

style = ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview', font=font2, foreground='#fff', background='#000', fieldbackground='#313837')
style.map('Treeview', background=[('selected', '#1A8F2D')])

tree = ttk.Treeview(app, height=18)

tree['columns'] = ('ID', 'Name', 'Designation', 'Gender', 'Status')

tree.column('#0', width=0, stretch=tk.NO)
tree.column('ID', anchor=tk.CENTER, width=120)
tree.column('Name', anchor=tk.CENTER, width=120)
tree.column('Designation', anchor=tk.CENTER, width=150)
tree.column('Gender', anchor=tk.CENTER, width=120)
tree.column('Status', anchor=tk.CENTER, width=120)

tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Designation', text='Designation')
tree.heading('Gender', text='Gender')
tree.heading('Status', text='Status')

tree.place(x=600, y=40)

tree.bind('<ButtonRelease>', display_data)
add_to_treeview()
app.mainloop()



