from tkinter import *  #tkinter모듈 안에 있는 모든 것들을 쓰겠다.

w = Tk()

w.title("Nado GUI")
w.geometry("640x640") #가로 * 세로
#w.resizable(False,False)
#widget

#button
btn1 = Button(w, text = "버튼1")  #버튼을 w에 위치시키고, 텍스트 표시
btn1.pack() #버튼 표시

btn2 = Button(w, padx = 5, pady = 10, text = "버튼22222222222")  #버튼 내 여백 조절 (유동적 크기)
btn2.pack()

btn3 = Button(w, padx = 10, pady = 5, text = "버튼3")
btn3.pack()

btn4 = Button(w, width = 10, height = 3, text = "버튼4")   #고정크기
btn4.pack()

btn5 = Button(w, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="C:/kangjs/python__project/pythonProject/day04/그래픽(GUI)/img_gui1.png")
btn6 = Button(w, image=photo)
btn6.pack()

def btncmd():                      #새로운 함수를 정의해줌
    print("버튼이 클릭되었습니다.")

btn7 = Button(w, text="동작하는 버튼", command=btncmd)
btn7.pack()

#레이블은 그냥 글씨
label1 = Label(w, text = "안녕하세요")
label1.pack()

label2 = Label(w, image=photo)
label2.pack()

def change():
    label1.config(text = "또 만나요.")  #config : 속성을 바꿔줌

btn = Button(w, text="클릭", command=change)
btn.pack()

#entry
txt = Text(w, width = 30, height = 5)
txt.pack()

txt.insert(END,"글자를 입력하세요.")

e = Entry(w, width = 30)  # Emtry 는 줄바꿈 안됨! Text 는 됨!
e.pack()
e.insert(0, "한 줄만 입력 하세요.")

def btncmd2():
    print(txt.get("1.0", END))  # 1번 라인, 0번 컬럼 부터 끝까지
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn8 = Button(w, text = "클릭", command = btncmd2)
btn8.pack()

w.mainloop()  #창이 닫히지 않도록 함