import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from HonorsProject import GenerateMatches
from HonorsProject import Match_perfect
from HonorsProject import change_text

app=QApplication(sys.argv)
matches=GenerateMatches()
class MTVSim(QMainWindow):
    def __init__(self, perfect_matches=[], no_matches=[], weeks=1):
        super().__init__()

        if len(perfect_matches)==16:
            self.setFixedSize(500, 500)
            new_w=QWidget(self)
            self.setCentralWidget(new_w)
            layout=QVBoxLayout()
            new_w.setLayout(layout)
            new_text=QLabel()
            new_text.setText("All matches found!")
            layout.addWidget(new_text)

        else:
            self.setWindowTitle("Choose a couple")
            self.setFixedSize(500, 500)
            self.generalLayout = QVBoxLayout()
            self._centralWidget=QWidget(self)
            self.setCentralWidget(self._centralWidget)
            self._centralWidget.setLayout(self.generalLayout)
            self.perfect_matches=perfect_matches
            self.no_matches=no_matches
            self.matches=GenerateMatches(self.perfect_matches, self.no_matches)
            self.weeks=weeks
            self._choose_couple()


    def _choose_couple(self):
        self.choices={}
        layout=QGridLayout()
        choices=dict()
        buttons=[]

        for i in range(4):
            for j in range(4):
                buttons.append((i, j))

        for i in range(len(self.matches)):

            choices['{}'.format(self.matches[i])]=buttons[i]

        for btnText, pos in choices.items():
            button=QPushButton(btnText)
            self.choices[btnText] = button
            self.choices[btnText].setFixedSize(60, 60)
            self.choices[btnText].setText(btnText)
            layout.addWidget(self.choices[btnText], pos[0], pos[1])

        self.generalLayout.addLayout(layout)
        week_count=QLabel()
        week_count.setText("Week: {}".format(self.weeks))
        week_count.move(100, 400)
        layout.addWidget(week_count)
        correct_matches=0
        for item in self.matches:
            if Match_perfect(item, matches):
                correct_matches+=1
        num_matches=QLabel()
        num_matches.setText("Perfect Matches: {}".format(correct_matches))
        num_matches.move(400, 400)
        layout.addWidget(num_matches)

        buttons_2=[]
        for txt in self.choices.keys():
            buttons_2.append(self.choices[txt])

        if len(buttons_2)>=1:
            button1=buttons_2[0]
            button1.clicked.connect(lambda: self.open_second_screen((change_text(button1.text())[0], change_text(button1.text())[1]), self.perfect_matches, self.no_matches))

        if len(buttons_2)>=2:
            button2=buttons_2[1]
            button2.clicked.connect(lambda: self.open_second_screen((change_text(button2.text())[0], change_text(button2.text())[1]), self.perfect_matches, self.no_matches))

        if len(buttons_2)>=3:
            button3=buttons_2[2]
            button3.clicked.connect(lambda: self.open_second_screen((change_text(button3.text())[0], change_text(button3.text())[1]), self.perfect_matches, self.no_matches))

        if len(buttons_2)>=4:
            button4=buttons_2[3]
            button4.clicked.connect(lambda: self.open_second_screen((change_text(button4.text())[0], change_text(button4.text())[1]), self.perfect_matches, self.no_matches))

        if len(buttons_2)>=5:
            button5=buttons_2[4]
            button5.clicked.connect(lambda: self.open_second_screen((change_text(button5.text())[0], change_text(button5.text())[1]), self.perfect_matches, self.no_matches))

        if len(buttons_2)>=6:
            button6=buttons_2[5]
            button6.clicked.connect(lambda: self.open_second_screen((change_text(button6.text())[0], change_text(button6.text())[1]), self.perfect_matches, self.no_matches))

        if len(buttons_2)>=7:
            button7=buttons_2[6]
            button7.clicked.connect(lambda: self.open_second_screen((change_text(button7.text())[0], change_text(button7.text())[1]), self.perfect_matches, self.no_matches))

        if len(buttons_2)>=8:
            button8=buttons_2[7]
            button8.clicked.connect(lambda: self.open_second_screen((change_text(button8.text())[0], change_text(button8.text())[1]), self.perfect_matches, self.no_matches))

    def open_second_screen(self, match, pm, nm):
        self.second_window = SecondWindow(match, pm, nm, self.weeks)
        self.second_window.show()

class SecondWindow(QWidget):
    def __init__(self, match, pm, nm, counter=1):
        super().__init__()
        self.counter=counter
        self.match=match
        self.pm=pm
        self.nm=nm
        self.setFixedSize(500, 500)
        layout=QVBoxLayout()
        self.setLayout(layout)
        new_2=QWidget()
        self.new_txt=QLabel()
        self.new_txt.setAlignment(Qt.AlignCenter)
        if Match_perfect(self.match, matches):
            self.new_txt.setText("Couple is a match!")
        else:
            self.new_txt.setText("Couple is not a match!")
        self.new_txt.setFixedSize(200, 200)
        layout.addWidget(self.new_txt)
        continue_b=QPushButton()
        continue_b.setText("Continue")
        continue_b.clicked.connect(lambda: self.open_og_screen())
        layout.addWidget(continue_b)

    
    def open_og_screen(self):
        if Match_perfect(self.match, matches):
            self.pm.append(self.match[0])
            self.pm.append(self.match[1])
            self.counter+=1
            self.new_screen=MTVSim(self.pm, self.nm, self.counter)
            self.new_screen.show()

        else:
            no_match=[]
            no_match.append(self.match[0])
            no_match.append(self.match[1])
            self.nm.append(no_match)
            self.counter+=1
            self.new_screen=MTVSim(self.pm, self.nm, self.counter)
            self.new_screen.show()

def main():
    sim=QApplication(sys.argv)
    view=MTVSim()
    view.show()
    sys.exit(sim.exec_())

if __name__ == '__main__':
    main()
    