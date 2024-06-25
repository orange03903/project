import tkinter
import tkinter.font
import random

window = tkinter.Tk()
window.title('국기 맞추기 퀴즈')
window.geometry('1000x700')

Start_font = tkinter.font.Font(family='한컴 말랑말랑 Bold', size=50)
Start_font2 = tkinter.font.Font(family='한컴 말랑말랑 Bold', size=15)
Quiz_font = tkinter.font.Font(family='한컴 말랑말랑 Bold', size=30)

start_frame = tkinter.Frame(window, width=1000, height=700)
quiz_frame = tkinter.Frame(window, width=1000, height=700)

for frame in (start_frame, quiz_frame):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

Start_img = tkinter.PhotoImage(file='시작.png')
bg = tkinter.PhotoImage(file="배경화면.png")
bg2 = tkinter.PhotoImage(file='퀴즈프레임.png')
next_img = tkinter.PhotoImage(file='next.png')

label1 = tkinter.Label(start_frame, image=bg)
label1.place(x=0, y=0)
Start = tkinter.Button(start_frame, image=Start_img, command=lambda: start_game(), bd=0)
nation_quiz = tkinter.Label(start_frame, text='나라 맞추기 퀴즈', font=Start_font, background='white', bd=2, relief='solid')
nation_quiz.place(x=250, y=100)
Start.place(x=350, y=450)

backg2 = tkinter.Label(quiz_frame, image=bg2)
backg2.place(x=0, y=0)
quiz_label = tkinter.Label(quiz_frame, text='이 나라의 이름은?', font=Quiz_font, background='#c7b2e4')
quiz_label.place(x=350, y=50)

flags = [
    {'image': tkinter.PhotoImage(file='union.png'), 'answer': '영국', 'hint': '이 나라는 아직도 왕이 존재합니다'},
    {'image': tkinter.PhotoImage(file='미국.png'), 'answer': '미국', 'hint': '이 나라는 가장 강합니다.'},
    {'image': tkinter.PhotoImage(file='프랑스.png'), 'answer': '프랑스', 'hint': '이 나라의 수도는 파리입니다.'},
    {'image': tkinter.PhotoImage(file='바티칸.png'), 'answer': '바티칸시국', 'hint': '이탈리아 안에 있는 가장 작은 나라임과 동시에 교황이 있습니다.'},
    {'image': tkinter.PhotoImage(file='독일.png'), 'answer': '독일', 'hint': '이 나라는 가장 끔찍한 전쟁을 일으킨 적 있습니다.'},
    {'image': tkinter.PhotoImage(file='벨기에.png'), 'answer': '벨기에', 'hint': '이 나라는 독일과 비슷하게 생겼습니다.'},
    {'image': tkinter.PhotoImage(file='터키.png'), 'answer': '튀르키예', 'hint': '이 나라의 이름은 터키가 아닙니다.'},
    {'image': tkinter.PhotoImage(file='대한민국.png'), 'answer': '대한민국', 'hint': '이 나라의 수도는 서울입니다.'},
    {'image': tkinter.PhotoImage(file='일본.png'), 'answer': '일본', 'hint': '이 나라는 냥코가 지배중입니다.'},
    {'image': tkinter.PhotoImage(file='이집트.png'), 'answer': '이집트', 'hint': '이 나라는 수에즈 운하를 가지고있습니다.'},
    {'image': tkinter.PhotoImage(file='스위스.png'), 'answer': '스위스', 'hint': '이 나라는 알프스 산맥이 있습니다.'},
]

random.shuffle(flags)

wrong_messages = [
    "이걸 모른다고?",
    "중등 교육 절차를 밟으신 게 맞습니까?",
    "IQ 20?",
    "아쉽네요(이 문제 특: 우리 집 햄스터도 맞춤)",
    "ㅋㅋ 나가라 넌"
]

current_index = 0
total_questions = len(flags)

def update_question_count():
    count_label.config(text=f'{current_index + 1} / {total_questions}')

def show_next_question():
    global current_index
    current_index = (current_index + 1) % total_questions
    flag_img.config(image=flags[current_index]['image'])
    answer_entry.delete(0, tkinter.END)
    hint_label.config(text='')
    update_question_count()

def check_answer(event=None):
    user_answer = answer_entry.get().strip()
    correct_answer = flags[current_index]['answer']
    if user_answer == correct_answer or (correct_answer == '바티칸시국' and user_answer in ['바티칸시국', '바티칸 시국']) or (correct_answer == '대한민국' and user_answer in ['대한민국', '대한 민국']):
        result_label.config(text="정답입니다!", fg='green')
        if current_index == total_questions - 1:
            congrats_label.config(text="축하합니다! 모든 문제를 맞추셨습니다!", fg='green')
            show_frame(start_frame)
        else:
            show_next_question()
    else:
        wrong_message = random.choice(wrong_messages)
        result_label.config(text=wrong_message, fg='red')

def start_game():
    global current_index
    current_index = 0
    random.shuffle(flags)
    flag_img.config(image=flags[current_index]['image'])
    answer_entry.delete(0, tkinter.END)
    result_label.config(text='')
    hint_label.config(text='')
    congrats_label.config(text='')
    update_question_count()
    show_frame(quiz_frame)

def show_hint():
    hint_label.config(text=flags[current_index]['hint'])

flag_img = tkinter.Label(quiz_frame)
flag_img.place(x=350, y=150)
flag_img.config(image=flags[current_index]['image'])

answer_entry = tkinter.Entry(quiz_frame, font=Quiz_font, width=20)
answer_entry.place(x=250, y=400)
answer_entry.bind('<Return>', check_answer)

next_button = tkinter.Button(quiz_frame, image=next_img, command=check_answer, bd=0)
result_label = tkinter.Label(quiz_frame, text='', font=Quiz_font, background='#c7b2e4')
result_label.place(x=300, y=500)
next_button.place(x=750, y=400)

hint_button = tkinter.Button(quiz_frame, text='힌트', font=Start_font2, command=show_hint, bd=0, bg='#c7b2e4', fg='black')
hint_label = tkinter.Label(quiz_frame, text='', font=Start_font2, background='#c7b2e4', fg='blue')
hint_label.place(x=300, y=600)
hint_button.place(x=500, y=350)

congrats_label = tkinter.Label(start_frame, text='', font=Start_font, background='white', fg='blue')
congrats_label.place(relx=0.5, rely=0.5, anchor='center')

home_button = tkinter.Button(quiz_frame, text='메인 화면으로 돌아가기', font=Start_font2, command=lambda: show_frame(start_frame), bd=0, bg='purple', fg='white')
home_button.place(x=20, y=20)
count_label = tkinter.Label(quiz_frame, text=f'1 / {total_questions}', font=Start_font2, background='#c7b2e4', fg='black')
count_label.place(x=850, y=20)

show_frame(start_frame)

window.mainloop()
