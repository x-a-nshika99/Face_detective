import cv2
import numpy as np
from deepface import DeepFace

# Load face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Start webcam
cap = cv2.VideoCapture(0)


font = cv2.FONT_HERSHEY_SIMPLEX


def age_category(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teen"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"


def analyze(face):
    try:
        result = DeepFace.analyze(
            face,
            actions=["age", "gender", "emotion"],
            enforce_detection=False
        )

        age = result[0]["age"]
        gender = result[0]["dominant_gender"]
        emotion = result[0]["dominant_emotion"]

        category = age_category(age)

        return age, gender, emotion, category

    except:
        return None, None, None, None


while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        1.3,
        5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:

        face_img = frame[y:y+h, x:x+w]

        age, gender, emotion, category = analyze(face_img)

        if age is not None:
            label = f"{gender} | {category} | Age:{age} | {emotion}"
        else:
            label = "Analyzing..."

        # Draw box
        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0,255,0),
            2
        )

        # Background for text
        cv2.rectangle(
            frame,
            (x, y-30),
            (x+w, y),
            (0,255,0),
            -1
        )

        cv2.putText(
            frame,
            label,
            (x+5, y-5),
            font,
            0.5,
            (0,0,0),
            2
        )

    cv2.imshow("AI Face Analyzer", frame)

    if cv2.waitKey(1) & 0xFF == 27:   # ESC key
        break

cap.release()
cv2.destroyAllWindows()