import threading
import pygame
import time


class WashingMachine:
    def __init__(self, weight):
        play_sound("sounds/error.mp3")
        assert weight > 5, "Вага повинна бути більше 5 кг!"
        self.weight = weight
        self.state = "OFF"

    def start(self, update_status_callback):
        threading.Thread(target=self.run_cycle, args=(update_status_callback,)).start()

    def run_cycle(self, update_status_callback):
        self.state = "Filling water"
        update_status_callback(self.state)
        play_sound("sounds/fill_water.mp3")
        time.sleep(2)

        self.state = "Washing"
        update_status_callback(self.state)
        play_sound("sounds/washing.mp3")
        time.sleep(5)

        self.state = "Rinsing"
        update_status_callback(self.state)
        play_sound("sounds/rinsing.mp3")
        time.sleep(3)

        self.state = "Spinning"
        update_status_callback(self.state)
        play_sound("sounds/spinning.mp3")
        time.sleep(2)

        self.state = "Finished"
        update_status_callback(self.state)
        play_sound("sounds/off.mp3")


def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
