### 실무 프로젝트 : 파이썬 영상 처리 프로그램 작성


import cv2

# 영상 소스 열기
src1=cv2.imread('/Users/junpyooh/images/111.jpg')

### 영상 처리 알고리즘을 구현###


dst1 = cv2.cvtColor(src1,cv2.COLOR_BGR2GRAY)



# 영상 디스플레이

cv2.imshow('src1',src1)

cv2.imshow('dst1', dst1)



# 마무리
cv2.waitKey(0)
cv2.destroyAllWindows()
