# DFA 1 Animation

import customtkinter as ctk

def draw_dfa1(self):
    self.state_coords = [
        (70, 120, 120, 170), (170, 60, 220, 110), (170, 195, 220, 245), (260, 120, 310, 170),
        (350, 60, 400, 110), (350, 195, 400, 245), (500, 60, 550, 110), (500, 195, 550, 245),
        (600, 120, 650, 170), (700, 60, 750, 110), (700, 195, 750, 245), (800, 120, 850, 170),
        (900, 120, 950, 170)
    ]
    self.states = []
    for i, coord in enumerate(self.state_coords):
        state = self.dfa_container.create_oval(coord[0], coord[1], coord[2], coord[3], fill='white')
        self.states.append(state)

    # Draw state labels
    state_labels = ['-', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', '+']
    for i, coord in enumerate(self.state_coords):
        x = (coord[0] + coord[2]) / 2
        y = (coord[1] + coord[3]) / 2
        label = state_labels[i]
        self.dfa_container.create_text(x, y, text=label)

    self.transition_coords = [
        (100, 120, 170, 85), (100, 170, 170, 220), (220, 85, 280, 120), (300, 125, 350, 90),
        (195, 110, 200, 150, 260, 145), (195, 195, 200, 150, 260, 155), (220, 220, 285, 170),
        (290, 170, 350, 220), (400, 90, 500, 90), (400, 220, 500, 220),
        (380, 195, 525, 110), (385, 110, 525, 195), (510, 65, 520, 10, 540, 60),
        (510, 240, 520, 300, 540, 245), (550, 220, 625, 170), (550, 85, 625, 120),
        (645, 130, 705, 95), (640, 165, 700, 210), (750, 90, 810, 125), (750, 220, 820, 170),
        (715, 200, 700, 150, 715, 110), (740, 105, 760, 150, 740, 195),
        (820, 120, 830, 50, 840, 120), (850, 150, 900, 150), (910, 125, 920, 60, 940, 120),
        (910, 170, 875, 200, 840, 170)
    ]

    self.transitions = []
    for coord in self.transition_coords:
        transition = self.dfa_container.create_line(coord, arrow=ctk.LAST, fill="black", width=2, tags="transition",
                                                        smooth=True)
        self.transitions.append(transition)

    self.dfa_container.create_text(130, 90, text='a')  # - -q1
    self.dfa_container.create_text(130, 210, text='b')  # - - q2
    self.dfa_container.create_text(250, 90, text='a')  # q1 - q3
    self.dfa_container.create_text(257, 205, text='b')  # q2 - q3
    self.dfa_container.create_text(210, 120, text='b')  # q1 - q3 curve
    self.dfa_container.create_text(210, 180, text='a')  # q2 -q3   curve
    self.dfa_container.create_text(315, 100, text='a')  # q3 -q4
    self.dfa_container.create_text(315, 205, text='b')  # q3 -q5
    self.dfa_container.create_text(450, 70, text='a')  # q4 -q6
    self.dfa_container.create_text(410, 110, text='b')  # q4 -q7
    self.dfa_container.create_text(395, 170, text='a')  # q5 -q6
    self.dfa_container.create_text(550, 40, text='a')  # q6 rotate
    self.dfa_container.create_text(450, 240, text='b')  # q5 -q7
    self.dfa_container.create_text(550, 260, text='b')  # q7 rotate
    self.dfa_container.create_text(615, 100, text='b')  # q6 -q8
    self.dfa_container.create_text(595, 200, text='a')  # q7 -q8
    self.dfa_container.create_text(670, 200, text='b')  # q8-q10
    self.dfa_container.create_text(670, 100, text='a')  # q8 -q9
    self.dfa_container.create_text(700, 180, text='b')  # q10 -q9
    self.dfa_container.create_text(760, 120, text='a')  # q9 -q10
    self.dfa_container.create_text(770, 85, text='b')  # q9 -q11
    self.dfa_container.create_text(850, 95, text='b')  # q11 rotate
    self.dfa_container.create_text(790, 200, text='a')  # q10 - q11
    self.dfa_container.create_text(870, 140, text='a')  # q11 - +
    self.dfa_container.create_text(950, 100, text='a')  # + rotate
    self.dfa_container.create_text(870, 200, text='b')  # + rotate

def animate_dfa1(self, input_string):
    draw_dfa1(self)

    current_state = 0  # Start from the initial state

    transitions = {
        0: {'a': 1, 'b': 2},
        1: {'a': 3, 'b': 3},
        2: {'a': 3, 'b': 3},
        3: {'a': 4, 'b': 5},
        4: {'a': 6, 'b': 7},
        5: {'a': 6, 'b': 7},
        6: {'a': 6, 'b': 8},
        7: {'a': 8, 'b': 7},
        8: {'a': 9, 'b': 10},
        9: {'a': 10, 'b': 11},
        10: {'a': 11, 'b': 9},
        11: {'a': 12, 'b': 11},
        12: {'a': 12, 'b': 11}
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


