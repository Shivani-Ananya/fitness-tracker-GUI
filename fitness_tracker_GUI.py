import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Fitness Tracker Project")
root.geometry("900x800")
root.config(bg="#DCC5B2")

notebook = ttk.Notebook(root)
notebook.pack(expand = True, fill = 'both')

tab1 = tk.Frame(notebook)
notebook.add(tab1, text = "Add Entry")
frame1 = tk.Frame(tab1, padx =20, pady = 20)
frame1.pack(pady = 40)
tk.Label(frame1, text="Date (YYYY-MM-DD):", font=('Arial', 12)).grid(row=0, column=0, sticky='w', pady=5)
date_entry = tk.Entry(frame1, width=30, font=('Arial', 12))
date_entry.grid(row=0, column=1, pady=5)
tk.Label(frame1, text="Steps: ", font=('Arial', 12)).grid(row=1, column=0, sticky='w', pady=5)
steps_entry = tk.Entry(frame1, width=30, font=('Arial', 12))
steps_entry.grid(row=1, column=1, pady=5)
tk.Label(frame1, text="Workout Type: ", font=('Arial', 12)).grid(row=2, column=0, sticky='w', pady=5)
workout_types = ['Jogging', 'Walking', 'Yoga', 'Gym', 'Cycling', 'Swimming']
workout_entry = ttk.Combobox(frame1, values=workout_types, font=('Arial', 12), state='readonly', width=28)
workout_entry.grid(row=2, column=1, pady=5)
workout_entry.current(0)
tk.Label(frame1, text="Duration: ", font=('Arial', 12)).grid(row=3, column=0, sticky='w', pady=5)
duration_entry = tk.Entry(frame1, width=30, font=('Arial', 12))
duration_entry.grid(row=3, column=1, pady=5)
tk.Label(frame1, text="Calorie Burnt: ", font=('Arial', 12)).grid(row=4, column=0, sticky='w', pady=5)
calorie_entry = tk.Entry(frame1, width=30, font=('Arial', 12))
calorie_entry.grid(row=4, column=1, pady=5)
def add_entry():
    date = date_entry.get()
    steps = steps_entry.get()
    workout = workout_entry.get()
    duration = duration_entry.get()
    calories = calorie_entry.get()
    if date and steps and workout and duration and calories:
        tree.insert("", "end", values=(date, steps, workout, duration, calories))
        print("Entry added to Treeview!")
        date_entry.delete(0, tk.END)
        steps_entry.delete(0, tk.END)
        workout_entry.current(0)
        duration_entry.delete(0, tk.END)
        calorie_entry.delete(0, tk.END)
    else:
        print("Please fill out all fields.")
submitbutton= tk.Button(frame1, text="Submit Entry", font=('Arial', 14), bg="#D9A299", fg="white", width=20, command = add_entry)
submitbutton.grid(row=5, column=0, columnspan=2, pady=20)

tab2 = tk.Frame(notebook)
notebook.add(tab2, text = "View logs")
frame2 = tk.Frame(tab2, padx=20, pady=20)
frame2.pack(pady=30)
columns = ("Date", "Steps", "Workout", "Duration", "Calories")
tree = ttk.Treeview(frame2, columns = columns, show = "headings", height = 15)
tree.pack(side = "left")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=130)
scrollbar = ttk.Scrollbar(frame2, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
tree.insert("", "end", values=("2025-07-11", "7000", "Jogging", "30", "250"))
tree.insert("", "end", values=("2025-07-12", "8000", "Cycling", "40", "300"))

tab3 = tk.Frame(notebook)
notebook.add(tab3, text="Search Log")
frame3 = tk.Frame(tab3, padx=20, pady=20)
frame3.pack(pady=30)
tk.Label(frame3, text="Enter Search Date (YYYY-MM-DD):", font=('Arial', 12)).grid(row=0, column=0, sticky='w', pady=5)
search_entry = tk.Entry(frame3, width=30, font=('Arial', 12))
search_entry.grid(row=0, column=1, pady=5)
search_columns = ("Date", "Steps", "Workout", "Duration", "Calories")
search_tree = ttk.Treeview(frame3, columns=search_columns, show="headings", height=5)
search_tree.grid(row=3, column=0, columnspan=2, pady=20)
for col in search_columns:
    search_tree.heading(col, text=col)
    search_tree.column(col, width=120)
def search_log():
    search_date = search_entry.get()
    for item in search_tree.get_children():
        search_tree.delete(item)
    found = False
    for child in tree.get_children():
        values = tree.item(child)["values"]
        if values[0] == search_date:
            search_tree.insert("", "end", values=values)
            found = True
    if not found:
        search_tree.insert("", "end", values=("No record found", "", "", "", ""))
search_button = tk.Button(frame3, text="Search", font=('Arial', 14), bg="#D9A299", fg="white", width=20, command=search_log)
search_button.grid(row=1, column=0, columnspan=2, pady=20)


tab4 = tk.Frame(notebook)
notebook.add(tab4, text = "update a log")
frame4 = tk.Frame(tab4, padx=20, pady=20)
frame4.pack(pady=30)
tk.Label(frame4, text="Select to update Date (YYYY-MM-DD):", font=('Arial', 12)).grid(row=0, column=0, sticky='w', pady=5)
new_name = tk.Entry(frame4, width=30, font=('Arial', 12))
new_name.grid(row=0, column=1, pady=5)
tk.Label(frame4, text="New steps:", font=('Arial', 12)).grid(row=1, column=0, sticky='w', pady=5)
new_steps = tk.Entry(frame4, width=30, font=('Arial', 12))
new_steps.grid(row=1, column=1, pady=5)
tk.Label(frame4, text="Workout Type: ", font=('Arial', 12)).grid(row=2, column=0, sticky='w', pady=5)
new_workout = ['Jogging', 'Walking', 'Yoga', 'Gym', 'Cycling', 'Swimming']
new_workout = ttk.Combobox(frame4, values=new_workout, font=('Arial', 12), state='readonly', width=28)
new_workout.grid(row=2, column=1, pady=5)
new_workout.current(0)
tk.Label(frame4, text="New Duration:", font=('Arial', 12)).grid(row=3, column=0, sticky='w', pady=5)
new_duration = tk.Entry(frame4, width=30, font=('Arial', 12))
new_duration.grid(row=3, column=1, pady=5)
tk.Label(frame4, text="New Calorie:", font=('Arial', 12)).grid(row=4, column=0, sticky='w', pady=5)
new_calorie = tk.Entry(frame4, width=30, font=('Arial', 12))
new_calorie.grid(row=4, column=1, pady=5)
def update_log():
    log_date = new_name.get()
    new_date_val = new_name.get()
    new_steps_val = new_steps.get()
    new_workout_val = new_workout.get()
    new_duration_val = new_duration.get()
    new_calorie_val = new_calorie.get()
    updated = False
    for child in tree.get_children():
        values = tree.item(child)["values"]
        if values[0] == log_date:
            tree.item(child, values=(new_date_val, new_steps_val, new_workout_val, new_duration_val, new_calorie_val))
            updated = True
            break
    if updated:
        print(f"Log for {log_date} updated successfully!")
    else:
        print(f"No log found for date: {log_date}")
update_button = tk.Button(frame4, text="Update", font=('Arial', 14), bg="#D9A299", fg="white", width=20, command=update_log)
update_button.grid(row= 7, column=0, columnspan=2, pady=20)


tab5 = tk.Frame(notebook)
notebook.add(tab5, text = "Delete a log")
frame5 = tk.Frame(tab5, padx = 20, pady = 20)
frame5. pack(pady = 50)
tk.Label(frame5, text="Enter Delete Date (YYYY-MM-DD):", font=('Arial', 12)).grid(row=0, column=0, sticky='w', pady=5)
delete_id = tk.Entry(frame5, width=30, font=('Arial', 12))
delete_id.grid(row=0, column=1, pady=5)
def delete_log():
    log_date = delete_id.get()
    deleted = False
    for child in tree.get_children():
        values = tree.item(child)["values"]
        if values[0] == log_date:
            tree.delete(child)
            deleted = True
            break
    if deleted:
        print(f"Log for {log_date} deleted successfully!")
    else:
        print(f"No log found for date: {log_date}")
delete_button = tk.Button(frame5, text="delete", font=('Arial', 14), bg="#D9A299", fg="white", width=20, command=delete_log)
delete_button.grid(row= 2, column=0, columnspan=2, pady=20)

tab6 = tk.Frame(notebook)
notebook.add(tab6, text = "Exit")
frame6 = tk.Frame(tab6, padx=20, pady=20)
frame6.pack(pady=100)
exit_button = tk.Button(tab6, text="Exit App", command=root.destroy, font=("Arial", 16), bg="red", fg="white")
exit_button.pack(pady=20)

