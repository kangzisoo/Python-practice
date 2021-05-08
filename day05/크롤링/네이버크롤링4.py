#import bs4
from bs4 import BeautifulSoup  #계속 다운받기 싫어서 위에서 from으로 불러줌
#bs4.BeautifulSoup #부품을 정식 용어로 class
from urllib import request

name = '챔피언 Top5'

con = request.urlopen('https://www.op.gg/champion/statistics') #연결부품획득
print('1. 연결 성공', con)

doc = BeautifulSoup(con, 'html.parser')    # 이 페이지는 html로 분석해야한다는 것을 알려줌

span_Value = doc.select('div.champion-index-table__name')  #검색의 결과를 리스트!!
print('챔피언의 수>> ',len(span_Value))

for i in range(0,5):
    print('챔피언',i+1,span_Value[i].text)  # 텍스트만 추출


file = open(name + '.txt', 'w')   # open() 파일을 만드는 함수

for i in range(0,5):
    file.write('전체 '+ str(i+1) + '위 ' + span_Value[i].text + '\n')
    # write 이하는 문장으로 취급한다. , 사용 불가!

file.close()


