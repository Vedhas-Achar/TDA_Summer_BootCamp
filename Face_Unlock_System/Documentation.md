# Face Unlock System — Project Documentation

## 1. Objective

To develop a real-time Face Unlock System using Deep Learning techniques, where users can register and authenticate themselves via webcam. The system is implemented using Streamlit for UI, OpenCV for camera access, and DeepFace for face detection and embedding.

---

## 2. Methodology

The system workflow is divided into the following steps:

### 2.1. User Modes
- **Register Face**: Capture a face image and register the corresponding embedding with a user-defined name.
- **Authenticate**: Capture a new face image and compare its embedding with saved ones in the database using cosine similarity.

### 2.2. Face Embedding Extraction
- We use the `DeepFace.represent()` function with the `Facenet` model to convert a captured face into a 128-dimensional embedding vector.
- The backend detector is OpenCV for efficiency.

### 2.3. Similarity Measure
- The similarity between the captured face and stored embeddings is calculated using cosine similarity.
- A threshold of **0.5** is used to determine whether a match is valid.

### 2.4. Live Preview
- A live webcam preview is shown continuously, and when a user clicks “Capture and Register” or “Capture and Authenticate,” a frame is captured for processing.

---

## 3. Dataset Preparation

### 3.1. Input Source
- Webcam live feed using OpenCV.

### 3.2. Storage Format
- Face embeddings are stored in a `.pkl` file using Python’s `pickle` module.
- Structure: `{ "name": [embedding vector] }`

### 3.3. Advantages
- Privacy is preserved since images are not stored.
- Lightweight compared to full image datasets.

---

## 4. Model and Architecture

### 4.1. DeepFace Framework
- **Model Used**: Facenet (others like VGG-Face, ArcFace, etc. are also supported)
- **Embedding Dimensionality**: 128
- **Backend Detector**: OpenCV

---

## 5. Experimental Results

| User     | Matching Status  | Cosine Similarity Score  |
|----------|------------------|--------------------------|
| Shreyas  | Success          | 0.96                     |
| Bala     | Success          | 0.81                     |
| Vedhas   | Failure          | 0.36                     |

- Threshold used: **0.5**
- Sample Accuracy: ~90%

---

## 6. Real-World Applications

1. Smart Door Locks  
   Replace traditional key systems with face authentication.

2. Attendance Systems  
   Automate attendance in schools or offices.

3. Device Login  
   Secure access to personal computers without passwords.

4. Multi-user Access Control  
   Shared access to smart TVs, home assistants, or games.

5. Visitor Management Systems  
   Track and log visitors using facial recognition.

---

## 7. Future Improvements

- Give option of adding photo from gallery or take a live pic
- Save face images for backup or retraining.
- Support multiple embeddings per user (for varied angles).
- UI enhancements (e.g., profile pictures, logs).
- Use a database (e.g., SQLite) instead of pickle files.

---

## 8. Dependencies

```bash
pip install deepface opencv-python streamlit scikit-learn
```
## 9. Conclusion

This project demonstrates a practical and user-friendly face recognition system using DeepFace with Streamlit UI. It is efficient, extendable, and suitable for real-world security and personalization applications.
