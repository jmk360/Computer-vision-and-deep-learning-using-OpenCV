import cv2

def cartoon_filter(img):
    # 입력영상을 축소한다음에 단순화를 시키면 효과가 더 크게 나타나게 된다. 연산시간도 빨라진다.
    h, w = img.shape[:2]
    img = cv2.resize(img, (w//2, h//2))
    blr = cv2.bilateralFilter(img, -1, 20, 7)
    edge = ~cv2.Canny(img, 50, 120)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    dst = cv2.bitwise_and(blr, edge)
    dst = cv2.resize(dst, (w,h), interpolation=cv2.INTER_NEAREST) # interpolation을 설정해주는게 좀더 결과가 좋음
    return dst

def pencil_sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (0,0), 3)
    dst = cv2.divide(gray, blur, scale=255)
    dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)

    return dst

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('cam open failed!')
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)

cnt = 3
cam_mode = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print('Image load failed!')
        exit()

    if cam_mode == 1:
        frame = cartoon_filter(frame)
    elif cam_mode == 2:
        frame = pencil_sketch(frame)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(delay)
    if key == ord(' '):
        cam_mode += 1
        if cam_mode == cnt:
            cam_mode = 0
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()