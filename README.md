# 🧠 Emotion Recognition App

A simple Streamlit web app that detects emotions from images and videos using DeepFace. Upload media, get emotion predictions, and visualize results in real-time.

## 🚀 Features

- 🎭 Emotion detection from **images**
- 🎥 Emotion analysis from **videos**
- 📊 Real-time bar chart visualization of emotions
- 🧠 Powered by deep learning (`DeepFace`)

## 🛠️ Built With

- Python
- [DeepFace](https://github.com/serengil/deepface)
- Streamlit
- OpenCV
- NumPy
- PIL

## 📦 Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/emotion-recognition-app.git
   cd emotion-recognition-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
emotion-recognition-app/
├── app.py               # Main Streamlit app
├── DeepFace.ipynb       # Notebook for DeepFace testing (optional)
├── requirements.txt     # Project dependencies
└── README.md            # You're reading it!
```

## 🖼️ Usage

- Go to the app UI
- Select input type (Image or Video) from the sidebar
- Upload your file
- View detected emotions and probability chart

## 📌 Notes

- Supports: `['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']`
- Video processing samples 1 frame per second

## 📜 License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
---

> Built with ❤️ using AI and Streamlit
