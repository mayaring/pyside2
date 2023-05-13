################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

## ==> GUI FILE
from main import *

GLOBAL_STATE = 0

class UIFunctions(MainWindow):

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:
            self.showMaximized()

            GLOBAL_STATE = 1
            #IF MAXMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.drop_show_frame.setContentsMargins(0,0,0,0)
            self.ui.drop_show_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.5 rgba(28, 29, 73, 255));border-radius: 10px;")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1,self.height()+1)
            self.ui.drop_show_frame.setContentsMargins(10,10,10,10)
            self.ui.drop_show_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.5 rgba(28, 29, 73, 255));border-radius: 10px;")
            self.ui.btn_maximize.setToolTip("Maximize")
    
    def uiDefinitions(self):

        #REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #MAXIMIZE / RESTORE
        self.ui.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))