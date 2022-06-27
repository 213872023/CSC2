from tkinter import *

from tkinter import ttk

#quit
def quit():
    main_window()

#Labels
def print_customer_details ():
    global j_names, total_entries, name_count
    name_count = 0
    Label(main_window, font='bold',text="Row").grid(column=0,row=7)
    Label(main_window, font='bold',text="Customer Name").grid(column=1,row=7)
    Label(main_window, font='bold',text="Receipt Number").grid(column=2,row=7)
    Label(main_window, font='bold',text="Item Hired").grid(column=3,row=7)
    Label(main_window, font='bold',text="Quantity Hired").grid(column=4,row=7)

    while name_count < total_entries:
        Label(main_window, text=name_count).grid(column=0, row=name_count + 8)
        Label(main_window, text=(customer_details[name_count][0])).grid(column=1, row=name_count + 8)
        Label(main_window, text=(customer_details[name_count][1])).grid(column=2, row=name_count + 8)
        Label(main_window, text=(customer_details[name_count][2])).grid(column=3, row=name_count + 8)
        Label(main_window, text=(customer_details[name_count][3])).grid(column=4, row=name_count + 8)
        name_count += 1







