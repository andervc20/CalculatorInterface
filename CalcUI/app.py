import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt

def click_button(value):
    current = entry.get()
    if value == "=":
        try:
            result = str(eval(current))  
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    elif value == "DEL":
        current = current[:-1]  
        entry.delete(0, tk.END)
        entry.insert(tk.END, current)
    else:
        entry.insert(tk.END, value)
def graph():
    values = simpledialog.askstring("Ingresar valores", 
                                    "Ingresa los valores de X y Y separados por coma (X1,Y1):")
    if not values:
        messagebox.showerror("Error", "Por favor, ingresa valores válidos.")
        return
    try:
        values = list(map(float, values.split(",")))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa solo números válidos.")
        return
    if len(values) % 2 != 0:
        messagebox.showerror("Error", "Debes ingresar un número par de valores, uno para X y otro para Y.")
        return

    x_values = values[::2]
    y_values = values[1::2]

    plt.plot(x_values, y_values, marker="o", color="b", label="Datos")
    plt.title("Gráfico de los valores ingresados")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.show()
    create_table(x_values, y_values)

def create_table(x_values, y_values):
    table_window = tk.Toplevel(root)
    table_window.title("Valores Ingresados")
    table_window.geometry("300x300")
    table = ttk.Treeview(table_window, columns=("X", "Y"), show="headings")
    table.heading("X", text="X")
    table.heading("Y", text="Y")
    for x, y in zip(x_values, y_values):
        table.insert("", tk.END, values=(x, y))
    table.pack(fill=tk.BOTH, expand=True)

root = tk.Tk()
root.title("Calculadora")
root.geometry("400x600")  
root.resizable(False, False)  

# centrar la ventana en la pantalla
window_width = 400
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
root.config(bg="#1b1b1b")  

# Estilo de la calculadora
style = ttk.Style()
style.configure("TButton", font=("Arial", 16, "bold"), padding=10, width=5, relief="raised", background="#4a4a4a", foreground="red")
style.map("TButton", background=[("active", "#5a5a5a")])   
entry = tk.Entry(root, font=("Arial", 24), bd=10, relief="sunken", justify="right", bg="#333333", fg="white")
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10, sticky="nsew")

# botones de la calculadora
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("DEL", 5, 1),
    ("Graficar", 5, 2),  
]

for (text, row, col) in buttons:
    button = ttk.Button(root, text=text, command=lambda value=text: click_button(value) if value != "Graficar" else graph())
    button.grid(row=row, column=col, padx=10, pady=10, ipadx=10, ipady=10, sticky="nsew")

# tamaño de la ventana
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()



