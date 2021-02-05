from PyQt4 import QtCore, QtGui, uic
import sys
sys.path.append("C:/Python27/Lib/site-packages")


class testTreeview(QtGui.QDialog):
    def __init__(self, data={}, parent=None):
        super(testTreeview, self).__init__(parent)
        uic.loadUi("TreeviewTest.ui", self)
        self.CB = 0
        self.VIEWPORT = 1
        self.CAMERA = 2
        self.MOV_TYPE = 3
        self.MOV_NAME = 4

        self.data = data
        self.mov_type = ['', 'WIREFRAME', 'SHADED', 'PERSP', 'CONE', 'CUSTOM']
        self.model = self.create_data_model(self)
        print(self.data)
        self.treeView.setModel(self.model)
        self.treeView.header().setVisible(False)
        self.treeView.setEditTriggers(self.treeView.NoEditTriggers)
        self.treeView.setSelectionMode(self.treeView.ExtendedSelection)
        # self.btn_cancel.clicked.connect(self.close)
        for row, viewport, mov_name in zip(range(len(self.data.keys())), self.data.keys(), self.data.values()):
            print(row, viewport, mov_name)
            self.addData_to_model(row, viewport, mov_name)
            print()

    def create_data_model(self, parent):
        model = QtGui.QStandardItemModel(0, 5, parent)
        model.setHeaderData(self.CB, QtCore.Qt.Horizontal, "")
        model.setHeaderData(self.VIEWPORT, QtCore.Qt.Horizontal, "Viewport")
        model.setHeaderData(self.CAMERA, QtCore.Qt.Horizontal, "Camera")
        model.setHeaderData(self.MOV_TYPE, QtCore.Qt.Horizontal, "Mov Type")
        model.setHeaderData(self.MOV_NAME, QtCore.Qt.Horizontal, "Mov Name")
        return model

    def addData_to_model(self, row, viewport, mov_name ):
        self.model.setData(self.model.index(row, self.VIEWPORT), viewport)
        self.model.setData(self.model.index(row, self.CAMERA), self.get_cam_data(viewport))
        self.model.setData(self.model.index(row, self.MOV_TYPE), self.get_mov_type(mov_name))
        self.model.setData(self.model.index(row, self.MOV_TYPE), self.set_mov_type(mov_name))

        

    def get_cam_data(self, viewport = ''):
        cam_data = {"modelPanel1": "RODCam1",
                    "modelPanel2": "RODCam1",
                    "modelPanel3": "Persp"
                    }
        print("camera: ", cam_data[viewport])
        return cam_data[viewport]

    def get_mov_type(self, mov_name):
        if mov_name in 'skip':
            print("movie type: ", self.mov_type[[index for index, string in enumerate(self.mov_type) if '' in string][0]])
            return self.mov_type[[index for index, string in enumerate(self.mov_type) if '' in string][0]]
        elif mov_name not in self.mov_type:
            print("movie type: ", self.mov_type[[index for index, string in enumerate(self.mov_type) if 'CUSTOM' in string][0]])
            return self.mov_type[[index for index, string in enumerate(self.mov_type) if 'CUSTOM' in string][0]]
        else:
            print("movie type: ", self.mov_type[[index for index, string in enumerate(self.mov_type) if mov_name in string][0]])
            return self.mov_type[[index for index, string in enumerate(self.mov_type) if mov_name in string][0]]

            
    def set_mov_type(self, mov_name):
        if mov_name == 'skip':
            return ''
        else:
            return mov_name

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    data = {"modelPanel1": "CONE",
            "modelPanel2": "skip",
            "modelPanel3": "TEST"
            }
    win = testTreeview(data)
    win.show()
    app.exec_()
