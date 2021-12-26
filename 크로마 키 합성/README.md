# 크로마 키 합성

---

## 크로마 키(Chroma Key) 합성이란?
* 녹색 또는 파란색 배경에서 촬영한 영상에 다른 배경 영상을 합성하는 기술

![image](https://user-images.githubusercontent.com/64933820/147403447-8c3e514e-70ba-4aa7-af94-f30b345cbf1e.png)

---

## 구현 할 기능
* 녹색 스크린 영역 추출하기
* 녹색 영역에 다른 배경 영상을 합성하여 저장하기
* 스페이스바를 이용하여 크로마 키 합성 동작 제어하기

---

## 녹색 스크린 영역 추출하기
* 크로마 키 영상을 HSV 색공간으로 변환
* cv2.inRange() 함수를 사용하여 50 <= H <= 80, 150 <= S <= 255, 0 <= V <= 255 범위의 영역을 검출

![image](https://user-images.githubusercontent.com/64933820/147403548-1469982c-1002-4478-9b1a-4ddb3e09ffff.png)

---

## 녹색 영역에 다른 배경 영상을 함성하기
* 마스크 연산을 지원하는 cv2.copyTo() 함수 사용

![image](https://user-images.githubusercontent.com/64933820/147403591-b50c4498-f05e-48c0-825f-5894d49353f2.png)

---

## 웹캠 영상에서 body 영역 추출하기
* 웹캠 영상을 HSV 색 공간으로 변환
* cv2.inRange() 함수를 사용하여 0 <= H <= 179, 0 <= S <= 88, 0 <= V <= 255 범위의 영역을 검출

![화면 캡처 2021-12-26 221357](https://user-images.githubusercontent.com/64933820/147409553-e06f7aae-17d2-4d9e-881d-207addc0247e.png)

---

## raining.mp4 영상에 body 영역을 합성하기
* 마스크 연산을 지원하는 cv2.copyTo() 함수 사용

![image](https://user-images.githubusercontent.com/64933820/147409640-08190d82-d198-43d5-a2be-78871bfacf0c.png)
