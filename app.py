import os
import numpy as np
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE' # a veces es muy pesado, se recomienda colocar

app = Flask(__name__)

# Ruta modelo previamente entrenado
modelo_path = " directorio con modelo.h5"
modelo = load_model(modelo_path)

# Directorio donde se guardarán las imágenes subidas
UPLOAD_FOLDER = "directorio uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No se ha seleccionado ningún archivo'})

    archivo = request.files['file']

    if archivo.filename == '':
        return jsonify({'error': 'No se ha seleccionado ningún archivo'})

    if archivo:
        # Guardar la imagen en el directorio 'uploads'
        imagen_path = os.path.join(app.config['UPLOAD_FOLDER'], archivo.filename)
        archivo.save(imagen_path)

        # Cargar y preprocesar la imagen
        img = image.load_img(imagen_path, target_size=(150, 150))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = img / 255.0  # Normalizar la imagen

        # Predicción
        prediction = modelo.predict(img)
        resultado = "Neumonía" if prediction > 0.5 else "Normal"

        # Eliminar la imagen subida después de la predicción, esto es recomendable
        os.remove(imagen_path)

        return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)

