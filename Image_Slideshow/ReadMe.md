# 이미지 슬라이드쇼

---

* 이미지 슬라이드쇼
  * 특정 폴더에 있는 모든 이미지 파일을 이용하여 슬라이드쇼를 수행

* 구현 할 기능
  * 특정 폴더에 있는 이미지 파일 목록 읽기
  * 이미지를 전체 화면으로 출력하기
  * 일정 시간동안 이미지를 화면에 출력하고, 다음 이미지로 교체하기(무한루프)

---

* 특정 폴더에 있는 이미지 파일(*.jpg)목록 읽기
  * os.listdir()

  ![os](https://user-images.githubusercontent.com/64933820/146668558-182758f5-eb22-42a4-85dc-fb063e617179.png)
  
  * glob.glob()
  
  ![glob](https://user-images.githubusercontent.com/64933820/146668587-96370c92-3098-48a6-9df6-36957a483d84.png)

* 전체 화면 영상 출력 창 만들기
  * 먼저 cv2.WINDOW_NORMAL 속성의 창을 만든 후, cv2.setWindowProperty() 함수를 사용하여 전체 화면 속성으로 변경

  ![fullscreen](https://user-images.githubusercontent.com/64933820/146668613-4cb079dc-5fa3-4518-9e42-cec4add158bd.png)
