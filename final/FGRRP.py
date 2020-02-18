# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FGRRP.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import model
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 220)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.HomeBox = QtWidgets.QGroupBox(self.centralwidget)
        self.HomeBox.setGeometry(QtCore.QRect(40, 30, 171, 121))
        self.HomeBox.setObjectName("HomeBox")
        self.HomeCountry = QtWidgets.QComboBox(self.HomeBox)
        self.HomeCountry.setEnabled(True)
        self.HomeCountry.setGeometry(QtCore.QRect(70, 30, 91, 21))
        self.HomeCountry.setObjectName("HomeCountry")
        self.HomeTeam = QtWidgets.QComboBox(self.HomeBox)
        self.HomeTeam.setGeometry(QtCore.QRect(70, 80, 91, 21))
        self.HomeTeam.setObjectName("HomeTeam")
        self.label = QtWidgets.QLabel(self.HomeBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 58, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.HomeBox)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 58, 15))
        self.label_2.setObjectName("label_2")
        self.AwayBox = QtWidgets.QGroupBox(self.centralwidget)
        self.AwayBox.setGeometry(QtCore.QRect(230, 30, 171, 121))
        self.AwayBox.setObjectName("AwayBox")
        self.AwayCountry = QtWidgets.QComboBox(self.AwayBox)
        self.AwayCountry.setGeometry(QtCore.QRect(70, 30, 91, 21))
        self.AwayCountry.setObjectName("AwayCountry")
        self.AwayTeam = QtWidgets.QComboBox(self.AwayBox)
        self.AwayTeam.setGeometry(QtCore.QRect(70, 80, 91, 21))
        self.AwayTeam.setObjectName("AwayTeam")
        self.label_3 = QtWidgets.QLabel(self.AwayBox)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 58, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.AwayBox)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 58, 15))
        self.label_4.setObjectName("label_4")
        self.ResultBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ResultBox.setGeometry(QtCore.QRect(420, 30, 161, 121))
        self.ResultBox.setObjectName("ResultBox")
        self.resultLabel = QtWidgets.QLabel(self.ResultBox)
        self.resultLabel.setGeometry(QtCore.QRect(10, 50, 141, 16))
        self.resultLabel.setText("")
        self.resultLabel.setObjectName("resultLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 25))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuDisclaimer = QtWidgets.QMenu(self.menubar)
        self.menuDisclaimer.setObjectName("menuDisclaimer")
        MainWindow.setMenuBar(self.menubar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menubar.addAction(self.menuDisclaimer.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        clist = ['Spain', 'Germany', 'France', 'Italy', 'England']
        self.HomeCountry.addItems(clist)
        self.AwayCountry.addItems(clist)
        self.HomeCountry.activated[str].connect(self.homeCountrySelected)
        self.AwayCountry.activated[str].connect(self.awayCountrySelected)
        self.AwayTeam.activated[str].connect(self.awayTeamSelected)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "G22-Football Game Result RISKY Predictor"))
        self.HomeBox.setTitle(_translate("MainWindow", "Home"))
        self.label.setText(_translate("MainWindow", "Country"))
        self.label_2.setText(_translate("MainWindow", "Team"))
        self.AwayBox.setTitle(_translate("MainWindow", "Away"))
        self.label_3.setText(_translate("MainWindow", "Country"))
        self.label_4.setText(_translate("MainWindow", "Team"))
        self.ResultBox.setTitle(_translate("MainWindow", "Result"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuDisclaimer.setTitle(_translate("MainWindow", "Disclaimer"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        
    def homeCountrySelected(self, text):
        c = model.conn.cursor()
        c.row_factory = lambda cursor, row: row[0]
        temp = c.execute('SELECT team_short_name AS name FROM Team').fetchall()
        tlist = []
        for i in temp:
            if i not in tlist:
                tlist.append(i)
        self.HomeTeam.addItems(sorted(tlist))
    
    def awayCountrySelected(self, text):
        c = model.conn.cursor()
        c.row_factory = lambda cursor, row: row[0]
        temp = c.execute('SELECT team_short_name AS name FROM Team').fetchall()
        tlist = []
        for i in temp:
            if i not in tlist:
                tlist.append(i)
        self.AwayTeam.addItems(sorted(tlist))
    
    def awayTeamSelected(self, text):
        self.predictResult()
    
    def predictResult(self):
        win = 0
        drawlose = 0
        # get attributions
        t1 = str(self.HomeTeam.currentText())
        t2 = str(self.AwayTeam.currentText())
        t1 = model.short2id.loc[model.short2id['short'] == t1].iloc[0,0]
        # print('t1:\n', t1)
        t2 = model.short2id.loc[model.short2id['short'] == t2].iloc[0,0]
        
        t1 = model.data.loc[model.data['HomeID'] == t1]
        print(t1)
        if (len(t1) > 0):
            hhha = [t1.iloc[0,6], t1.iloc[0,8]]
        else:
            t1 = model.data.loc[model.data['AwayID'] == t1]
            hhha = [t1.iloc[0,7], t1.iloc[0,9]]
            
        
        t2 = model.data.loc[model.data['HomeID'] == t2]
        print(t2)
        if (len(t2) > 0):
            ahaa = [t2.iloc[0,6], t2.iloc[0,8]]
        else:
            t2 = model.data.loc[model.data['AwayID'] == t2]
            ahaa = [t2.iloc[0,7], t2.iloc[0,9]]
        
        # prepare for prediction
        hhha.insert(1, ahaa[0])
        hhha.append(ahaa[1])
        xx = []
        xx.append(hhha)
        yy1 = model.model1.predict(xx)
        yy2 = model.model2.predict(xx)
        yy3 = model.model3.predict(xx)
        
        print(yy1, yy2, yy3)
        if yy1 == 1:
            win += 1
        else:
            drawlose +=1
        if yy2 == 1:
            win += 1
        else:
            drawlose +=1
        if yy3 == 1:
            win += 1
        else:
            drawlose +=1
        
        if win > drawlose:
            self.resultLabel.setText('Home Win')
        else:
            self.resultLabel.setText('Home Draw or Lose')
        
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow) 
    MainWindow.show()
    
    sys.exit(app.exec_()) 