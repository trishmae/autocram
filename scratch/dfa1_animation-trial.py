import customtkinter as ctk


class DFAApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("DFA Animation")
        self.geometry("1000x500")
        self.canvas = ctk.CTkCanvas(self, width=2000, height=500)
        self.canvas.pack()
        self.current_regex_index = 0
        self.regex_list = ["(a+b) (a+b)* (aa+bb) (ab+ba) (a+b)* (aba+baa)"]
        self.draw_dfa()
        self.validate_string()

    def draw_dfa(self):
        # Draw state circles
        self.state_coords = [
            (70, 120, 120, 170), (170, 60, 220, 110), (170, 195, 220, 245), (260, 120, 310, 170),
            (350, 60, 400, 110), (350, 195, 400, 245), (500, 60, 550, 110), (500, 195, 550, 245),
            (600, 120, 650, 170), (700, 60, 750, 110), (700, 195, 750, 245), (800, 120, 850, 170),
            (900, 120, 950, 170)
        ]
        self.states = []
        for i, coord in enumerate(self.state_coords):
            state = self.canvas.create_oval(coord[0], coord[1], coord[2], coord[3], fill='white')
            self.states.append(state)

        # Draw state labels
            state_labels = ['-', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', '+']
            for i, coord in enumerate(self.state_coords):
                x = (coord[0] + coord[2]) / 2
                y = (coord[1] + coord[3]) / 2
                label = state_labels[i]
                self.canvas.create_text(x, y, text=label)

        # Draw transitions
        self.transition_coords = [
            (100, 120, 170, 85), (100, 170, 170, 220), (220, 85, 280, 120), (300, 125, 350, 90),
            (195, 110, 200, 150, 260, 145), (195, 195, 200, 150, 260, 155), (220, 220, 285, 170),
            (290, 170, 350, 220), (400, 90, 500, 90), (400, 220, 500, 220),
            (380, 195, 525, 110), (385, 110, 525, 195), (510, 65, 520, 10, 540, 60),
            (510, 240, 520, 300, 540, 245), (550, 220, 625, 170), (550, 85, 625, 120),
            (645, 130, 705, 95), (640, 165, 700, 210), (750, 90, 810, 125), (750, 220, 820, 170),
            (715, 200, 700, 150, 715, 110), (740, 105, 760, 150, 740, 195),
            (820, 120, 830, 50, 840, 120), (850, 150, 900, 150), (910, 125, 920, 60, 940, 120),
            (910, 170, 875, 200, 840, 170)]

        self.transitions = []
        for coord in self.transition_coords:
            transition = self.canvas.create_line(coord, arrow=ctk.LAST, fill="black", width=2, tags="transition",
                                                 smooth=True)
            self.transitions.append(transition)

            self.canvas.create_text(130, 90, text='a')  # - -q1
            self.canvas.create_text(130, 210, text='b')  # - - q2
            self.canvas.create_text(250, 90, text='a')  # q1 - q3
            self.canvas.create_text(257, 205, text='b')  # q2 - q3
            self.canvas.create_text(210, 120, text='b')  # q1 - q3 curve
            self.canvas.create_text(210, 180, text='a')  # q2 -q3   curve
            self.canvas.create_text(315, 100, text='a')  # q3 -q4
            self.canvas.create_text(315, 205, text='b')  # q3 -q5
            self.canvas.create_text(450, 70, text='a')  # q4 -q6
            self.canvas.create_text(410, 110, text='b')  # q4 -q7
            self.canvas.create_text(395, 170, text='a')  # q5 -q6
            self.canvas.create_text(550, 40, text='a')  # q6 rotate
            self.canvas.create_text(450, 240, text='b')  # q5 -q7
            self.canvas.create_text(550, 260, text='b')  # q7 rotate
            self.canvas.create_text(615, 100, text='b')  # q6 -q8
            self.canvas.create_text(595, 200, text='a')  # q7 -q8
            self.canvas.create_text(670, 200, text='b')  # q8-q10
            self.canvas.create_text(670, 100, text='a')  # q8 -q9
            self.canvas.create_text(700, 180, text='b')  # q10 -q9
            self.canvas.create_text(760, 120, text='a')  # q9 -q10
            self.canvas.create_text(770, 85, text='b')  # q9 -q11
            self.canvas.create_text(850, 95, text='b')  # q11 rotate
            self.canvas.create_text(790, 200, text='a')  # q10 - q11
            self.canvas.create_text(870, 140, text='a')  # q11 - +
            self.canvas.create_text(950, 100, text='a')  # + rotate
            self.canvas.create_text(870, 200, text='b')  # + rotate

    def validate_string(self):
        current_regex = self.regex_list[self.current_regex_index]
        self.current_regex_index = (self.current_regex_index + 1) % len(self.regex_list)

        # Reset colors to default
        self.canvas.itemconfig("transition", fill="black")

        # Start state
        current_state = 'q0'
        transition_id = self.states[0]
        self.canvas.itemconfig(transition_id, fill="green")
        self.canvas.update()
        self.canvas.after(1000)  # Pause for 1 second

        string = input("Enter a string to validate: ")
        current_state = 'q0'

        # Define the state transition table
        transitions = {
            'q0': {'a': ('q1', self.states[1]), 'b': ('q2', self.states[2])},
            'q1': {'a': ('q3', self.states[3]), 'b': ('q3', self.states[3])},
            'q2': {'a': ('q3', self.states[3]), 'b': ('q3', self.states[3])},
            'q3': {'a': ('q4', self.states[4]), 'b': ('q5', self.states[5])},
            'q4': {'a': ('q6', self.states[6]), 'b': ('q7', self.states[7])},
            'q5': {'a': ('q6', self.states[6]), 'b': ('q7', self.states[7])},
            'q6': {'a': ('q6', self.states[6]), 'b': ('q8', self.states[8])},
            'q7': {'a': ('q8', self.states[8]), 'b': ('q7', self.states[7])},
            'q8': {'a': ('q9', self.states[9]), 'b': ('q10', self.states[10])},
            'q9': {'a': ('q10', self.states[10]), 'b': ('q11', self.states[11])},
            'q10': {'a': ('q11', self.states[11]), 'b': ('q9', self.states[9])},
            'q11': {'a': ('q12', self.states[12]), 'b': ('q11', self.states[11])},
            'q12': {'a': ('q12', self.states[12]), 'b': ('q11', self.states[11])}
        }

        # Iterate over symbols in the string
        for symbol in string:
            # Update current state based on symbol
            if symbol in transitions[current_state]:
                current_state, transition_id = transitions[current_state][symbol]
            else:
                current_state = 'q13'  # Invalid state
                transition_id = None

            # Highlight the transition
            if transition_id is not None:
                self.canvas.itemconfig(transition_id, fill="green")
                self.canvas.update()
                self.canvas.after(1000)  # Pause for 1 second

        if current_state == 'q12':
            print("Valid string.")
        else:
            print("Invalid string.")
            self.canvas.itemconfig(transition_id, fill="red")

        self.canvas.update()



    def run(self):
        self.validate_string()
        self.mainloop()

if __name__ == "__main__":
    app = DFAApplication()
    app.run()
