import sys
sys.path.append('C:/Python38/Lib/site-packages')
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QFont, QColor

class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size =12, set_bold = False, color=QColor(0,0,0)):
        super().__init__()
        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)
        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)



class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("World Diagram")
        self.resize(500, 700)

        treeView = QTreeView()
        print("treeView: ", treeView)
        treeView.setHeaderHidden(True)
        self.treeModel = QStandardItemModel()
        print("self.treeModel: ", self.treeModel)
        rootNode = self.treeModel.invisibleRootItem()
        print("rootNode: ", rootNode)

        '---------------------------------------'
        # why is california and america on the same row?
        america = StandardItem('America', 16, set_bold=True)
        print("america: ", america)

        california = StandardItem('California', 14, set_bold=True)
        print("california: ", california)
        america.appendRow(california)
        
        oakland = StandardItem('Oakland', 12, color=QColor(155,0,0))
        print("oakland: ", oakland)
        sanfrancisco = StandardItem('San Francisco', 12, color=QColor(155,0,0))
        print("sanfrancisco: ", sanfrancisco)
        sanjose = StandardItem('San Jose', 12, color=QColor(155,0,0))
        print("sanjose: ", sanjose)
        california.appendRow(oakland)
        california.appendRow(sanfrancisco)
        california.appendRow(sanjose)

        texas = StandardItem('Texas', 14, set_bold=True)
        america.appendRow(texas)

        austin = StandardItem('Austin', 12, color=QColor(155,0,0))
        houston = StandardItem('Houston', 12, color=QColor(155,0,0))
        dallas = StandardItem('Dallas', 12, color=QColor(155,0,0))
        texas.appendRow(austin)
        texas.appendRow(houston)
        texas.appendRow(dallas)

        canada = StandardItem('Canada', 16, set_bold=True)
        alberta = StandardItem('Alberta', font_size=14)
        britishcolumbia = StandardItem('British Columbia', font_size=14)
        ontario = StandardItem('Ontario', font_size=14)
        canada.appendRows([alberta, britishcolumbia,ontario])

        rootNode.appendRow(america)

        rootNode.appendRow(canada)

        treeView.setModel(self.treeModel)
        treeView.expandAll()


        level = 0
        tree_list = []
        for i in range(self.treeModel.rowCount()):
            tm = self.treeModel.item(i)
            print(tm.data(0))
            treev = self.getInfo(tm, level)

        treeView.doubleClicked.connect(self.getValue)

        self.setCentralWidget(treeView)

    def getInfo(self, item, level):
        if item.hasChildren():
            # print(item.rowCount())
            # print(item.columnCount())
            level+=1
            for i in range(item.rowCount()):
                for j in range(item.columnCount()):
                    print("-"*level+item.child(i,j).data(0))
                    self.getInfo( item.child(i,j), level)
        # else:
        #     print("no children")



app = QApplication(sys.argv)
demo= AppDemo()
demo.show()
sys.exit(app.exec_())
