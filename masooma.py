from tkinter import *
import customtkinter
from tkinter import messagebox
import Courses_db
from customtkinter import CTkSwitch



app = customtkinter.CTk()
app.title("Data Entry")
app.geometry("1920x1080+0+0")
app.resizable(True,True)

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")

font1 = ("Arial", 30, "bold")
font2 = ("Arial", 20, "bold")


def search_course():
    selection = variable3.get()
    if selection != "Select":
        row = Courses_db.search_courses(selection)
        if row:
            id_result_label.configure(text=str(row[0][0]))
            name_result_label.configure(text=str(row[0][1]))
            duration_result_label.configure(text=str(row[0][2]))
            format_result_label.configure(text=str(row[0][3]))
            language_result_label.configure(text=str(row[0][4]))
            price_result_label.configure(text=str(row[0][5]))
        else:
            messagebox.showerror("Error", "No course found with that ID.")
    else:
        messagebox.showerror("Error", "Select ID")


def insert_ids_options():
    ids = Courses_db.fetch_all_ids()
    print("Fetched IDs:", ids)  
    ids = Courses_db.fetch_all_ids()
    if ids is not None:
        ids = [str(id) for id in ids]
        ids_options.configure(values=ids)
    else:
        ids_options.configure(values=["No IDs Found"])



def submit_course():
    id_value = id_entry.get().strip()
    name_value = name_entry.get().strip()
    duration_value = duration_options.get()
    course_format_value = format_variable.get()
    language_value = language_entry.get().strip()
    price_value = price_entry.get().strip()

    try:
        if not (id_value and name_value and duration_value and course_format_value and language_value and price_value):
            messagebox.showerror("Error", "Enter all the fields.")
        elif not price_value.isdigit():
            messagebox.showerror("Error", "Price should be an integer.")
        elif Courses_db.id_exists(id_value):
            messagebox.showerror("Error", "ID already exists.")
        else:
            Courses_db.insert_course(id_value, name_value, duration_value, course_format_value, language_value, price_value)
            insert_ids_options()  # Update the ID options after insertion
            messagebox.showinfo("Success", "Data has been inserted.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def new_course():
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    duration_options.set("DURATION")
    format_variable.set("")
    language_entry.delete(0, END)
    price_entry.delete(0, END)


title_label = customtkinter.CTkLabel(app, font=font1, text="Courses Data Entry",fg_color="#131314",text_color="#CDCDC1", corner_radius=50)
title_label.place(x=345, y=63)

sw_01 = CTkSwitch(app, text="dark", onvalue="light", offvalue="dark",
                  command=lambda: [customtkinter.set_appearance_mode(sw_01.get()), sw_01.configure(text=sw_01.get())])
sw_01.grid(row=0, column=1)

frame1 = customtkinter.CTkFrame(app, fg_color="#131314", corner_radius=10, border_width=5,border_color="black", width=650, height=230)
frame1.place(x=350, y=120)

frame2 = customtkinter.CTkFrame(app, fg_color="#131314", corner_radius=10, border_width=5,border_color="black", width=650, height=230)
frame2.place(x=350, y=425)

id_label = customtkinter.CTkLabel(frame1, font=font2, text="Course ID:", text_color="#fff")
id_label.place(x=50, y=15)

id_entry = customtkinter.CTkEntry(frame1, font=font2, text_color="#000", fg_color="#fff", border_width=2, width=150)
id_entry.place(x=50, y=45)

name_label = customtkinter.CTkLabel(frame1, font=font2, text="Course Name:", text_color="#fff")
name_label.place(x=245, y=15)

name_entry = customtkinter.CTkEntry(frame1, font=font2, text_color="#000", fg_color="#fff", border_width=2, width=150)
name_entry.place(x=245, y=45)

duration_label = customtkinter.CTkLabel(frame1, font=font2, text="Course Duration:", text_color="#fff")
duration_label.place(x=445, y=15)

duration_options = customtkinter.CTkComboBox(frame1, font=font2, text_color="#000", fg_color="#fff", width=150, values=["1 Month", "2 Months", "3 Months"], state="readonly")
duration_options.set("DURATION")
duration_options.place(x=445, y=45)

format_label = customtkinter.CTkLabel(frame1, font=font2, text="Course Format:", text_color="#fff")
format_label.place(x=40, y=90)

format_variable = StringVar()
rb1 = customtkinter.CTkRadioButton(frame1, text="Online",text_color="white",fg_color="grey", font=font2, variable=format_variable, value="Online")
rb2 = customtkinter.CTkRadioButton(frame1, text="Class",text_color="white", fg_color="grey", font=font2, variable=format_variable, value="Class")
rb1.place(x=40, y=125)
rb2.place(x=140, y=125)

language_label = customtkinter.CTkLabel(frame1, font=font2, text="Course Language:", text_color="#fff")
language_label.place(x=245, y=90)

language_entry = customtkinter.CTkEntry(frame1, font=font2, text_color="#000", fg_color="#fff", border_width=2, width=150)
language_entry.place(x=245, y=120)

price_label = customtkinter.CTkLabel(frame1, font=font2, text="Course Price:", text_color="#fff")
price_label.place(x=445, y=90)

price_entry = customtkinter.CTkEntry(frame1, font=font2, text_color="#000", fg_color="#fff", border_width=2, width=150)
price_entry.place(x=445, y=120)

submit_button = customtkinter.CTkButton(frame1, font=font2, command=submit_course, text_color="#fff", text="Submit", cursor="hand2", corner_radius=5, width=100)
submit_button.place(x=410, y=170)

clear_button = customtkinter.CTkButton(frame1, font=font2, command=new_course, text_color="#fff", text="New Entry", cursor="hand2", corner_radius=5, width=100)
clear_button.place(x=520, y=170)

search_label = customtkinter.CTkLabel(app, font=font1,fg_color="#131314",corner_radius=50,text_color="#CDCDC1", text="Search by ID:")
search_label.place(x=360, y=370)

variable3 = StringVar()

ids_options = customtkinter.CTkComboBox(app, font=font2, text_color="#000", fg_color="#fff", width=150, variable=variable3)
ids_options.set("SELECT ID")
ids_options.place(x=600, y=375)

search_button = customtkinter.CTkButton(app, font=font2, command=search_course, text_color="#fff", text="Search", cursor="hand2", corner_radius=5, width=100)
search_button.place(x=780, y=375)

# Place frame 2 elements
id_result_label = customtkinter.CTkLabel(frame2, font=font2, text="Course ID:", text_color="#fff")
id_result_label.place(x=50, y=15)

name_result_label = customtkinter.CTkLabel(frame2, font=font2, text="Course Name:", text_color="#fff")
name_result_label.place(x=240, y=15)

duration_result_label = customtkinter.CTkLabel(frame2, font=font2, text="Course Duration:", text_color="#fff")
duration_result_label.place(x=450, y=15)

format_result_label = customtkinter.CTkLabel(frame2, font=font2, text="Course Format:", text_color="#fff")
format_result_label.place(x=40, y=110)

language_result_label = customtkinter.CTkLabel(frame2, font=font2, text="Course Language:", text_color="#fff")
language_result_label.place(x=240, y=110)

price_result_label = customtkinter.CTkLabel(frame2, font=font2, text="Course Price:", text_color="#fff")
price_result_label.place(x=450, y=110)

insert_ids_options()

app.mainloop()