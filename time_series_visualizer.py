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