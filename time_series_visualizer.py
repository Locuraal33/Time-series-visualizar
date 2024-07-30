import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 1. Importar los datos y establecer el índice en la columna de fecha
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
print("Datos importados:")
print(df.head())

# 2. Calcular los límites del 2.5% superior e inferior y filtrar
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)

filtered_df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]

print("\nDatos después de la limpieza:")
print(filtered_df.head())

# 3. Crear la función para el gráfico de líneas
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

    # Guardar la imagen y devolver la figura
    fig.savefig('line_plot.png')
    return fig

# 4. Crear el gráfico de barras
def draw_bar_plot(df):
    # Crear un DataFrame con el promedio de vistas diarias para cada mes
    df['year'] = df.index.year
    df['month'] = df.index.month
    df_grouped = df.groupby(['year', 'month'])['value'].mean().unstack()

    # Dibujar el gráfico de barras
    fig, ax = plt.subplots(figsize=(12, 6))
    df_grouped.plot(kind='bar', ax=ax)

    # Establecer el título y las etiquetas
    ax.set_title('Average Daily Page Views per Month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=[
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ])

    # Mostrar el gráfico
    plt.show()

    # Guardar la imagen y devolver la figura
    fig.savefig('bar_plot.png')
    return fig

# 5. Dibujar gráficos de caja
def draw_box_plot(df):
    # Preparar los datos
    df['year'] = df.index.year
    df['month'] = df.index.month
    df['month_name'] = df.index.strftime('%b')  # Obtener el nombre abreviado del mes
    df['month'] = pd.Categorical(df['month_name'], categories=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ordered=True)

    # Dibujar los gráficos de caja
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 7))

    # Gráfico de caja por año
    sns.boxplot(x='year', y='value', data=df, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Gráfico de caja por mes
    sns.boxplot(x='month', y='value', data=df, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Ajustar el diseño y mostrar el gráfico
    plt.tight_layout()
    plt.show()

    # Guardar la imagen y devolver la figura
    fig.savefig('box_plot.png')
    return fig

# Llamar a las funciones para generar los gráficos
def main():
    draw_line_plot(filtered_df)
    draw_bar_plot(filtered_df)
    draw_box_plot(filtered_df)

if __name__ == "__main__":
    main()