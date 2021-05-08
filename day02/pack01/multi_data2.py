hobby = []  #[]비워두는 경우가 실생활에 더 많음
hobby.append('코딩') #hobby 안에 '코딩'이라는 값을 넣어라
print('개수>> ', len(hobby)) #hobby의 길이를 출력하라 (hobby안의 값의 갯수)

hobby.append('등산') #hobby 안에 '등산'이라는 값을 넣어라
print('개수>> ', len(hobby)) #hobby의 길이를 출력하라 (코딩, 등산 두개)
#for문으로 추가하기
for _ in range(3): #아래 for문을 3번 반복하라
    data = input('당신의 새로운 취미는 >> ') #data라는 변수에 값을 입력하라
    hobby.append(data) #hobby라는 목록(공간)에 data변수에 입력된 값을 넣어라
    #위 두 줄을 세번 반복함

print('개수>> ', len(hobby))
#hobby라는 목록의 길이를 출력하라(data를 세번 넣어줬기때문에 값 3개, 길이=3)

for x in hobby: #hobby라는 목록의 값을 모두 출력해라.
    print(x)