import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter App")
        self.geometry("400x200")

        self.label = ttk.Label(self, text="Hello, World!")
        self.label.pack(pady=10)

        self.button = ttk.Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        self.label.config(text="Button Clicked!")
    
if __name__ == "__main__":
    app = App()
    app.mainloop()