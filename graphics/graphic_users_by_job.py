import plotly.express as px
import pandas as pd

def create_graph(df):
    """
    Crea un gráfico de barras de usuarios por oficio.
    """
    df = df.drop(columns=['_id'])  # Eliminar la columna _id que no necesitamos
    df_users_by_job = df['oficio'].value_counts().reset_index()
    df_users_by_job.columns = ['oficio', 'cantidad_usuarios']
    df_users_by_job = df_users_by_job.sort_values(by='cantidad_usuarios', ascending=False)  # Orden por edad promedio descendente
    
    print(f'\nNumero de Trabajadores por Oficio:\n {df_users_by_job}')
    
    bar_chart = px.bar(
        df_users_by_job,
        x='oficio',
        y='cantidad_usuarios', 
        title='Usuarios por Oficio',
        labels={'oficio': 'Oficio', 'cantidad_usuarios': 'Cantidad Usuario'},
        color='oficio',  # Esto asigna colores diferentes a cada barra basándose en el género
        color_discrete_sequence=['#005b99', '#0977c2', '#1b87d1', '#61ade2','#87c4ee', '#c0def3']  # Lista personalizada de colores)
    )
    
        # Aplicar las modificaciones al diseño del gráfico
    bar_chart.update_layout(
        xaxis_title="Oficios",                     # Título del eje X
        yaxis_title="Cantidad de Usuarios",       # Título del eje Y
        xaxis_tickangle=-45,                      # Rotar etiquetas del eje X
        bargap=0.6,                               # Ajustar el espacio entre barras (0.2 para hacerlas más estrechas)
        plot_bgcolor='rgba(30,30,30,0.1)',       # Color de fondo del área del gráfico
        paper_bgcolor='rgba(30,30,30,0.5)',      # Color de fondo de la página
        font=dict(size=14, color='white')                        # Ajustar el tamaño de la fuente
)
    return bar_chart
