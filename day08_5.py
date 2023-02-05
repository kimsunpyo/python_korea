# opencv 모듈추가
# mediapipe 모듈추가
import cv2
import mediapipe as mp

def ShowImage(img_path):
    img = cv2.imread(img_path)
    cv2.imshow('kimsunpyo', img)
    cv2.waitKey(0)


def ShowVedio(vedio_path):
    vc = cv2.VideoCapture(vedio_path)
    while True:
        success, img = vc.read()
        if success:
            cv2.imshow('kimsunpyo', img)
        if cv2.waitKey(20) & 0xFF == 27:
            break




cap=cv2.VideoCapture('person3.mp4')
mp_fd = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
fd = mp_fd.FaceDetection()



while True:
    success, img = cap.read()
    if success:
        from_bgr_to_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face = fd.process(from_bgr_to_rgb)

        if face.detections:
            for id, detection in enumerate(face.detections):
                fd_box = detection.location_data.relative_bounding_box
                box = int(fd_box.xmin * img.shape[1]), int(fd_box.ymin * img.shape[0]), int(fd_box.width * img.shape[1]), int(fd_box.height * img.shape[0])
            cv2.rectangle(img, box, (255,0,255), 2)
            cv2.putText(img,f'{round(detection.score[0]*100, 2)}%', (box[0],box[1]), cv2.FONT_ITALIC, 1, (255,0,255), 2)
        cv2.imshow('title', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break






# ShowImage('person2.jpg')
# ShowVedio('person2.mp4')