import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QLabel, QLineEdit,  qApp, QApplication, QPushButton, QWidget, QTextEdit, QGridLayout,  QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

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
        self.tab1.setLayout(self.tab1.grid)




        #adding to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        @pyqtSlot()
        def on_click(self):
            print("\n")
            for currentQTableWidgetItem in self.tableWidget.selectedItems():
                print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())