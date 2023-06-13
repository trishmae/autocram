import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Automata Project")
        self.geometry("1080x700")
        self.resizable(True, True)

        combobox_var = ctk.StringVar(value="option 2")  # set initial value

        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)

        combobox = ctk.CTkComboBox(self, values=["option 1", "option 2"],
                                     command=combobox_callback,
                                     variable=combobox_var)
        combobox.pack(padx=20, pady=10)

app = App()
app.mainloop()