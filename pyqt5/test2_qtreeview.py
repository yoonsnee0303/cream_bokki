from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDir, Qt
import sys
from PyQt5.QtGui import QPixmap,QIcon

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

        # QTreeView
        tree_view = QTreeView()
        tree_view.setFixedWidth(300)

        # QFileSystemModel
        file_system_model = QFileSystemModel()
        file_system_model.setRootPath(QDir.rootPath("C:\\"))  # set the root path to "C:\\" here
        file_system_model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)  # show all directories, excluding "." and ".."
        tree_view.setModel(file_system_model)
        tree_view.setRootIndex(file_system_model.index(QDir.rootPath()))  # set the root index to the "C:\\" directory
        hbox.addWidget(tree_view)

        # QLineEdit
        hbox_1 = QLineEdit('hbox_1')
        hbox.addWidget(hbox_1)

        #vbox
        vbox = QVBoxLayout()
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
