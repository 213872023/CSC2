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

#Entry's
def append_name ():
    global customer_details, entry_Customer_Name,entry_Receipt_Number,entry_Item_Hired,entry_Quantity_Hired, total_entries
    if len(entry_Customer_Name.get()) != 0 :
        customer_details.append([entry_Customer_Name.get(),entry_Receipt_Number.get(),entry_Item_Hired.get(),entry_Quantity_Hired.get()])
        entry_Customer_Name.delete(0,'end')
        entry_Receipt_Number.delete(0,'end')
        entry_Item_Hired.delete(0,'end')
        entry_Quantity_Hired.delete(0,'end')
        total_entries +=  1

#delete a row from the list
def delete_row ():
    global customer_details, delete_item, total_entries, name_count
    del customer_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0,'end')
    Label(main_window, text="                                 ").grid(column=0,row=name_count+7)
    Label(main_window, text="                                 ").grid(column=1,row=name_count+7)
    Label(main_window, text="                                 ").grid(column=2,row=name_count+7)
    Label(main_window, text="                                 ").grid(column=3,row=name_count+7)
    Label(main_window, text="                                 ").grid(column=4,row=name_count+7)
    print_customer_details()

def check():
    #variables used
    global details, entry_Customer_Name,entry_Receipt_Number,entry_Item_Hired,entry_Quantity_Hired,total_entries
    entry_check=1
    Label(main_window, text="                                                           ") .grid(column=2, row=2)
    Label(main_window, text="                                                           ") .grid(column=2, row=3)
    Label(main_window, text="                                                           ") .grid(column=2, row=4)
    Label(main_window, text="                                                           ") .grid(column=2, row=5)






