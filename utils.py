from deepface import DeepFace
import cv2
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import logging
from config import MOOD_TO_GENRE
from dotenv import load_dotenv
import os
import time
import numpy as np
import random
from functools import lru_cache

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Spotify client setup
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
if not spotify_client_id or not spotify_client_secret:
    logger.error("Spotify credentials missing in .env")
    raise ValueError("SPOTIFY_CLIENT_ID or SPOTIFY_CLIENT_SECRET not set in .env")
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret))

def detect_emotion(image):
    """
    Detects the dominant emotion and all emotion scores from an input image using DeepFace.

    Args:
        image (numpy.ndarray): Input image in BGR format (from OpenCV).

    Returns:
        tuple: (emotion, confidence, emotion_scores) where:
               - emotion is a string (e.g., 'happy')
               - confidence is a float (0 to 1)
               - emotion_scores is a dict of all emotions and their scores
    """
    try:
        start_time = time.time()

        # Preprocess image: resize
        max_size = 224  # Reduced size for faster processing
        height, width = image.shape[:2]
        if max(height, width) > max_size:
            scale = max_size / max(height, width)
            image = cv2.resize(image, (int(width * scale), int(height * scale)), interpolation=cv2.INTER_AREA)

        # Convert BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Analyze emotion
        result = DeepFace.analyze(image_rgb, actions=['emotion'], detector_backend='mtcnn', enforce_detection=False)

        elapsed_time = time.time() - start_time
        logger.info(f"Emotion detection took {elapsed_time:.2f} seconds")

        # Get all emotion scores
        emotion_scores = result[0]['emotion']
        logger.info("All emotion scores: %s", emotion_scores)

        # Extract dominant emotion and confidence
        emotion = result[0]['dominant_emotion']
        confidence = emotion_scores[emotion] / 100.0

        # Fallback for misdetection
        if emotion in ["fear", "neutral", "angry"] and confidence < 0.8:  # Added angry, lower threshold
            sorted_emotions = sorted(emotion_scores.items(), key=lambda x: x[1], reverse=True)
            emotion = sorted_emotions[0][0]  # Take highest score
            confidence = sorted_emotions[0][1] / 100.0
            logger.info(f"Overriding to {emotion} with confidence {confidence:.2f}")

        logger.info(f"Final detected emotion: {emotion} with confidence: {confidence:.2f}")
        return emotion, confidence, emotion_scores

    except Exception as e:
        logger.error(f"Error detecting emotion: {str(e)}")
        return "neutral", 0.0, {}

@lru_cache(maxsize=100)
def get_spotify_playlist(emotion, language="English"):
    """
    Fetches Spotify playlists based on emotion and language preference.

    Args:
        emotion (str): Detected emotion (e.g., 'happy', 'sad').
        language (str): Preferred language or region (e.g., 'English', 'Indonesia', 'Korea').

    Returns:
        list: List of tuples [(playlist_name, playlist_url), ...] for multiple playlists.
    """
    try:
        # Get genres from mood mapping
        genres = MOOD_TO_GENRE.get(emotion, "chill")
        # Adjust query based on language
        if language == "Indonesia":
            query = "relax indonesia" if emotion == "neutral" else f"{genres} indonesia"
        elif language == "Korea":
            query = f"{genres} k-pop"
        elif language == "Japan":
            query = f"{genres} j-pop"
        elif language == "Mandarin":
            query = f"{genres} mandarin"
        else:
            query = f"{genres}"
        logger.info(f"Searching playlists for emotion: {emotion}, language: {language}, query: {query}")

        # Search for multiple playlists
        result = sp.search(q=query, type="playlist", limit=5, offset=random.randint(0, 200))
        playlists = result["playlists"]["items"]
        logger.info(f"Spotify API response: {playlists}")

        # Filter out None items
        playlist_list = []
        for p in playlists:
            if p is None:
                logger.warning("Skipping None playlist in API response")
                continue
            try:
                playlist_list.append((p["name"], p["external_urls"]["spotify"]))
            except (KeyError, TypeError) as e:
                logger.warning(f"Skipping invalid playlist: {str(e)}")

        if playlist_list:
            logger.info(f"Found playlists: {playlist_list}")
            return playlist_list
        else:
            logger.warning(f"No valid playlists found for query: {query}")
            return [("Default Chill Playlist", "https://open.spotify.com/playlist/37i9dQZF1DX0UrRvztWcAU")]

    except Exception as e:
        logger.error(f"Error fetching Spotify playlist: {str(e)}")
        return [("Default Chill Playlist", "https://open.spotify.com/playlist/37i9dQZF1DX0UrRvztWcAU")]