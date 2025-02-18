import tkinter as tk
from PIL import Image, ImageTk
from .Board import Board
from .Menu import Menu
from .Pieces import Pieces
import os


class GUImanager:

    def __init__(self, title, size, controller):
        self.main_window = tk.Tk()
        self.main_window.title(title)
        self.main_window.geometry(size)
        self.main_window.config(bg="skyblue")

        self.Controller = controller
        self.Board = Board(self, self.main_window, tk)
        self.Menu = Menu(self, self.main_window, tk)
        self.Pieces = Pieces(self, self.main_window, tk, Image, os)

    def set_white_turn(self):
        self. Controller.set_white_turn()

    def set_black_turn(self):
        self.Controller.set_black_turn()

    def analyze_btn(self):
        self.Controller.analayzer()
        print("analyze btn clicked")

    def reset_btn(self):
        print("reset btn clicked")

    def startWindow(self):
        self.main_window.mainloop()
