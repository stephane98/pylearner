from PyQt5 import QtWidgets, Qt
from assets.utils import *

class CollapsibleBox(QtWidgets.QWidget):

    def __init__(self, content=None, parent=None):
        super(CollapsibleBox, self).__init__(parent)

        self.toggle_button = Title()
        self.toggle_button.clicked.connect(self.toggle)
        
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setContentsMargins(0, 0, 6, 0)
        self.vertical_layout.setSpacing(0)
        self.vertical_layout.addWidget(self.toggle_button)
        self.setLayout(self.vertical_layout)
        
        self.content_area = QtWidgets.QScrollArea()
        self.content_area.setWidgetResizable(True)
        self.content_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        
        size_policy =  QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.content_area.sizePolicy().hasHeightForWidth())
        self.content_area.setSizePolicy(size_policy)
        self.content_area.setMaximumSize(QtCore.QSize(0, 0))
        
        self.vertical_layout.addWidget(self.content_area)
        self.vertical_layout.setStretch(1, 4)
        #self.vertical_layout.setStretch(1, 1)
        
        


        lay = QtWidgets.QVBoxLayout()
        lay.setSizeConstraint(QtWidgets.QVBoxLayout.SetDefaultConstraint)
        for j in range(10):
            st = SubTitle()
            label = QtWidgets.QLabel("{}".format(j))
            color = QtGui.QColor(*[random.randint(0, 255) for _ in range(3)])
            label.setStyleSheet(
                "background-color: {}; color : white;".format(color.name())
            )
            label.setAlignment(QtCore.Qt.AlignCenter)
            lay.addWidget(st)
        


        self.toggle_animation = QtCore.QParallelAnimationGroup(self)
        self.toggle_animation.addAnimation(
            QtCore.QPropertyAnimation(self, b"minimumHeight")
        )
        self.toggle_animation.addAnimation(
            QtCore.QPropertyAnimation(self, b"maximumHeight")
        )
        self.toggle_animation.addAnimation(
            QtCore.QPropertyAnimation(self.content_area, b"maximumHeight")
        )


        
        self.setContentLayout(lay)
        


    def toggle(self):
        checked = self.toggle_button.checked
        if not checked:
            direction = QtCore.QAbstractAnimation.Forward
            self.content_area.setMaximumSize(QtCore.QSize(400, 100))
        else:
            direction = QtCore.QAbstractAnimation.Backward
            self.content_area.setMaximumSize(QtCore.QSize(0, 0))
        self.toggle_animation.setDirection(direction)
        self.toggle_animation.start()
        

    def setContentLayout(self, layout):
        old_lay = self.content_area.layout()
        del old_lay
        self.content_area.setLayout(layout)
        collapsed_height = (
            self.sizeHint().height() - self.content_area.maximumHeight()
        )
        content_height = layout.sizeHint().height()
        for i in range(self.toggle_animation.animationCount()):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(250)
            animation.setStartValue(collapsed_height)
            animation.setEndValue(collapsed_height + content_height)

        content_animation = self.toggle_animation.animationAt(
            self.toggle_animation.animationCount() - 1
        )
        content_animation.setDuration(250)
        content_animation.setStartValue(0)
        content_animation.setEndValue(content_height)
        self.toggle_animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self.toggle_animation.start()
        #self.toggle()

if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    collapse = CollapsibleBox()
    collapse.show()
    sys.exit(app.exec_())