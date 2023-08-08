import sys
import serial
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QMainWindow, QPushButton, QTabWidget, QCalendarWidget, QTextEdit, QWidget, QComboBox, QCheckBox, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor, QFont, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        width = 1024
        height = 600
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        # changing the background color to white
        self.setStyleSheet("background-color: rgb(204, 230, 255);")

    def initUI(self):
        self.label1 = QLabel(self)
        self.pixmap = QPixmap('Logo.png')
        
        #newpixmap = pixmap.scaled(400, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Set the image on the label
        self.label1.setPixmap(self.pixmap)

        #resize the label
        self.label1.resize(self.pixmap.width(),
                          self.pixmap.height())

        self.label1.move(160,100)
        #self.label1.setFont(QFont('Times', 20))

        self.button1 = QPushButton("NEW USER", self)
        self.button1.move(285, 250)
        self.button1.resize(400, 75)
        self.button1.setFont(QFont('Times', 20))
        self.button1.clicked.connect(self.openNewUserWindow)
        self.button1.setStyleSheet("background-color: rgb(240, 240, 240); color: black;")
        #self.button1.setStyleSheet("border: 1px solid black;")

        self.button2 = QPushButton("LOGIN", self)
        self.button2.move(285, 405)
        self.button2.resize(400, 75)
        self.button2.setFont(QFont('Times', 20))
        self.button2.clicked.connect(self.openLoginWindow)
        self.button2.setStyleSheet("background-color: rgb(240, 240, 240); color: black;")
        #self.button2.setStyleSheet("border: 1px solid black;")

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Main Window")
        self.show()

    def openNewUserWindow(self):
        self.close()
        self.window1 = NewUserWindow()
        self.window1.show()

    def openLoginWindow(self):
        self.close()
        self.window2 = LoginWindow()
        self.window2.show()


class NewUserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        width = 1024
        height = 600
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        # changing the background color to white
        self.setStyleSheet("background-color: rgb(204, 230, 255);")

    def initUI(self):
        self.label1 = QLabel("CREATE YOUR USERNAME: ",self)
        self.label1.move(300,50)
        self.label1.setFont(QFont('Times', 20))

        self.line_edit1 = QLineEdit(self)
        self.line_edit1.move(300,100)
        self.line_edit1.resize(400, 75)
        self.line_edit1.setFont(QFont('Times', 20))
        self.line_edit1.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label2 = QLabel("CREATE YOUR PASSWORD: ",self)
        self.label2.move(300,200)
        self.label2.setFont(QFont('Times', 20))

        self.line_edit2 = QLineEdit(self)
        self.line_edit2.move(300,250)
        self.line_edit2.resize(400, 75)
        self.line_edit2.setFont(QFont('Times', 20))
        self.line_edit2.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        #self.label3 = QLabel("CREATE YOUR DISPENSING PIN: ",self)
        #self.label3.move(265,350)
        #self.label3.setFont(QFont('Times', 20))

        #self.line_edit3 = QLineEdit(self)
        #self.line_edit3.move(300,400)
        #self.line_edit3.resize(400, 75)
        #self.line_edit3.setFont(QFont('Times', 20))
        #self.line_edit3.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.button4 = QPushButton("DONE",self)
        self.button4.clicked.connect(self.openAddMedsWindow_CH1)
        self.button4.move(300, 500)
        self.button4.resize(400, 50)
        self.button4.setFont(QFont('Times', 20))
        self.button4.setStyleSheet("background-color: rgb(240, 240, 240); color: black;")
        self.show()
        self.setWindowTitle("New User")

    def openAddMedsWindow_CH1(self):
        self.close()
        username = self.line_edit1.text()
        with open("username.txt", "w") as f:
            f.write(username)

        password = self.line_edit2.text()
        with open("password.txt", "w") as f:
            f.write(password)

        #pin = self.line_edit3.text()
        #with open("pin.txt", "w") as f:
        #    f.write(pin)
        self.window4 = AddMedsWindow_CH1()
        self.window4.show()


class AddMedsWindow_CH1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        width = 1024
        height = 600
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        #self.ser = serial.Serial('COM5', 9600)

        # changing the background color to white
        self.setStyleSheet("background-color: rgb(204, 230, 255);")

    def initUI(self):
        self.label = QLabel("ENTER MEDICATION DETAILS ",self)
        self.label.move(325,25)
        self.label.setFont(QFont('Times', 20))

        self.label1 = QLabel("MEDICATION NAME: ",self)
        self.label1.move(25,100)
        self.label1.setFont(QFont('Times', 20))

        self.line_edit1 = QLineEdit(self)
        self.line_edit1.move(340,85)
        self.line_edit1.resize(200, 75)
        self.line_edit1.setFont(QFont('Times', 20))
        self.line_edit1.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label2 = QLabel("DOCTOR/PHARMACY: ",self)
        self.label2.move(25,190)
        self.label2.setFont(QFont('Times', 20))

        self.line_edit2 = QLineEdit(self)
        self.line_edit2.move(340,175)
        self.line_edit2.resize(200, 75)
        self.line_edit2.setFont(QFont('Times', 20))
        self.line_edit2.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label3 = QLabel("DOSAGE: ",self)
        self.label3.move(560,100)
        self.label3.setFont(QFont('Times', 20))

        self.line_edit3 = QLineEdit(self)
        self.line_edit3.move(730,85)
        self.line_edit3.resize(200, 75)
        self.line_edit3.setFont(QFont('Times', 20))
        self.line_edit3.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label4 = QLabel("QUANTITY: ",self)
        self.label4.move(560,190)
        self.label4.setFont(QFont('Times', 20))

        self.line_edit4 = QLineEdit(self)
        self.line_edit4.move(730,175)
        self.line_edit4.resize(200, 75)
        self.line_edit4.setFont(QFont('Times', 20))
        self.line_edit4.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label5 = QLabel("MORNING TIME: ",self)
        self.label5.move(50,400)
        self.label5.setFont(QFont('Times', 20))

        self.line_edit5 = QLineEdit(self)
        self.line_edit5.move(50,440)
        self.line_edit5.resize(200, 75)
        self.line_edit5.setFont(QFont('Times', 20))
        self.line_edit5.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb1 = QComboBox(self)
        self.cb1.addItem('AM')
        self.cb1.move(170,440)
        self.cb1.resize(100, 75)
        self.cb1.setFont(QFont('Times', 20))
        self.mflag = '0'
        self.cb1.activated[str].connect(self.set_mflag)

        self.label6 = QLabel("AFTERNOON TIME: ",self)
        self.label6.move(390,400)
        self.label6.setFont(QFont('Times', 20))

        self.line_edit6 = QLineEdit(self)
        self.line_edit6.move(390,440)
        self.line_edit6.resize(200, 75)
        self.line_edit6.setFont(QFont('Times', 20))
        self.line_edit6.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb2 = QComboBox(self)
        self.cb2.addItem('AM')
        self.cb2.addItem('PM')
        self.cb2.move(510,440)
        self.cb2.resize(100, 75)
        self.cb2.setFont(QFont('Times', 20))
        self.aflag = '0'
        self.cb2.activated[str].connect(self.set_aflag)

        self.label7 = QLabel("EVENING TIME: ",self)
        self.label7.move(750,400)
        self.label7.setFont(QFont('Times', 20))

        self.line_edit7 = QLineEdit(self)
        self.line_edit7.move(750,440)
        self.line_edit7.resize(200, 75)
        self.line_edit7.setFont(QFont('Times', 20))
        self.line_edit7.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb3 = QComboBox(self)
        self.cb3.addItem('PM')
        self.cb3.move(870,440)
        self.cb3.resize(100, 75)
        self.cb3.setFont(QFont('Times', 20))

        self.label8 = QLabel("SELECT DAYS ON WHICH YOU TAKE THIS MEDICATION", self)
        self.label8.move(115, 255)
        self.label8.setFont(QFont('Times', 20))

        self.monday = QCheckBox("MON", self)
        self.monday.move(205, 300)
        self.monday.setFont(QFont('Times', 20))
        self.mon = '0'
        self.monday.stateChanged.connect(self.checkedmon)

        self.tuesday = QCheckBox("TUES", self)
        self.tuesday.move(345, 300)
        self.tuesday.setFont(QFont('Times', 20))
        self.tues = '0'
        self.tuesday.stateChanged.connect(self.checkedtues)

        self.wednesday = QCheckBox("WED", self)
        self.wednesday.move(485, 300)
        self.wednesday.setFont(QFont('Times', 20))
        self.wed = '0'
        self.wednesday.stateChanged.connect(self.checkedwed)

        self.thursday = QCheckBox("THURS", self)
        self.thursday.move(625, 300)
        self.thursday.setFont(QFont('Times', 20))
        self.thur = '0'
        self.thursday.stateChanged.connect(self.checkedthur)

        self.friday = QCheckBox("FRI", self)
        self.friday.move(290, 335)
        self.friday.setFont(QFont('Times', 20))
        self.fri = '0'
        self.friday.stateChanged.connect(self.checkedfri)

        self.saturday = QCheckBox("SAT", self)
        self.saturday.move(420, 335)
        self.saturday.setFont(QFont('Times', 20))
        self.sat = '0'
        self.saturday.stateChanged.connect(self.checkedsat)

        self.sunday = QCheckBox("SUN", self)
        self.sunday.move(550, 335)
        self.sunday.setFont(QFont('Times', 20))
        self.sun = '0'
        self.sunday.stateChanged.connect(self.checkedsun)

        self.button3 = QPushButton("DONE",self)
        self.button3.clicked.connect(self.openHomeWindow)
        self.button3.move(775, 525)
        self.button3.resize(225, 50)
        self.button3.setFont(QFont('Times', 20))
        self.button3.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")

        self.button4 = QPushButton("ADD NEW CHAMBER",self)
        self.button4.clicked.connect(self.openAddMedsWindow_CH2)
        self.button4.move(410, 525)
        self.button4.resize(325, 50)
        self.button4.setFont(QFont('Times', 20))
        self.button4.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")

        self.button5 = QPushButton("SAVE INFORMATION",self)
        self.button5.clicked.connect(self.send_data)
        self.button5.move(50, 525)
        self.button5.resize(325, 50)
        self.button5.setFont(QFont('Times', 20))
        self.button5.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")
        self.show()
        self.setWindowTitle("CHAMBER 1")

    def set_mflag(self, text): self.mflag = '0'

    def set_aflag(self, text):
        self.temp2 = self.line_edit6.text()
        self.aflag = '0'
        if text == 'AM':
            self.aflag = '0'
            self.temp2 = self.line_edit6.text()
        if text == 'PM':
            self.temp = self.line_edit6.text()
            self.temp1 = int(self.temp)
            self.temp1 = self.temp1 + 12
            self.temp2 = str(self.temp1)
            self.aflag = '1'

    def set_eflag(self, text): self.eflag = '1'

    def checkedmon(self, state):
        if state == QtCore.Qt.Checked:
            self.mon = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("monmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.mon = '0'

    def checkedtues(self, state):
        if state == QtCore.Qt.Checked:
            self.tues = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("tuesmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.tues = '0'

    def checkedwed(self, state):
        if state == QtCore.Qt.Checked:
            self.wed = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("wedmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.wed = '0'

    def checkedthur(self, state):
        if state == QtCore.Qt.Checked:
            self.thur = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("thurmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.thur = '0'

    def checkedfri(self, state):
        if state == QtCore.Qt.Checked:
            self.fri = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("frimedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.fri = '0'

    def checkedsat(self, state):
        if state == QtCore.Qt.Checked:
            self.sat = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("satmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.sat = '0'

    def checkedsun(self, state):
        if state == QtCore.Qt.Checked:
            self.sun = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("sunmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.sun = '0'

    def send_data(self):
        medname1 = self.line_edit1.text()
        with open("medname1.txt", "w") as f:
            f.write(medname1)
        
        docph1 = self.line_edit2.text()
        with open("docph1.txt", "w") as f:
            f.write(docph1)

        dos1 = self.line_edit3.text()
        with open("dos1.txt", "w") as f:
            f.write(dos1)

        quan1 = self.line_edit4.text()
        with open("quan1.txt", "w") as f:
            f.write(quan1)
        
        self.dosage = self.line_edit3.text()
        self.quantity = self.line_edit4.text()
        self.mtime = self.line_edit5.text()
        if self.aflag == '0':
            self.atime = self.line_edit6.text()
        else:
            self.atime = self.temp2
        self.etime = self.line_edit7.text()
        text = '1' + ',' + self.dosage + ',' + self.quantity + ',' + self.mtime  + ',' + self.atime +  ',' + self.etime + ',' + self.mon + ',' + self.tues + ',' + self.wed + ',' + self.thur + ',' + self.fri + ',' + self.sat + ',' + self.sun
        #self.ser.write(text.encode())
        print(text)
        #line = self.ser.readline().decode()
        #print(line)
        #time.sleep(1)
        #self.ser.close()

    def openAddMedsWindow_CH2(self):
        self.close()
        self.window5 = AddMedsWindow_CH2()
        self.window5.show()

    def openHomeWindow(self):
        self.close()
        self.window3 = HomeWindow()
        self.window3.show()


class AddMedsWindow_CH2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        width = 1024
        height = 600
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        #self.ser = serial.Serial('COM5', 9600)

        # changing the background color to white
        self.setStyleSheet("background-color: rgb(204, 230, 255);")

    def initUI(self):
        self.label = QLabel("ENTER MEDICATION DETAILS ",self)
        self.label.move(325,25)
        self.label.setFont(QFont('Times', 20))

        self.label1 = QLabel("MEDICATION NAME: ",self)
        self.label1.move(25,100)
        self.label1.setFont(QFont('Times', 20))

        self.line_edit1 = QLineEdit(self)
        self.line_edit1.move(340,85)
        self.line_edit1.resize(200, 75)
        self.line_edit1.setFont(QFont('Times', 20))
        self.line_edit1.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label2 = QLabel("DOCTOR/PHARMACY: ",self)
        self.label2.move(25,190)
        self.label2.setFont(QFont('Times', 20))

        self.line_edit2 = QLineEdit(self)
        self.line_edit2.move(340,175)
        self.line_edit2.resize(200, 75)
        self.line_edit2.setFont(QFont('Times', 20))
        self.line_edit2.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label3 = QLabel("DOSAGE: ",self)
        self.label3.move(560,100)
        self.label3.setFont(QFont('Times', 20))

        self.line_edit3 = QLineEdit(self)
        self.line_edit3.move(730,85)
        self.line_edit3.resize(200, 75)
        self.line_edit3.setFont(QFont('Times', 20))
        self.line_edit3.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label4 = QLabel("QUANTITY: ",self)
        self.label4.move(560,190)
        self.label4.setFont(QFont('Times', 20))

        self.line_edit4 = QLineEdit(self)
        self.line_edit4.move(730,175)
        self.line_edit4.resize(200, 75)
        self.line_edit4.setFont(QFont('Times', 20))
        self.line_edit4.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label5 = QLabel("MORNING TIME: ",self)
        self.label5.move(50,400)
        self.label5.setFont(QFont('Times', 20))

        self.line_edit5 = QLineEdit(self)
        self.line_edit5.move(50,440)
        self.line_edit5.resize(200, 75)
        self.line_edit5.setFont(QFont('Times', 20))
        self.line_edit5.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb1 = QComboBox(self)
        self.cb1.addItem('AM')
        self.cb1.move(170,440)
        self.cb1.resize(100, 75)
        self.cb1.setFont(QFont('Times', 20))
        self.mflag = '0'
        self.cb1.activated[str].connect(self.set_mflag)

        self.label6 = QLabel("AFTERNOON TIME: ",self)
        self.label6.move(390,400)
        self.label6.setFont(QFont('Times', 20))

        self.line_edit6 = QLineEdit(self)
        self.line_edit6.move(390,440)
        self.line_edit6.resize(200, 75)
        self.line_edit6.setFont(QFont('Times', 20))
        self.line_edit6.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb2 = QComboBox(self)
        self.cb2.addItem('AM')
        self.cb2.addItem('PM')
        self.cb2.move(510,440)
        self.cb2.resize(100, 75)
        self.cb2.setFont(QFont('Times', 20))
        self.aflag = '0'
        self.cb2.activated[str].connect(self.set_aflag)

        self.label7 = QLabel("EVENING TIME: ",self)
        self.label7.move(750,400)
        self.label7.setFont(QFont('Times', 20))

        self.line_edit7 = QLineEdit(self)
        self.line_edit7.move(750,440)
        self.line_edit7.resize(200, 75)
        self.line_edit7.setFont(QFont('Times', 20))
        self.line_edit7.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb3 = QComboBox(self)
        self.cb3.addItem('PM')
        self.cb3.move(870,440)
        self.cb3.resize(100, 75)
        self.cb3.setFont(QFont('Times', 20))

        self.label8 = QLabel("SELECT DAYS ON WHICH YOU TAKE THIS MEDICATION", self)
        self.label8.move(115, 255)
        self.label8.setFont(QFont('Times', 20))

        self.monday = QCheckBox("MON", self)
        self.monday.move(205, 300)
        self.monday.setFont(QFont('Times', 20))
        self.mon = '0'
        self.monday.stateChanged.connect(self.checkedmon)

        self.tuesday = QCheckBox("TUES", self)
        self.tuesday.move(345, 300)
        self.tuesday.setFont(QFont('Times', 20))
        self.tues = '0'
        self.tuesday.stateChanged.connect(self.checkedtues)

        self.wednesday = QCheckBox("WED", self)
        self.wednesday.move(485, 300)
        self.wednesday.setFont(QFont('Times', 20))
        self.wed = '0'
        self.wednesday.stateChanged.connect(self.checkedwed)

        self.thursday = QCheckBox("THURS", self)
        self.thursday.move(625, 300)
        self.thursday.setFont(QFont('Times', 20))
        self.thur = '0'
        self.thursday.stateChanged.connect(self.checkedthur)

        self.friday = QCheckBox("FRI", self)
        self.friday.move(290, 335)
        self.friday.setFont(QFont('Times', 20))
        self.fri = '0'
        self.friday.stateChanged.connect(self.checkedfri)

        self.saturday = QCheckBox("SAT", self)
        self.saturday.move(420, 335)
        self.saturday.setFont(QFont('Times', 20))
        self.sat = '0'
        self.saturday.stateChanged.connect(self.checkedsat)

        self.sunday = QCheckBox("SUN", self)
        self.sunday.move(550, 335)
        self.sunday.setFont(QFont('Times', 20))
        self.sun = '0'
        self.sunday.stateChanged.connect(self.checkedsun)

        self.button3 = QPushButton("DONE",self)
        self.button3.clicked.connect(self.openHomeWindow)
        self.button3.move(775, 525)
        self.button3.resize(225, 50)
        self.button3.setFont(QFont('Times', 20))
        self.button3.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")

        self.button4 = QPushButton("ADD NEW CHAMBER",self)
        self.button4.clicked.connect(self.openAddMedsWindow_CH3)
        self.button4.move(410, 525)
        self.button4.resize(325, 50)
        self.button4.setFont(QFont('Times', 20))
        self.button4.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")

        self.button5 = QPushButton("SAVE INFORMATION",self)
        self.button5.clicked.connect(self.send_data)
        self.button5.move(50, 525)
        self.button5.resize(325, 50)
        self.button5.setFont(QFont('Times', 20))
        self.button5.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")
        self.show()
        self.setWindowTitle("CHAMBER 2")

    def set_mflag(self, text): self.mflag = '0'

    def set_aflag(self, text):
        self.temp2 = self.line_edit6.text()
        self.aflag = '0'
        if text == 'AM':
            self.aflag = '0'
            self.temp2 = self.line_edit6.text()
        if text == 'PM':
            self.temp = self.line_edit6.text()
            self.temp1 = int(self.temp)
            self.temp1 = self.temp1 + 12
            self.temp2 = str(self.temp1)
            self.aflag = '1'

    def set_eflag(self, text): self.eflag = '1'

    def checkedmon(self, state):
        if state == QtCore.Qt.Checked:
            self.mon = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("monmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.mon = '0'

    def checkedtues(self, state):
        if state == QtCore.Qt.Checked:
            self.tues = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("tuesmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.tues = '0'

    def checkedwed(self, state):
        if state == QtCore.Qt.Checked:
            self.wed = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("wedmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.wed = '0'

    def checkedthur(self, state):
        if state == QtCore.Qt.Checked:
            self.thur = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("thurmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.thur = '0'

    def checkedfri(self, state):
        if state == QtCore.Qt.Checked:
            self.fri = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("frimedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.fri = '0'

    def checkedsat(self, state):
        if state == QtCore.Qt.Checked:
            self.sat = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("satmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.sat = '0'

    def checkedsun(self, state):
        if state == QtCore.Qt.Checked:
            self.sun = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("sunmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.sun = '0'

    def send_data(self):
        medname2 = self.line_edit1.text()
        with open("medname2.txt", "w") as f:
            f.write(medname2)
        
        docph2 = self.line_edit2.text()
        with open("docph2.txt", "w") as f:
            f.write(docph2)

        dos2 = self.line_edit3.text()
        with open("dos2.txt", "w") as f:
            f.write(dos2)

        quan2 = self.line_edit4.text()
        with open("quan2.txt", "w") as f:
            f.write(quan2)
        
        self.dosage = self.line_edit3.text()
        self.quantity = self.line_edit4.text()
        self.mtime = self.line_edit5.text()
        if self.aflag == '0':
            self.atime = self.line_edit6.text()
        else:
            self.atime = self.temp2
        self.etime = self.line_edit7.text()
        text = '2' + ',' + self.dosage + ',' + self.quantity + ',' + self.mtime  + ',' + self.atime +  ',' + self.etime + ',' + self.mon + ',' + self.tues + ',' + self.wed + ',' + self.thur + ',' + self.fri + ',' + self.sat + ',' + self.sun + ','
        #self.ser.write(text.encode('utf-8'))
        print(text)
        #line = self.ser.readline().decode('utf-8').rstrip()
        #print(line)
        #self.ser.close()

    def openAddMedsWindow_CH3(self):
        self.close()
        self.window6 = AddMedsWindow_CH3()
        self.window6.show()

    def openHomeWindow(self):
        self.close()
        self.window3 = HomeWindow()
        self.window3.show()


class AddMedsWindow_CH3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        width = 1024
        height = 600
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        #self.ser = serial.Serial("COM", 9600)

        # changing the background color to white
        self.setStyleSheet("background-color: rgb(204, 230, 255);")

    def initUI(self):
        self.label = QLabel("ENTER MEDICATION DETAILS ",self)
        self.label.move(325,25)
        self.label.setFont(QFont('Times', 20))

        self.label1 = QLabel("MEDICATION NAME: ",self)
        self.label1.move(25,100)
        self.label1.setFont(QFont('Times', 20))

        self.line_edit1 = QLineEdit(self)
        self.line_edit1.move(340,85)
        self.line_edit1.resize(200, 75)
        self.line_edit1.setFont(QFont('Times', 20))
        self.line_edit1.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label2 = QLabel("DOCTOR/PHARMACY: ",self)
        self.label2.move(25,190)
        self.label2.setFont(QFont('Times', 20))

        self.line_edit2 = QLineEdit(self)
        self.line_edit2.move(340,175)
        self.line_edit2.resize(200, 75)
        self.line_edit2.setFont(QFont('Times', 20))
        self.line_edit2.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label3 = QLabel("DOSAGE: ",self)
        self.label3.move(560,100)
        self.label3.setFont(QFont('Times', 20))

        self.line_edit3 = QLineEdit(self)
        self.line_edit3.move(730,85)
        self.line_edit3.resize(200, 75)
        self.line_edit3.setFont(QFont('Times', 20))
        self.line_edit3.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label4 = QLabel("QUANTITY: ",self)
        self.label4.move(560,190)
        self.label4.setFont(QFont('Times', 20))

        self.line_edit4 = QLineEdit(self)
        self.line_edit4.move(730,175)
        self.line_edit4.resize(200, 75)
        self.line_edit4.setFont(QFont('Times', 20))
        self.line_edit4.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label5 = QLabel("MORNING TIME: ",self)
        self.label5.move(50,400)
        self.label5.setFont(QFont('Times', 20))

        self.line_edit5 = QLineEdit(self)
        self.line_edit5.move(50,440)
        self.line_edit5.resize(200, 75)
        self.line_edit5.setFont(QFont('Times', 20))
        self.line_edit5.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb1 = QComboBox(self)
        self.cb1.addItem('AM')
        self.cb1.move(170,440)
        self.cb1.resize(100, 75)
        self.cb1.setFont(QFont('Times', 20))
        self.mflag = '0'
        self.cb1.activated[str].connect(self.set_mflag)

        self.label6 = QLabel("AFTERNOON TIME: ",self)
        self.label6.move(390,400)
        self.label6.setFont(QFont('Times', 20))

        self.line_edit6 = QLineEdit(self)
        self.line_edit6.move(390,440)
        self.line_edit6.resize(200, 75)
        self.line_edit6.setFont(QFont('Times', 20))
        self.line_edit6.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb2 = QComboBox(self)
        self.cb2.addItem('AM')
        self.cb2.addItem('PM')
        self.cb2.move(510,440)
        self.cb2.resize(100, 75)
        self.cb2.setFont(QFont('Times', 20))
        self.aflag = '0'
        self.cb2.activated[str].connect(self.set_aflag)

        self.label7 = QLabel("EVENING TIME: ",self)
        self.label7.move(750,400)
        self.label7.setFont(QFont('Times', 20))

        self.line_edit7 = QLineEdit(self)
        self.line_edit7.move(750,440)
        self.line_edit7.resize(200, 75)
        self.line_edit7.setFont(QFont('Times', 20))
        self.line_edit7.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb3 = QComboBox(self)
        self.cb3.addItem('PM')
        self.cb3.move(870,440)
        self.cb3.resize(100, 75)
        self.cb3.setFont(QFont('Times', 20))

        self.label8 = QLabel("SELECT DAYS ON WHICH YOU TAKE THIS MEDICATION", self)
        self.label8.move(115, 255)
        self.label8.setFont(QFont('Times', 20))

        self.monday = QCheckBox("MON", self)
        self.monday.move(205, 300)
        self.monday.setFont(QFont('Times', 20))
        self.mon = '0'
        self.monday.stateChanged.connect(self.checkedmon)

        self.tuesday = QCheckBox("TUES", self)
        self.tuesday.move(345, 300)
        self.tuesday.setFont(QFont('Times', 20))
        self.tues = '0'
        self.tuesday.stateChanged.connect(self.checkedtues)

        self.wednesday = QCheckBox("WED", self)
        self.wednesday.move(485, 300)
        self.wednesday.setFont(QFont('Times', 20))
        self.wed = '0'
        self.wednesday.stateChanged.connect(self.checkedwed)

        self.thursday = QCheckBox("THURS", self)
        self.thursday.move(625, 300)
        self.thursday.setFont(QFont('Times', 20))
        self.thur = '0'
        self.thursday.stateChanged.connect(self.checkedthur)

        self.friday = QCheckBox("FRI", self)
        self.friday.move(290, 335)
        self.friday.setFont(QFont('Times', 20))
        self.fri = '0'
        self.friday.stateChanged.connect(self.checkedfri)

        self.saturday = QCheckBox("SAT", self)
        self.saturday.move(420, 335)
        self.saturday.setFont(QFont('Times', 20))
        self.sat = '0'
        self.saturday.stateChanged.connect(self.checkedsat)

        self.sunday = QCheckBox("SUN", self)
        self.sunday.move(550, 335)
        self.sunday.setFont(QFont('Times', 20))
        self.sun = '0'
        self.sunday.stateChanged.connect(self.checkedsun)

        self.button3 = QPushButton("DONE",self)
        self.button3.clicked.connect(self.openHomeWindow)
        self.button3.move(775, 525)
        self.button3.resize(225, 50)
        self.button3.setFont(QFont('Times', 20))
        self.button3.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")

        self.button4 = QPushButton("ADD NEW CHAMBER",self)
        self.button4.clicked.connect(self.openAddMedsWindow_CH4)
        self.button4.move(410, 525)
        self.button4.resize(325, 50)
        self.button4.setFont(QFont('Times', 20))
        self.button4.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")

        self.button5 = QPushButton("SAVE INFORMATION",self)
        self.button5.clicked.connect(self.send_data)
        self.button5.move(50, 525)
        self.button5.resize(325, 50)
        self.button5.setFont(QFont('Times', 20))
        self.button5.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")
        self.show()
        self.setWindowTitle("CHAMBER 3")

    def set_mflag(self, text): self.mflag = '0'

    def set_aflag(self, text):
        self.temp2 = self.line_edit6.text()
        self.aflag = '0'
        if text == 'AM':
            self.aflag = '0'
            self.temp2 = self.line_edit6.text()
        if text == 'PM':
            self.temp = self.line_edit6.text()
            self.temp1 = int(self.temp)
            self.temp1 = self.temp1 + 12
            self.temp2 = str(self.temp1)
            self.aflag = '1'

    def set_eflag(self, text): self.eflag = '1'

    def checkedmon(self, state):
        if state == QtCore.Qt.Checked:
            self.mon = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("monmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.mon = '0'

    def checkedtues(self, state):
        if state == QtCore.Qt.Checked:
            self.tues = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("tuesmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.tues = '0'

    def checkedwed(self, state):
        if state == QtCore.Qt.Checked:
            self.wed = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("wedmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.wed = '0'

    def checkedthur(self, state):
        if state == QtCore.Qt.Checked:
            self.thur = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("thurmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.thur = '0'

    def checkedfri(self, state):
        if state == QtCore.Qt.Checked:
            self.fri = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("frimedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.fri = '0'

    def checkedsat(self, state):
        if state == QtCore.Qt.Checked:
            self.sat = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("satmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.sat = '0'

    def checkedsun(self, state):
        if state == QtCore.Qt.Checked:
            self.sun = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("sunmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.sun = '0'

    def send_data(self):
        medname3 = self.line_edit1.text()
        with open("medname3.txt", "w") as f:
            f.write(medname3)
        
        docph3 = self.line_edit2.text()
        with open("docph3.txt", "w") as f:
            f.write(docph3)

        dos3 = self.line_edit3.text()
        with open("dos3.txt", "w") as f:
            f.write(dos3)

        quan3 = self.line_edit4.text()
        with open("quan3.txt", "w") as f:
            f.write(quan3)
        
        self.dosage = self.line_edit3.text()
        self.quantity = self.line_edit4.text()
        self.mtime = self.line_edit5.text()
        if self.aflag == '0':
            self.atime = self.line_edit6.text()
        else:
            self.atime = self.temp2
        self.etime = self.line_edit7.text()
        text = '3' + ',' + self.dosage + ',' + self.quantity + ',' + self.mtime  + ',' + self.atime +  ',' + self.etime + ',' + self.mon + ',' + self.tues + ',' + self.wed + ',' + self.thur + ',' + self.fri + ',' + self.sat + ',' + self.sun
        #self.ser.write(text.encode())
        print(text)
        #line = self.ser.readline().decode()
        #print(line)
        #time.sleep(1)
        #self.ser.close()

    def openAddMedsWindow_CH4(self):
        self.close()
        self.window7 = AddMedsWindow_CH4()
        self.window7.show()

    def openHomeWindow(self):
        self.close()
        self.window3 = HomeWindow()
        self.window3.show()


class AddMedsWindow_CH4(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        width = 1024
        height = 600
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        #self.ser = serial.Serial("COM", 9600)

        # changing the background color to white
        self.setStyleSheet("background-color: rgb(204, 230, 255);")

    def initUI(self):
        self.label = QLabel("ENTER MEDICATION DETAILS ",self)
        self.label.move(325,25)
        self.label.setFont(QFont('Times', 20))

        self.label1 = QLabel("MEDICATION NAME: ",self)
        self.label1.move(25,100)
        self.label1.setFont(QFont('Times', 20))

        self.line_edit1 = QLineEdit(self)
        self.line_edit1.move(340,85)
        self.line_edit1.resize(200, 75)
        self.line_edit1.setFont(QFont('Times', 20))
        self.line_edit1.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label2 = QLabel("DOCTOR/PHARMACY: ",self)
        self.label2.move(25,190)
        self.label2.setFont(QFont('Times', 20))

        self.line_edit2 = QLineEdit(self)
        self.line_edit2.move(340,175)
        self.line_edit2.resize(200, 75)
        self.line_edit2.setFont(QFont('Times', 20))
        self.line_edit2.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label3 = QLabel("DOSAGE: ",self)
        self.label3.move(560,100)
        self.label3.setFont(QFont('Times', 20))

        self.line_edit3 = QLineEdit(self)
        self.line_edit3.move(730,85)
        self.line_edit3.resize(200, 75)
        self.line_edit3.setFont(QFont('Times', 20))
        self.line_edit3.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label4 = QLabel("QUANTITY: ",self)
        self.label4.move(560,190)
        self.label4.setFont(QFont('Times', 20))

        self.line_edit4 = QLineEdit(self)
        self.line_edit4.move(730,175)
        self.line_edit4.resize(200, 75)
        self.line_edit4.setFont(QFont('Times', 20))
        self.line_edit4.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label5 = QLabel("MORNING TIME: ",self)
        self.label5.move(50,400)
        self.label5.setFont(QFont('Times', 20))

        self.line_edit5 = QLineEdit(self)
        self.line_edit5.move(50,440)
        self.line_edit5.resize(200, 75)
        self.line_edit5.setFont(QFont('Times', 20))
        self.line_edit5.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb1 = QComboBox(self)
        self.cb1.addItem('AM')
        self.cb1.move(170,440)
        self.cb1.resize(100, 75)
        self.cb1.setFont(QFont('Times', 20))
        self.mflag = '0'
        self.cb1.activated[str].connect(self.set_mflag)

        self.label6 = QLabel("AFTERNOON TIME: ",self)
        self.label6.move(390,400)
        self.label6.setFont(QFont('Times', 20))

        self.line_edit6 = QLineEdit(self)
        self.line_edit6.move(390,440)
        self.line_edit6.resize(200, 75)
        self.line_edit6.setFont(QFont('Times', 20))
        self.line_edit6.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb2 = QComboBox(self)
        self.cb2.addItem('AM')
        self.cb2.addItem('PM')
        self.cb2.move(510,440)
        self.cb2.resize(100, 75)
        self.cb2.setFont(QFont('Times', 20))
        self.aflag = '0'
        self.cb2.activated[str].connect(self.set_aflag)

        self.label7 = QLabel("EVENING TIME: ",self)
        self.label7.move(750,400)
        self.label7.setFont(QFont('Times', 20))

        self.line_edit7 = QLineEdit(self)
        self.line_edit7.move(750,440)
        self.line_edit7.resize(200, 75)
        self.line_edit7.setFont(QFont('Times', 20))
        self.line_edit7.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb3 = QComboBox(self)
        self.cb3.addItem('PM')
        self.cb3.move(870,440)
        self.cb3.resize(100, 75)
        self.cb3.setFont(QFont('Times', 20))

        self.label8 = QLabel("SELECT DAYS ON WHICH YOU TAKE THIS MEDICATION", self)
        self.label8.move(115, 255)
        self.label8.setFont(QFont('Times', 20))

        self.monday = QCheckBox("MON", self)
        self.monday.move(205, 300)
        self.monday.setFont(QFont('Times', 20))
        self.mon = '0'
        self.monday.stateChanged.connect(self.checkedmon)

        self.tuesday = QCheckBox("TUES", self)
        self.tuesday.move(345, 300)
        self.tuesday.setFont(QFont('Times', 20))
        self.tues = '0'
        self.tuesday.stateChanged.connect(self.checkedtues)

        self.wednesday = QCheckBox("WED", self)
        self.wednesday.move(485, 300)
        self.wednesday.setFont(QFont('Times', 20))
        self.wed = '0'
        self.wednesday.stateChanged.connect(self.checkedwed)

        self.thursday = QCheckBox("THURS", self)
        self.thursday.move(625, 300)
        self.thursday.setFont(QFont('Times', 20))
        self.thur = '0'
        self.thursday.stateChanged.connect(self.checkedthur)

        self.friday = QCheckBox("FRI", self)
        self.friday.move(290, 335)
        self.friday.setFont(QFont('Times', 20))
        self.fri = '0'
        self.friday.stateChanged.connect(self.checkedfri)

        self.saturday = QCheckBox("SAT", self)
        self.saturday.move(420, 335)
        self.saturday.setFont(QFont('Times', 20))
        self.sat = '0'
        self.saturday.stateChanged.connect(self.checkedsat)

        self.sunday = QCheckBox("SUN", self)
        self.sunday.move(550, 335)
        self.sunday.setFont(QFont('Times', 20))
        self.sun = '0'
        self.sunday.stateChanged.connect(self.checkedsun)

        self.button3 = QPushButton("DONE",self)
        self.button3.clicked.connect(self.openHomeWindow)
        self.button3.move(775, 525)
        self.button3.resize(225, 50)
        self.button3.setFont(QFont('Times', 20))
        self.button3.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")

        self.button4 = QPushButton("ADD NEW CHAMBER",self)
        self.button4.clicked.connect(self.openAddMedsWindow_CH5)
        self.button4.move(410, 525)
        self.button4.resize(325, 50)
        self.button4.setFont(QFont('Times', 20))
        self.button4.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")

        self.button5 = QPushButton("SAVE INFORMATION",self)
        self.button5.clicked.connect(self.send_data)
        self.button5.move(50, 525)
        self.button5.resize(325, 50)
        self.button5.setFont(QFont('Times', 20))
        self.button5.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")
        self.show()
        self.setWindowTitle("CHAMBER 4")

    def set_mflag(self, text): self.mflag = '0'

    def set_aflag(self, text):
        self.temp2 = self.line_edit6.text()
        self.aflag = '0'
        if text == 'AM':
            self.aflag = '0'
            self.temp2 = self.line_edit6.text()
        if text == 'PM':
            self.temp = self.line_edit6.text()
            self.temp1 = int(self.temp)
            self.temp1 = self.temp1 + 12
            self.temp2 = str(self.temp1)
            self.aflag = '1'

    def set_eflag(self, text): self.eflag = '1'

    def checkedmon(self, state):
        if state == QtCore.Qt.Checked:
            self.mon = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("monmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.mon = '0'

    def checkedtues(self, state):
        if state == QtCore.Qt.Checked:
            self.tues = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("tuesmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.tues = '0'

    def checkedwed(self, state):
        if state == QtCore.Qt.Checked:
            self.wed = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("wedmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.wed = '0'

    def checkedthur(self, state):
        if state == QtCore.Qt.Checked:
            self.thur = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("thurmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.thur = '0'

    def checkedfri(self, state):
        if state == QtCore.Qt.Checked:
            self.fri = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("frimedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.fri = '0'

    def checkedsat(self, state):
        if state == QtCore.Qt.Checked:
            self.sat = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("satmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.sat = '0'

    def checkedsun(self, state):
        if state == QtCore.Qt.Checked:
            self.sun = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("sunmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.sun = '0'

    def send_data(self):
        medname4 = self.line_edit1.text()
        with open("medname4.txt", "w") as f:
            f.write(medname4)
        
        docph4 = self.line_edit2.text()
        with open("docph4.txt", "w") as f:
            f.write(docph4)

        dos4 = self.line_edit3.text()
        with open("dos4.txt", "w") as f:
            f.write(dos4)

        quan4 = self.line_edit4.text()
        with open("quan4.txt", "w") as f:
            f.write(quan4)
        
        self.dosage = self.line_edit3.text()
        self.quantity = self.line_edit4.text()
        self.mtime = self.line_edit5.text()
        if self.aflag == '0':
            self.atime = self.line_edit6.text()
        else:
            self.atime = self.temp2
        self.etime = self.line_edit7.text()
        text = '4' + ',' + self.dosage + ',' + self.quantity + ',' + self.mtime  + ',' + self.atime +  ',' + self.etime + ',' + self.mon + ',' + self.tues + ',' + self.wed + ',' + self.thur + ',' + self.fri + ',' + self.sat + ',' + self.sun
        #self.ser.write(text.encode())
        print(text)
        #line = self.ser.readline().decode()
        #print(line)
        #time.sleep(1)
        #self.ser.close()

    def openAddMedsWindow_CH5(self):
        self.close()
        self.window8 = AddMedsWindow_CH5()
        self.window8.show()

    def openHomeWindow(self):
        self.close()
        self.window3 = HomeWindow()
        self.window3.show()


class AddMedsWindow_CH5(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        width = 1024
        height = 600
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        #self.ser = serial.Serial("COM", 9600)

        # changing the background color to white
        self.setStyleSheet("background-color: rgb(204, 230, 255);")

    def initUI(self):
        self.label = QLabel("ENTER MEDICATION DETAILS ",self)
        self.label.move(325,25)
        self.label.setFont(QFont('Times', 20))

        self.label1 = QLabel("MEDICATION NAME: ",self)
        self.label1.move(25,100)
        self.label1.setFont(QFont('Times', 20))

        self.line_edit1 = QLineEdit(self)
        self.line_edit1.move(340,85)
        self.line_edit1.resize(200, 75)
        self.line_edit1.setFont(QFont('Times', 20))
        self.line_edit1.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label2 = QLabel("DOCTOR/PHARMACY: ",self)
        self.label2.move(25,190)
        self.label2.setFont(QFont('Times', 20))

        self.line_edit2 = QLineEdit(self)
        self.line_edit2.move(340,175)
        self.line_edit2.resize(200, 75)
        self.line_edit2.setFont(QFont('Times', 20))
        self.line_edit2.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label3 = QLabel("DOSAGE: ",self)
        self.label3.move(560,100)
        self.label3.setFont(QFont('Times', 20))

        self.line_edit3 = QLineEdit(self)
        self.line_edit3.move(730,85)
        self.line_edit3.resize(200, 75)
        self.line_edit3.setFont(QFont('Times', 20))
        self.line_edit3.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label4 = QLabel("QUANTITY: ",self)
        self.label4.move(560,190)
        self.label4.setFont(QFont('Times', 20))

        self.line_edit4 = QLineEdit(self)
        self.line_edit4.move(730,175)
        self.line_edit4.resize(200, 75)
        self.line_edit4.setFont(QFont('Times', 20))
        self.line_edit4.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label5 = QLabel("MORNING TIME: ",self)
        self.label5.move(50,400)
        self.label5.setFont(QFont('Times', 20))

        self.line_edit5 = QLineEdit(self)
        self.line_edit5.move(50,440)
        self.line_edit5.resize(200, 75)
        self.line_edit5.setFont(QFont('Times', 20))
        self.line_edit5.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb1 = QComboBox(self)
        self.cb1.addItem('AM')
        self.cb1.move(170,440)
        self.cb1.resize(100, 75)
        self.cb1.setFont(QFont('Times', 20))
        self.mflag = '0'
        self.cb1.activated[str].connect(self.set_mflag)

        self.label6 = QLabel("AFTERNOON TIME: ",self)
        self.label6.move(390,400)
        self.label6.setFont(QFont('Times', 20))

        self.line_edit6 = QLineEdit(self)
        self.line_edit6.move(390,440)
        self.line_edit6.resize(200, 75)
        self.line_edit6.setFont(QFont('Times', 20))
        self.line_edit6.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb2 = QComboBox(self)
        self.cb2.addItem('AM')
        self.cb2.addItem('PM')
        self.cb2.move(510,440)
        self.cb2.resize(100, 75)
        self.cb2.setFont(QFont('Times', 20))
        self.aflag = '0'
        self.cb2.activated[str].connect(self.set_aflag)

        self.label7 = QLabel("EVENING TIME: ",self)
        self.label7.move(750,400)
        self.label7.setFont(QFont('Times', 20))

        self.line_edit7 = QLineEdit(self)
        self.line_edit7.move(750,440)
        self.line_edit7.resize(200, 75)
        self.line_edit7.setFont(QFont('Times', 20))
        self.line_edit7.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb3 = QComboBox(self)
        self.cb3.addItem('PM')
        self.cb3.move(870,440)
        self.cb3.resize(100, 75)
        self.cb3.setFont(QFont('Times', 20))

        self.label8 = QLabel("SELECT DAYS ON WHICH YOU TAKE THIS MEDICATION", self)
        self.label8.move(115, 255)
        self.label8.setFont(QFont('Times', 20))

        self.monday = QCheckBox("MON", self)
        self.monday.move(205, 300)
        self.monday.setFont(QFont('Times', 20))
        self.mon = '0'
        self.monday.stateChanged.connect(self.checkedmon)

        self.tuesday = QCheckBox("TUES", self)
        self.tuesday.move(345, 300)
        self.tuesday.setFont(QFont('Times', 20))
        self.tues = '0'
        self.tuesday.stateChanged.connect(self.checkedtues)

        self.wednesday = QCheckBox("WED", self)
        self.wednesday.move(485, 300)
        self.wednesday.setFont(QFont('Times', 20))
        self.wed = '0'
        self.wednesday.stateChanged.connect(self.checkedwed)

        self.thursday = QCheckBox("THURS", self)
        self.thursday.move(625, 300)
        self.thursday.setFont(QFont('Times', 20))
        self.thur = '0'
        self.thursday.stateChanged.connect(self.checkedthur)

        self.friday = QCheckBox("FRI", self)
        self.friday.move(290, 335)
        self.friday.setFont(QFont('Times', 20))
        self.fri = '0'
        self.friday.stateChanged.connect(self.checkedfri)

        self.saturday = QCheckBox("SAT", self)
        self.saturday.move(420, 335)
        self.saturday.setFont(QFont('Times', 20))
        self.sat = '0'
        self.saturday.stateChanged.connect(self.checkedsat)

        self.sunday = QCheckBox("SUN", self)
        self.sunday.move(550, 335)
        self.sunday.setFont(QFont('Times', 20))
        self.sun = '0'
        self.sunday.stateChanged.connect(self.checkedsun)

        self.button3 = QPushButton("DONE",self)
        self.button3.clicked.connect(self.openHomeWindow)
        self.button3.move(775, 525)
        self.button3.resize(225, 50)
        self.button3.setFont(QFont('Times', 20))
        self.button3.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")

        self.button4 = QPushButton("ADD NEW CHAMBER",self)
        self.button4.clicked.connect(self.openAddMedsWindow_CH6)
        self.button4.move(410, 525)
        self.button4.resize(325, 50)
        self.button4.setFont(QFont('Times', 20))
        self.button4.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")

        self.button5 = QPushButton("SAVE INFORMATION",self)
        self.button5.clicked.connect(self.send_data)
        self.button5.move(50, 525)
        self.button5.resize(325, 50)
        self.button5.setFont(QFont('Times', 20))
        self.button5.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")
        self.show()
        self.setWindowTitle("CHAMBER 5")

    def set_mflag(self, text): self.mflag = '0'

    def set_aflag(self, text):
        self.temp2 = self.line_edit6.text()
        self.aflag = '0'
        if text == 'AM':
            self.aflag = '0'
            self.temp2 = self.line_edit6.text()
        if text == 'PM':
            self.temp = self.line_edit6.text()
            self.temp1 = int(self.temp)
            self.temp1 = self.temp1 + 12
            self.temp2 = str(self.temp1)
            self.aflag = '1'

    def set_eflag(self, text): self.eflag = '1'

    def checkedmon(self, state):
        if state == QtCore.Qt.Checked:
            self.mon = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("monmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.mon = '0'

    def checkedtues(self, state):
        if state == QtCore.Qt.Checked:
            self.tues = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("tuesmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.tues = '0'

    def checkedwed(self, state):
        if state == QtCore.Qt.Checked:
            self.wed = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("wedmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.wed = '0'

    def checkedthur(self, state):
        if state == QtCore.Qt.Checked:
            self.thur = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("thurmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.thur = '0'

    def checkedfri(self, state):
        if state == QtCore.Qt.Checked:
            self.fri = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("frimedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.fri = '0'

    def checkedsat(self, state):
        if state == QtCore.Qt.Checked:
            self.sat = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("satmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.sat = '0'

    def checkedsun(self, state):
        if state == QtCore.Qt.Checked:
            self.sun = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("sunmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.sun = '0'

    def send_data(self):
        medname5 = self.line_edit1.text()
        with open("medname5.txt", "w") as f:
            f.write(medname5)
        
        docph5 = self.line_edit2.text()
        with open("docph5.txt", "w") as f:
            f.write(docph5)

        dos5 = self.line_edit3.text()
        with open("dos5.txt", "w") as f:
            f.write(dos5)

        quan5 = self.line_edit4.text()
        with open("quan5.txt", "w") as f:
            f.write(quan5)
        
        self.dosage = self.line_edit3.text()
        self.quantity = self.line_edit4.text()
        self.mtime = self.line_edit5.text()
        if self.aflag == '0':
            self.atime = self.line_edit6.text()
        else:
            self.atime = self.temp2
        self.etime = self.line_edit7.text()
        text = '5' + ',' + self.dosage + ',' + self.quantity + ',' + self.mtime  + ',' + self.atime +  ',' + self.etime + ',' + self.mon + ',' + self.tues + ',' + self.wed + ',' + self.thur + ',' + self.fri + ',' + self.sat + ',' + self.sun
        #self.ser.write(text.encode())
        print(text)
        #line = self.ser.readline().decode()
        #print(line)
        #time.sleep(1)
        #self.ser.close()

    def openAddMedsWindow_CH6(self):
        self.close()
        self.window9 = AddMedsWindow_CH6()
        self.window9.show()

    def openHomeWindow(self):
        self.close()
        self.window3 = HomeWindow()
        self.window3.show()


class AddMedsWindow_CH6(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        width = 1024
        height = 600
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        #self.ser = serial.Serial("COM", 9600)

        # changing the background color to white
        self.setStyleSheet("background-color: rgb(204, 230, 255);")

    def initUI(self):
        self.label = QLabel("ENTER MEDICATION DETAILS ",self)
        self.label.move(325,25)
        self.label.setFont(QFont('Times', 20))

        self.label1 = QLabel("MEDICATION NAME: ",self)
        self.label1.move(25,100)
        self.label1.setFont(QFont('Times', 20))

        self.line_edit1 = QLineEdit(self)
        self.line_edit1.move(340,85)
        self.line_edit1.resize(200, 75)
        self.line_edit1.setFont(QFont('Times', 20))
        self.line_edit1.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label2 = QLabel("DOCTOR/PHARMACY: ",self)
        self.label2.move(25,190)
        self.label2.setFont(QFont('Times', 20))

        self.line_edit2 = QLineEdit(self)
        self.line_edit2.move(340,175)
        self.line_edit2.resize(200, 75)
        self.line_edit2.setFont(QFont('Times', 20))
        self.line_edit2.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label3 = QLabel("DOSAGE: ",self)
        self.label3.move(560,100)
        self.label3.setFont(QFont('Times', 20))

        self.line_edit3 = QLineEdit(self)
        self.line_edit3.move(730,85)
        self.line_edit3.resize(200, 75)
        self.line_edit3.setFont(QFont('Times', 20))
        self.line_edit3.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label4 = QLabel("QUANTITY: ",self)
        self.label4.move(560,190)
        self.label4.setFont(QFont('Times', 20))

        self.line_edit4 = QLineEdit(self)
        self.line_edit4.move(730,175)
        self.line_edit4.resize(200, 75)
        self.line_edit4.setFont(QFont('Times', 20))
        self.line_edit4.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label5 = QLabel("MORNING TIME: ",self)
        self.label5.move(50,400)
        self.label5.setFont(QFont('Times', 20))

        self.line_edit5 = QLineEdit(self)
        self.line_edit5.move(50,440)
        self.line_edit5.resize(200, 75)
        self.line_edit5.setFont(QFont('Times', 20))
        self.line_edit5.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb1 = QComboBox(self)
        self.cb1.addItem('AM')
        self.cb1.move(170,440)
        self.cb1.resize(100, 75)
        self.cb1.setFont(QFont('Times', 20))
        self.mflag = '0'
        self.cb1.activated[str].connect(self.set_mflag)

        self.label6 = QLabel("AFTERNOON TIME: ",self)
        self.label6.move(390,400)
        self.label6.setFont(QFont('Times', 20))

        self.line_edit6 = QLineEdit(self)
        self.line_edit6.move(390,440)
        self.line_edit6.resize(200, 75)
        self.line_edit6.setFont(QFont('Times', 20))
        self.line_edit6.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb2 = QComboBox(self)
        self.cb2.addItem('AM')
        self.cb2.addItem('PM')
        self.cb2.move(510,440)
        self.cb2.resize(100, 75)
        self.cb2.setFont(QFont('Times', 20))
        self.aflag = '0'
        self.cb2.activated[str].connect(self.set_aflag)

        self.label7 = QLabel("EVENING TIME: ",self)
        self.label7.move(750,400)
        self.label7.setFont(QFont('Times', 20))

        self.line_edit7 = QLineEdit(self)
        self.line_edit7.move(750,440)
        self.line_edit7.resize(200, 75)
        self.line_edit7.setFont(QFont('Times', 20))
        self.line_edit7.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.cb3 = QComboBox(self)
        self.cb3.addItem('PM')
        self.cb3.move(870,440)
        self.cb3.resize(100, 75)
        self.cb3.setFont(QFont('Times', 20))

        self.label8 = QLabel("SELECT DAYS ON WHICH YOU TAKE THIS MEDICATION", self)
        self.label8.move(115, 255)
        self.label8.setFont(QFont('Times', 20))

        self.monday = QCheckBox("MON", self)
        self.monday.move(205, 300)
        self.monday.setFont(QFont('Times', 20))
        self.mon = '0'
        self.monday.stateChanged.connect(self.checkedmon)

        self.tuesday = QCheckBox("TUES", self)
        self.tuesday.move(345, 300)
        self.tuesday.setFont(QFont('Times', 20))
        self.tues = '0'
        self.tuesday.stateChanged.connect(self.checkedtues)

        self.wednesday = QCheckBox("WED", self)
        self.wednesday.move(485, 300)
        self.wednesday.setFont(QFont('Times', 20))
        self.wed = '0'
        self.wednesday.stateChanged.connect(self.checkedwed)

        self.thursday = QCheckBox("THURS", self)
        self.thursday.move(625, 300)
        self.thursday.setFont(QFont('Times', 20))
        self.thur = '0'
        self.thursday.stateChanged.connect(self.checkedthur)

        self.friday = QCheckBox("FRI", self)
        self.friday.move(290, 335)
        self.friday.setFont(QFont('Times', 20))
        self.fri = '0'
        self.friday.stateChanged.connect(self.checkedfri)

        self.saturday = QCheckBox("SAT", self)
        self.saturday.move(420, 335)
        self.saturday.setFont(QFont('Times', 20))
        self.sat = '0'
        self.saturday.stateChanged.connect(self.checkedsat)

        self.sunday = QCheckBox("SUN", self)
        self.sunday.move(550, 335)
        self.sunday.setFont(QFont('Times', 20))
        self.sun = '0'
        self.sunday.stateChanged.connect(self.checkedsun)

        self.button3 = QPushButton("DONE",self)
        self.button3.clicked.connect(self.openHomeWindow)
        self.button3.move(775, 525)
        self.button3.resize(225, 50)
        self.button3.setFont(QFont('Times', 20))
        self.button3.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")

        self.button5 = QPushButton("SAVE INFORMATION",self)
        self.button5.clicked.connect(self.send_data)
        self.button5.move(50, 525)
        self.button5.resize(325, 50)
        self.button5.setFont(QFont('Times', 20))
        self.button5.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")
        self.show()
        self.setWindowTitle("CHAMBER 6")

    def set_mflag(self, text): self.mflag = '0'

    def set_aflag(self, text):
        self.temp2 = self.line_edit6.text()
        self.aflag = '0'
        if text == 'AM':
            self.aflag = '0'
            self.temp2 = self.line_edit6.text()
        if text == 'PM':
            self.temp = self.line_edit6.text()
            self.temp1 = int(self.temp)
            self.temp1 = self.temp1 + 12
            self.temp2 = str(self.temp1)
            self.aflag = '1'

    def set_eflag(self, text): self.eflag = '1'

    def checkedmon(self, state):
        if state == QtCore.Qt.Checked:
            self.mon = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("monmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.mon = '0'

    def checkedtues(self, state):
        if state == QtCore.Qt.Checked:
            self.tues = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("tuesmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.tues = '0'

    def checkedwed(self, state):
        if state == QtCore.Qt.Checked:
            self.wed = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("wedmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.wed = '0'

    def checkedthur(self, state):
        if state == QtCore.Qt.Checked:
            self.thur = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("thurmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.thur = '0'

    def checkedfri(self, state):
        if state == QtCore.Qt.Checked:
            self.fri = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("frimedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.fri = '0'

    def checkedsat(self, state):
        if state == QtCore.Qt.Checked:
            self.sat = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("satmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.sat = '0'

    def checkedsun(self, state):
        if state == QtCore.Qt.Checked:
            self.sun = '1'
            self.medname = self.line_edit1.text()
            self.meddoc = self.line_edit2.text()
            self.dosage = self.line_edit3.text()
            self.quantity = self.line_edit4.text()
            self.mtime = self.line_edit5.text()
            self.atime = self.line_edit6.text()
            self.etime = self.line_edit7.text()
            text = "MEDICINE NAME: " + self.medname + "  " + "DOCTOR: " + self.meddoc + "  " + "DOSAGE: " + self.dosage + "  " + "QUANTITY: " + self.quantity + '\n'
            with open("sunmedicine.txt", 'a') as f:
                f.write(text)
        else:
            self.sun = '0'

    def send_data(self):
        medname6 = self.line_edit1.text()
        with open("medname6.txt", "w") as f:
            f.write(medname6)
        
        docph6 = self.line_edit2.text()
        with open("docph6.txt", "w") as f:
            f.write(docph6)

        dos6 = self.line_edit3.text()
        with open("dos6.txt", "w") as f:
            f.write(dos6)

        quan6 = self.line_edit4.text()
        with open("quan6.txt", "w") as f:
            f.write(quan6)
        
        self.dosage = self.line_edit3.text()
        self.quantity = self.line_edit4.text()
        self.mtime = self.line_edit5.text()
        if self.aflag == '0':
            self.atime = self.line_edit6.text()
        else:
            self.atime = self.temp2
        self.etime = self.line_edit7.text()
        text = '6' + ',' + self.dosage + ',' + self.quantity + ',' + self.mtime  + ',' + self.atime +  ',' + self.etime + ',' + self.mon + ',' + self.tues + ',' + self.wed + ',' + self.thur + ',' + self.fri + ',' + self.sat + ',' + self.sun
        #self.ser.write(text.encode())
        print(text)
        #line = self.ser.readline().decode()
        #print(line)
        #time.sleep(1)
        #self.ser.close()

    def openHomeWindow(self):
        self.close()
        self.window3 = HomeWindow()
        self.window3.show()


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        width = 1024
        height = 600
        self.setFixedWidth(width)
        self.setFixedHeight(height)

        # changing the background color to white
        self.setStyleSheet("background-color: rgb(204, 230, 255);")

    def initUI(self):
        self.username = open('username.txt').read()
        self.password = open('password.txt').read()
        
        self.label1 = QLabel("ENTER YOUR USERNAME: ",self)
        self.label1.move(300,50)
        self.label1.setFont(QFont('Times', 20))

        self.line_edit1 = QLineEdit(self)
        self.line_edit1.move(285,100)
        self.line_edit1.resize(400, 75)
        self.line_edit1.setFont(QFont('Times', 20))
        self.line_edit1.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.label2 = QLabel("ENTER YOUR PASSWORD: ",self)
        self.label2.move(300,255)
        self.label2.setFont(QFont('Times', 20))

        self.line_edit2 = QLineEdit(self)
        self.line_edit2.move(285,305)
        self.line_edit2.resize(400, 75)
        self.line_edit2.setFont(QFont('Times', 20))
        self.line_edit2.setStyleSheet("QLineEdit" "{" "background: white;" "}")

        self.button3 = QPushButton("Login",self)
        self.button3.clicked.connect(self.openHomeWindow)
        self.button3.move(285, 450)
        self.button3.resize(400, 75)
        self.button3.setFont(QFont('Times', 20))
        self.button3.setStyleSheet("background-color: rgb(240, 240, 240) ; color: black;")
        self.show()
        self.setWindowTitle("Login")

    def openHomeWindow(self):
        self.username1 = self.line_edit1.text()
        self.password1 = self.line_edit2.text()
        if self.username1 != self.username or self.password1 != self.password:
            self.label3 = QLabel("WRONG USERNAME OR PASSWORD, TRY AGAIN" ,self)
            self.label3.move(130,255)
            self.label3.setFont(QFont('Times', 20))
            self.label3.show()
        else:
            self.close()
            self.window3 = HomeWindow()
            self.window3.show()

        
class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        width = 1024
        height = 600
        self.setFixedWidth(width)
        self.setFixedHeight(height)

        # changing the background color to white
        self.setStyleSheet("background-color: white;")

    def initUI(self):
        self.tabs = QTabWidget()
        self.calendar_tab = QCalendarWidget()
        self.tabs.addTab(self.calendar_tab, "Calendar")

        self.summary_tab = QTextEdit()
        self.summary_tab.setReadOnly(True)
        self.tabs.addTab(self.summary_tab, "Summary")
        self.summary_tab.setStyleSheet("background-color: rgb(204, 230, 255);")


        self.chamber1_tab = QWidget(self)
        self.tabs.addTab(self.chamber1_tab, "Chamber 1")
        self.chamber1_tab.layout = QVBoxLayout(self)
        
        self.label11 = QLabel("MEDICATION NAME: ",self)
        self.label11.setFont(QFont('Times', 20))
        self.chamber1_tab.layout.addWidget(self.label11)

        self.medname1 = open('medname1.txt').read()

        self.label12 = QLabel(self.medname1,self)
        self.label12.setFont(QFont('Times', 20))
        self.chamber1_tab.layout.addWidget(self.label12)

        self.label13 = QLabel("DOCTOR/PHARMACY: ",self)
        self.label13.setFont(QFont('Times', 20))
        self.chamber1_tab.layout.addWidget(self.label13)

        self.docph1 = open('docph1.txt').read()

        self.label14 = QLabel(self.docph1, self)
        self.label14.setFont(QFont('Times', 20))
        self.chamber1_tab.layout.addWidget(self.label14)

        self.label15 = QLabel("DOSAGE: ",self)
        self.label15.setFont(QFont('Times', 20))
        self.chamber1_tab.layout.addWidget(self.label15)

        self.dos1 = open('dos1.txt').read()

        self.label16 = QLabel(self.dos1, self)
        self.label16.setFont(QFont('Times', 20))
        self.chamber1_tab.layout.addWidget(self.label16)

        self.label17 = QLabel("QUANTITY: ",self)
        self.label17.setFont(QFont('Times', 20))
        self.chamber1_tab.layout.addWidget(self.label17)

        self.quan1 = open('quan1.txt').read()

        self.label18 = QLabel(self.quan1, self)
        self.label18.setFont(QFont('Times', 20))
        self.chamber1_tab.setStyleSheet("background-color: rgb(204, 230, 255);")
        self.chamber1_tab.layout.addWidget(self.label18)

        self.chamber1_tab.setLayout(self.chamber1_tab.layout)


        self.chamber2_tab = QWidget(self)
        self.tabs.addTab(self.chamber2_tab, "Chamber 1")
        self.chamber2_tab.layout = QVBoxLayout(self)
        
        self.label21 = QLabel("MEDICATION NAME: ",self)
        self.label21.setFont(QFont('Times', 20))
        self.chamber2_tab.layout.addWidget(self.label21)

        self.medname2 = open('medname2.txt').read()

        self.label22 = QLabel(self.medname2,self)
        self.label22.setFont(QFont('Times', 20))
        self.chamber2_tab.layout.addWidget(self.label22)

        self.label23 = QLabel("DOCTOR/PHARMACY: ",self)
        self.label23.setFont(QFont('Times', 20))
        self.chamber2_tab.layout.addWidget(self.label23)

        self.docph2 = open('docph2.txt').read()

        self.label24 = QLabel(self.docph2, self)
        self.label24.setFont(QFont('Times', 20))
        self.chamber2_tab.layout.addWidget(self.label24)

        self.label25 = QLabel("DOSAGE: ",self)
        self.label25.setFont(QFont('Times', 20))
        self.chamber2_tab.layout.addWidget(self.label25)

        self.dos2 = open('dos2.txt').read()

        self.label26 = QLabel(self.dos2, self)
        self.label26.setFont(QFont('Times', 20))
        self.chamber2_tab.layout.addWidget(self.label26)

        self.label27 = QLabel("QUANTITY: ",self)
        self.label27.setFont(QFont('Times', 20))
        self.chamber2_tab.layout.addWidget(self.label27)

        self.quan2 = open('quan2.txt').read()

        self.label28 = QLabel(self.quan2, self)
        self.label28.setFont(QFont('Times', 20))
        self.chamber2_tab.setStyleSheet("background-color: rgb(204, 230, 255);")
        self.chamber2_tab.layout.addWidget(self.label28)

        self.chamber2_tab.setLayout(self.chamber2_tab.layout)


        self.chamber3_tab = QWidget(self)
        self.tabs.addTab(self.chamber3_tab, "Chamber 1")
        self.chamber3_tab.layout = QVBoxLayout(self)
        
        self.label31 = QLabel("MEDICATION NAME: ",self)
        self.label31.setFont(QFont('Times', 20))
        self.chamber3_tab.layout.addWidget(self.label31)

        self.medname3 = open('medname3.txt').read()

        self.label32 = QLabel(self.medname3,self)
        self.label32.setFont(QFont('Times', 20))
        self.chamber3_tab.layout.addWidget(self.label32)

        self.label33 = QLabel("DOCTOR/PHARMACY: ",self)
        self.label33.setFont(QFont('Times', 20))
        self.chamber3_tab.layout.addWidget(self.label33)

        self.docph3 = open('docph3.txt').read()

        self.label34 = QLabel(self.docph3, self)
        self.label34.setFont(QFont('Times', 20))
        self.chamber3_tab.layout.addWidget(self.label34)

        self.label35 = QLabel("DOSAGE: ",self)
        self.label35.setFont(QFont('Times', 20))
        self.chamber3_tab.layout.addWidget(self.label35)

        self.dos3 = open('dos3.txt').read()

        self.label36 = QLabel(self.dos3, self)
        self.label36.setFont(QFont('Times', 20))
        self.chamber3_tab.layout.addWidget(self.label36)

        self.label37 = QLabel("QUANTITY: ",self)
        self.label37.setFont(QFont('Times', 20))
        self.chamber3_tab.layout.addWidget(self.label37)

        self.quan3 = open('quan3.txt').read()

        self.label38 = QLabel(self.quan3, self)
        self.label38.setFont(QFont('Times', 20))
        self.chamber3_tab.setStyleSheet("background-color: rgb(204, 230, 255);")
        self.chamber3_tab.layout.addWidget(self.label38)

        self.chamber3_tab.setLayout(self.chamber3_tab.layout)


        self.chamber4_tab = QWidget(self)
        self.tabs.addTab(self.chamber4_tab, "Chamber 4")
        self.chamber4_tab.layout = QVBoxLayout(self)
        
        self.label41 = QLabel("MEDICATION NAME: ",self)
        self.label41.setFont(QFont('Times', 20))
        self.chamber4_tab.layout.addWidget(self.label41)

        self.medname4 = open('medname4.txt').read()

        self.label42 = QLabel(self.medname4,self)
        self.label42.setFont(QFont('Times', 20))
        self.chamber4_tab.layout.addWidget(self.label42)

        self.label43 = QLabel("DOCTOR/PHARMACY: ",self)
        self.label43.setFont(QFont('Times', 20))
        self.chamber4_tab.layout.addWidget(self.label43)

        self.docph4 = open('docph4.txt').read()

        self.label44 = QLabel(self.docph4, self)
        self.label44.setFont(QFont('Times', 20))
        self.chamber4_tab.layout.addWidget(self.label44)

        self.label45 = QLabel("DOSAGE: ",self)
        self.label45.setFont(QFont('Times', 20))
        self.chamber4_tab.layout.addWidget(self.label45)

        self.dos4 = open('dos4.txt').read()

        self.label46 = QLabel(self.dos4, self)
        self.label46.setFont(QFont('Times', 20))
        self.chamber4_tab.layout.addWidget(self.label46)

        self.label47 = QLabel("QUANTITY: ",self)
        self.label47.setFont(QFont('Times', 20))
        self.chamber4_tab.layout.addWidget(self.label47)

        self.quan4 = open('quan4.txt').read()

        self.label48 = QLabel(self.quan4, self)
        self.label48.setFont(QFont('Times', 20))
        self.chamber4_tab.setStyleSheet("background-color: rgb(204, 230, 255);")
        self.chamber4_tab.layout.addWidget(self.label48)

        self.chamber4_tab.setLayout(self.chamber4_tab.layout)


        self.chamber5_tab = QWidget(self)
        self.tabs.addTab(self.chamber5_tab, "Chamber 5")
        self.chamber5_tab.layout = QVBoxLayout(self)
        
        self.label51 = QLabel("MEDICATION NAME: ",self)
        self.label51.setFont(QFont('Times', 20))
        self.chamber5_tab.layout.addWidget(self.label51)

        self.medname5 = open('medname5.txt').read()

        self.label52 = QLabel(self.medname5,self)
        self.label52.setFont(QFont('Times', 20))
        self.chamber5_tab.layout.addWidget(self.label52)

        self.label53 = QLabel("DOCTOR/PHARMACY: ",self)
        self.label53.setFont(QFont('Times', 20))
        self.chamber5_tab.layout.addWidget(self.label53)

        self.docph5 = open('docph5.txt').read()

        self.label54 = QLabel(self.docph5, self)
        self.label54.setFont(QFont('Times', 20))
        self.chamber5_tab.layout.addWidget(self.label54)

        self.label55 = QLabel("DOSAGE: ",self)
        self.label55.setFont(QFont('Times', 20))
        self.chamber5_tab.layout.addWidget(self.label55)

        self.dos5 = open('dos5.txt').read()

        self.label56 = QLabel(self.dos5, self)
        self.label56.setFont(QFont('Times', 20))
        self.chamber5_tab.layout.addWidget(self.label56)

        self.label57 = QLabel("QUANTITY: ",self)
        self.label57.setFont(QFont('Times', 20))
        self.chamber5_tab.layout.addWidget(self.label57)

        self.quan5 = open('quan5.txt').read()

        self.label58 = QLabel(self.quan5, self)
        self.label58.setFont(QFont('Times', 20))
        self.chamber5_tab.setStyleSheet("background-color: rgb(204, 230, 255);")
        self.chamber5_tab.layout.addWidget(self.label58)

        self.chamber5_tab.setLayout(self.chamber5_tab.layout)


        self.chamber6_tab = QWidget(self)
        self.tabs.addTab(self.chamber6_tab, "Chamber 6")
        self.chamber6_tab.layout = QVBoxLayout(self)
        
        self.label61 = QLabel("MEDICATION NAME: ",self)
        self.label61.setFont(QFont('Times', 20))
        self.chamber6_tab.layout.addWidget(self.label61)

        self.medname6 = open('medname6.txt').read()

        self.label62 = QLabel(self.medname6,self)
        self.label62.setFont(QFont('Times', 20))
        self.chamber6_tab.layout.addWidget(self.label62)

        self.label63 = QLabel("DOCTOR/PHARMACY: ",self)
        self.label63.setFont(QFont('Times', 20))
        self.chamber6_tab.layout.addWidget(self.label63)

        self.docph6 = open('docph6.txt').read()

        self.label64 = QLabel(self.docph6, self)
        self.label64.setFont(QFont('Times', 20))
        self.chamber6_tab.layout.addWidget(self.label64)

        self.label65 = QLabel("DOSAGE: ",self)
        self.label65.setFont(QFont('Times', 20))
        self.chamber6_tab.layout.addWidget(self.label65)

        self.dos6 = open('dos6.txt').read()

        self.label66 = QLabel(self.dos6, self)
        self.label66.setFont(QFont('Times', 20))
        self.chamber6_tab.layout.addWidget(self.label66)

        self.label67 = QLabel("QUANTITY: ",self)
        self.label67.setFont(QFont('Times', 20))
        self.chamber6_tab.layout.addWidget(self.label67)

        self.quan6 = open('quan6.txt').read()

        self.label68 = QLabel(self.quan6, self)
        self.label68.setFont(QFont('Times', 20))
        self.chamber6_tab.setStyleSheet("background-color: rgb(204, 230, 255);")
        self.chamber6_tab.layout.addWidget(self.label68)

        self.chamber6_tab.setLayout(self.chamber6_tab.layout)


        self.setCentralWidget(self.tabs)
        self.show()

        self.calendar_tab.clicked.connect(self.show_summary)

    def show_summary(self, date):
        cursor = QTextCursor(self.summary_tab.document())
        self.day = date.toString()
        #cursor.insertText("Selected date: {}\n".format(date.toString()))
        if  (self.day[:3] == 'Mon'):
            self.info = open('monmedicine.txt').read()
            cursor.insertText("{}\n".format(self.info))
        if  (self.day[:3] == 'Tue'):
            self.info = open('tuesmedicine.txt').read()
            cursor.insertText("{}\n".format(self.info))
        if  (self.day[:3] == 'Wed'):
            self.info = open('wedmedicine.txt').read()
            cursor.insertText("{}\n".format(self.info))
        if  (self.day[:3] == 'Thu'):
            self.info = open('thurmedicine.txt').read()
            cursor.insertText("{}\n".format(self.info))
        if  (self.day[:3] == 'Fri'):
            self.info = open('frimedicine.txt').read()
            cursor.insertText("{}\n".format(self.info))
        if  (self.day[:3] == 'Sat'):
            self.info = open('satmedicine.txt').read()
            cursor.insertText("{}\n".format(self.info))
        if  (self.day[:3] == 'Sun'):
            self.info = open('sunmedicine.txt').read()
            cursor.insertText("{}\n".format(self.info))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
