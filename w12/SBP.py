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
    frame.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    display_options(frame)
    display_calendar(frame)

    root.mainloop()


def display_options(frame):

    new_sale = tk.Button(frame, text="Record Sale", fg="green",
            font=('Mistral 14 bold'), padx=5, pady=5, command=lambda:add_sale())
    new_sale.grid(row=1, column=0)

    edit_sale = tk.Button(frame, text="Edit Sale", fg="goldenrod",
            font=('Mistral 14 bold'), padx=5, pady=5, command=lambda:change_sale())
    edit_sale.grid(row=1, column=1)

    delete_sale = tk.Button(frame, text="Remove Sale", fg="red",
            font=('Mistral 14 bold'), padx=5, pady=5, command=lambda:remove_sale())
    delete_sale.grid(row=1, column=2)

    new_appt = tk.Button(frame, text="Add Appointment", fg="green",
            font=('Mistral 14 bold'), padx=5, pady=5, command=lambda:add_appt(frame))
    new_appt.grid(row=2, column=0)

    edit_appt = tk.Button(frame, text="Edit Appointment", fg="goldenrod",
            font=('Mistral 14 bold'), padx=5, pady=5, command=lambda:change_appt())
    edit_appt.grid(row=2, column=1)

    delete_appt = tk.Button(frame, text="Remove Appointment", fg="red",
            font=('Mistral 14 bold'), padx=5, pady=5, command=lambda:remove_appt())
    delete_appt.grid(row=2, column=2)


def display_calendar(frame):

    tk.Label(frame, text="Appointments:", font=('Mistral 18 bold')).grid(row=3, columnspan=3)
    
    with open(APPT_FILE, "r") as file:

        file.readline()

        count = 0
        for i in file:
            count += 1
            event = tk.Button(frame, text=i, padx=5)
            event.grid(row=count+3, columnspan=3)


def get_date_and_time():

    current_date_and_time = datetime.now()

    today = f"{current_date_and_time:%a, %b %d }"
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
        display_calendar(frame)


def change_appt():
    pass


def remove_appt():
    pass


def add_sale():
    pass


def change_sale():
    pass


def remove_sale():
    pass


def refresh_page():
    pass


if __name__ == "__main__":
    main()