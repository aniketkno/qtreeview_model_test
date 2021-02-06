import sys
sys.path.append('C:/Python38/Lib/site-packages')
from PyQt5.QtWidgets import QWidget,QApplication, QMainWindow, QTreeView, QCheckBox, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt


class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size =12, set_bold = False, color=QColor(0,0,0)):
        super().__init__()
        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)
        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)

class testTreeview(QWidget):
    def __init__(self, parent=None):
        super(testTreeview, self).__init__(parent)
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        self.setWindowTitle("World Diagram")
        # self.resize(500, 700)

        treeView = QTreeView()
        vbox.addWidget(treeView)
        vbox.addLayout(hbox)
        self.ok_Btn = QPushButton('OK')
        self.cancel_Btn = QPushButton('Cancel')
        # hbox.addStretch(1)
        hbox.addWidget(self.ok_Btn)
        hbox.addWidget(self.cancel_Btn)
        # vbox.addStretch(1)
        # row types
        self.CB = 0
        self.ONE = 1
        self.TWO = 2
        self.THREE = 3

        self.treeModel = QStandardItemModel()
        self.model = self.create_data_model(self)
        self.rootNode = self.model.invisibleRootItem()

        for row in range(3):
            print(row)
            self.rootNode.appendRow(self.addData_to_model(row))
            print()

        treeView.setModel(self.model)
        # self.setCentralWidget(treeView)
  
  
        # setting geometry of button 
        # adding action to a button 
        self.ok_Btn.clicked.connect(self.clickme) 
        self.cancel_Btn.clicked.connect(self.close)

    def create_data_model(self, parent):
        model = QStandardItemModel(0, 4, parent)
        model.setHeaderData(self.CB, Qt.Horizontal, "1")
        model.setHeaderData(self.ONE, Qt.Horizontal, "2")
        model.setHeaderData(self.TWO, Qt.Horizontal, "3")
        model.setHeaderData(self.THREE, Qt.Horizontal, "4")
        return model

    def addData_to_model(self, row):
        cb = StandardItem('')
        cb.setCheckable(True)
        one = StandardItem('1')
        two = StandardItem('2')
        three = StandardItem('3')
        return [cb, one, two, three]

    def clickme(self):
        print(self.rootNode.rowCount())
        dict_data = {}
        for row in range(self.rootNode.rowCount()):
            print("{0} checkBox".format(row), self.rootNode.child(row, 0).checkState())
            if self.rootNode.child(row, 0).checkState():
                tm1 = self.rootNode.child(row,1)
                tm2 = self.rootNode.child(row,2)
                tm3 = self.rootNode.child(row,3)
                dict_data.setdefault(row, [tm1.data(0), tm2.data(0), tm3.data(0)])
        print(dict_data)

app = QApplication(sys.argv)
win = testTreeview()
win.show()
sys.exit(app.exec_())
