import random
import csv
from faker import Faker
from datetime import datetime

# Crear una instancia de Faker
fake = Faker()
now = datetime.now()

# Lista de oficios posibles
oficios = ["Electricista", "Informatico", "Medico", "Profesor", "Estudiante", "Camarero"]

# Función para generar un registro aleatorio
def generar_dato(campo_vacio_probabilidad):
    nombre = fake.first_name() if random.random() > campo_vacio_probabilidad else None
    apellido1 = fake.last_name() if random.random() > campo_vacio_probabilidad else None
    apellido2 = fake.last_name() if random.random() > campo_vacio_probabilidad else None
    alias = fake.first_name()
    edad = random.randint(18, 80) if random.random() > campo_vacio_probabilidad else None
    email = fake.email()
    
    # Selección ponderada para el género (45% Masculino, 40% Femenino, 15% No binario)
    genero = random.choices(
        ["Masculino", "Femenino", "No binario"],
        weights=[45, 40, 15],  # Ponderación
        k=1
    )[0]
    
    oficio = random.choice(oficios)

    # Crear una fila con los datos generados
    return [nombre, apellido1, apellido2, alias, edad, email, genero, oficio]

# Definir el nombre del archivo CSV
csv_file = f'data/datos_aleatorios_{now.strftime("%S%M%H_%d%m%Y")}.csv'

# Calcular la probabilidad de que un campo esté vacío (10% como máximo)
campo_vacio_probabilidad = 0.1

# Abrir el archivo CSV para escribir
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Escribir la cabecera
    writer.writerow(["nombre", "apellido1", "apellido2", "alias", "edad", "email", "genero", "oficio"])

    # Generar y escribir 100 registros aleatorios
    for _ in range(20):
        writer.writerow(generar_dato(campo_vacio_probabilidad))

print(f"CSV generado correctamente en la ruta: {csv_file}")
