import streamlit as st


import numpy as np
import cv2
import pickle


st.title('🎈 App Name')

st.write('Hello world!')
frameWidth = 1280  # CAMERA RESOLUTION
frameHeight = 720
brightness = 180
threshold = 0.90  # PROBABILITY THRESHOLD
font = cv2.FONT_HERSHEY_SIMPLEX

##############################################

# SETUP THE VIDEO CAMERA
cap = cv2.VideoCapture(0)  # 0 for the default webcam
cap.set(3, frameWidth)  # Set width
cap.set(4, frameHeight)  # Set height
cap.set(10, brightness)  # Set brightness

# Load the trained model
pickle_in = open("model_trained.p", "rb")
model = pickle.load(pickle_in)


# Preprocessing functions
def grayscale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def equalize(img):
    img = cv2.equalizeHist(img)
    return img


def preprocessing(img):
    img = grayscale(img)  # Convert to grayscale
    img = equalize(img)  # Equalize histogram
    img = img / 255.0  # Normalize to range [0, 1]
    return img


# Function to map class numbers to traffic sign names
def getClassName(classNo):
    if classNo == 0:
        return 'Speed Limit 20 km/h'
    elif classNo == 1:
        return 'Speed Limit 30 km/h'
    elif classNo == 2:
        return 'Speed Limit 50 km/h'
    elif classNo == 3:
        return 'Speed Limit 60 km/h'
    elif classNo == 4:
        return 'Speed Limit 70 km/h'
    elif classNo == 5:
        return 'Speed Limit 80 km/h'
    elif classNo == 6:
        return 'End of Speed Limit 80 km/h'
    elif classNo == 7:
        return 'Speed Limit 100 km/h'
    elif classNo == 8:
        return 'Speed Limit 120 km/h'
    elif classNo == 9:
        return 'No passing'
    elif classNo == 10:
        return 'No passing for vehicles over 3.5 metric tons'
    elif classNo == 11:
        return 'Right-of-way at the next intersection'
    elif classNo == 12:
        return 'Priority road'
    elif classNo == 13:
        return 'Yield'
    elif classNo == 14:
        return 'Stop'
    elif classNo == 15:
        return 'No vehicles'
    elif classNo == 16:
        return 'Vehicles over 3.5 metric tons prohibited'
    elif classNo == 17:
        return 'No entry'
    elif classNo == 18:
        return 'General caution'
    elif classNo == 19:
        return 'Dangerous curve to the left'
    elif classNo == 20:
        return 'Dangerous curve to the right'
    elif classNo == 21:
        return 'Double curve'
    elif classNo == 22:
        return 'Bumpy road'
    elif classNo == 23:
        return 'Slippery road'
    elif classNo == 24:
        return 'Road narrows on the right'
    elif classNo == 25:
        return 'Road work'
    elif classNo == 26:
        return 'Traffic signals'
    elif classNo == 27:
        return 'Pedestrians'
    elif classNo == 28:
        return 'Children crossing'
    elif classNo == 29:
        return 'Bicycles crossing'
    elif classNo == 30:
        return 'Beware of ice/snow'
    elif classNo == 31:
        return 'Wild animals crossing'
    elif classNo == 32:
        return 'End of all speed and passing limits'
    elif classNo == 33:
        return 'Turn right ahead'
    elif classNo == 34:
        return 'Turn left ahead'
    elif classNo == 35:
        return 'Ahead only'
    elif classNo == 36:
        return 'Go straight or right'
    elif classNo == 37:
        return 'Go straight or left'
    elif classNo == 38:
        return 'Keep right'
    elif classNo == 39:
        return 'Keep left'
    elif classNo == 40:
        return 'Roundabout mandatory'
    elif classNo == 41:
        return 'End of no passing'
    elif classNo == 42:
        return 'End of no passing by vehicles over 3.5 metric tons'


# Main loop
while True:
    success, imgOriginal = cap.read()  # Capture frame
    if not success:
        print("Failed to capture frame. Exiting...")
        break

    # Preprocess the frame
    img = cv2.resize(imgOriginal, (32, 32))  # Resize to 32x32
    img = preprocessing(img)  # Apply preprocessing
    img = img.reshape(1, 32, 32, 1)  # Reshape for model input

    # Predict and get class/probability
    predictions = model.predict(img)  # Predict probabilities
    classIndex = np.argmax(predictions)  # Get the class with the highest probability
    probabilityValue = np.amax(predictions)  # Get the highest probability

    # Display predictions if probability exceeds threshold
    if probabilityValue > threshold:
        className = getClassName(classIndex)
        cv2.putText(imgOriginal, f"CLASS: {className}", (20, 35), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(imgOriginal, f"PROBABILITY: {round(probabilityValue * 100, 2)}%", (20, 75), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the camera feed with results
    cv2.imshow("Traffic Sign Recognition", imgOriginal)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
