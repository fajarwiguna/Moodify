import streamlit as st
from utils import detect_emotion
import cv2
import numpy as np

def main():
    """Main function to run the Moodify Streamlit app."""
    st.title("🎧 Moodify: AI Mood-to-Music Recommender")
    st.write("Upload a photo or use your webcam to detect your mood and get music recommendations!")

    # Option to upload image or use webcam
    option = st.radio("Choose input method:", ("Upload Photo", "Use Webcam"))

    if option == "Upload Photo":
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            # Read image
            image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Detect emotion
            with st.spinner("Detecting mood..."):
                emotion, confidence = detect_emotion(image)
                st.write(f"Detected Mood: **{emotion}** (Confidence: {confidence:.2f})")

    elif option == "Use Webcam":
        picture = st.camera_input("Take a selfie")
        if picture is not None:
            # Read webcam image
            image = cv2.imdecode(np.frombuffer(picture.getvalue(), np.uint8), 1)
            st.image(image, caption="Webcam Capture", use_column_width=True)

            # Detect emotion
            with st.spinner("Detecting mood..."):
                emotion, confidence = detect_emotion(image)
                st.write(f"Detected Mood: **{emotion}** (Confidence: {confidence:.2f})")

if __name__ == "__main__":
    main()