# Automata Main

import customtkinter as ctk
import re
from customtkinter import CTkEntry, StringVar, CTkButton
from string_validation import *
from dfa1_illustration import *
from dfa2_illustration import *
# from navigation_frames import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Automata Project")
        self.geometry("1080x700")
        self.resizable(True, True)

        # Create Navigation Frame
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

        # Create Home Frame
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.pack_configure(padx = 0, pady = 0, anchor = 'center')

        # Welcome Label
        self.welcome_label = ctk.CTkLabel(self.home_frame, text="WELCOME!\nChoose a regular expression to get started.")
        self.welcome_label.configure(font=(None, 25))
        self.welcome_label.pack_configure(padx = 20, pady = 30)

        # Set initial value for combobox
        regex = ctk.StringVar(value="RegEx 1")

        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)
            if (choice == "RegEx 1"):
                text = "(a+b) (a+b)* (aa+bb) (ab+ba) (a+b)* (aba+baa)"
            if (choice == "RegEx 2"):
                text = "(11+00) (1+0)* (101+111+01) (00*+11*) (1+0+11)"
            self.strings_label.configure(text=text)
            print(text)
            return text

        self.combobox = ctk.CTkComboBox(self.home_frame, values=["RegEx 1", "RegEx 2"], command=combobox_callback, variable=regex)
        self.combobox.pack_configure(padx = 20, pady = 10)

        self.strings_label = ctk.CTkLabel(self.home_frame, text="")
        self.strings_label.configure(font=(None, 20))
        self.strings_label.pack(padx = 20, pady = 20)

        self.entry = ctk.CTkEntry(self.home_frame, width = 400, placeholder_text="Enter String")
        self.entry.configure(font=(None, 15))
        self.entry.pack_configure(side = 'left', padx = 20, pady = 20, anchor = 'center')

        def validate_string():
            if (self.combobox.get() == "RegEx 1"):
                pattern = r"^[ab](?:[ab])*(?:aa|bb)(?:ab|ba)(?:[ab])*?(?:aba|baa)$"
            if (self.combobox.get() == "RegEx 2"):
                pattern = r"^(?:11|00)(?:1|0)*(?:101|111|01)(?:00*|11*)(?:1|0|11)$"
            result = validateString(pattern, self.entry.get())
            self.valid_label.configure(text=result)
            print(result)
            return result
            # validateString(pattern2, self.entry)
            # self.btn.configure(text=self.entry.get())

        self.btnValidateString = CTkButton(self.home_frame, text="Validate String", command=validate_string)
        self.btnValidateString.pack_configure(side = 'left', padx = 0, pady = 0, anchor = 'center')

        self.valid_label = ctk.CTkLabel(self.home_frame, text="")
        self.valid_label.pack_configure(side = 'left', padx = 20, pady = 30, anchor = 'center')

        # self.valid_label = ctk.CTkLabel(self.home_frame, text="string")
        # self.valid_label.pack(side = 'left', padx = 0, pady = 0, anchor = 'center')
        # self.valid_label.grid(row=0, column=1, padx=70, pady=200, sticky="s")

        # create second frame
        self.second_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.pack_configure(padx = 0, pady = 0, anchor = 'center')
        # self.second_frame.grid_columnconfigure(0, weight=1)
        # self.second_frame.pack()

        self.second_frame_label = ctk.CTkLabel(self.second_frame,
                                                         text="WELCOME!\n")
        self.second_frame_label.pack_configure(padx = 20, pady = 30)

        # Set initial value for combobox
        regex = ctk.StringVar(value="RegEx 1")

        # def string_select(choice):
        #     print("combobox dropdown clicked:", choice)
        #     if (choice == "RegEx 1"):
        #         text = "(a+b) (a+b)* (aa+bb) (ab+ba) (a+b)* (aba+baa)"
        #         draw_dfa1(self).pack()
        #         # draw_dfa2(self).pack_forget()
        #     # else:
        #     #     draw_dfa1(self).pack_forget()
        #     if (choice == "RegEx 2"):
        #         text = "(11+00) (1+0)* (101+111+01) (00*+11*) (1+0+11)"
        #         draw_dfa2(self).pack()
        #         # draw_dfa1(self).pack_forget()
        #     else:
        #         draw_dfa1(self).pack_forget() 
        #         draw_dfa2(self).pack_forget()              
        #     # else:
        #     #     draw_dfa2(self).pack_forget()
        #     self.strings_label2.configure(text=text)
        #     print(text)
        #     return text
        
        def string_select(choice):
            if (choice == "RegEx 1"):
                text = "(a+b) (a+b)* (aa+bb) (ab+ba) (a+b)* (aba+baa)"
                # draw_dfa2(self).pack_forget()  # Hide draw_dfa2 if it was displayed
                # draw_dfa2(self).clear()
                draw = draw_dfa1(self)  # Display draw_dfa1
                # draw_dfa2(self).forget()
            elif (choice == "RegEx 2"):
                text = "(11+00) (1+0)* (101+111+01) (00*+11*) (1+0+11)"
                # draw_dfa1(self).clear()
                # draw_dfa1(self).forget()  # Hide draw_dfa1 if it was displayed
                draw = draw_dfa2(self) # Display draw_dfa2
                # draw_dfa1(self).forget()
            self.strings_label2.configure(text=text)
            self.dfa_container.pack_configure(draw)
            return text

        self.combobox2 = ctk.CTkComboBox(self.second_frame, values=["RegEx 1", "RegEx 2"], command=string_select, variable=regex)
        self.combobox2.pack_configure(padx = 20, pady = 10)

        self.strings_label2 = ctk.CTkLabel(self.second_frame, text="")
        self.strings_label2.configure(font=(None, 20))
        self.strings_label2.pack(padx = 20, pady = 20)

        self.dfa_container = ctk.CTkCanvas(self.second_frame, width=2000, height=300)
        self.dfa_container.pack_configure(side = 'top', padx = 50, pady = 100, anchor = 's')
        # dfa_visual
        # draw_dfa().pack

        def draw_dfa():
            if (self.combobox2.get() == "RegEx 1"):
                return draw_dfa1(self)
            if (self.combobox2.get() == "RegEx 2"):
                return draw_dfa2(self)
            # self.strings_label.configure(text=text)
            # print(text)
            # return text

        # draw_dfa1(self)

        # create third frame
        self.third_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create fourth frame
        self.fourth_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.pack()
            # self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.pack_forget()
        if name == "frame_2":
            self.second_frame.pack()
            # self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.pack_forget()
        if name == "frame_3":
            self.third_frame.pack()
            # self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.pack_forget()
        if name == "frame_4":
            self.fourth_frame.pack()
            # self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.pack_forget()

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