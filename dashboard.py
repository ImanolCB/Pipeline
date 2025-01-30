import dash
from dash import dcc, html
from pymongo import MongoClient
import pandas as pd

# Importar los gráficos modulares
from graphics.graphic_avg_age_by_job import create_graph as create_graph_avg_age
from graphics.graphic_users_by_job import create_graph as create_graph_users_by_job
from graphics.graphic_users_by_gender import create_graph as create_graph_users_by_gender

# pip install pymongo dash plotly pandas

# Conectar a MongoDB Atlas
client = MongoClient("mongodb+srv://iabd08:iabdiabd08@cluster0.tjxm7.mongodb.net")
db = client['KPI_users_oficios']
all_users = db['all_users']


# Obtener los datos de la colección y convertirlos en un DataFrame
cursor_all_users = all_users.find()


df_all_users = pd.DataFrame(list(cursor_all_users))


# Crear los gráficos con las funciones importadas
bar_chart_avg = create_graph_avg_age(df_all_users)
bar_chart_by_job = create_graph_users_by_job(df_all_users)
bar_chart_by_gender = create_graph_users_by_gender(df_all_users)

# Iniciar la aplicación Dash
app = dash.Dash(__name__)

# Configuración del layout del dashboard
app.layout = html.Div([
    html.H1("Dashboard de KPIs", style={'textAlign': 'center'}),

    html.Div([
        # html.H3("Promedio de Edad por Oficio"),
        dcc.Graph(
            id='bar_chart_avg',
            figure=bar_chart_avg
        ),
    ], style={'width': '80%', 'margin': '10rem auto'}),  # Asegura que el gráfico esté centrado
    
    html.Div([
        # html.H3("Usuarios por Oficio"),
        dcc.Graph(
            id='bar_chart_by_job',
            figure=bar_chart_by_job
        ),
    ], style={'width': '80%', 'margin': '10rem auto'}),  # Asegura que el gráfico esté centrado
    
    html.Div([
        # html.H3("Usuarios por Genero"),
        dcc.Graph(
            id='bar_chart_by_gender',
            figure=bar_chart_by_gender
        ),
    ], style={'width': '80%', 'margin': '10rem auto'}),  # Asegura que el gráfico esté centrado
])

# Correr la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
