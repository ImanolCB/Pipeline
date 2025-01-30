from azure.storage.blob import BlobServiceClient
import os
import re

# Expresión regular para coincidir con el patrón
pattern = r'.*\.csv$'

# Ruta donde está almacenados los datos
data_directory = 'data/'

# Obtener una lista de archivos en el directorio actual
# Verifica si el directorio existe
if not os.path.exists(data_directory):
    print(f"El directorio '{data_directory}' no existe.")
else:
    # Obtener una lista de archivos en el directorio data/
    files = os.listdir(data_directory)

# Filtrar archivos que coincidan con la expresión regular
matching_files = [file for file in files if re.match(pattern, file)]

# Imprimir archivos coincidentes
print("Archivos coincidentes:", matching_files)

# Configuración de Azure Blob Storage
connection_string = "DefaultEndpointsProtocol=https;AccountName=iabd08almacenamiento1;AccountKey=VmLA58rv52lAyWN9HZZ88uB5z5dfk5LyZX6NF6xgcQ2usQunW74ANqxn9kkL+OT9Y+ez1D3fLV+b+ASt3LVPmg==;EndpointSuffix=core.windows.net"
# connection_string = "DefaultEndpointsProtocol=https;AccountName=iabd08almacenamiento1;AccountKey=VmLA58rv52lAyWN9HZZ88uB5z5dfk5LyZX6NF6xgcQ2usQunW74ANqxn9kkL+OT9Y+ez1D3fLV+b+ASt3LVPmg==;EndpointSuffix=dataonstream@iabd08almacenamiento1"
# connection_string = "wasbs://dataonstream@iabd08almacenamiento1.blob.core.windows.net/archivoscsv/"  # Reemplázalo con tu cadena de conexión
container_name = "dataonstream/archivoscsv"           # Nombre del contenedor en Azure

for file in matching_files:
    blob_name = file    # Nombre que tendrá el archivo en Azure
# Archivo CSV local que deseas subir
    local_csv_file = data_directory + file  # Cambia esto por el nombre de tu archivo local
    print(type(file), " -> ", file)
    # Comprobar si el archivo existe en el directorio actual
    if not os.path.exists(local_csv_file):
        print(f"El archivo '{local_csv_file}' no se encuentra en el path actual.")
    else:
        try:
            # Crear cliente para interactuar con Blob Storage
            blob_service_client = BlobServiceClient.from_connection_string(connection_string)
            container_client = blob_service_client.get_container_client(container_name)

            # Subir el archivo al contenedor
            with open(local_csv_file, "rb") as data_file:
                blob_client = container_client.get_blob_client(blob_name)
                blob_client.upload_blob(data_file, overwrite=True)  # Sobrescribe si ya existe
                print(f"Archivo '{local_csv_file}' subido como '{blob_name}' en el contenedor '{container_name}'.")

        except Exception as e:
            print(f"Error al subir el archivo: {e}")
