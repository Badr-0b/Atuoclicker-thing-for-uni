import tkinter as tk
import threading
import time
from pynput.mouse import Listener, Controller, Button
from pynput import keyboard

# Global variables to store coordinates and control the flow
coordinates = []
recording = False
playing = False
looping = False
stop_flag = False

mouse = Controller()

def on_click(x, y, button, pressed):
    global recording
    if pressed and recording:
        coordinates.append((x, y))

def start_recording():
    global recording, stop_flag
    recording = True
    coordinates.clear()  # Clear any previous recordings
    stop_flag = False
    listener = Listener(on_click=on_click)
    listener.start()
    
    def on_key_press(key):
        global recording
        if key == keyboard.KeyCode.from_char('h'):
            recording = False  # Stop recording when "H" is pressed
            return False  # Stop the listener
    
    # Start a keyboard listener to stop recording on 'H' press
    keyboard_listener = keyboard.Listener(on_press=on_key_press)
    keyboard_listener.start()

def stop_playback():
    global stop_flag
    stop_flag = True

def play_coordinates(loop=False):
    global playing, stop_flag
    playing = True
    stop_flag = False
    
    def play():
        while True:
            for coord in coordinates:
                if stop_flag:
                    playing = False
                    return
                mouse.position = coord
                mouse.click(Button.left, 1)
                time.sleep(1)  # Delay between moves
            if loop:
                time.sleep(3)  # 2-second cooldown before the next loop
            else:
                break
    
    # Start playback in a thread to avoid blocking the GUI
    threading.Thread(target=play).start()

def on_press(key):
    if key == keyboard.KeyCode.from_char('g'):
        stop_playback()

def start_keyboard_listener():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def create_gui():
    window = tk.Tk()
    window.title("Mouse Controller")
    
    record_button = tk.Button(window, text="Record", command=start_recording)
    record_button.pack(pady=10)
    
    play_button = tk.Button(window, text="Play", command=lambda: play_coordinates(loop=False))
    play_button.pack(pady=10)
    
    loop_button = tk.Button(window, text="Loop", command=lambda: play_coordinates(loop=True))
    loop_button.pack(pady=10)

    window.geometry("300x200")
    window.mainloop()

# Start the keyboard listener to stop playback on 'G' press
start_keyboard_listener()

# Create and run the GUI
create_gui()
