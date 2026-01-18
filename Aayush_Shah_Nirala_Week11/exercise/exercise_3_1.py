# You need to create a simple calculator using GUI programing. The graphical interface should allow
# the user to enter a number in a text field and either add it to or subtract it from a running total. The
# running total should always be displayed. The user should be able to resit the running total to zero
# using a button Resit. The user will need to input a new value and then either press the button “+” to
# add the value to the running total or press “-” button to decrement the value in the entry from the
# running total. Each time the buttons “+” or “-” are pressed, the entry will be cleared, and the running
# total will be updated.

import tkinter as tk

class SimpleCalculator:
    def __init__(self, root):
        self.total = 0

        root.title("Calculator")
        root.geometry("250x150")

        self.total_label = tk.Label(root, text=f"Total: {self.total}", font=("Arial", 14))
        self.total_label.pack(pady=5)

        self.entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=5)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="+", width=6, command=self.add).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="-", width=6, command=self.subtract).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Reset", width=6, command=self.reset).grid(row=0, column=2, padx=5)

    def update_total_label(self):
        self.total_label.config(text=f"Total: {self.total}")

    def get_input_value(self):
        try:
            value = float(self.entry.get())
            return value
        except ValueError:
            return 0

    def add(self):
        self.total += self.get_input_value()
        self.entry.delete(0, tk.END)
        self.update_total_label()

    def subtract(self):
        self.total -= self.get_input_value()
        self.entry.delete(0, tk.END)
        self.update_total_label()

    def reset(self):
        self.total = 0
        self.entry.delete(0, tk.END)
        self.update_total_label()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()