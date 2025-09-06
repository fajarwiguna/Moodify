import streamlit as st
from utils import detect_emotion, get_spotify_playlist
import cv2
import numpy as np
import time


st.set_page_config(
    page_title="Moodify",       
    page_icon="🎧",             
    layout="centered",           
    initial_sidebar_state="auto" 
)

def main():
    """Main function to run the Moodify Streamlit app."""
    # Load custom CSS
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.title("🎧 Moodify: AI Mood-to-Music Recommender")
    st.write("Upload a photo, use your webcam, or pick your mood manually to get Spotify playlist recommendations!")

    # Language selection
    language = st.selectbox("Select playlist language:", ["English", "Indonesia", "Korea", "Japan", "Mandarin"])

    # Option to upload image, webcam, or manual input
    option = st.radio("Choose input method:", ("Upload Photo", "Use Webcam", "Manual Input"))

    emotion = None
    confidence = 0.0
    emotion_scores = {}

    if option == "Upload Photo":
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            # Read image
            image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Detect emotion
            start_time = time.time()
            with st.spinner("Analyzing your mood..."):
                try:
                    emotion, confidence, emotion_scores = detect_emotion(image)
                    elapsed_time = time.time() - start_time
                    st.write(f"Detected Mood: **{emotion.capitalize()}** (Confidence: {confidence:.2f})")
                    st.write(f"Analysis took {elapsed_time:.2f} seconds")

                    # Warn if confidence is low
                    if confidence < 0.5:
                        st.warning("Low confidence in mood detection. Try a clearer photo or override manually.")

                    # Show all emotion scores
                    if emotion_scores:
                        st.markdown("<div class='emotion-scores'>All Emotion Scores:</div>", unsafe_allow_html=True)
                        for emo, score in emotion_scores.items():
                            st.write(f"{emo.capitalize()}: {score:.2f}%")
                    else:
                        st.error("Failed to retrieve emotion scores. Please try a clearer photo.")
                except Exception as e:
                    st.error(f"Failed to detect mood: {str(e)}. Defaulting to Neutral.")
                    emotion, confidence, emotion_scores = "neutral", 0.0, {}

            if st.button("Retry Mood Detection"):
                st.rerun()

    elif option == "Use Webcam":
        picture = st.camera_input("Take a selfie")
        if picture is not None:
            # Read webcam image
            image = cv2.imdecode(np.frombuffer(picture.getvalue(), np.uint8), 1)
            st.image(image, caption="Webcam Capture", use_column_width=True)

            # Detect emotion
            start_time = time.time()
            with st.spinner("Analyzing your mood..."):
                try:
                    emotion, confidence, emotion_scores = detect_emotion(image)
                    elapsed_time = time.time() - start_time
                    st.write(f"Detected Mood: **{emotion.capitalize()}** (Confidence: {confidence:.2f})")
                    st.write(f"Analysis took {elapsed_time:.2f} seconds")

                    # Warn if confidence is low
                    if confidence < 0.5:
                        st.warning("Low confidence in mood detection. Try a clearer selfie or override manually.")

                    # Show all emotion scores
                    if emotion_scores:
                        st.markdown("<div class='emotion-scores'>All Emotion Scores:</div>", unsafe_allow_html=True)
                        for emo, score in emotion_scores.items():
                            st.write(f"{emo.capitalize()}: {score:.2f}%")
                    else:
                        st.error("Failed to retrieve emotion scores. Please try a clearer selfie.")
                except Exception as e:
                    st.error(f"Failed to detect mood: {str(e)}. Defaulting to Neutral.")
                    emotion, confidence, emotion_scores = "neutral", 0.0, {}

            if st.button("Retry Mood Detection"):
                st.rerun()

    elif option == "Manual Input":
        manual_mood = st.selectbox(
            "Select your mood:",
            ["None", "Happy", "Sad", "Angry", "Surprised", "Neutral", "Fear", "Disgust"]
        )
        if manual_mood != "None":
            emotion = manual_mood.lower()
            st.success(f"You selected: {manual_mood}")

    if emotion is not None:
        if option != "Manual Input":
            st.markdown("---")
            st.subheader("😎 Not accurate? Override manually:")
            manual_override = st.selectbox(
                "Adjust your mood if needed:",
                ["None", "Happy", "Sad", "Angry", "Surprised", "Neutral", "Fear", "Disgust"]
            )
            if manual_override != "None":
                emotion = manual_override.lower()
                st.info(f"Manual override applied: **{manual_override}**")

        # --- Spotify playlist recommendation ---
        with st.spinner("Fetching your playlists..."):
            try:
                playlists = get_spotify_playlist(emotion, language)
                if playlists and playlists[0][0] != "Default Chill Playlist":
                    st.success("Recommended Playlists:")
                    for i, (name, url) in enumerate(playlists, 1):
                        st.markdown(f"{i}. [{name}]({url})")
                else:
                    st.warning("No playlists found for your mood and language. Showing default playlist.")
                    st.markdown(f"🎵 [Default Chill Playlist](https://open.spotify.com/playlist/37i9dQZF1DX0UrRvztWcAU)")
                if st.button("Get Different Playlists"):
                    get_spotify_playlist.cache_clear()
                    st.rerun()
            except Exception as e:
                st.error(f"Failed to fetch playlists: {str(e)}. Using default playlist.")
                st.markdown(f"🎵 [Default Chill Playlist](https://open.spotify.com/playlist/37i9dQZF1DX0UrRvztWcAU)")

if __name__ == "__main__":
    main()