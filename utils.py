from deepface import DeepFace
import cv2
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def detect_emotion(image):
    """
    Detects the dominant emotion from an input image using DeepFace.

    Args:
        image (numpy.ndarray): Input image in BGR format (from OpenCV).

    Returns:
        tuple: (emotion, confidence) where emotion is a string (e.g., 'happy')
               and confidence is a float (0 to 1).

    Raises:
        Exception: If emotion detection fails.
    """
    try:
        # Convert BGR to RGB (DeepFace expects RGB)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Analyze emotion using DeepFace
        result = DeepFace.analyze(image_rgb, actions=['emotion'], enforce_detection=False)

        # Extract dominant emotion and confidence
        emotion = result[0]['dominant_emotion']
        confidence = result[0]['emotion'][emotion] / 100.0  # Normalize to 0-1

        logger.info(f"Detected emotion: {emotion} with confidence: {confidence:.2f}")
        return emotion, confidence

    except Exception as e:
        logger.error(f"Error detecting emotion: {str(e)}")
        return "neutral", 0.0  # Fallback emotion