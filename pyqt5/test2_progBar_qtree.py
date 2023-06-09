from PyQt5.QtWidgets import *
import sys
import urllib.request
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import Qt

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initImageUI()

    def initImageUI(self):

        #menubar
        # exit action
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        # coupang
        cou_action = QAction(QIcon('coupang.png'), '&coupang', self)
        cou_action.setStatusTip('open application')
        cou_action.triggered.connect(self.test)

        # 11번가
        street_action = QAction(QIcon('11번가.png'), '&11번가', self)
        street_action.setStatusTip('open application')
        street_action.triggered.connect(self.test)

        # gmarket
        g_action = QAction(QIcon('gmarket.png'), '&지마켓', self)
        g_action.setStatusTip('open application')
        g_action.triggered.connect(self.test)

        # Naver
        naver_action = QAction(QIcon('naver.png'), '&네이버', self)
        naver_action.setStatusTip('open application')
        naver_action.triggered.connect(self.test)

        #menubar_main
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        filemenu.addAction(cou_action)

        # toolbar
        self.setWindowTitle('이미지 표시')
        self.setGeometry(800, 800, 700, 400)
        self.toolbar = self.addToolBar('Exit')

        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(cou_action)
        self.toolbar.addAction(g_action)
        self.toolbar.addAction(naver_action)
        self.toolbar.addAction(street_action)

        #hbox
        hbox = QHBoxLayout()
        
        # Add treeview to hbox
        self.treeview = QTreeView()
        self.treeview.setModel(QDirModel())
        self.treeview.setRootIndex(QDirModel().index("C:/"))
        hbox.addWidget(self.treeview)

        hbox_2 = QLineEdit('hbox_2')
        hbox.addWidget(hbox_2)

        #vbox
        vbox = QVBoxLayout()
        
        # Add progressbar to vbox
        self.progressbar = QProgressBar()
        self.progressbar.setValue(0)
        vbox.addWidget(self.progressbar)
        
        vbox_1 = QLineEdit('vbox_1')
        vbox.addWidget(vbox_1)
        vbox.addLayout(hbox)

        #main
        main = QWidget()
        main.setStyleSheet("background-color: yellow;")
        main.setLayout(vbox)

        #show
        self.setCentralWidget(main)
        self.show()


    def test(self):
        print('test')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
