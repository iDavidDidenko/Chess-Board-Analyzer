import tkinter as tk
from PIL import Image, ImageTk
from .Board import Board
from .Menu import Menu
from .Pieces import Pieace

import os


class GUImanager:

    def __init__(self, title, size):
        self.main_window = tk.Tk()
        self.main_window.title(title)
        self.main_window.geometry(size)
        self.main_window.config(bg="skyblue")

        self.Board = Board(self, self.main_window, tk)
        self.Menu = Menu(self, self.main_window, tk)
        self.Pieces = Pieace(self, self.main_window, tk, Image, os)



    def startWindow(self):
        self.main_window.mainloop()

