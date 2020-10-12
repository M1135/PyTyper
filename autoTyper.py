from pynput.keyboard import Key, Controller
import keyboard as keeb
import time

keyboard = Controller()
lines = []
f = open("content.txt", "r")


def main():
    line = f.read()
    if line != "end##":
        lines.append(line)
    message = '\n'.join(lines)
# Wait until F9 is pressed
    while True:
        if keeb.read_key() == 'f9':
            break
    time.sleep(0.3)
    for char in message:
        keyboard.press(char)
        keyboard.release(char)
# Adjust the typing speed here
        time.sleep(0.055)


main()
