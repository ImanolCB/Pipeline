import plotly.express as px
import pandas as pd

def create_graph(df):
    """
    Crea un gráfico de barras de usuarios por género.
    """
    df = df.drop(columns=['_id'])  # Eliminar la columna _id que no necesitamos
    df_users_by_gender = df['genero'].value_counts().reset_index()
    df_users_by_gender.columns = ['genero', 'cantidad_usuarios']
    
    print(f'\nCantidad de trabajadores por genero:\n {df_users_by_gender}')
    
    
    bar_chart = px.bar(
        df_users_by_gender, 
        x='genero', 
        y='cantidad_usuarios', 
        title='Usuarios por Género',
        labels={'genero': 'Género', 'cantidad_usuarios': 'Cantidad Usuario'},
        color='genero',  # Esto asigna colores diferentes a cada barra basándose en el género
        color_discrete_sequence=['#e9556b', '#55a4e9', '#cb89ec']  # Lista personalizada de colores
)
    # Aplicar las modificaciones al diseño del gráfico
    bar_chart.update_layout(
        xaxis_title="Género",                     # Título del eje X
        yaxis_title="Cantidad de Usuarios",       # Título del eje Y
        xaxis_tickangle=-45,                      # Rotar etiquetas del eje X
        bargap=0.6,                               # Ajustar el espacio entre barras (0.2 para hacerlas más estrechas)
        plot_bgcolor='rgba(30,30,30,0.1)',       # Color de fondo del área del gráfico
        paper_bgcolor='rgba(30,30,30,0.5)',      # Color de fondo de la página
        font=dict(size=14, color='white'),                        # Ajustar el tamaño de la fuente
)
    return bar_chart
