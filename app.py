import streamlit as st
import tensorflow as tf
import numpy as np


# Load trained model
model = tf.keras.models.load_model("plant_disease_model.keras")


# Class names
class_names = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___healthy",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___healthy",
    "Potato___Late_blight",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_healthy",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_mosaic_virus",
    "Tomato__Tomato_YellowLeaf__Curl_Virus"
]


# App title
st.title("🌱 Plant Disease Detection")


# Image uploader
uploaded_file = st.file_uploader(
    "Upload a plant leaf image",
    type=["jpg", "jpeg", "JPG", "JPEG", "png", "PNG"]
)


# Display uploaded image
if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Uploaded Image"
    )


# Prediction button
if st.button("Predict Disease"):

    image = tf.keras.utils.load_img(
        uploaded_file,
        target_size=(128, 128)
    )

    image_array = tf.keras.utils.img_to_array(image)

    image_array = image_array / 255.0

    image_array = tf.expand_dims(image_array, 0)

    predictions = model.predict(image_array)

    predicted_class = np.argmax(predictions[0])

    confidence = predictions[0][predicted_class] * 100

    predicted_disease = class_names[predicted_class]

    st.success(
        f"Predicted Disease: {predicted_disease}"
    )

    st.info(
        f"Confidence: {confidence:.2f}%"
    )