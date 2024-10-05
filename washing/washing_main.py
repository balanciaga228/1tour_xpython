import tkinter as tk
from WashingMachineGUI import WashingMachineGUI
import pygame

if __name__ == "__main__":
    pygame.mixer.init()
    root = tk.Tk()
    app = WashingMachineGUI(root)
    root.mainloop()
