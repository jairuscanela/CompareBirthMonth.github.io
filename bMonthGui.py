import tkinter as tk

GROUP_SIZE = 3
set_A = set([])
set_B = set([])
my_Bday = set([])

def compare_birthmonths():
    set_A.clear()
    set_B.clear()
    my_Bday.clear()

    # Input for set A
    for _ in range(GROUP_SIZE):
        get_birthmonth1 = entry_A.get()
        set_A.add(get_birthmonth1)

    # Input for set B
    for _ in range(GROUP_SIZE):
        get_birthmonth2 = entry_B.get()
        set_B.add(get_birthmonth2)

    get_bday = entry_my_bday.get()
    my_Bday.add(get_bday)

    result_text.set(f"Your Birth Month: {my_Bday}\nUnion: {set_A | set_B}\nIntersection: {set_A & set_B}\nDifference: {set_A - set_B}")

    if my_Bday.issubset(set_B) or my_Bday.issubset(set_A):
        result_text.set(result_text.get() + "\nYou have the same Birth Month with your classmates")
    else:
        result_text.set(result_text.get() + "\nYou don't have the same Birth Month with your classmates")

# GUI setup
root = tk.Tk()
root.title("Birth Month Comparison")

# Entry widgets
entry_A = tk.Entry(root, width=20, )
entry_B = tk.Entry(root, width=15)
entry_my_bday = tk.Entry(root, width=15)

# Labels
label_A = tk.Label(root, text="Enter birth month of set A:")
label_B = tk.Label(root, text="Enter birth month of set B:")
label_my_bday = tk.Label(root, text="Enter your Birth Month:")

# Button
compare_button = tk.Button(root, text="Compare Birth Months", command=compare_birthmonths)

# Result Label
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)

# Layout
label_A.grid(row=0, column=0)
entry_A.grid(row=0, column=1)
label_B.grid(row=1, column=0)
entry_B.grid(row=1, column=1)
label_my_bday.grid(row=2, column=0)
entry_my_bday.grid(row=2, column=1)
compare_button.grid(row=3, column=0, columnspan=2)
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
