# -*- coding: utf-8 -*-
"""파이썬제어문.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YUa9xajkbPMbyeFqUlr5sMgCvT-hWP0P
"""

food = input('먹고싶은 음식을 입력하세요 >> ')
print('당신이 먹고싶은 음식은 ',food,'이다')
if food == "짜장면":
  print('우산을 들고 간다.')
  print('중국집으로 간다.')
elif food == "우동":
  print('우동집에서 배달시킨다.')
elif food == "햄버거":
  print('버거킹에서 테이크아웃한다.')
else:        #else 뒤에는 조건을 쓰지 않는다!
  print('직접 요리해서 집에서 먹는다.')

start = 1
while start < 10: #True
  print(start, '> 내가 반복')
  start = start + 1 # cpu가 ram에 있는 start가져와서 계산한 것 (start에 대입해줘야함)

for _ in range(0,10): #0~9 기본값이 1씩 증가!
  print('나도 반복')

time = int(input('현재시각? '))
print('현재시각은 ',time,'시 입니다.')
if time <11:
  print('good morning')
elif time <15:
  print('good afternoon')
elif time<20:
  print('good evening')
else:
  print('good night')

m = int(input('이번 달은? '))
print('이번 달은 ',m,'월 입니다.')
if 3<= m <= 5:
  print('봄!')
elif 6<= m <= 8:
  print('여름!')
elif 9<= m <= 11:
  print('가을!')
else:
  print('겨울!')

