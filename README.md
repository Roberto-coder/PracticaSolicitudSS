# PracticaSolicitudSS

## Descripción

CSV Analyzer es una aplicación desarrollada en Python que permite cargar un archivo CSV con datos de fechas y valores, y luego analizar los datos para identificar patrones. La aplicación utiliza una interfaz gráfica creada con **Tkinter**, y grafica los datos con **Matplotlib**. Los patrones se determinan en base a las siguientes condiciones:

- **Patrón A**: El primer valor es mayor que el último, y la diferencia entre ambos supera el margen de tolerancia.
- **Patrón B**: El primer valor es aproximadamente igual al último, dentro del margen de tolerancia.
- **Patrón C**: El primer valor es menor que el último, y la diferencia entre ambos supera el margen de tolerancia.

## Requisitos

- Python 3.x
- **Tkinter**: Para la interfaz gráfica.
- **Pandas**: Para leer y manipular los datos del CSV.
- **Matplotlib**: Para graficar los datos.

Puedes instalar las librerías necesarias ejecutando:
pip install pandas matplotlib

## Uso

1. Ejecutar la aplicación: 
Inicia la aplicación ejecutando el archivo controller.oy dentro del carpeta PracticaSolicitudSS\controllers> .
python controller.py

2. Cargar el archivo CSV:
Haz clic en el botón "Cargar CSV" y selecciona el archivo CSV que deseas analizar, puedos usar alguno de los que se encuentran en la carpeta de pruebas.
El archivo debe contener dos columnas: Fecha (formato YYYY-MM-DD HH:MM:SS) y Valor (numérico).

3. Configurar parámetros:
Intervalo de datos: Elige el intervalo en minutos (5, 10, 15 o 30).
Margen de tolerancia: Ingresa un margen de tolerancia en porcentaje (por ejemplo, 5% para una diferencia máxima permitida entre los valores).

4. Analizar los datos:
Haz clic en "Analizar datos" para que la aplicación procese los datos y determine qué patrón se ajusta a los valores cargados.
La aplicación mostrará el patrón encontrado y actualizará la gráfica con los datos analizados.

5. Ver la gráfica:
La aplicación graficará los datos, destacando el primer y último valor con colores amarillo y verde, respectivamente.

## Prueba de Fucionalidad

![image](https://github.com/user-attachments/assets/ab1c3bb7-221d-4824-a45c-be61d001ec24)
