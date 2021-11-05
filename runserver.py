#!/usr/bin/env python3

from PyQt5.QtCore    import pyqtSlot , QObject, QUrl
from PyQt5.QtQuick   import QQuickView
from PyQt5.QtWidgets import QApplication
import sys, subprocess, os

class QmlToQt(QObject):
        def __init__(self):
            QObject.__init__(self)
            self.desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
            self.desktop = self.desktop.replace(os.sep, '/')

            self.folder_server = 'datalogger'

        @pyqtSlot(bool,result=bool)
        def runServer(self,serverAccess):
                if not serverAccess:
                    self.p1 = subprocess.Popen('python {0}/{1}/data_logger_backend/manager.py'.format(self.desktop,self.folder_server), stdin=subprocess.PIPE, shell=True)
                    self.p2 = subprocess.Popen('python {0}/{1}/data_logger_socket/sensor.py'.format(self.desktop,self.folder_server), stdin=subprocess.PIPE, shell=True)
                    self.p3 = subprocess.Popen('cd {0}/{1}/datalogger_ui && SET PORT=3001 && npm start'.format(self.desktop,self.folder_server), stdin=subprocess.PIPE, shell=True)
                    return True
                
                else:
                    self.kill(self.p1.pid)
                    self.kill(self.p2.pid)
                    self.kill(self.p3.pid)
                    return False
        
        def kill(self,proc_pid):
            subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=proc_pid))
        
class MainWindow(QQuickView):
    def __init__(self):
        super().__init__()

        self.rootContext().setContextProperty("qmlToQt",qmlToQt) 
        self.setSource(QUrl('runserver/autorun.qml'))
        self.show()
        
    
def keep_alive():
    try:
        qmlToQt.kill(qmlToQt.p1.pid)  
        qmlToQt.kill(qmlToQt.p2.pid)  
        qmlToQt.kill(qmlToQt.p3.pid)  
    except:
        pass
    
    os._exit(0)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    qmlToQt = QmlToQt()
    app.lastWindowClosed.connect(keep_alive)
    w = MainWindow()
    sys.exit(app.exec_())
