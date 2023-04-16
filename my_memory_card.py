from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, 
QGroupBox, QPushButton, QRadioButton, QLabel, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский','Русский','Испанский','Бразильский'))
question_list.append(Question('Какого цвета нет на флаге России', 'Жёлтый','Белый','Синий','Красный'))
question_list.append(Question('Национальная хижина якутов', 'Ураса','Иглу','Хата','Юрта'))

app = QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox('Варианты ответа:')

rbtn1 = QRadioButton('1')
rbtn2 = QRadioButton('2')
rbtn3 = QRadioButton('3')
rbtn4 = QRadioButton('4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Резльтат теста')
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Ответ будет тут')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)

layout_l1 = QHBoxLayout()
layout_l2 = QHBoxLayout()
layout_l3 = QHBoxLayout()

layout_l1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_l2.addWidget(RadioGroupBox)
layout_l2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_l3.addStretch(1)
layout_l3.addWidget(btn_OK, stretch=2)
layout_l3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_l1,stretch=2)
layout_card.addLayout(layout_l2,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_l3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Обосраться')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

answer = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q: Question):
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    shuffle(answer)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct('ок')
        window.score += 1
        print('Статистика\nВсего вопросов', window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Лох')
            print('Рейтинг: ', (window.score/window.total*100), '%')

def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов', window.total, '\n-Правильных ответов:', window.score)
    car_question = randint(0, len(question_list)-1)
    q = question_list[car_question]
    ask(q)


def click_OK():
    if btn_OK.text == 'Обосраться':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo card')
window.car_question = -1
btn_OK.clicked.connect(click_OK)

window.score = 0
window.total = 0
next_question()
window.resize(500,500)
window.show()
app.exec()