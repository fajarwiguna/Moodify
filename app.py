import streamlit as st
from utils import detect_emotion, get_spotify_playlist
import cv2
import numpy as np
import time

def main():
    """Main function to run the Moodify Streamlit app."""
    st.title("🎧 Moodify: AI Mood-to-Music Recommender")
    st.write("Upload a photo or use your webcam to detect your mood and get Spotify playlist recommendations!")

    # Language selection
    language = st.selectbox("Select playlist language:", ["English", "Indonesia", "Korea", "Japan", "Mandarin"])

    # Option to upload image or use webcam
    option = st.radio("Choose input method:", ("Upload Photo", "Use Webcam"))

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

                    # Show all emotion scores
                    if emotion_scores:
                        st.write("All Emotion Scores:")
                        for emo, score in emotion_scores.items():
                            st.write(f"{emo.capitalize()}: {score:.2f}%")
                    else:
                        st.error("Failed to retrieve emotion scores. Please try a clearer photo.")
                except Exception as e:
                    st.error(f"Failed to detect mood: {str(e)}. Please try a clearer photo with good lighting.")
                    emotion, confidence, emotion_scores = "neutral", 0.0, {}

            # Retry detection button
            if st.button("Retry Mood Detection"):
                st.rerun()

            # Get Spotify playlists
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
                    # Refresh playlist button
                    if st.button("Get Different Playlists"):
                        get_spotify_playlist.cache_clear()  # Clear cache
                        st.rerun()
                except Exception as e:
                    st.error(f"Failed to fetch playlists: {str(e)}. Using default playlist.")
                    st.markdown(f"🎵 [Default Chill Playlist](https://open.spotify.com/playlist/37i9dQZF1DX0UrRvztWcAU)")

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

                    # Show all emotion scores
                    if emotion_scores:
                        st.write("All Emotion Scores:")
                        for emo, score in emotion_scores.items():
                            st.write(f"{emo.capitalize()}: {score:.2f}%")
                    else:
                        st.error("Failed to retrieve emotion scores. Please try a clearer selfie.")
                except Exception as e:
                    st.error(f"Failed to detect mood: {str(e)}. Please try a clearer selfie with good lighting.")
                    emotion, confidence, emotion_scores = "neutral", 0.0, {}

            # Retry detection button
            if st.button("Retry Mood Detection"):
                st.rerun()

            # Get Spotify playlists
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
                    # Refresh playlist button
                    if st.button("Get Different Playlists"):
                        get_spotify_playlist.cache_clear()  # Clear cache
                        st.rerun()
                except Exception as e:
                    st.error(f"Failed to fetch playlists: {str(e)}. Using default playlist.")
                    st.markdown(f"🎵 [Default Chill Playlist](https://open.spotify.com/playlist/37i9dQZF1DX0UrRvztWcAU)")

if __name__ == "__main__":
    main()