# DFA FOR REGEX 2

import customtkinter as ctk

def draw_dfa1(self):
    
    # self.dfa_container = ctk.CTkCanvas(self.second_frame, width=2000, height=300)
    # self.dfa_container.pack_configure(side = 'top', padx = 50, pady = 100, anchor = 's')

    # Draw state circles
    q0_circle = self.dfa_container.create_oval(70, 120, 120, 170, fill='lightblue')
    q1_circle = self.dfa_container.create_oval(170, 60, 220, 110, fill='lightblue')
    q2_circle = self.dfa_container.create_oval(170, 195, 220, 245, fill='lightblue')
    q3_circle = self.dfa_container.create_oval(260, 120, 310, 170, fill='lightblue')
    q4_circle = self.dfa_container.create_oval(350, 60, 400, 110, fill='lightblue')
    q5_circle = self.dfa_container.create_oval(350, 195, 400, 245, fill='lightblue')
    q6_circle = self.dfa_container.create_oval(500, 60, 550, 110, fill='lightblue')
    q7_circle = self.dfa_container.create_oval(500, 195, 550, 245, fill='lightblue')
    q8_circle = self.dfa_container.create_oval(600, 120, 650, 170, fill='lightblue')
    q9_circle = self.dfa_container.create_oval(700, 60, 750, 110, fill='lightblue')
    q10_circle = self.dfa_container.create_oval(700, 195, 750, 245, fill='lightblue')
    q8_circle = self.dfa_container.create_oval(800, 120, 850, 170, fill='lightblue')
    q8_circle = self.dfa_container.create_oval(900, 120, 950, 170, fill='lightblue')
    
    # Draw state labels
    # higa  #haba
    self.dfa_container.create_text(95, 145, text='-')
    self.dfa_container.create_text(195, 85, text='q1')
    self.dfa_container.create_text(195, 220, text='q2')
    self.dfa_container.create_text(285, 145, text='q3')
    self.dfa_container.create_text(375, 85, text='q4')
    self.dfa_container.create_text(375, 220, text='q5')
    self.dfa_container.create_text(525, 85, text='q6')
    self.dfa_container.create_text(525, 220, text='q7')
    self.dfa_container.create_text(625, 145, text='q8')
    self.dfa_container.create_text(725, 85, text='q9')
    self.dfa_container.create_text(725, 220, text='q10')
    self.dfa_container.create_text(825, 145, text='q11')
    self.dfa_container.create_text(925, 145, text='+')
    
    # start   end
    # Draw transitions             #x y     x  y
    self.dfa_container.create_line(100, 120, 170, 85, arrow=ctk.LAST)  # - - q1
    self.dfa_container.create_line(100, 169, 170, 220, arrow=ctk.LAST)  # - - q2
    self.dfa_container.create_line(220, 85, 280, 120, arrow=ctk.LAST)  # q1 - q3
    self.dfa_container.create_line(300, 125, 350, 90, arrow=ctk.LAST)  # q2 - q3
    self.dfa_container.create_line(195, 110, 200, 150, 260, 145, smooth=True, arrow=ctk.LAST)  # q1 - q3
    self.dfa_container.create_line(195, 195, 200, 150, 260, 155, smooth=True, arrow=ctk.LAST)  # q2 - q3
    self.dfa_container.create_line(220, 220, 285, 170, arrow=ctk.LAST)  # q3 -q4
    self.dfa_container.create_line(290, 170, 350, 220, arrow=ctk.LAST)  # q3 - q5
    self.dfa_container.create_line(400, 90, 500, 90, arrow=ctk.LAST)  # q4-q6
    self.dfa_container.create_line(400, 220, 500, 220, arrow=ctk.LAST)  # q5-q7
    self.dfa_container.create_line(380, 195, 525, 110, arrow=ctk.LAST)  # q5-q6
    self.dfa_container.create_line(385, 110, 525, 195, arrow=ctk.LAST)  # q4-q7
    self.dfa_container.create_line(510, 65, 520, 10, 540, 60, smooth=True, arrow=ctk.LAST)  # rotate q6
    self.dfa_container.create_line(510, 240, 520, 300, 540, 245, smooth=True, arrow=ctk.LAST)  # rotate q7
    self.dfa_container.create_line(550, 220, 625, 170, arrow=ctk.LAST)  # q7-q8
    self.dfa_container.create_line(550, 85, 625, 120, arrow=ctk.LAST)  # q6-q8
    self.dfa_container.create_line(645, 130, 705, 95, arrow=ctk.LAST)  # q8-q9
    self.dfa_container.create_line(640, 165, 700, 210, arrow=ctk.LAST)  # q8-q10
    self.dfa_container.create_line(750, 90, 810, 125, arrow=ctk.LAST)  # q9-q11
    self.dfa_container.create_line(750, 220, 820, 170, arrow=ctk.LAST)  # q10-q11
    self.dfa_container.create_line(715, 200, 700, 150, 715, 110, smooth=True, arrow=ctk.LAST)  # q10-q9
    self.dfa_container.create_line(740, 105, 760, 150, 740, 195, smooth=True, arrow=ctk.LAST)  # q9-q10
    self.dfa_container.create_line(820, 120, 830, 50, 840, 120, smooth=True, arrow=ctk.LAST)  # rotate 11
    self.dfa_container.create_line(850, 150, 900, 150, arrow=ctk.LAST)  # q11 - +
    self.dfa_container.create_line(910, 125, 920, 60, 940, 120, smooth=True, arrow=ctk.LAST)  # rotate +
    self.dfa_container.create_line(910, 170, 875, 200, 840, 170, smooth=True, arrow=ctk.LAST)  # + - q11
    
    # Transition labels            HABA HIGA
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


    