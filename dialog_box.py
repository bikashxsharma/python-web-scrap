from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("Sipuli and Pikkulu App")

startD = StringVar()
endD = StringVar()
cityD = StringVar()


def database():
    start_d = startD.get()
    end_d = endD.get()
    city_d = c.get()
    print(start_d+end_d+city_d)


label_0 = Label(root, text="Sipuli and Pikkulu App",
                width=20, font=("bold", 20))
label_0.place(x=90, y=53)


start_date = Label(root, text="Start Date", width=20, font=("bold", 10))
start_date.place(x=80, y=130)

start_date_input = Entry(root, textvar=startD)
start_date_input.place(x=240, y=130)

end_date = Label(root, text="End Date", width=20, font=("bold", 10))
end_date.place(x=68, y=180)

end_date_input = Entry(root, textvar=endD)
end_date_input.place(x=240, y=180)


city = Label(root, text="City", width=20, font=("bold", 10))
city.place(x=70, y=280)

city_list = ['Helsinki', 'Vantaa', 'Espoo']
c = StringVar()
droplist = OptionMenu(root, c, *city_list)
droplist.config(width=15)
c.set('Select city')
droplist.place(x=240, y=280)


Button(root, text='Submit', width=20, bg='brown',
       fg='white', command=database).place(x=180, y=380)

root.mainloop()
