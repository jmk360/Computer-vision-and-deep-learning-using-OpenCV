import cv2
import numpy as np

# 두 개의 동영상을 열어서 cap1, cap2로 지정
cap1 = cv2.VideoCapture('video1.mp4')
cap2 = cv2.VideoCapture('video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed!')
    exit()

# 두 동영상의 크기, FPS는 같다고 가정함
fourcc = cv2.VideoWriter_fourcc(*"DIVX")
fps = cap1.get(cv2.CAP_PROP_FPS)
w = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 출력 동영상 객체 생성
out = cv2.VideoWriter('output7.avi', fourcc, fps, (w,h), True)
if not out.isOpened():
    print('video open failed!')
    cap1.release()
    cap2.release()
    exit()

delay = int(1000/fps)
frame_cnt1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
effect_frames = int(fps * 2)

# 1번 동영상 복사
for i in range(frame_cnt1-effect_frames):
    ret1, frame1 = cap1.read()
    if not ret1:
        print('Image load failed!')
        break
    out.write(frame1)
    cv2.imshow('frame', frame1)
    if cv2.waitKey(delay) == 27:
        break

img = np.empty((h,w,3), np.uint8)

# 1번 동영상 뒷부분과 2번 동영상 앞부분을 합성
for i in range(effect_frames):
    ret1, frame1 = cap1.read()    
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print('Image load failed!')
        break

    # dx = int(w * (i / effect_frames)) # 왼쪽으로 밀기
    # img[:,:dx] = frame2[:,:dx]
    # img[:,dx:] = frame1[:,dx:]

    # dx = int(w - (i*w / effect_frames)) # 오른쪽으로 밀기
    # img[:,:dx] = frame1[:,:dx]
    # img[:,dx:] = frame2[:,dx:]

    # dy = int(h - (i*h/effect_frames)) # 위로 밀기
    # img[0:dy,:] = frame1[0:dy,:]
    # img[dy:,:] = frame2[dy:,:]

    # dy = int(h * (i / effect_frames)) # 아래로 밀기
    # img[0:dy,:] = frame2[0:dy,:]
    # img[dy:,:] = frame1[dy:,:]

    # 디졸브 : 첫번째 동영상이 점점 흐려지다가, 두번째 동영상이 점점 진해지면서 나타난다.
    alpha = 1 - (i / effect_frames)
    img = cv2.addWeighted(frame1, alpha, frame2, (1-alpha), 0)
    
    out.write(img)
    cv2.imshow('frame', img)
    if cv2.waitKey(delay) == 27:
        break

# 2번 동영상을 복사
for i in range(frame_cnt2-effect_frames):
    ret2, frame2 = cap2.read()
    if not ret2:
        print('Image load failed!')
        break
    out.write(frame2)
    cv2.imshow('frame', frame2)
    if cv2.waitKey(delay) == 27:
        break

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()