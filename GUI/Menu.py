class Menu:

    def __init__(self, GUImanager, main_window, tk):
        self.GUImanager = GUImanager
        self.tk = tk

        self.menu_frame = self.tk.Frame(main_window, width=120, height=400, bg="blue")
        self.menu_frame.grid(row=0, column=1, padx=2, pady=10)

        self.analiyze_btn = self.tk.Frame(self.menu_frame, width=100, height=50, bg="red")
        self.analiyze_btn.grid(row=0, column=0, padx=0, pady=0)

        self.reset_btn = self.tk.Frame(self.menu_frame, width=100, height=50, bg="yellow")
        self.reset_btn.grid(row=1, column=0, padx=0, pady=0)

        self.__createMenu()

    def __createMenu(self):
        self.btn_analiyze = self.tk.Button(self.menu_frame, text="Analyze", width=10, height=2, bg="white")
        self.btn_analiyze.grid(row=0, column=0, padx=0, pady=0)

        btn_reset = self.tk.Button(self.reset_btn, text="Reset", width=10, height=2, bg="orange")
        btn_reset.grid(row=1, column=0, padx=0, pady=0)


