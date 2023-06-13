# DFA FOR REGEX 2

import customtkinter as ctk

def draw_dfa2(self):

    # self.dfa_container = ctk.CTkCanvas(self.second_frame, width=2000, height=300)
    # self.dfa_container.pack_configure(side = 'top', padx = 50, pady = 100, anchor = 's')

    # Draw state circles
    q0_circle = self.dfa_container.create_oval(70, 120, 120, 170, fill='lightblue')
    q1_circle = self.dfa_container.create_oval(170, 50, 220, 100, fill='lightblue')
    q2_circle = self.dfa_container.create_oval(170, 195, 220, 245, fill='lightblue')
    t_circle = self.dfa_container.create_oval(170, 120, 220, 170, fill='lightblue')
    q3_circle = self.dfa_container.create_oval(290, 50, 340, 100, fill='lightblue')
    q4_circle = self.dfa_container.create_oval(290, 195, 340, 245, fill='lightblue')
    q5_circle = self.dfa_container.create_oval(410, 50, 460, 100, fill='lightblue')
    q6_circle = self.dfa_container.create_oval(410, 195, 460, 245, fill='lightblue')
    q7_circle = self.dfa_container.create_oval(530, 50, 580, 100, fill='lightblue')
    q8_circle = self.dfa_container.create_oval(650, 50, 700, 100, fill='lightblue')
    q9_circle = self.dfa_container.create_oval(650, 195, 700, 245, fill='lightblue')
    q10_circle = self.dfa_container.create_oval(770, 50, 820, 100, fill='lightblue')
    q11_circle = self.dfa_container.create_oval(770, 195, 820, 245, fill='lightblue')
    q12_circle = self.dfa_container.create_oval(890, 50, 940, 100, fill='lightblue')
    q13_circle = self.dfa_container.create_oval(890, 195, 940, 245, fill='lightblue')

    # Draw state labels
                                 #higa  #haba
    self.dfa_container.create_text(95, 145, text='-')
    self.dfa_container.create_text(195, 75, text='q1')
    self.dfa_container.create_text(195, 220, text='q2')
    self.dfa_container.create_text(195, 145, text='T')
    self.dfa_container.create_text(315, 75, text='q3')
    self.dfa_container.create_text(315, 220, text='q4')
    self.dfa_container.create_text(435, 75, text='q5')
    self.dfa_container.create_text(435, 220, text='q6')
    self.dfa_container.create_text(555, 75, text='q7')
    self.dfa_container.create_text(675, 75, text='q8')
    self.dfa_container.create_text(675, 220, text='q9')
    self.dfa_container.create_text(795, 75, text='q10')
    self.dfa_container.create_text(795, 220, text='q11')
    self.dfa_container.create_text(915, 75, text='+')
    self.dfa_container.create_text(915, 220, text='+')

                                   #start   end
    # Draw transitions             #x y     x  y
    self.dfa_container.create_line(113, 127, 175, 90, arrow=ctk.LAST)  # - -q1
    self.dfa_container.create_line(109, 165, 173, 210, arrow=ctk.LAST) #-- q2
    self.dfa_container.create_line(195, 100, 195, 120, arrow=ctk.LAST)  # q1 - T
    self.dfa_container.create_line(195, 195, 195, 170, arrow=ctk.LAST) # q2 - T
    self.dfa_container.create_line(220, 75, 290, 75, arrow=ctk.LAST)  # q1-q3
    self.dfa_container.create_line(220, 220, 290, 220, arrow=ctk.LAST)  # q2-q4
    self.dfa_container.create_line(340, 75, 410, 75, arrow=ctk.LAST)  # q3-q5
    self.dfa_container.create_line(340, 220, 410, 220, arrow=ctk.LAST)  # q4-q6
    self.dfa_container.create_line(460, 75, 530, 75, arrow=ctk.LAST)  # q5-q7
    self.dfa_container.create_line(580, 75, 650, 75, arrow=ctk.LAST)  # q7-q8
    self.dfa_container.create_line(460, 220, 650, 220, arrow=ctk.LAST)  # q6-q9
    self.dfa_container.create_line(700, 75, 770, 75, arrow=ctk.LAST)  # q8-q10
    self.dfa_container.create_line(700, 220, 770, 220, arrow=ctk.LAST)  # q9-q11
    self.dfa_container.create_line(820, 75, 890, 75, arrow=ctk.LAST)  # q10- +
    self.dfa_container.create_line(820, 220, 890, 220, arrow=ctk.LAST)  # q11- +
    self.dfa_container.create_line(315, 195, 420, 93, arrow=ctk.LAST)  # q5-q6
    self.dfa_container.create_line(315, 100, 420, 203, arrow=ctk.LAST)  # q4-q7

    self.dfa_container.create_line(435, 100, 435, 195, arrow=ctk.LAST)  # q6 - q7

    self.dfa_container.create_line(555, 100, 450, 200, arrow=ctk.LAST)  # q8-q7
    self.dfa_container.create_line(460, 210, 660, 93, arrow=ctk.LAST)  # q7-q9

    self.dfa_container.create_line(675, 195, 795, 100, arrow=ctk.LAST)  # q10-q11
    self.dfa_container.create_line(675, 100, 795, 195, arrow=ctk.LAST)  # q9-q12

    self.dfa_container.create_line(220, 135, 290, 145, 220, 155, smooth=True, arrow=ctk.LAST)  # rotate T

    self.dfa_container.create_line(925, 98, 910, 170, 905, 100, smooth=True, arrow=ctk.LAST)  # rotate +

    self.dfa_container.create_line(905, 198, 910, 130, 925, 200, smooth=True, arrow=ctk.LAST)  # rotate +




    # Transition labels            x     y
    self.dfa_container.create_text(130, 90, text='1')  # - -q1
    self.dfa_container.create_text(130, 210, text='0')  # - - q2
    self.dfa_container.create_text(250, 65, text='1')   # q1 - q3
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
    

