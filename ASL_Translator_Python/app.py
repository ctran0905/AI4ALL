import streamlit as st
import cv2
from models import load_model
from utils import preprocess_image, predict_sign
from PIL import Image
import numpy as np

# Load model
model = load_model()

st.title("American Sign Language Recognition")

option = st.radio("Choose input method", ["Webcam", "Upload Image"])

if option == "Webcam":
    img_file_buffer = st.camera_input("Take a picture")
    if img_file_buffer is not None:
        image = Image.open(img_file_buffer)
        st.image(image, caption="Captured image")
        pred = predict_sign(model, image)
        st.success(f"Predicted sign: {pred}")

elif option == "Upload Image":
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded image")
        pred = predict_sign(model, image)
        st.success(f"Predicted sign: {pred}")
