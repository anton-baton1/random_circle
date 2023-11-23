import io
import random
import sys

from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtWidgets import QApplication, QWidget

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="circle_btn">
   <property name="geometry">
    <rect>
     <x>140</x>
     <y>260</y>
     <width>93</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string>не нажимай</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Example(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.paint = False
        self.circle_btn.clicked.connect(self.click)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        pos_x, pos_y = random.randint(0, 400), random.randint(0, 300)
        diameter = random.randint(0, 100)
        qp.drawEllipse(pos_x, pos_y, diameter, diameter)
        qp.end()

    def click(self):
        self.paint = True
        self.update()

    def paint(self, qp):
        qp.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        pos_x, pos_y = random.randint(0, 400), random.randint(0, 300)
        diameter = random.randint(0, 100)
        qp.drawEllipse(pos_x, pos_y, diameter, diameter)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
