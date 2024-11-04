# main.py
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
import sys

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

# Load the QML file
engine.load(QUrl.fromLocalFile("main.qml"))

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec())
