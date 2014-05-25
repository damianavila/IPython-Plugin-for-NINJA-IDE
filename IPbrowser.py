#A simple web browser to embed IPython into NINJA-IDE

import sys
from PyQt4 import QtGui, QtCore, QtWebKit


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.tabs = QtGui.QTabWidget(self,
                                     tabsClosable=True,
                                     tabCloseRequested=self.closeTabRequested)
        self.setCentralWidget(self.tabs)

    def addTab(self, url=QtCore.QUrl("")):
        self.tabs.setCurrentIndex(self.tabs.addTab(Tab(url, self), ""))
        return self.tabs.currentWidget()

    def closeTabRequested(self, idx):
        if idx != 0:
            self.tabs.widget(idx).deleteLater()


class Tab(QtWebKit.QWebView):
    def __init__(self, url, container):
        self.container = container
        QtWebKit.QWebView.__init__(self, titleChanged=self.titleTabChanged)
        self.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled,
            True)
        self.load(url)

    def titleTabChanged(self, t):
        self.container.tabs.setTabText(self.container.tabs.indexOf(self), t)

    def createWindow(self, windowType):
        return self.container.addTab()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    web = MainWindow()
    web.addTab(QtCore.QUrl('http://www.google.com/'))
    web.show()
    sys.exit(app.exec_())
