import pyautogui
import uuid
import os
import sys
import keyboard

def take_screenshot():
    try:
        # Take a screenshot
        im = pyautogui.screenshot()

        # Specify the directory where you want to save the image
        save_directory = "your-directory-here"

        # Generate a random filename using uuid
        random_filename = str(uuid.uuid4()) + ".jpg"

        # Concatenate the directory path with the random filename
        save_path = os.path.join(save_directory, random_filename)

        # Save the screenshot to the specified directory with the random filename
        im.save(save_path)
        
        print(f"Saved screenshot at {save_directory} with name {random_filename}")

    except Exception as e:
        print("Error:", e)

# Listen for the F6 keypress event
keyboard.add_hotkey('win+shift+s', take_screenshot)

# Block until Ctrl+P     is pressed
try:
    keyboard.wait('ctrl+p')
except KeyboardInterrupt:
    # Remove the hotkey listener when Ctrl+P is pressed
    keyboard.remove_hotkey('win+shift+s')
