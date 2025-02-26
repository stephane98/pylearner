from PyQt5 import QtWidgets, QtCore, QtGui
import random


TEXT_STYLE1 = """QLabel\n
        {\n
               font-weight: bold;\n
        }"""

TEXT_STYLE2 = """QLabel\n
        {\n
               font-weight: bold;\n
               font-size: 18px;\n
        }"""

FRAME_STYLE = """QFrame\n
        {\n
               background-color: #28d;\n
        }"""

FRAME_STYLE1 = """QFrame\n
        {\n
               background-color: #6fd;\n
        }"""


class CustomFrame(QtWidgets.QFrame, QtWidgets.QWidget):
    clicked  = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(CustomFrame, self).__init__(parent)

    def mousePressEvent(self, a0: QtGui.QMouseEvent):
        self.clicked.emit()
        
        



class SubTitle(QtWidgets.QWidget):
    title = ""
    number = 0
    clicked = QtCore.pyqtSignal()
    def __init__(self, number=0, title="Subtile", parent=None):
        super(SubTitle, self).__init__(parent)
        
        self.number = number
        self.title = title

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setStyleSheet("""
        QFrame
        {
        background-color: rgb(211, 211, 211);
        }
        """)        
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setMinimumSize(QtCore.QSize(0, 32))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 32))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.frame_layout = QtWidgets.QHBoxLayout(self.frame)
        self.frame_layout.setContentsMargins(12, 0, 12, 0)
        self.frame_layout.setSpacing(6)

        self.number_label = QtWidgets.QLabel(self.frame)
        self.number_label.setText("{}.".format(self.number))
        self.number_label.setStyleSheet(TEXT_STYLE1)
        self.frame_layout.addWidget(self.number_label)

        self.title_label = QtWidgets.QLabel(self.frame)
        self.title_label.setText("{}".format(self.title))
        self.title_label.setStyleSheet(TEXT_STYLE1)
        self.frame_layout.addWidget(self.title_label)

        self.frame_layout.setStretch(1, 1)
        self.layout.addWidget(self.frame)




class Title(SubTitle):
    
    checked = False
    def __init__(self,number=0, title="Title", parent=None):
        super(Title, self).__init__(number, title, parent)
        
        self.icon_label = QtWidgets.QLabel(self.frame)
        self.icon_label.setMaximumSize(QtCore.QSize(12, 12))
        self.icon_label.setPixmap(QtGui.QPixmap(":/svg/up-arrow.svg"))
        self.icon_label.setScaledContents(True)
        self.frame_layout.addWidget(self.icon_label)
        self.frame.setMinimumSize(QtCore.QSize(0, 48))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 48))
        self.frame.setStyleSheet(FRAME_STYLE)


    def mousePressEvent(self, event):
        self.clicked.emit()
        checked = self.checked
        self.checked = not self.checked
        if checked:
            self.icon_label.setPixmap((QtGui.QPixmap(":/svg/angle-arrow-down.svg")))
        else:
            self.icon_label.setPixmap(QtGui.QPixmap(":/svg/up-arrow"))



