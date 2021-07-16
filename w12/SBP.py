""" The Small Business Planner.
Uses tkinter and firebase to schedule and organize appointments.
"""

import tkinter as tk
from datetime import datetime
import csv

APPT_FILE = "cs111/w12/appt_data.csv"
SALES_FILE = "cs111/w12/sales_data.csv"


def main():

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.master.title("Small Business Planner")
    frame.pack(padx=15, pady=10, fill=tk.BOTH, expand=1,)

    display_header(frame)
    display_options(frame)
    display_appts(frame)

    root.mainloop()


def display_header(frame):

    now_date, now_time = get_date_and_time()
    time_text = f"{now_date} - {now_time}"

    clock = tk.Label(frame, text=time_text, font=('Mistral 16'),
            bg="white", padx=8, pady=4, width=30)
    clock.grid(row=0, columnspan=3)

    tk.Canvas(frame, width=5, height=10, fill=None).grid(row=1)


def display_options(frame):

    new_appt = tk.Button(frame, text="Add Appointment", fg="green", height=2,
            font=('Mistral 14 bold'), padx=5, pady=5, command=lambda:add_appt(frame))
    new_appt.grid(row=2, column=0)

    edit_appt = tk.Button(frame, text="Edit Appointment", fg="goldenrod", height=2,
            font=('Mistral 14 bold'), padx=5, pady=5, command=lambda:change_appt(frame))
    edit_appt.grid(row=2, column=1)

    delete_appt = tk.Button(frame, text="Remove Appointment", fg="red", height=2,
            font=('Mistral 14 bold'), padx=5, pady=5, command=lambda:remove_appt(frame))
    delete_appt.grid(row=2, column=2)


def display_appts(frame):

    tk.Label(frame, text="Appointments:", font=('Mistral 18 bold'), pady=5).grid(row=3, columnspan=3)

    all_appts = []
    
    with open(APPT_FILE, "r") as file:

        file.readline()

        for i in file:

            i_list = i.strip().split(",")
            all_appts.append(i_list)

    all_appts.sort()

    count = 0

    for i in all_appts:
        count += 1
            
        date = i[0]
        time = i[1]
        with_who = i[2]
        notes = i[3]

        button_text = f"{date} {time} - {with_who}\n{notes}"

        placeholder = tk.Canvas(frame, height=40, width=500, bg="lemon chiffon")
        placeholder.grid(row=count+3, columnspan=3)

        event = tk.Label(frame, text=button_text, background="lemon chiffon")
        event.grid(row=count+3, columnspan=3)


def get_date_and_time():

    current_date_and_time = datetime.now()

    today = f"{current_date_and_time:%A, %B %d}"
    now = f"{current_date_and_time:%I:%M %p}"

    return today, now


def add_appt(frame):

    top = tk.Toplevel(frame)
    top.title("Add an Appointment")
    tk.Label(top, text= "Enter the following:", font=('Mistral 18 bold')).grid(row=0, column=1)

    tk.Label(top, text= "Date:", font=('Mistral 14')).grid(row=1, column=0)
    ent_date = tk.Entry(top)
    ent_date.grid(row=1, column=1)

    tk.Label(top, text= "Time:", font=('Mistral 14')).grid(row=2, column=0)
    ent_time = tk.Entry(top)
    ent_time.grid(row=2, column=1)
    
    tk.Label(top, text= "With:", font=('Mistral 14')).grid(row=3, column=0)
    ent_title = tk.Entry(top)
    ent_title.grid(row=3, column=1)

    tk.Label(top, text= "Notes:", font=('Mistral 14')).grid(row=4, column=0)
    ent_notes = tk.Entry(top)
    ent_notes.grid(row=4, column=1)

    submit = tk.Button(top, text="Submit", padx=5, pady=5,
            command=lambda:push_info())
    submit.grid(row=5, column=1)


    def push_info():
    
        date = ent_date.get()
        time = ent_time.get()
        title = ent_title.get()
        notes = ent_notes.get()

        with open(APPT_FILE, "a") as file:
            write = csv.writer(file)
            write.writerow((date, time, title, notes))

        top.destroy()
        display_appts(frame)


def change_appt(frame):
    top = tk.Toplevel(frame)
    top.title("Select an Appointment")
    tk.Label(top, text= "Type the index of the appointment you wish to change.",
            font=('Mistral 18 bold'), padx=5, pady=5).grid(row=0, columnspan=3)

    ent_index = tk.Entry(top)
    ent_index.grid(row=1, column=0)
    select = tk.Button(top, text="Select", font=('Mistral 14'), command=lambda:edit_appt())
    select.grid(row=1, column=1)
    
    all_appts = []
    with open(APPT_FILE, "r") as file:

        file.readline()
        line_count = 0

        for i in file:
            line_count += 1

            i_list = i.strip().split(",")
            all_appts.append(i_list)

    row_count = 0
    for i in all_appts:
        row_count += 1
        
        date = i[0]
        time = i[1]
        with_who = i[2]
        notes = i[3]

        button_text = f"{date} {time} - {with_who}\n{notes}"

        tk.Label(top, text=row_count, font=('Mistral 22 bold'), bg="white").grid(row=row_count+1, column=3)

        placeholder = tk.Canvas(top, height=50, width=500, bg="lemon chiffon")
        placeholder.grid(row=row_count+1, columnspan=3)

        event_info = tk.Label(top, text=button_text, bg="lemon chiffon", padx=5, pady=5)
        event_info.grid(row=row_count+1, columnspan=3)

    def edit_appt():

        line_number = int(ent_index.get())

        with open(APPT_FILE, "r") as file:
            file_list = file.readlines()

            line = file_list[line_number]
    
        line = line.strip().split(",")

        date = line[0]
        time = line[1]
        with_who = line[2]
        notes = line[3]

        top_2 = tk.Toplevel(frame)
        top_2.title("Edit Appointment")
        tk.Label(top_2, text= "Edit the following:", font=('Mistral 18 bold')).grid(row=0, column=1)

        tk.Label(top_2, text= "Date:", font=('Mistral 14')).grid(row=1, column=0)
        ent_date = tk.Entry(top_2)
        ent_date.grid(row=1, column=1)
        ent_date.insert(0, date)

        tk.Label(top_2, text= "Time:", font=('Mistral 14')).grid(row=2, column=0)
        ent_time = tk.Entry(top_2)
        ent_time.grid(row=2, column=1)
        ent_time.insert(0, time)
        
        tk.Label(top_2, text= "With:", font=('Mistral 14')).grid(row=3, column=0)
        ent_title = tk.Entry(top_2)
        ent_title.grid(row=3, column=1)
        ent_title.insert(0, with_who)

        tk.Label(top_2, text= "Notes:", font=('Mistral 14')).grid(row=4, column=0)
        ent_notes = tk.Entry(top_2)
        ent_notes.grid(row=4, column=1)
        ent_notes.insert(0, notes)

        submit = tk.Button(top_2, text="Submit changes", padx=5, pady=5,
                command=lambda:push_info())
        submit.grid(row=5, column=1)

        def push_info():
        
            date = ent_date.get()
            time = ent_time.get()
            title = ent_title.get()
            notes = ent_notes.get()

            with open(APPT_FILE, "r") as file:
                appt_list = file.readlines()

            appt_list[line_number] = f"{date},{time},{title},{notes}\n"

            with open(APPT_FILE, "w") as file:
                
                for i in appt_list:
                    file.write(i)

            top_2.destroy()
            top.destroy()
            display_appts(frame)


def remove_appt(frame):
    top = tk.Toplevel(frame)
    top.title("Select an Appointment")
    tk.Label(top, text= "Type the index of the appointment you wish to delete.",
            font=('Mistral 18 bold'), padx=5, pady=5).grid(row=0, columnspan=3)

    ent_index = tk.Entry(top)
    ent_index.grid(row=1, column=0)
    select = tk.Button(top, text="delete", font=('Mistral 14'), command=lambda:delete_appt())
    select.grid(row=1, column=1)
    
    all_appts = []
    with open(APPT_FILE, "r") as file:

        file.readline()
        line_count = 0

        for i in file:
            line_count += 1

            i_list = i.strip().split(",")
            all_appts.append(i_list)

    row_count = 0
    for i in all_appts:
        row_count += 1
        
        date = i[0]
        time = i[1]
        with_who = i[2]
        notes = i[3]

        button_text = f"{date} {time} - {with_who}\n{notes}"

        tk.Label(top, text=row_count, font=('Mistral 22 bold'), bg="white").grid(row=row_count+1, column=3)

        placeholder = tk.Canvas(top, height=50, width=500, bg="lemon chiffon")
        placeholder.grid(row=row_count+1, columnspan=3)

        event_info = tk.Label(top, text=button_text, bg="lemon chiffon", padx=5, pady=5)
        event_info.grid(row=row_count+1, columnspan=3)

    def delete_appt():

        line_number = int(ent_index.get())

        top_2 = tk.Toplevel(frame)
        top_2.title("Verification")
        tk.Label(top_2, text= "Are you sure you want to delete this forever?",
                font=('Mistral 18 bold')).grid(row=0, columnspan=2)

        cancel = tk.Button(top_2, text="Cancel", padx=5, pady=5,
                command=lambda:leave())
        cancel.grid(row=1, column=0)
        submit = tk.Button(top_2, text="Submit changes", padx=5, pady=5,
                command=lambda:push_info())
        submit.grid(row=1, column=1)

        def leave():
            top_2.destroy()

        def push_info():

            with open(APPT_FILE, "r") as file:
                appt_list = file.readlines()

            appt_list[line_number] = ""

            with open(APPT_FILE, "w") as file:
                
                for i in appt_list:
                    file.write(i)

            top_2.destroy()
            top.destroy()
            display_appts(frame)


if __name__ == "__main__":
    main()