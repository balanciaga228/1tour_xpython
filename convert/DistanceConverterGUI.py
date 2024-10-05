import tkinter as tk
from tkinter import messagebox
from convert_distance import convert_distance


class DistanceConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Перетворення відстані")

        self.input_label = tk.Label(root, text="Введіть відстань у футах:")
        self.input_label.pack(pady=10)

        self.input_entry = tk.Entry(root)
        self.input_entry.pack(pady=5)

        self.convert_button = tk.Button(root, text="Перетворити", command=self.convert_distance)
        self.convert_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def convert_distance(self):
        try:
            feet = float(self.input_entry.get())
            inches, yards, miles = convert_distance(feet)
            result_text = (f"{feet} футів = {inches} дюймів\n"
                           f"{feet} футів = {yards} ярдів\n"
                           f"{feet} футів = {miles} миль")
            self.result_label.config(text=result_text)
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть правильне число.")
