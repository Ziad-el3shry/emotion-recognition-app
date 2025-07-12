import streamlit as st
from deepface import DeepFace
import cv2
import numpy as np
from PIL import Image
import tempfile

st.set_page_config(page_title="Emotion Analyzer", layout="centered")

# Emotion Analysis Function
def analyze_emotion(image):
    try:
        result = DeepFace.analyze(image, actions=['emotion'], enforce_detection=False)
        return result[0]['emotion']
    except Exception as e:
        st.error(f"Analysis failed: {e}")
        return None

# Image Upload Handler
def handle_image():
    st.subheader("Upload an Image")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        img_array = np.array(image)

        st.image(image, caption='Uploaded Image', use_container_width=True)

        emotion_scores = analyze_emotion(img_array)
        if emotion_scores:
            detected_emotion = max(emotion_scores, key=emotion_scores.get)
            st.success(f"Detected Emotion: **{detected_emotion}**")
            st.bar_chart(emotion_scores)
        else:
            st.error("Failed to detect emotion from the image.")

# Video Upload Handler
def handle_video():
    st.subheader("Upload a Video")
    uploaded_file = st.file_uploader("Choose a video", type=["mp4", "avi", "mov"])
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        cap = cv2.VideoCapture(temp_file_path)
        if not cap.isOpened():
            st.error("Error opening video file.")
            return

        stframe = st.empty()
        st.info("Processing video... This may take a while.")
        frame_rate = 30
        frame_count = 0
        detected = []

        progress = st.progress(0)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_count += 1
            if frame_count % frame_rate == 0:
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                emotion_scores = analyze_emotion(rgb_frame)

                if emotion_scores:
                    detected_emotion = max(emotion_scores, key=emotion_scores.get)
                    cv2.putText(rgb_frame, detected_emotion, (30, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    detected.append(detected_emotion)
                else:
                    cv2.putText(rgb_frame, "Unknown", (30, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                stframe.image(rgb_frame, channels="RGB", use_column_width=True)
                progress.progress(min(frame_count / total_frames, 1.0))

        cap.release()
        if detected:
            st.success(f"Most Frequent Emotion: **{max(set(detected), key=detected.count)}**")
        else:
            st.warning("No emotions detected from the video.")

# Main UI
def main():
    st.title("🧠 Emotion Recognition App")
    st.markdown("Analyze emotions from images or videos using deep learning.")

    with st.sidebar:
        st.header("Choose Input Type")
        choice = st.radio("Input Source", ["Image", "Video"])

    if choice == "Image":
        handle_image()
    elif choice == "Video":
        handle_video()

if __name__ == "__main__":
    main()
