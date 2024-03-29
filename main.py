from tkinter import *

from tkinter import ttk

#quit
def quit():
    main_window.destroy()

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



#create the buttons and labels
def append_details():
    pass


def setup_buttons():
    global customer_details, entry_Customer_Name,entry_Receipt_Number,entry_Item_Hired,entry_Quantity_Hired, total_entries, delete_item
    Button(main_window, text="Quit",command=quit) .grid(column=3, row=4)
    Button(main_window, text="Append Details",command=append_name) .grid(column=3,row=2)
    Button(main_window, text="Print Details",command=print_customer_details) .grid(column=3,row=3)

    # UI/Label
    Label(main_window, text='Julie''s Party Hire Store', font=('bold', 15)).grid(column=1, row=0, sticky=W + E)
    Label(main_window, text="Customer Name").grid(column=0, row=2)
    entry_Customer_Name = Entry(main_window)
    entry_Customer_Name.grid(column=1, row=2)
    Label(main_window, text="Receipt Number").grid(column=0, row=3)
    entry_Receipt_Number = Entry(main_window)
    entry_Receipt_Number.grid(column=1, row=3)
    Label(main_window, text="Item Hired").grid(column=0, row=4)

    item = StringVar()
    entry_Item_Hired = ttk.Combobox(main_window, state='readonly', textvariable=item, values=(
        "Chairs Tables Tableware Drapes Backdrops Props Balloons Partyhats Catering Lights Bouncyhouse"), width=17)
    entry_Item_Hired.grid(column=0, row=5)

    Label(main_window, text="Quantity Hired").grid(column=1, row=4)
    entry_Quantity_Hired = Entry(main_window)
    entry_Quantity_Hired.grid(column=1, row=5)
    Label(main_window, text="Row #").grid(column=0, row=6)
    delete_item = Entry(main_window)
    delete_item.grid(column=1, row=6)
    Button(main_window, text="Delete", command=delete_row).grid(column=2, row=6)

#Message to user to fill out Customer Name
    if len(entry_Customer_Name.get())==0:
        Label(main_window,fg='green',text='Please enter your name').grid(column=2,row=2,sticky=W)
        entry_check=1

    #Message to user to fill out a Custom Receipt number
    if len(entry_Receipt_Number.get())==0:
        Label(main_window,fg='green',text='Please enter your receipt number').grid(column=2,row=3,sticky=W)
        entry_check=1

    #Message to user to fill out wanted Hired Item
    if len(entry_Item_Hired.get())==0:
        Label(main_window,fg='green',text='Please choose your item').grid(column=2,row=5,sticky=W)
        entry_check=1

    #Message to user to fill out Quantity of hired Item
    if (entry_Quantity_Hired.get().isdigit()):
        if int(entry_Quantity_Hired.get()) < 1 or int(entry_Quantity_Hired.get()) > 500:
            Label(main_window,fg='green',text='1 to 500 only').grid(column=3,row=5,sticky=W)
            entry_check=1
    else:
        Label(main_window,fg='green',text='1 to 500 only').grid(column=3,row=5,sticky=W)
        entry_check=1
    if entry_check ==1:
        append_details()

#starting the program
def main():
    global main_window
    global customer_details, entry_name,entry_age,entry_gender, total_entries
    customer_details = ()
    total_entries = 0
    main_window = Tk()
    setup_buttons()
    main_window.mainloop()



main()





