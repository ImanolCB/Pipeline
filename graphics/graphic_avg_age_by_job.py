import plotly.express as px
import pandas as pd

def create_graph(df):
    """
    Crea un gráfico de barras de promedio de edad por oficio.
    """
    # Asegúrate de que el DataFrame tenga las columnas correctas
    df = df.drop(columns=['_id'])  # Eliminar la columna _id que no necesitamos
    df_avg_age_by_job = df.groupby('oficio')['edad'].mean().reset_index()
    df_avg_age_by_job = df_avg_age_by_job.sort_values(by='edad', ascending=False)  # Orden por edad promedio descendente
    
    print(f'\nEdad media por Oficio:\n {df_avg_age_by_job}')
    
    bar_chart = px.bar(
        df_avg_age_by_job,
        x='oficio',
        y='edad', 
        title='Promedio de Edad por Oficio',
        labels={'oficio': 'Oficio', 'edad': 'Edad'},
        color='oficio',  # Esto asigna colores diferentes a cada barra basándose en el género
        color_discrete_sequence=['#a20000', '#ce1414', '#f14b4b', '#ed7474','#f29898', '#f7c2c2']  # Lista personalizada de colores)
    )
    
        # Aplicar las modificaciones al diseño del gráfico
    bar_chart.update_layout(
        xaxis_title="Oficios",                    # Título del eje X
        yaxis_title="Edad Promedio",                 # Título del eje Y
        xaxis_tickangle=-45,                      # Rotar etiquetas del eje X
        bargap=0.6,                               # Ajustar el espacio entre barras (0.2 para hacerlas más estrechas)
        plot_bgcolor='rgba(30,30,30,0.1)',          # Color de fondo del área del gráfico
        paper_bgcolor='rgba(30,30,30,0.5)',      # Color de fondo de la página
        font=dict(size=14, color='white'),                        # Ajustar el tamaño de la fuente
)
    return bar_chart
