# Draft

import customtkinter as ctk
import re
from customtkinter import CTkEntry, StringVar, CTkButton
from string_validation import *
from dfa1_illustration import *
from scratch.navigation_frames import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Automata Project")
        self.geometry("1080x700")
        self.resizable(True, True)

        # create navigation frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.pack(side = 'left', ipadx = 5, ipady = 700, anchor = 'e')

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="Regular Expression",
                                                             compound="center",
                                                             font=ctk.CTkFont(size=15, weight="bold", family="Helvetica Neue"))
        self.navigation_frame_label.pack(side = 'top', pady = 20, ipadx = 10, ipady = 10, anchor = 'n')

        self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=10, height=10, border_spacing=10,
                                                   text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.home_button_event)
        self.home_button.pack(side = 'top', ipadx = 5, ipady = 5, anchor = 'n')

        self.frame_2_button = ctk.CTkButton(self.navigation_frame, corner_radius=10, height=10,
                                                      border_spacing=10, text="DFA",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.pack(side = 'top', ipadx = 5, ipady = 5, anchor = 'n')

        self.frame_3_button = ctk.CTkButton(self.navigation_frame, corner_radius=10, height=10,
                                                      border_spacing=10, text="CFG",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.pack(side = 'top', ipadx = 5, ipady = 5, anchor = 'n')

        self.frame_4_button = ctk.CTkButton(self.navigation_frame, corner_radius=10, height=10,
                                                      border_spacing=10, text="PDA",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.pack(side = 'top', ipadx = 5, ipady = 5, anchor = 'n')

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame,
                                                                values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.pack(side = 'bottom', padx = 20, pady = 20, ipadx = 5, ipady = 0, anchor = 's')

        # create home frame
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.pack_configure(padx = 0, pady = 0, anchor = 'center')
        # self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = ctk.CTkLabel(self.home_frame, text="WELCOME!\nChoose a regular expression to get started.")
        self.home_frame_large_image_label.configure(font=(None, 25))
        self.home_frame_large_image_label.pack_configure(padx = 20, pady = 30)
        # self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=30)

        regex = ctk.StringVar(value="RegEx 1")  # set initial value

        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)
            if (choice == "RegEx 1"):
                text = "(a+b) (a+b)* (aa+bb) (ab+ba) (a+b)* (aba+baa)"
            if (choice == "RegEx 2"):
                text = "(11+00) (1+0)* (101+111+01) (00*+11*) (1+0+11)"
            self.validate_strings_label.configure(text=text)
            print(text)
            return text

        # regex = StringVar()
        self.combobox = ctk.CTkComboBox(self.home_frame, values=["RegEx 1", "RegEx 2"], command=combobox_callback, variable=regex)
        self.combobox.pack_configure(padx = 20, pady = 10)
        # self.combobox.bind("<<ComboboxSelected>>", lambda event: self.combobox_callback())
        # self.combobox.grid(row=0, column=1, padx=0, pady=90, sticky="n")
        # regex = ctk.StringVar(value="RegEx 1")

        self.validate_strings_label = ctk.CTkLabel(self.home_frame, text="")
        self.validate_strings_label.configure(font=(None, 20))
        self.validate_strings_label.pack(padx = 20, pady = 20)
        # self.validate_strings_label.grid(row=1, column=0, padx=20, pady=150)

        self.entry = ctk.CTkEntry(self.home_frame, width = 400, placeholder_text="Enter String")
        self.entry.configure(font=(None, 15))
        self.entry.pack_configure(side = 'left', padx = 20, pady = 20, anchor = 'center')
        # self.entry.grid(row=0, column=1, padx=70, pady=140, sticky="s")
        # self.entry = StringVar()

        pattern1 = r"^[ab](?:[ab])*(?:aa|bb)(?:ab|ba)(?:[ab])*?(?:aba|baa)$"
        pattern2 = r"^(?:11|00)(?:1|0)*(?:101|111|01)(?:00*|11*)(?:1|0|11)$"
        # call(["python", "string_validation.py"])
        # self.validateString(pattern2, self.entry)
        # result = validateString(pattern2, self.entry.get())

        def btn_handler():
            result = validateString(pattern2, self.entry.get())
            self.valid_label.configure(text=result)
            print(result)
            return result
            # validateString(pattern2, self.entry)
            # self.btn.configure(text=self.entry.get())

        self.btn = CTkButton(self.home_frame, text="Validate String", command=btn_handler)
        self.btn.pack_configure(side = 'left', padx = 0, pady = 0, anchor = 'center')

        self.valid_label = ctk.CTkLabel(self.home_frame, text="")
        self.valid_label.pack_configure(side = 'left', padx = 20, pady = 20, anchor = 'center')

        # self.btn.grid(row=0, column=1, padx=70, pady=190, sticky="s")

        # self.valid_label = ctk.CTkLabel(self.home_frame, text="string")
        # self.valid_label.pack(side = 'left', padx = 0, pady = 0, anchor = 'center')
        # self.valid_label.grid(row=0, column=1, padx=70, pady=200, sticky="s")

    #     # create second frame
    #     self.second_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
    #     self.second_frame.grid_columnconfigure(0, weight=1)
    #     # self.second_frame.pack()

    #     # self.second_frame_large_image_label = ctk.CTkLabel(self.home_frame,
    #     #                                                  text="WELCOME!\n")
    #     # self.second_frame_large_image_label.grid(row=0, column=0, padx=20, pady=30)

    #     self.dfa_container = ctk.CTkCanvas(self, width=2000, height=300)
    #     self.dfa_container.grid(row=0, column=1, padx=20, pady=30)
    #     # dfa_visual
    #     # draw = draw_dfa()
    #     # draw.grid(row=0, column=1, padx=20, pady=30)

    #     # create third frame
    #     self.third_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

    #     # create fourth frame
    #     self.fourth_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

    #     # select default frame
    #     self.select_frame_by_name("home")

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
        # self.combobox.configure(fg_color=("gray75", "gray25")
        # if (regex == "regex_1"):
        #     print(regex)
        # combobox.configure(fg_color=("gray75", "gray25") if name == "regex_1" else "transparent")

        # self.combobox.bind("<<ComboboxSelected>>", combobox_callback)


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

    

app = App()
app.mainloop()