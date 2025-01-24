import sys
import os
import tkinter as tk
from tkinter import filedialog

# Agregar el directorio raíz al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.model import CSVModel
from views.view import CSVView

class CSVController:
    def __init__(self, root):
        self.model = CSVModel()
        self.view = CSVView(root)

        self.view.load_button.config(command=self.load_csv)
        self.view.analyze_button.config(command=self.analyze_data)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
        if file_path:
            try:
                self.model.load_csv(file_path)
                self.view.show_message("Éxito", "Archivo CSV cargado correctamente.")
                self.view.plot_data(self.model.data)
            except Exception as e:
                self.view.show_message("Error", f"No se pudo cargar el archivo CSV: {e}")

    def analyze_data(self):
        try:
            pattern = self.model.analyze_data(self.view.interval.get(), self.view.tolerance.get())
            self.view.show_message("Resultado", f"El patrón que más se asemeja es: {pattern}")
            self.view.plot_data(self.model.data)
        except ValueError as e:
            self.view.show_message("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVController(root)
    root.mainloop()