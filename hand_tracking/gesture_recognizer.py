# Import necessary modules
import cv2
import mediapipe as mp
import numpy as np

class GestureRecognizer:
    def __init__(self):
        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False,
                                         max_num_hands=1,
                                         min_detection_confidence=0.7,
                                         min_tracking_confidence=0.5)
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return img

    def recognize_gesture(self, img):
        gesture = ""
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                # Example: Recognize an open hand gesture
                # Check if the distance between the tips of thumb and index finger is greater than a threshold
                thumb_tip = np.array([hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x,
                                      hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y])
                index_finger_tip = np.array([hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x,
                                             hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y])
                distance = np.linalg.norm(index_finger_tip - thumb_tip)

                # This threshold might need adjustment for your setup and distance from the camera
                if distance > 0.1:
                    gesture = "Open Hand"
                else:
                    gesture = "Closed Hand"
                
        return gesture

def main():
    cap = cv2.VideoCapture(0)  # Use the correct camera index
    recognizer = GestureRecognizer()

    while True:
        success, img = cap.read()
        if not success:
            break

        img = recognizer.find_hands(img)
        gesture = recognizer.recognize_gesture(img)
        if gesture:
            print(gesture)  # For demonstration, print the recognized gesture
            cv2.putText(img, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
