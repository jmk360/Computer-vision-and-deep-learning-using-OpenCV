import cv2

# 두 동영상의 크기, FPS는 같다고 가정
cap1 = cv2.VideoCapture('woman.mp4') # 녹색 배경 동영상
cap2 = cv2.VideoCapture('raining.mp4') # 비오는 배경 동영상
if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed!')
    exit()

fourcc = cv2.VideoWriter_fourcc(*"DIVX")
fps = cap1.get(cv2.CAP_PROP_FPS)
w = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 출력 동영상 객체 생성
out = cv2.VideoWriter('output.avi', fourcc, fps, (w,h), True)
if not out.isOpened():
    cap1.release()
    cap2.release()
    print('video open failed!')
    exit()

delay = int(1000 / fps)
do_composit = False # 합성 여부 플래그

# 전체 동영상 재생
while True:
    ret1, frame1 = cap1.read()
    if not ret1:
        break
    
    # do_composit 플르그가 True일 때에만 합성
    if do_composit:
        ret2, frame2 = cap2.read()
        if not ret2:
            break

        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50, 150, 0), (80, 255, 255))
        cv2.copyTo(frame2, mask, frame1)
    
    out.write(frame1)
    cv2.imshow('frame1', frame1)
    key = cv2.waitKey(delay)

    # 스페이스바를 누르면 do_composit 플래그를 변경
    if key == ord(' '):
        do_composit = not do_composit
    elif key == 27:
        break

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()