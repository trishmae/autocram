# Automata Main

from tkinter import Widget, PhotoImage, Canvas
import customtkinter as ctk
import re
from customtkinter import CTkEntry, StringVar, CTkButton
from string_validation import *
# from dfa1_illustration import *
# from dfa2_illustration import *
from dfa1_animation import *
from dfa2_animation import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Automata Project")
        self.geometry("1300x650")
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

        # Create Home Frame: User Manual
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.pack_configure(padx = 0, pady = 0, anchor = 'center')

        # User Manual Label
        self.welcome_label = ctk.CTkLabel(self.home_frame, text="User Manual")
        self.welcome_label.configure(font=(None, 25))
        self.welcome_label.pack_configure(padx = 20, pady = 30)

        # Create Second Frame: DFA
        self.second_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.pack_configure(padx = 0, pady = 0, anchor = 'center')

        self.second_frame_label = ctk.CTkLabel(self.second_frame, text="Deterministic Finite Automata (DFA)\n")
        self.second_frame_label.pack_configure(padx = 20, pady = 30)

        # Set initial value for combobox
        regex = ctk.StringVar(value="RegEx 1")

        def string_select(choice):
            if choice == "RegEx 1":
                text = "(a+b) (a+b)* (aa+bb) (ab+ba) (a+b)* (aba+baa)"
                self.dfa_container.delete("all")  # Clear the canvas
                draw = draw_dfa1(self)  # Display draw_dfa1
            elif choice == "RegEx 2":
                text = "(11+00) (1+0)* (101+111+01) (00*+11*) (1+0+11)"
                self.dfa_container.delete("all")  # Clear the canvas
                draw = draw_dfa2(self)  # Display draw_dfa2
            self.strings_label2.configure(text=text)
            self.dfa_container.pack_configure(draw)
            return text

        self.combobox2 = ctk.CTkComboBox(self.second_frame, values=["RegEx 1", "RegEx 2"], command=string_select, variable=regex)
        self.combobox2.pack_configure(padx = 20, pady = 10)

        # Label that will display the chosen Regex
        self.strings_label2 = ctk.CTkLabel(self.second_frame, text="")
        self.strings_label2.configure(font=(None, 20))
        self.strings_label2.pack(padx = 20, pady = 20)

        # DFA Container
        self.dfa_container = ctk.CTkCanvas(self.second_frame, width=2000, height=300)
        self.dfa_container.pack_configure(side = 'top', padx = 50, pady = 10, anchor = 's')

        # Entry Widget where user enters a string to validate
        self.entry = ctk.CTkEntry(self.second_frame, width=400, placeholder_text="Enter String")
        self.entry.configure(font=(None, 15))
        self.entry.pack_configure(side='top', padx=20, pady=20, anchor='center')

        # Function to validate a string
        def validate_string():
            if (self.combobox2.get() == "RegEx 1"):
                pattern = r"^[ab](?:[ab])*(?:aa|bb)(?:ab|ba)(?:[ab])*?(?:aba|baa)$"
            if (self.combobox2.get() == "RegEx 2"):
                pattern = r"^(?:11|00)(?:1|0)*(?:101|111|01)(?:00*|11*)(?:1|0|11)$"
            result = validateString(pattern, self.entry.get())
            self.valid_label.configure(text=result)
            print(result)
            return result
        
        # Function to animate a string
        def animate_string():
            if (self.combobox2.get() == "RegEx 1"):
                self.dfa_container.delete("all")
                ani = animate_dfa1(self, self.entry.get())
            elif (self.combobox2.get() == "RegEx 2"):
                self.dfa_container.delete("all")
                ani = animate_dfa2(self, self.entry.get())
            # self.dfa_container.delete("all")  # Clear the canvas
            self.dfa_container.pack_configure(ani)

        # Button to validate string
        self.btnValidateString = CTkButton(self.second_frame, text="Validate String", command=validate_string)
        self.btnValidateString.pack_configure(side='top', padx=0, pady=0, anchor='center')
        
        # Label that will indicate 'Valid String' or 'Invalid String'
        self.valid_label = ctk.CTkLabel(self.second_frame, text="")
        self.valid_label.pack_configure(side='top', padx=0, pady=0, anchor='center')

        # Button to animate string
        self.btnValidateString = CTkButton(self.second_frame, text="Animate String", command=animate_string)
        self.btnValidateString.pack_configure(side='top', padx=0, pady=0, anchor='center')

        # Create Third Frame: CFG
        self.third_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.pack_configure(padx = 0, pady = 0, anchor = 'center')

        self.third_frame_label = ctk.CTkLabel(self.third_frame, text="Context-Free Grammar (CFG)\n")
        self.third_frame_label.pack_configure(padx = 20, pady = 30)

        # Set initial value for combobox
        regex = ctk.StringVar(value="RegEx 1")

        # CFG Pictures
        self.cfg1 = PhotoImage(file="CFG1.png")
        self.cfg2 = PhotoImage(file="CFG2.png")

        def display_cfg(choice):
            if choice == "RegEx 1":
                text = "(a+b) (a+b)* (aa+bb) (ab+ba) (a+b)* (aba+baa)"
                self.cfg_container.delete("all")  # Clear the canvas
                cfg = self.cfg_container.create_image(200, 200, image=self.cfg1)
            elif choice == "RegEx 2":
                text = "(11+00) (1+0)* (101+111+01) (00*+11*) (1+0+11)"
                self.cfg_container.delete("all")  # Clear the canvas
                cfg = self.cfg_container.create_image(200, 200, image=self.cfg2)
            self.strings_label3.configure(text=text)
            self.cfg_container.pack_configure(cfg)
            return text

        # CFG Container
        self.combobox3 = ctk.CTkComboBox(self.third_frame, values=["RegEx 1", "RegEx 2"], command=display_cfg, variable=regex)
        self.combobox3.pack_configure(padx = 20, pady = 10)

        # Label that will display the chosen Regex
        self.strings_label3 = ctk.CTkLabel(self.third_frame, text="")
        self.strings_label3.configure(font=(None, 20))
        self.strings_label3.pack(padx = 20, pady = 20)

        self.cfg_container = ctk.CTkCanvas(self.third_frame, width=400, height=400)
        self.cfg_container.pack_configure(side = 'top', padx = 50, pady = 10, anchor = 's')

        # Create Fourth Frame: PDA
        self.fourth_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fourth_frame.pack_configure(padx = 0, pady = 0, anchor = 'center')

        self.fourth_frame_label = ctk.CTkLabel(self.fourth_frame, text="Pushdown Automata (PDA)\n")
        self.fourth_frame_label.pack_configure(padx = 20, pady = 30)

        # Set initial value for combobox
        regex = ctk.StringVar(value="RegEx 1")

        # PDA pictures
        self.pda1 = PhotoImage(file="PDA1.png")
        self.pda2 = PhotoImage(file="PDA2.png")

        def display_pda(choice):
            if choice == "RegEx 1":
                text = "(a+b) (a+b)* (aa+bb) (ab+ba) (a+b)* (aba+baa)"
                self.pda_container.delete("all")  # Clear the canvas
                pda = self.pda_container.create_image(610, 200, image=self.pda1)
            elif choice == "RegEx 2":
                text = "(11+00) (1+0)* (101+111+01) (00*+11*) (1+0+11)"
                self.pda_container.delete("all")  # Clear the canvas
                pda = self.pda_container.create_image(450, 200, image=self.pda2)
            self.strings_label4.configure(text=text)
            self.pda_container.pack_configure(pda)
            return text

        self.combobox4 = ctk.CTkComboBox(self.fourth_frame, values=["RegEx 1", "RegEx 2"], command=display_pda, variable=regex)
        self.combobox4.pack_configure(padx = 20, pady = 10)

        # Label that will display the chosen Regex
        self.strings_label4 = ctk.CTkLabel(self.fourth_frame, text="")
        self.strings_label4.configure(font=(None, 20))
        self.strings_label4.pack(padx = 20, pady = 20)

        # PDA Container
        self.pda_container = ctk.CTkCanvas(self.fourth_frame, width=1220, height=400)
        self.pda_container.pack_configure(side = 'top', padx = 50, pady = 10, anchor = 's')

        # Select default frame
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
        else:
            self.home_frame.pack_forget()
        if name == "frame_2":
            self.second_frame.pack()
        else:
            self.second_frame.pack_forget()
        if name == "frame_3":
            self.third_frame.pack()
        else:
            self.third_frame.pack_forget()
        if name == "frame_4":
            self.fourth_frame.pack()
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