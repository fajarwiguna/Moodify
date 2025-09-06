# Moodify: AI Mood-to-Music Recommender

Moodify is a web application that detects a user's mood from a photo or webcam selfie using DeepFace and recommends Spotify playlists tailored to the detected emotion and preferred language. Built with Streamlit, it provides an intuitive interface for users to upload images or use their webcam, analyze their mood, and receive personalized music recommendations.

## Features
- **Emotion Detection**: Uses DeepFace to analyze facial emotions (e.g., happy, sad, neutral) from images or webcam captures.
- **Spotify Playlist Recommendations**: Fetches playlists from Spotify based on the detected mood and user-selected language (e.g., English, Indonesia, Korea).
- **User-Friendly Interface**: Built with Streamlit for easy photo uploads, webcam support, and interactive playlist display.
- **Customizable**: Supports multiple languages and mood-to-genre mappings.

## Prerequisites
- Python 3.8+
- Spotify Developer Account (for API credentials)
- Webcam (optional, for real-time mood detection)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/fajarwiguna/Moodify.git
   cd moodify
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Ensure `requirements.txt` includes:
   ```
   streamlit==1.29.0
   deepface==0.0.86
   opencv-python==4.10.0
   spotipy==2.24.0
   python-dotenv==1.0.1
   numpy==1.26.4
   ```

4. **Set Up Spotify API Credentials**:
   - Create a Spotify Developer account and set up an app at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
   - Copy your `Client ID` and `Client Secret`.
   - Create a `.env` file in the project root:
     ```env
     SPOTIFY_CLIENT_ID=your_client_id
     SPOTIFY_CLIENT_SECRET=your_client_secret
     ```

## Usage
1. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
   - Open your browser and go to `http://localhost:8501`.

2. **Interact with Moodify**:
   - **Select Language**: Choose a playlist language (e.g., Indonesia, English, Korea).
   - **Choose Input Method**: Upload a photo (JPG/PNG) or use your webcam to take a selfie.
   - **Analyze Mood**: The app will detect your mood and display the confidence score and all emotion scores.
   - **Get Playlists**: Receive Spotify playlist recommendations based on your mood.
   - **Retry or Refresh**: Use buttons to retry mood detection, try a different backend, or fetch new playlists.

3. **Example Output**:
   ```
   Detected Mood: Neutral (Confidence: 0.83)
   Analysis took 0.5 seconds
   All Emotion Scores:
   Neutral: 82.56%
   Angry: 12.94%
   ...
   Recommended Playlists:
   1. Indo santai
   2. lagu relax indo
   ```

## Project Structure
```
moodify/
├── app.py              # Main Streamlit app
├── utils.py            # Emotion detection and Spotify API functions
├── config.py           # Mood-to-genre mappings
├── .env                # Spotify API credentials (not tracked)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Troubleshooting
- **Emotion Detection Issues**:
  - If detection is inaccurate (e.g., "angry" instead of "neutral"), ensure good lighting and a frontal face.
  - Try switching the DeepFace backend by clicking "Retry with Different Backend" (uses `mtcnn` by default).
  - Clear DeepFace cache:
    ```bash
    rm -rf ~/.deepface
    ```

- **Spotify API Errors**:
  - If you see `401` errors, rotate your Spotify Client Secret in the Spotify Developer Dashboard.
  - Test API manually:
    ```python
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="your_client_id", client_secret="your_client_secret"))
    print(sp.search(q="relax indonesia", type="playlist", limit=10))
    ```

- **Slow Analysis**:
  - Ensure TensorFlow optimizations are disabled for faster processing:
    ```bash
    export TF_ENABLE_ONEDNN_OPTS=0
    ```
  - Use a smaller image size in `utils.py` (e.g., `max_size = 160`).

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## Future Improvements
- Add custom CSS for a polished Streamlit UI.
- Deploy to Hugging Face Spaces or Streamlit Cloud.
- Support additional languages and genres.
- Improve emotion detection with ensemble models.

## 📜 License
MIT © Fajar Wiguna