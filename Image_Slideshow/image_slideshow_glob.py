import sys
import cv2
# glob.glob을 사용해서 특정폴더안에 있는 파일들의 이름을 읽어온다.
import glob

# glob.glob은 특정폴더 안에 파일들의 이름을 읽어오는데, 인자로 넣어준 경로에다가 파일으름을 합쳐서 가지고 온다.
file_list = glob.glob('.\\images\\*.jpg')
# 파일을 제대로 읽어오지 못했을 경우를 대비한 예외처리
if not file_list:
    print('There are no jpg files in "images" folder')
    sys.exit()

# 전체화면 설정
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cnt = len(file_list)
idx = 0

while True:
    img = cv2.imread(file_list[idx], cv2.IMREAD_COLOR)
    if img is None:
        print('Image load failed!')
        break
    cv2.imshow('image', img)
    # 키보드로부터 아무키나 누르면 종료
    if cv2.waitKey(1000) > 0:
        break
    idx += 1
    if idx == cnt:
        idx = 0

cv2.destroyAllWindows()