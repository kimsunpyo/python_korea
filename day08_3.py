import cv2
import mediapipe as mp
# pip install mediapipe

# 만약에 OS권한문제로 설치가 안될경우
'''
0. 파이썬 실행 중인지 체크한다 (만약 실행중이면 중지버튼 눌러 중단)
1. anaconda prompt를 관리자 권한으로 실행
2. python -m pip install --upgrade pip 를 입력해서 pip를 업그레이드 시켜줌
'''

'''
만약에 웹캠이면 VideoCapture에 0을 넣고, 맨 밑 WaitKey에 1을 넣는다
'''
# 동영상 읽어줘
cap = cv2.VideoCapture('person.mp4')        # 0으로 입력하면 웹캠
mp_fd = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
fd = mp_fd.FaceDetection()

# 무한반복 (동영상 == 빠르게 여러 이미지를 출력)
while True:
    # 읽기성공여부. 동영상을 자른 이미지
    success, img = cap.read()
    # 동영상을 성공적으로 읽었으면 보여주기전에 얼굴을 찾는다
    if success:
        from_bgr_to_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)      # 얼굴찾기 정확도 향상을 위해 BGR -> RGB
        face = fd.process(from_bgr_to_rgb)      # 얼굴찾기

        if face.detections:
            # 얼굴을 찾았다! ==> 사람 얼굴을 찾은다음 하고 싶은 동작
            # 함수 사용하기
            for id, detection in enumerate(face.detections):
                # mp_draw.draw_detection(img, detection)     # medeapipe 얼굴표시
                fd_box = detection.location_data.relative_bounding_box
                box = int(fd_box.xmin * img.shape[1]), int(fd_box.ymin * img.shape[0]), int(fd_box.width * img.shape[1]), int(fd_box.height * img.shape[0])
            cv2.rectangle(img, box, (255,0,255), 2)     # BGR, 두께 2
            cv2.putText(img,f'{round(detection.score[0]*100, 2)}%', (box[0],box[1]), cv2.FONT_ITALIC, 1, (255,0,255), 2)

        cv2.imshow('title', img)
    if cv2.waitKey(20) & 0xFF == 27:
        # 동영상 waitKey 20~25, 웹캠 .waitKey1, 이미지 waitKey 0
        # ESC키를 눌러 종료
        break
