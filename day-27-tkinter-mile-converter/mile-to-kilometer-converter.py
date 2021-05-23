import tkinter


def convert_miles():
    km = float(entry_mile.get()) * 1.609
    label_km_converted.config(
        text=f"{km:.2f}"
    )


app = tkinter.Tk()
app.title("Mile to Km converter")
app.minsize(width=250, height=100)
app.config(padx=20, pady=20)

entry_mile = tkinter.Entry(width=7)
entry_mile.focus()
entry_mile.grid(row=0, column=1)

label_mile = tkinter.Label(text="Mile")
label_mile.grid(row=0, column=2)

label_equals = tkinter.Label(text="equals")
label_equals.grid(row=1, column=0)

label_km_converted = tkinter.Label(text="")
label_km_converted.grid(row=1, column=1)

label_km = tkinter.Label(text="Km")
label_km.grid(row=1, column=2)


button_convert = tkinter.Button(text="Convert", command=convert_miles)
button_convert.grid(row=2, column=1)


app.mainloop()
