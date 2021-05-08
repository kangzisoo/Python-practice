#import bs4
from bs4 import BeautifulSoup  #계속 다운받기 싫어서 위에서 from으로 불러줌
#bs4.BeautifulSoup #부품을 정식 용어로 class
from urllib import request

con = request.urlopen('http://www.naver.com') #연결부품획득
print('1. 연결 성공', con)

doc = BeautifulSoup(con, 'html.parser')    # 이 페이지는 html로 분석해야한다는 것을 알려줌
# print('2.받은 것을 프린트 >> ', doc)
#doc안에는 naver.com의 첫 페이지인 index.html 파일의 소스가 통째로 들어있음
a_nav = doc.select('a.nav')  #검색의 결과를 리스트!!
# print(a_nav)
print(len(a_nav))
print(a_nav[0])  # a태그 부가적인 정보도 포함
print(a_nav[0].text)  # 텍스트만 추출

print(a_nav[7:10])
print(a_nav[7].text)
print(a_nav[8].text)
print(a_nav[9].text)