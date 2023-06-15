# navigation frames

import customtkinter as ctk

# create navigation frame

def nav_frame(self):
    # self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
    # self.navigation_frame.pack(side = 'left', ipadx = 5, ipady = 700, anchor = 'e')
    #     # self.navigation_frame.grid(row=0, column=0, sticky="nsew")
    #     # self.navigation_frame.grid_rowconfigure(5, weight=1)

    # navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="Regular Expression",
    #                                       compound="center", font=ctk.CTkFont(size=15, weight="bold", family="Helvetica Neue"))
    # navigation_frame_label.pack(side = 'top', pady = 20, ipadx = 10, ipady = 10, anchor = 'n')
    #     # self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

    # home_button = ctk.CTkButton(self.navigation_frame, corner_radius=10, height=10, border_spacing=10,
    #                                                text="Home",
    #                                                fg_color="transparent", text_color=("gray10", "gray90"),
    #                                                hover_color=("gray70", "gray30"),
    #                                                anchor="w", command=home_button_event)
    # home_button.pack(side = 'top', ipadx = 5, ipady = 5, anchor = 'n')
    #     # self.home_button.grid(row=1, column=0, sticky="ew")

    # frame_2_button = ctk.CTkButton(self.navigation_frame, corner_radius=10, height=10,
    #                                                   border_spacing=10, text="DFA",
    #                                                   fg_color="transparent", text_color=("gray10", "gray90"),
    #                                                   hover_color=("gray70", "gray30"),
    #                                                   anchor="w", command=frame_2_button_event)
    # frame_2_button.pack(side = 'top', ipadx = 5, ipady = 5, anchor = 'n')
    #     # self.frame_2_button.grid(row=2, column=0, sticky="ew")

    # frame_3_button = ctk.CTkButton(self.navigation_frame, corner_radius=10, height=10,
    #                                                   border_spacing=10, text="CFG",
    #                                                   fg_color="transparent", text_color=("gray10", "gray90"),
    #                                                   hover_color=("gray70", "gray30"),
    #                                                   anchor="w", command=frame_3_button_event)
    # frame_3_button.pack(side = 'top', ipadx = 5, ipady = 5, anchor = 'n')
    #     # self.frame_3_button.grid(row=3, column=0, sticky="ew")

    # frame_4_button = ctk.CTkButton(self.navigation_frame, corner_radius=10, height=10,
    #                                                   border_spacing=10, text="PDA",
    #                                                   fg_color="transparent", text_color=("gray10", "gray90"),
    #                                                   hover_color=("gray70", "gray30"),
    #                                                   anchor="w", command=frame_4_button_event)
    # frame_4_button.pack(side = 'top', ipadx = 5, ipady = 5, anchor = 'n')
    #     # self.frame_4_button.grid(row=4, column=0, sticky="ew")

    # appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame,
    #                                                             values=["Light", "Dark", "System"],
    #                                                             command=change_appearance_mode_event)
    # appearance_mode_menu.pack(side = 'bottom', padx = 20, pady = 20, ipadx = 5, ipady = 0, anchor = 's')
    #     # self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()

    def combobox_callback(choice):
        print("combobox dropdown clicked:", choice)
        # self.combobox.configure(fg_color=("gray75", "gray25") if name == "regex_1" else "transparent")
        # combobox.configure(fg_color=("gray75", "gray25") if name == "regex_1" else "transparent")

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

    def button_callback(self):
        print("button pressed")
