from tkinter import *
from tkinter import messagebox

# id/pw 를 입력받아, 설정된 id/pw와 일치하는지 비교하여 메세지박스 출력하는 login 함수를 정의
def login():
    id2 = id_entry.get()    #입력받는 함수 get
    print('입력한 ID는 ', id2)
    pw2 = pw_entry.get()
    print('입력한 PW는 ', pw2)

    if id2 == 'root' and pw2 == '1234':
        messagebox.showinfo('로그인성공', '환영합니다.')  # 메세지박스의 제목 . 내용
        print('>> 로그인 성공')
    else:
        messagebox.showinfo('로그인실패', '다시 시도하세요.')
        print('>> 로그인 실패')



w = Tk()
w.title("로그인 화면 입니다.")       #창의 제목
w.geometry("500x250")  #가로 * 세로

id = Label(w, text="ID입력", font=('궁서, 30'))  # ID 레이블 (그냥 글씨)
id.pack()

id_entry = Entry(w, font=('궁서, 30'), bg='blue', fg='white')  # ID 입력받음, 줄바꿈 못함
id_entry.pack()

pw = Label(w, text="PW입력", font=('궁서, 30'))
pw.pack()

pw_entry = Entry(w, font=('궁서, 30'), bg='blue', fg='white')    # PW 입력받음, 줄바꿈 못함
pw_entry.pack()


# 버튼 생성 & 버튼 클릭했을때 처리(command)할 함수
b = Button(w, text="로그인",
           font=('궁서, 30'),
           bg='yellow',
           command=login     #로그인 함수 위에서 정의
           )
b.pack()

w.mainloop()  #창이 닫히지 않도록 함