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

        self.black_btn = self.tk.Frame(self.menu_frame, width=100, height=50, bg="green")
        self.black_btn.grid(row=2, column=0, padx=0, pady=0)

        self.white_btn = self.tk.Frame(self.menu_frame, width=100, height=50, bg="orange")
        self.white_btn.grid(row=3, column=0, padx=0, pady=0)


        self.__createMenu()

    def __createMenu(self):
        self.btn_analiyze = self.tk.Button(self.menu_frame, text="Analyze", width=10, height=2, bg="white")
        self.btn_analiyze.grid(row=0, column=0, padx=0, pady=0)
        self.btn_analiyze.bind("<Button-1>", lambda event: self.__handle_on_click_analyze())    

        self.btn_reset = self.tk.Button(self.reset_btn, text="Reset", width=10, height=2, bg="orange")
        self.btn_reset.grid(row=1, column=0, padx=0, pady=0)
        self.btn_reset.bind("<Button-1>", lambda event: self.__handle_on_click_reset())

        self.black_btn = self.tk.Button(self.reset_btn, text="Black", width=10, height=2, bg="orange")
        self.black_btn.grid(row=2, column=0, padx=0, pady=0)
        self.black_btn.bind("<Button-1>", lambda event: self.__handle_on_click_black())

        self.white_btn = self.tk.Button(self.reset_btn, text="White", width=10, height=2, bg="white")
        self.white_btn.grid(row=3, column=0, padx=0, pady=0)
        self.white_btn.bind("<Button-1>", lambda event: self.__handle_on_click_white())



    def __handle_on_click_white(self):
        self.GUImanager.set_white_turn()

    def __handle_on_click_black(self):
        self.GUImanager.set_black_turn()

    def __handle_on_click_analyze(self):
        self.GUImanager.analyze_btn()

    def __handle_on_click_reset(self):
        self.GUImanager.reset_btn()


