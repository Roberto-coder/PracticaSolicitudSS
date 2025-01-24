import pandas as pd

class CSVModel:
    def __init__(self):
        self.data = None

    def load_csv(self, file_path):
        # Cargar el archivo CSV y parsear la columna 'Fecha' como tipo datetime
        self.data = pd.read_csv(file_path, parse_dates=['Fecha'])

    def analyze_data(self, interval, tolerance):
        if self.data is None:
            raise ValueError("No data loaded")

        # Resample the data based on the selected interval
        self.data = self.data.set_index('Fecha').resample(f'{interval}min').mean().reset_index()

        # Obtener el primer y último valor de la columna 'Valor'
        first_value = self.data['Valor'].iloc[0]
        last_value = self.data['Valor'].iloc[-1]
        # Calcular el valor del margen de tolerancia
        tolerance_value = (tolerance / 100) * first_value

        # Comparar los valores del primer y último registro según las condiciones para determinar el patrón
        if first_value > last_value and (first_value - last_value) > tolerance_value:
            return "Patrón A"  # El primer valor está por encima del último y la diferencia es mayor al margen de tolerancia
        elif abs(first_value - last_value) <= tolerance_value:
            return "Patrón B"  # El primer valor está aproximadamente igual al último dentro del margen de tolerancia
        elif first_value < last_value and (last_value - first_value) > tolerance_value:
            return "Patrón C"  # El primer valor está por debajo del último y la diferencia es mayor al margen de tolerancia
        else:
            return "No se encontró un patrón claro"  # Si no se cumple ninguna de las condiciones anteriores