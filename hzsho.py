import random
import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QAction, QLabel, QMenu, QSizePolicy, QLineEdit,  qApp, QApplication, QCheckBox, QPushButton, QWidget, QTextEdit, QGridLayout,  QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt, QCoreApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Title'
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle(self.title)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)


        self.show()


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        #initialize
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(300, 200)

        #adding
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tabs.addTab(self.tab3, "Tab 3")

        #firsttab
        self.tab1.data1 = QLabel('data1')
        self.tab1.data1Edit = QTextEdit()
        self.tab1.data2 = QLabel('data2')
        self.tab1.data2Edit = QTextEdit()
        self.tab1.grid = QGridLayout()
        self.tab1.grid.setSpacing(10)
        self.tab1.grid.addWidget(self.tab1.data1, 0, 1)
        self.tab1.grid.addWidget(self.tab1.data1Edit, 1, 1)
        self.tab1.grid.addWidget(self.tab1.data2, 0, 2)
        self.tab1.grid.addWidget(self.tab1.data2Edit, 1, 2)
        self.tab1.cb = QCheckBox('sraka', self)
        self.tab1.grid.addWidget(self.tab1.cb, 0, 3)
        self.tab1.cb.toggle()
        self.tab1.cb1 = QCheckBox('hui', self)
        self.tab1.cb1.toggle()
        self.tab1.grid.addWidget(self.tab1.cb1, 1, 3)
        self.tab1.setLayout(self.tab1.grid)


        #tab2


        #self.tab2.gr = PlotCanvas(self, width=5, height=4)



        #self.tab2.gr.plot()
        #self.tab2.gr.draw()

        #tab3
        self.tab3.qbtn = QPushButton('Quit', self)
        self.tab3.qbtn.clicked.connect(QCoreApplication.instance().quit)
        self.tab3.qbtn.resize(self.tab3.qbtn.sizeHint())
        self.tab3.grid = QGridLayout()
        self.tab3.grid.setSpacing(10)
        self.tab3.grid.addWidget(self.tab3.qbtn, 3, 0)
        self.tab3.setLayout(self.tab3.grid)
        self.tab3.ibtn = QPushButton('Import', self)
        self.tab3.ibtn.clicked.connect(QCoreApplication.instance().quit)
        self.tab3.grid.addWidget(self.tab3.ibtn, 2, 0)
        self.tab3.ebtn = QPushButton('Export', self)
        self.tab3.grid.addWidget(self.tab3.ebtn, 1, 0)
        self.tab3.ebtn.resize(self.tab3.ebtn.sizeHint())






#    def showDialog(self):
#        self.tab3.fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
#
#        self.tab3.f = open(self.tab3.fname, 'r')
#
#        with self.tab3.f:
#            data = self.tab3.f.read()
#            self.textEdit.setText(data)
















        #adding to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)



#class PlotCanvas(FigureCanvas):

#    def __init__(self, parent=None, width=5, height=4, dpi=100):
#        fig = Figure(figsize=(width, height), dpi=dpi)
#        self.axes = fig.add_subplot(111)

#        FigureCanvas.__init__(self, fig)
#        self.setParent(parent)

#        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
#        FigureCanvas.updateGeometry(self)



#    def plot(self):
#        daata = [random.random() for i in range(25)]
#        ax = self.figure.add_subplot(111)
#        ax.plot(daata, 'r-')
#        ax.set_title('sho proishodit')







if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())