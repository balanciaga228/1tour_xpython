import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from WashingMachine import WashingMachine, play_sound


class WashingMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Симуляція пральної машини")

        self.input_label = tk.Label(root, text="Введіть вагу білизни (кг):")
        self.input_label.pack(pady=10)

        self.input_entry = tk.Entry(root)
        self.input_entry.pack(pady=5)

        self.start_button = tk.Button(root, text="Запустити пральну машину", command=self.start_machine)
        self.start_button.pack(pady=10)

        self.status_label = tk.Label(root, text="Стан: OFF", font=("Arial", 14))
        self.status_label.pack(pady=20)

        self.image_label = tk.Label(root)
        self.image_label.pack()

    def start_machine(self):
        try:
            weight = float(self.input_entry.get())
            self.machine = WashingMachine(weight)
            self.machine.start(self.update_status)
        except AssertionError as e:
            play_sound("sounds/error.mp3")
            messagebox.showerror("Помилка", str(e))
        except ValueError:
            play_sound("sounds/error.mp3")
            messagebox.showerror("Помилка", "Будь ласка, введіть коректне число.")

    def update_status(self, state):
        self.status_label.config(text=f"Стан: {state}")
        self.update_image(state)
        if state == "Finished":
            messagebox.showinfo("Інформація", "Цикл прання завершено!")

    def update_image(self, state):
        image_file = {
            "Filling water": "images/fill_water.png",
            "Washing": "images/washing.png",
            "Rinsing": "images/rinsing.png",
            "Spinning": "images/spinning.png",
            "Finished": "images/finished.png"
        }.get(state, "images/off.png")

        image = Image.open(image_file)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
