#A simple plugin to give IPython support for NINJA-IDE

from ninja_ide.core import plugin
from PyQt4 import QtCore
from IPbrowser import MainWindow

SERVICE_NAME = "misc"


class my_IPython_qt(plugin.Plugin):
    def initialize(self):
        misc_service = self.locator.get_service(SERVICE_NAME)
        web = MainWindow()
        web.addTab(QtCore.QUrl('http://127.0.0.1:8888/'))
        web.show()
        icon_path = QtCore.QDir.homePath() + "/.ninja_ide/addins/plugins/ipynblogo.png"
        description = "IPython embedded into NINJA-IDE"
        #add the widget to NINJA-IDE
        misc_service.add_widget(web, icon_path, description)

    def finish(self):
        print("The plugin is shutting down cause the user has closed NINJA-IDE")
