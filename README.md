# Proyecto ETL con Python, Azure, Databricks, MongoDB y Dash

Este proyecto implementa un proceso ETL (Extract, Transform, Load) utilizando diversas tecnologías modernas para manejar, procesar y visualizar datos. Los datos extraídos se almacenan en **MongoDB**, se procesan mediante **Databricks** en la nube de **Azure**, y se visualizan en una interfaz interactiva utilizando **Dash**.

## Tecnologías utilizadas

- **Python**: Lenguaje principal para la implementación del proceso ETL.
- **Azure**: Plataforma en la nube utilizada para gestionar los recursos y ejecutar los procesos de Databricks.
- **Databricks**: Entorno de trabajo basado en Apache Spark utilizado para el procesamiento de grandes volúmenes de datos.
- **MongoDB**: Base de datos NoSQL utilizada para almacenar los datos extraídos.
- **Dash**: Framework para crear aplicaciones web interactivas y visualizaciones de datos en tiempo real.

## Descripción

Este proyecto tiene como objetivo integrar múltiples tecnologías para realizar un flujo ETL completo:

1. **Extracción (Extract)**: Los datos se extraen desde diversas fuentes y se almacenan en MongoDB.
2. **Transformación (Transform)**: Usando Databricks, se procesan los datos extraídos para limpiarlos, transformarlos y estructurarlos de acuerdo con los requisitos.
3. **Carga (Load)**: Los datos transformados se cargan nuevamente en MongoDB.
4. **Visualización**: Se utiliza Dash para crear una aplicación web que permita filtrar y visualizar los datos almacenados en MongoDB mediante gráficos interactivos.

## Requisitos

Antes de ejecutar este proyecto, asegúrate de tener los siguientes requisitos instalados:

- **Python** 3.7+
- **Azure** SDK para Python
- **Databricks** CLI configurado
- **MongoDB** (local o en la nube)
- **Dash** y **Plotly** para visualización de datos

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
