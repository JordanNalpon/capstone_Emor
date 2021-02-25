from scipy.spatial import distance as dist
import numpy as np
import cv2
from imutils import face_utils
from imutils.video import VideoStream
from fastai.vision import *

import imutils
import argparse
import time
import dlib
import os
import pickle
import pathlib


temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


path = os.getcwd()

#arguments
ap = argparse.ArgumentParser()
ap.add_argument("--savedata", dest="savedata", action="store_true")
ap.add_argument("--no-savedata", dest="savedata", action="store_false")
ap.set_defaults(savedata=False)
args = vars(ap.parse_args())

print('loading') #to check if code is properly loaded


#imported materials

#load CNN model. change folder to try different models
learn = load_learner('../01_materials/exported_model/all_images/') # all images


face_cascade = cv2.CascadeClassifier(
    "../01_materials/haarcascade/haarcascade_frontalface_default.xml")

predictor = dlib.shape_predictor(
    "../01_materials/predictor/shape_predictor_68_face_landmarks.dat")

start = time.perf_counter()
data = []
time_value = 0

capture_imutils = VideoStream(src=0).start()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
videoWriter = cv2.VideoWriter(
    'C:/Users/JDN/Desktop/Github/ga_capstone/01_materials/exported_materials/vsc_video_2.mp4', fourcc, 30.0, (640, 480))


#eyes tracking
EYE_AR_THRESH = 0.20
EYE_AR_CONSEC_FRAMES = 10

COUNTER = 0

#eye
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

def data_time(time_value, prediction, probability, ear):
    current_time = int(time.perf_counter()-start)
    if current_time != time_value:
        data.append([current_time, prediction, probability, ear])
        time_value = current_time
    return time_value

def emoji_layer(current_emotion):
    emo_img = cv2.imread('../05_external_folder/emoji_icon/' + current_emotion, cv2.IMREAD_UNCHANGED)
    emo_img = cv2.cvtColor(emo_img, cv2.COLOR_RGB2RGBA)
    y1, y2 = Y_1, Y_1 + emo_img.shape[0]
    x1, x2 = X_1, X_1 + emo_img.shape[1]
    emo_img = cv2.resize(emo_img,(x2-x1,y2-y1))
    alpha_s = emo_img[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s
    try:
        for c in range(0, 3):
            frame[y1:y2, x1:x2, c] = (alpha_s * emo_img[:, :, c] + alpha_l * frame[y1:y2, x1:x2, c])
    except:
        pass


print('showtime!')
n =1 
while True:
    
    #video feed   
    frame = capture_imutils.read()
    frame = imutils.resize(frame, width=640, height = 480)
    
    #gray scale the images
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coord = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))

    for coords in face_coord:
        X, Y, w, h = coords
        H, W, _ = frame.shape
        X_1, X_2 = (max(0, X - int(w * 0.3)), min(X + int(1.3 * w), W))
        Y_1, Y_2 = (max(0, Y - int(0.3 * h)), min(Y + int(1.3 * h), H))
        img_cp = gray[Y_1:Y_2, X_1:X_2].copy()
        prediction, idx, probability = learn.predict(
            Image(pil2tensor(img_cp, np.float32).div_(225)))

        cv2.rectangle(
            img=frame,
            pt1=(X_1, Y_1),
            pt2=(X_2, Y_2),
            color=(128, 128, 0),
            thickness=2,
        )

        rect = dlib.rectangle(X, Y, X+w, Y+h)
        # text modifier
        cv2.putText(frame, str(prediction), (X_1+50, Y_1 + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (225, 255, 255), 2)
        
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        # emoicon
        if str(prediction) == 'happy':
            current_emotion = 'smile_blush_resized.png'
            emoji_layer(current_emotion)
        
        elif str(prediction) == 'angry':
            current_emotion = 'angry_resized.png'
            emoji_layer(current_emotion)
        
        elif str(prediction) == 'sad':
            current_emotion = 'sad_resized.png'
            emoji_layer(current_emotion)
        
        elif str(prediction) == 'surprise':
            current_emotion = 'surprise_resized.png'
            emoji_layer(current_emotion)
        
        elif str(prediction) == 'neutral':
            current_emotion = 'neutral_resized.png'
            emoji_layer(current_emotion)
        
        elif str(prediction) == 'fear':
            current_emotion = 'fear_resized.png'
            emoji_layer(current_emotion)
        
        elif str(prediction) == 'disgust':
            current_emotion = 'disgust_resized.png'
            emoji_layer(current_emotion)
 
 
        # check if person is distracted based on eye ratio
        if ear < EYE_AR_THRESH:
            COUNTER += 1
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                cv2.putText(frame, "Distracted", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            COUNTER = 0
        
        time_value = data_time(time_value, prediction, probability, ear)
    videoWriter.write(frame)

    cv2.imshow("EmoR", frame)


    if cv2.waitKey(1) == 27:
        break

if args["savedata"]:
    df = pd.DataFrame(
        data, columns=['Time (seconds)', 'Expression', 'Probability', 'EAR'])
    df.to_csv(path+'/exportlive.csv')
    print("data saved to exportlive.csv")


videoWriter.release()

cv2.destroyAllWindows()