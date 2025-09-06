# 🎧 AI Mood-to-Music Recommender: Project Overview

## 📌 Project Summary

The **AI Mood-to-Music Recommender** is an interactive web application that leverages artificial intelligence to detect a user's emotional state from a selfie or uploaded photo and recommends personalized Spotify playlists matching that mood. By integrating computer vision for emotion detection, machine learning for mood mapping, and the Spotify API for music recommendations, this project creates a seamless, fun, and engaging experience for users seeking mood-aligned music.

This application addresses the common challenge of discovering music that fits one's current emotional state, making music listening more intuitive and personal. It serves as a professional portfolio piece, demonstrating skills in machine learning (ML), computer vision (CV), API integration, web development, and software engineering best practices.

**Target Audience**: Music enthusiasts, casual users looking for personalized recommendations, and developers/recruiters interested in AI applications.

## 🎯 Project Goals

- **Technical Showcase**: Highlight proficiency in ML/CV models (e.g., DeepFace for emotion recognition), API integrations (Spotify), and rapid prototyping with Python-based tools.
- **User-Centric Design**: Deliver a fun, interactive tool that enhances daily music experiences by linking emotions to curated playlists.
- **Portfolio Enhancement**: Provide a deployable, demo-ready project with comprehensive documentation to attract recruiters on platforms like LinkedIn and GitHub.
- **Educational Value**: Illustrate how pre-trained ML models can be applied to real-world, consumer-facing applications.
- **Scalability Demonstration**: Lay the foundation for future enhancements, showing thoughtful design for extensibility.

## ✨ Key Features (MVP - Minimum Viable Product)

1. **User Input Interface**:
   - Upload a photo or capture a selfie via webcam for real-time interaction.

2. **Facial Emotion Detection**:
   - Analyzes facial expressions using the DeepFace library to identify emotions such as happy, sad, angry, neutral, surprised, fear, or disgust.
   - Handles edge cases like low lighting or partial faces with basic preprocessing via OpenCV.

3. **Mood-to-Music Mapping**:
   - Maps detected emotions to music genres or moods (e.g., happy → upbeat pop/rock; sad → acoustic/ballads).
   - Uses a simple rule-based system in MVP, with potential for ML-based enhancements later.

4. **Spotify Playlist Recommendations**:
   - Integrates with Spotify Web API via Spotipy to fetch or generate playlists.
   - Provides direct links to Spotify playlists or embeds previews where possible.

5. **Interactive UI**:
   - Built with Streamlit for a responsive, user-friendly web interface.
   - Displays detected emotion, confidence score, and recommended playlists with thumbnails.

## 🛠️ Tech Stack

| Area                  | Tools/Libraries                          | Purpose |
|-----------------------|------------------------------------------|---------|
| **Frontend/UI**       | Streamlit                                | Interactive web app with webcam support. |
| **Emotion Detection** | DeepFace, OpenCV                         | Facial analysis and image preprocessing. |
| **Music Integration** | Spotify Web API, Spotipy                 | Fetching and recommending playlists. |
| **Backend**           | Python (3.10+)                           | Core logic and scripting. |
| **Deployment**        | Hugging Face Spaces or Streamlit Cloud   | Hosting for live demos. |
| **Documentation**     | Markdown, draw.io (diagrams)             | Project docs and visuals. |
| **Testing**           | pytest                                   | Unit tests for key functions. |
| **Environment**       | .env for API keys, requirements.txt      | Dependency management. |

## 📈 MVP Scope and Timeline

- **Scope**:
  - Core functionality: Photo upload/webcam → Emotion detection → Mood mapping → Spotify recommendations → UI display.
  - Exclusions in MVP: User authentication, real-time streaming, or advanced personalization (e.g., based on Spotify user history).

- **Timeline (1 Week)**:
  - Day 1: Planning and docs.
  - Day 2-3: Emotion detection and mapping.
  - Day 4: Spotify integration and UI.
  - Day 5-6: Testing and refinements.
  - Day 7: Deployment and final docs.

- **Success Metrics**:
  - Accurate emotion detection (>70% on standard test images).
  - Seamless API calls without errors.
  - Positive user feedback in demos (e.g., via LinkedIn shares).

## ⚠️ Limitations and Ethical Considerations

- **Limitations**:
  - Relies on pre-trained models; may have biases in emotion detection (e.g., less accurate for diverse ethnicities or ages—addressed in future with fine-tuning).
  - Spotify API requires developer credentials; public demo uses curated playlists to avoid auth issues.
  - No handling for privacy-sensitive data (e.g., photos are processed locally/in-memory, not stored).

- **Ethical Considerations**:
  - **Privacy**: User photos are not saved; processing is ephemeral.
  - **Bias Mitigation**: Acknowledge potential biases in ML models and reference sources like the DeepFace documentation.
  - **Accessibility**: Ensure UI is responsive and works on mobile; add alt text for visuals.
  - **Transparency**: Document model accuracy and limitations in MODEL_CARD.md.

## 🔮 Future Enhancements

- **Advanced Features**: Real-time emotion tracking from video streams, integration with user Spotify accounts for personalized playlists, or multi-emotion blending.
- **Improvements**: Custom ML model training on diverse datasets, support for other music services (e.g., Apple Music), or voice input for mood detection.
- **Monetization/Expansion**: Turn into a full app with ads or premium features.

## 🗺️ System Architecture

![System Architecture Diagram](docs/architecture.png)

## 📂 Project Structure Reference

See the roadmap for the full folder structure, including `docs/` for this overview and diagrams.

For questions or contributions, reach out via GitHub issues.

---

*Author: Fajar Satria Wiguna*  
*License: MIT*