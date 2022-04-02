from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, \
    QRadioButton, QButtonGroup

from random import shuffle, randint




class Question:
    def __init__(self, question, right_answ, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answ = right_answ
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
# questions_list.append(Question('Зимой и летом одним цветом. Что это?', 'Сосна', 'Ель', 'Береза', 'Клен'))
# questions_list.append(Question('Батон разрезали на три части. Сколько сделали разрезов?', '1', '2', '3', '4'))
# questions_list.append(Question('Кто родился раньше?', 'Курица', 'Яйцо', 'Микроб', 'Тиранозавр'))

que = ['Зимой и летом одним цветом. Что это?', 'Батон разрезали на три части. Сколько сделали разрезов?', 'Кто родился раньше?', "Кто я такой?"]
right = ['Ель', '2', 'Яйцо', "Человек"]
wr1 = ['Сосна', '1', 'Курица', "Тирекс"]
wr2 = ['Береза', '3', 'Микроб', "Диана"]
wr3 = ['Клен', '4', 'Тиранозавр', "Максим"]

for i in range(len(que)):
    questions_list.append(Question(que[i], right[i], wr1[i], wr2[i], wr3[i]))

def ask(question, right_answ, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[0].setText(right_answ)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    label_name.setText(question)
    label_answ.setText('Правильный ответ: ' + right_answ)


def check_answer():
    if answers[0].isChecked():
        label_check.setText('Правильно')
    else:
        label_check.setText('Неправильно')

    RadioGroupBox.hide()
    AnswGroupBox.show()
    button.setText('Следующий вопрос')


def show_question():
    x = randint(0, 3)
    ask(que[x], right[x], wr1[x], wr2[x], wr3[x])
    RadioGroup.setExclusive(False)
    r1.setChecked(False)
    r2.setChecked(False)
    r3.setChecked(False)
    r4.setChecked(False)
    RadioGroup.setExclusive(True)
    AnswGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')


def show_choice():
    if button.text() == 'Ответить':
        check_answer()
    else:
        show_question()


app = QApplication([])
main_win = QWidget()

label_name = QLabel()

RadioGroupBox = QGroupBox("Варианты ответа")

r1 = QRadioButton()
r2 = QRadioButton()
r3 = QRadioButton()
r4 = QRadioButton()

answers = [r1, r2, r3, r4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(r1)
RadioGroup.addButton(r2)
RadioGroup.addButton(r3)
RadioGroup.addButton(r4)

button = QPushButton("Ответить")

layoutV1 = QVBoxLayout()
layoutV1.addWidget(r1)
layoutV1.addWidget(r2)

layoutV2 = QVBoxLayout()
layoutV2.addWidget(r3)
layoutV2.addWidget(r4)

layoutH = QHBoxLayout()

layoutH.addLayout(layoutV1)
layoutH.addLayout(layoutV2)

RadioGroupBox.setLayout(layoutH)

AnswGroupBox = QGroupBox("Результат теста")
label_check = QLabel('Правильно/Неправильно')
label_answ = QLabel('Правильный ответ')

layout_new = QVBoxLayout()

layout_new.addWidget(label_check)
layout_new.addWidget(label_answ)

AnswGroupBox.setLayout(layout_new)

layoutV_last = QVBoxLayout()
layoutV_last.addWidget(label_name)
layoutV_last.addWidget(RadioGroupBox)
layoutV_last.addWidget(AnswGroupBox)
layoutV_last.addWidget(button)

AnswGroupBox.hide()


button.clicked.connect(show_choice)


main_win.setLayout(layoutV_last)
main_win.show()
app.exec_()