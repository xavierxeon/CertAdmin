#!/usr/bin/env python3

import os, sys, signal

# pylint: disable=E0611
from PySide2.QtCore import QTimer
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine 
# pylint: enable=E0611

from xxpystuff.tools import JSONSettings

from ..settings import Settings
from ..certca import CertCA

from .interface import Interface
from .usermodel import UserModel

def signit_handler(*args):

    QGuiApplication.quit()

def startGui():

    settings = Settings()
    try:
        settings.load()
    except JSONSettings.SettingsError as e:
        print(e)
        quit()

    certCA = CertCA.loadOrCreate(settings)    
    usermodel = UserModel(settings)        

    app = QGuiApplication([])
    signal.signal(signal.SIGINT, signit_handler)

    timer = QTimer()
    timer.start(500)  # You may change this if you wish.
    timer.timeout.connect(lambda: None)  # Let the interpreter run each 500 ms.

    engine = QQmlApplicationEngine()

    interface = Interface(settings, certCA, usermodel)
    context = engine.rootContext()
    context.setContextProperty("PyInterface", interface)
    context.setContextProperty("userModel", usermodel)

    thisFile = os.path.realpath(__file__)
    thisDir = os.path.dirname(thisFile)
    engine.load(thisDir + '/qml/MainWidget.qml')
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())

if __name__ == '__main__':
    startGui()   