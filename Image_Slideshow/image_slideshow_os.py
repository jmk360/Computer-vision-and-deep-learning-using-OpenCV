import sys
import cv2
# os.listdir 함수로 특정 폴더안에 있는 파일들의 이름을 읽어 올거기때문에 os를 import 시킨다.
import os 

# os.listdir 은 특정 폴더 안에 있는 파일들의 이름만 가지고 온다.
file_list = os.listdir('.\\images\\') 

# 파일을 읽어오지 못한 경우를 대비한 예외처리
if not file_list: 
    print('There are no files in "images" folder')
    sys.exit()

# os.listdir로 읽어 온 파일 이름 중에서 확장자가 jpg인 것들만 필터링한다.
file_list = [file for file in file_list if file.endswith('.jpg')]

# 전체화면을 보여주기위한 설정
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cnt = len(file_list)
idx = 0

while True:
    img = cv2.imread('.\\images\\' + file_list[idx], cv2.IMREAD_COLOR)
    if img is None:
        print('Image load failed!')
        break
    cv2.imshow('image', img)
    # 키보드로 부터 아무키나 누르면 종료
    if cv2.waitKey(1000) > 0:
        break
    idx += 1
    if idx == cnt:
        idx = 0

cv2.destroyAllWindows()