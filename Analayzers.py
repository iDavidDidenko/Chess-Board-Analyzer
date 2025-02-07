import GUI.GUImanager as MainWindow
from ChessEngine.Controller import Controller as controller

c = controller()

win = MainWindow.GUImanager("Chess", "1024x720", controller=c)
win.startWindow()

