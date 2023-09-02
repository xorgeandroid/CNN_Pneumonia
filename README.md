# CNN_Pneumonia
CNN 
# Proyecto de Detección de Neumonía con Red Neuronal Convolucional (CNN)

Este proyecto implementa una Red Neuronal Convolucional (CNN) para la detección de neumonía en imágenes médicas de radiografías de tórax. La CNN se entrena en un conjunto de datos de radiografías etiquetadas y se utiliza para realizar predicciones de diagnóstico de neumonía en imágenes de pacientes.

## Requisitos

Asegúrate de tener instalado lo siguiente en tu entorno de desarrollo:

- Python 3.x
- Bibliotecas Python (como TensorFlow, NumPy, Flask, etc.) instaladas. Puedes instalarlas usando `pip`.

## Configuración

1. Clona este repositorio en tu sistema local:

```bash
git clone https://github.com/xorgeandroid/CNN_Pneumonia

## Uso
Asegúrate de tener el modelo de CNN previamente entrenado en formato .h5 en la ruta correcta. Puedes entrenar tu propio modelo o utilizar uno existente.

Ejecuta la aplicación Flask para cargar imágenes y realizar predicciones:

bash
Copy code
python app.py
Abre un navegador web y navega a http://localhost:5000 para interactuar con la aplicación web.
Estructura del Proyecto
app.py: El script principal que define la aplicación web Flask para cargar imágenes y realizar predicciones de neumonía.
templates/index.html: El archivo HTML que muestra el formulario para cargar imágenes.
No Olvides agregar en la misma ruta tu "index.html"
