import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# 1.Importar los datos y establecer el índice en la columna de fecha
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
print("Datos importados:")
print(df.head())

# 2.Calcular los límites del 2.5% superior e inferior y filtrar
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)

filtered_df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]

print("\nDatos después de la limpieza:")
print(filtered_df.head())

# 3.Crear la funcion para el grafico de lineas
def draw_line_plot(df):
    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Dibujar el gráfico de líneas
    ax.plot(df.index, df['value'], color='green', linewidth=1)

    # Establecer el título y las etiquetas
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Mostrar el gráfico
    plt.show()

# Suponiendo que filtered_df es el DataFrame filtrado después de limpiar los datos
draw_line_plot(filtered_df)