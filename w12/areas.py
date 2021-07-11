import tkinter as tk
import number_entry as numy
from math import pi as p

def main():

    root = tk.Tk()

    frm_main = tk.Frame(root)
    frm_main.master.title("Area Calculator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    setup_window(frm_main)

    root.mainloop()

def setup_window(frame):

    title_label = tk.Label(frame, text= "Welcome to the Circle Area Calculator.")
    title_label.grid(row=0)

    radius = tk.Label(frame, text="Please enter a measurement: ")
    ent_radius = numy.IntEntry(frame, 1, 90, width =5)
    ent_radius.grid(row=3)
    final_area = tk.Label(frame, width=20)
    final_area.grid(row=4)
    radius.grid(row=2, padx=3, pady=3)

    def calc(event):
        try:
            radius = ent_radius.get()
            area = p*radius**2
            final_area.config(text=f"{area:.2f}")
            

        except ValueError:
            print("Error.")
    
    ent_radius.bind("<KeyRelease>", calc)

        

main()