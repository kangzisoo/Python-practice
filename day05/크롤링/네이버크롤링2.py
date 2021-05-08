#import bs4
from bs4 import BeautifulSoup  #계속 다운받기 싫어서 위에서 from으로 불러줌
#bs4.BeautifulSoup #부품을 정식 용어로 class
from urllib import request

#네이버 금융 - 국내증시

name = '삼성전자'

con = request.urlopen('https://finance.naver.com/item/main.nhn?code=005930') #연결부품획득
print('1. 연결 성공', con)

doc = BeautifulSoup(con, 'html.parser')    # 이 페이지는 html로 분석해야한다는 것을 알려줌
# print('2.받은 것을 프린트 >> ', doc)
# doc안에는 naver.com의 첫 페이지인 index.html 파일의 소스가 통째로 들어있음
span_code = doc.select('span.code')  #검색의 결과를 리스트!!
# print(a_nav)
print('code의 개수>> ',len(span_code))
print(span_code[0])  # a태그 부가적인 정보도 포함
print(span_code[0].text)  # 텍스트만 추출

code = span_code[0].text  #나중에 쓰기위해 변수에 넣어둔다!
print('code: ', code)

div_today = doc.select('div.today')  #검색의 결과를 리스트!!
# print(a_nav)
print('today의 개수>> ',len(div_today))
#print(div_today[0])  # 리스트의 첫번째 것만 추출
today1 = div_today[0].select('span.blind')  #첫번째 안에서 특정 정보만 추출 (이것도 리스트)
print(today1)
print(today1[0])  # 특정 정보 span.blind 에서도 첫번째 것만 추출
print(today1[0].text)  # 텍스트만

print()
span_blind = doc.select('span.blind')
print(len(span_blind))

for i in range(len(span_blind)):
    print(i,':',span_blind[i].text)


# 전일 고가 시가 저가
# yesterday, high, start, low
# 15 16 19 20
print()
yesterday = span_blind[15].text
high = span_blind[16].text
start = span_blind[19].text
low = span_blind[20].text

print('전일:',yesterday)
print('고가:',high)
print('시가:',start)
print('저가:',low)

all = doc.select('div.today span.blind')  # 바로 아래 있을때 공백으로 가능
print(len(all))
print(all)

file = open(name + '.txt', 'w')   # open() 파일을 만드는 함수
file.write(code + '\n')
file.write(yesterday + '\n')
file.write(high + '\n')
file.write(start + '\n')
file.write(low + '\n')
file.close()