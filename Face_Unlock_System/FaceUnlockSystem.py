import streamlit as st
import cv2
import os
import numpy as np
from deepface import DeepFace
from sklearn.metrics.pairwise import cosine_similarity
import pickle

db_file = "face_db.pkl"

def get_face_embedding(frame, model_name = "Facenet"):
    try:
        embedding = DeepFace.represent(img_path= frame, model_name= model_name, enforce_detection= True, detector_backend='opencv')
        return embedding[0]["embedding"]
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_db(db):
    with open(db_file, "wb") as f:
        pickle.dump(db, f)

def load_db():
    if os.path.exists(db_file):
        with open(db_file, "rb") as f:
            return pickle.load(f)
    return {}
    
st.title("Face Unlock System")
option = st.sidebar.selectbox("Choose Action", ["Register Face", "Authenticate"])

cap = cv2.VideoCapture(0)
stframe = st.empty()
db = load_db()

captured = False
frame = None

if option == "Register Face":
    name = st.text_input("Enter Name:")
    capture_btn = st.button("Capture and Register", key= "register")
elif option == "Authenticate":
    capture_btn = st.button("Capture and Authenticate", key= "authenticate")

while not captured:
    ret, live = cap.read()
    if not ret:
        st.error("Camera not working!")
        break
    live = cv2.flip(live, 1)
    stframe.image(live, channels="BGR")

    if capture_btn:
        frame = live.copy()
        captured = True


cap.release()

if captured and frame is not None:
    if option == "Register Face":

        embed = get_face_embedding(frame)
        if embed is not None:
            db[name] = embed
            save_db(db)
            st.success(f"GOOD BOI {name} registered successfully!")
        else:
            st.error("No face Detected, Try Again Bad BOI!")

    elif option == "Authenticate":
        st.header("Authenticate Your Face")
        if not db:
            st.warning("No Registered Users")
        else:
            embed = get_face_embedding(frame)
            if embed is not None:
                max_score = -1
                identity = None
                embed = np.array(embed).reshape(1, -1)
                for name, emb_db in db.items():
                    emb_db = np.array(emb_db).reshape(1, -1)
                    score = cosine_similarity(embed, emb_db)[0][0]
                    if score > max_score:
                        max_score = score
                        identity = name
                if max_score > 0.6:
                    st.success(f"Welcome Back {identity} King/Queen! Similarity: {max_score}")
                else:
                    st.error(f"Who TF are you?. Similarity: {max_score}")
            else:
                st.error("No Face Detected")

