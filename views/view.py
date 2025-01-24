import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class CSVView:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador de CSV")
        self.root.geometry("1300x800")

        # Variables
        self.interval = tk.IntVar(value=5)
        self.tolerance = tk.DoubleVar(value=5.0)

        # Crear los elementos de la interfaz
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Selecciona un archivo CSV:").pack(pady=5)
        self.load_button = ttk.Button(self.root, text="Cargar CSV")
        self.load_button.pack(pady=5)

        ttk.Label(self.root, text="Intervalo de datos (min):").pack(pady=5)
        ttk.OptionMenu(self.root, self.interval, 5, 5, 10, 15, 30).pack(pady=5)

        ttk.Label(self.root, text="Margen de tolerancia (%):").pack(pady=5)
        ttk.Entry(self.root, textvariable=self.tolerance).pack(pady=5)

        self.analyze_button = ttk.Button(self.root, text="Analizar datos")
        self.analyze_button.pack(pady=10)

        self.graph_frame = ttk.Frame(self.root)
        self.graph_frame.pack(fill=tk.BOTH, expand=True)

    def show_message(self, title, message):
        # Mostrar un mensaje en una ventana emergente
        messagebox.showinfo(title, message)

    def plot_data(self, data):
        # Limpiar la gráfica anterior (si existe)
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        # Crear una nueva figura y ejes para la gráfica
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(data['Fecha'], data['Valor'], color='red', label="Datos")
        ax.scatter(data['Fecha'].iloc[0], data['Valor'].iloc[0], color='yellow', label="Inicio")
        ax.scatter(data['Fecha'].iloc[-1], data['Valor'].iloc[-1], color='green', label="Fin")
        ax.set_title("Gráfica de datos")
        ax.set_xlabel("Fecha")
        ax.set_ylabel("Valor")
        ax.legend()

        # Dibujar la gráfica en la interfaz de Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Cerrar la figura para liberar memoria
        plt.close(fig)