food = ['아이스크림','아메리카노','딸기'] #목록(list), 목차(index)
##food라는 목록을 생성하고, 아이스크림 아메리카노 딸기 세개의 값을 할당해라
print(food[0]) #food라는 목록의 index 0번 값을 출력해라
print(food[1]) #food라는 목록의 index 1번 값을 출력해라
print(food[2]) #food라는 목록의 index 2번 값을 출력해라

print('<for문_ver1>')
for i in range(0,3): #inedx(i)가 0~2까지 !!! range로 하는 경우 인덱스 있음
## i가 0부터 3미만까지 (0~2) 아래 for문을 반복하라
    print(food[i],end=' ') #end는 기본값이 enter ##food라는 목록의 index i번 값을 출력하고 한칸 띄어쓰기
    ##i=0, 1, 2까지 3번 반복하므로 아이스크림 아메리카노 딸기 출력됨
print() #한줄 공백을 위함
print('<for문_ver2>')
for i in range(0,len(food)): #inedx(i)가 0~2까지
## i가 0부터 food의 길이 미만까지 for문을 반복하라
    print(food[i],end=' ') #end는 기본값이 enter
    ## food라는 목록의 index i값을 출력하고 한칸 띄어쓰기. (기본 end는 줄바꾸기이나, end를 ' '로 지정)
print() #한줄 공백을 위함
print('<for문_ver3>')
for x in food:  #for-each !!! 인덱스 없음
## food라는 목록 내 값 만큼 아래 for문을 반복하라
    print(x,end=' ') #food라는 목록의 값을 프린트하라
print()
print('목록의 개수는 ', len(food)) #food라는 목록의 길이 : 3 (아이스크림 아메리카노 딸기)

print('<to do list>')
########오늘 끝나고 할 일 5가지를 목록으로 만들어, 두 가지 방식으로 출력
todo = ['복습하기', '선물사기', '운동하기', '저녁먹기', '스피치연습'] ##todo라는 list를 만들고 값 5개 넣음
#1
for i in range(0,5): #i=0 부터 5 미만까지 아래 for문을 반복하라
    print(todo[i], end=' ') #todo라는 목록의 index i값을 출력하고 한칸띄어 마무리하라
    ## 5번 반복되므로 todo 안에 맨 앞부터 5개 값 출력
print() #한줄 공백

#2
for y in todo: #todo라는 목록 안의 값 갯수만큼 for문을 반복해라
    print(y,end=' ') #food안의 값을 출력하고 한칸 띄어 마무리 ## 5개만큼 반복
print() #한줄 공백
#3
for i in range(0,len(todo)): #i=0부터 todo라는 목록의 길이 미만만큼 for문을 반복해라
    print(todo[i],end=' ') #todo라는 목록의 index i를 출력하고 한칸 띄어 마무리 ## i= 0~4 로 5번 반복

