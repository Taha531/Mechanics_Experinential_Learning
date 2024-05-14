import tkinter as tk
import math
from tkinter import messagebox
from PIL import Image, ImageTk

def calculate_resultant():
    angle1_str = angle1_entry.get()
    angle2_str = angle2_entry.get()
    force1_str = force1_entry.get()
    force2_str = force2_entry.get()

    if not angle1_str or not angle2_str or not force1_str or not force2_str:
        messagebox.showerror("Error", "Please enter values for all fields.")
        return

    try:
        angle1 = float(angle1_str)
        angle2 = float(angle2_str)
        force1 = float(force1_str)
        force2 = float(force2_str)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
        return

    x_component = force1 * math.cos(math.radians(angle1)) + force2 * math.cos(math.radians(angle2))
    y_component = force1 * math.sin(math.radians(angle1)) + force2 * math.sin(math.radians(angle2))

    resultant_magnitude = math.sqrt(x_component**2 + y_component**2)
    resultant_angle = math.degrees(math.atan2(y_component, x_component))

    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "The x component of resultant = {:.2f}\n".format(x_component))
    result_text.insert(tk.END, "The y component of resultant = {:.2f}\n".format(y_component))
    result_text.insert(tk.END, "The resultant = {:.2f}\n".format(resultant_magnitude))
    result_text.insert(tk.END, "Angle made by resultant = {:.2f}\n".format(resultant_angle))
    result_text.config(state=tk.DISABLED)

def create_gui():
    global angle1_entry, angle2_entry, force1_entry, force2_entry
    global result_text
    root = tk.Tk()
    root.title("Force Calculator")
    root.geometry("1366x768")
    root.resizable(True, True)

    # Load the image and resize it
    image = Image.open("question_image.jpg")
    image = image.resize((450, 350))
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)
    image_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

    angle1_label = tk.Label(root, text="Angle 1:")
    angle1_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)
    angle1_entry = tk.Entry(root, width=15)
    angle1_entry.grid(row=1, column=1, padx=10, pady=10)

    angle2_label = tk.Label(root, text="Angle 2:")
    angle2_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)
    angle2_entry = tk.Entry(root, width=15)
    angle2_entry.grid(row=2, column=1, padx=10, pady=10)

    force1_label = tk.Label(root, text="Force 1:")
    force1_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)
    force1_entry = tk.Entry(root, width=15)
    force1_entry.grid(row=3, column=1, padx=10, pady=10)

    force2_label = tk.Label(root, text="Force 2:")
    force2_label.grid(row=4, column=0, sticky="e", padx=10, pady=10)
    force2_entry = tk.Entry(root, width=15)
    force2_entry.grid(row=4, column=1, padx=10, pady=10)

    submit_button = tk.Button(root, text="Calculate", command=calculate_resultant, width=10)
    submit_button.grid(row=5, column=0, pady=10, padx=10, sticky="nsew")

    exit_button = tk.Button(root, text="Close", command=lambda: close_application(root), width=10)
    exit_button.grid(row=5, column=1, pady=10, padx=10, sticky="nsew")

    result_text = tk.Text(root, height=10, width=50, state=tk.DISABLED, bg="lightgray", fg="blue", font=("Helvetica", 12))
    result_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    result_text.insert(tk.END, "The x component of resultant = 0.00\n")
    result_text.insert(tk.END, "The y component of resultant = 0.00\n")
    result_text.insert(tk.END, "The resultant = 0.00\n")
    result_text.insert(tk.END, "Angle made by resultant = 0.00\n")

    # Center-align all elements
    for row in range(7):
        root.grid_rowconfigure(row, weight=1)
    for col in range(2):
        root.grid_columnconfigure(col, weight=1)

    root.mainloop()

def close_application(root):
    if messagebox.askquestion("Close", "Are you sure you want to close the application?") == "yes":
        root.destroy()

create_gui()