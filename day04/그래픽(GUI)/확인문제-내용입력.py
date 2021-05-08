from tkinter import *
from tkinter.messagebox import *

def writing():
    showinfo('내용 확인', '입력되었습니다!')
    # 입력한 값 가지고 와서, 동일한지 체크!
    get_num = num_entry.get()
    get_title = title_entry.get()
    get_content = content_entry.get()
    get_name = name_entry.get()
    print('입력하신 번호는', get_num )
    print('입력하신 제목은', get_title )
    print('입력하신 내용은', get_content )
    print('작성자는', get_name )

w = Tk()
w.geometry("500x250")

num = Label(w, text='번호', font('궁서',30))
num.pack()




id_label.pack()
id_text.pack()
pw_label.pack()
pw_text.pack()
button.pack()
button2.pack()
w.mainloop()