import streamlit as st
from models import load_model
from utils import predict_sign
from PIL import Image

# Load model
model = load_model()

st.title("American Sign Language Recognition")

option = st.radio("Choose input method", ["Webcam", "Upload Image"])

if option == "Webcam":
    col1, col2 = st.columns([3, 1])
    
    with col1:
        img_file_buffer = st.camera_input("Take a picture", key="camera")
    
    with col2:
        if st.button("Clear Camera"):
            # Clear all camera-related session state
            for key in list(st.session_state.keys()):
                if "camera" in key:
                    del st.session_state[key]
            st.rerun()
    
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
