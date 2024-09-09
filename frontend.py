import streamlit as st
from PIL import Image
from utils.model_trained import model_prediction
from utils.preprocessing import preprocess_image


st.title("Classifier de races de chiens")

upload = st.file_uploader("Chargez une image de chien",
                          type=['jpeg', 'jpg'])

c1, c2 = st.columns(2)

if upload:
    file = {"file" :  upload.getvalue()}
    image = Image.open(upload)

    processed_image = preprocess_image(image)

    breed_name = model_prediction(processed_image)

    # Affiche l'image
    c1.image(image)

    # Affiche l'output de l'API
    c2.write("Race du chien:")
    c2.write(breed_name)