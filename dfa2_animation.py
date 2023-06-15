# DFA 2 Animation

import customtkinter as ctk

def draw_dfa2(self):
    self.state_coords = [
        (70, 120, 120, 170), (170, 50, 220, 100), (170, 195, 220, 245), (170, 120, 220, 170),
        (290, 50, 340, 100), (290, 195, 340, 245), (410, 50, 460, 100), (410, 195, 460, 245),
        (530, 50, 580, 100), (650, 50, 700, 100), (650, 195, 700, 245), (770, 50, 820, 100),
        (770, 195, 820, 245), (890, 50, 940, 100), (890, 195, 940, 245)
    ]
    self.states = []
    for i, coord in enumerate(self.state_coords):
        state = self.dfa_container.create_oval(coord[0], coord[1], coord[2], coord[3], fill='white')
        self.states.append(state)

        # Draw state labels
        state_labels = ['-', 'q1', 'q2', 'T', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', '+', '+']
    for i, coord in enumerate(self.state_coords):
        x = (coord[0] + coord[2]) / 2
        y = (coord[1] + coord[3]) / 2
        label = state_labels[i]
        self.dfa_container.create_text(x, y, text=label)

    # Draw transitions
    self.transition_coords = [
        (113, 127, 175, 90), (109, 165, 173, 210), (195, 100, 195, 120), (195, 195, 195, 170),
        (220, 75, 290, 75), (220, 220, 290, 220), (340, 75, 410, 75),
        (340, 220, 410, 220), (460, 75, 530, 75), (580, 75, 650, 75),
        (460, 220, 650, 220), (700, 75, 770, 75), (700, 220, 770, 220),
        (820, 75, 890, 75), (820, 220, 890, 220), (315, 195, 420, 93),
        (315, 100, 420, 203), (435, 100, 435, 195), (555, 100, 450, 200), (460, 210, 660, 93),
        (675, 195, 795, 100), (675, 100, 795, 195),
        (220, 135, 290, 145, 220, 155), (925, 98, 910, 170, 905, 100), (905, 198, 910, 130, 925, 200)
    ]

    self.transitions = []
    for coord in self.transition_coords:
        transition = self.dfa_container.create_line(coord, arrow=ctk.LAST, fill="black", width=2, tags="transition",
                                                        smooth=True)
        self.transitions.append(transition)

    # Transition labels            x     y
    self.dfa_container.create_text(130, 90, text='1')  # - -q1
    self.dfa_container.create_text(130, 210, text='0')  # - - q2
    self.dfa_container.create_text(250, 65, text='1')  # q1 - q3
    self.dfa_container.create_text(250, 230, text='0')  # q2 - q4
    self.dfa_container.create_text(245, 130, text='0, 1')  # T curve
    self.dfa_container.create_text(210, 110, text='0')  # q1 - T
    self.dfa_container.create_text(210, 185, text='1')  # q2 - T
    self.dfa_container.create_text(370, 65, text='1')  # q3 - q5
    self.dfa_container.create_text(370, 230, text='0')  # q4 - q6
    self.dfa_container.create_text(490, 65, text='1')  # q5 - q7
    self.dfa_container.create_text(550, 230, text='1')  # q6 - q9
    self.dfa_container.create_text(610, 65, text='1')  # q7 - q8
    self.dfa_container.create_text(730, 65, text='1')  # q8 - q10
    self.dfa_container.create_text(730, 230, text='0')  # q9 - q11
    self.dfa_container.create_text(850, 65, text='0, 1')  # q10 - +
    self.dfa_container.create_text(850, 230, text='0, 1')  # q11 - +
    self.dfa_container.create_text(330, 130, text='0')  # q3 - q6
    self.dfa_container.create_text(330, 165, text='1')  # q4 - q5
    self.dfa_container.create_text(420, 145, text='0')  # q5 - q6
    self.dfa_container.create_text(490, 145, text='0')  # q7 - q6
    self.dfa_container.create_text(560, 165, text='0')  # q6 - q8
    self.dfa_container.create_text(690, 130, text='0')  # q8 - q11
    self.dfa_container.create_text(690, 170, text='1')  # q9 - q10
    self.dfa_container.create_text(930, 130, text='0, 1')  # + curve
    self.dfa_container.create_text(930, 170, text='0, 1')  # + curve

    # # Create string validation components
    # self.entry = ctk.CTkEntry(self.second_frame, width=400, placeholder_text="Enter String")
    # self.entry.configure(font=(None, 15))
    # self.entry.pack_configure(side='left', padx=20, pady=20, anchor='center')

    # self.btnValidateString = ctk.CTkButton(self.second_frame, text="Validate String", command=self.validate_dfa)
    # self.btnValidateString.pack_configure(side='left', padx=0, pady=0, anchor='center')

    # self.valid_label = ctk.CTkLabel(self.second_frame, text="")
    # self.valid_label.pack_configure(side='left', padx=20, pady=30, anchor='center')

# def validate_dfa(self):
#     input_string = self.entry.get()
#     self.animate_dfa(input_string)

def animate_dfa2(self, input_string):
    draw_dfa2(self)

    current_state = 0  # Start from the initial state

    transitions = {
        0: {'1': 1, '0': 2},
        1: {'1': 4, '0': 3},
        2: {'1': 3, '0': 5},
        3: {'1': 3, '0': 3},  # trapstate
        4: {'1': 6, '0': 7},
        5: {'1': 6, '0': 7},
        6: {'1': 8, '0': 7},
        7: {'1': 10, '0': 9},
        8: {'1': 9, '0': 7},
        9: {'1': 11, '0': 12},
        10: {'1': 11, '0': 12},
        11: {'1': 13, '0': 13},
        12: {'1': 14, '0': 14},
        13: {'1': 13, '0': 13},
        14: {'1': 14, '0': 14}

    }

    for char in input_string:
        # Highlight the current state
        self.dfa_container.itemconfigure(self.states[current_state], fill='yellow')
        self.update()
        self.after(1000)  # Pause for 1 second

        # Reset the fill color of the previous state
        self.dfa_container.itemconfigure(self.states[current_state], fill='white')

        # Get the next state based on the current state and input character
        next_state = transitions[current_state].get(char)
        if next_state is None:
            print(f"Rejected: No transition for input '{char}' from state {current_state}")
            return

        current_state = next_state

    # Highlight the final state
    self.dfa_container.itemconfigure(self.states[current_state], fill='yellow')
    self.update()
    self.after(1000)  # Pause for 1 second

    # Reset the fill color of the final state
    self.dfa_container.itemconfigure(self.states[current_state], fill='white')

    # Check if the final state is accepting or not
    if current_state == 12:
        self.dfa_container.itemconfigure(self.states[current_state], fill='green')
        self.valid_label.configure(text="Accepted")
    else:
        self.dfa_container.itemconfigure(self.states[current_state], fill='red')
        self.valid_label.configure(text="Rejected")
