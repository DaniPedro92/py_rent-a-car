import os
import time

def fade_out(message):
    # Print the message initially
    print(message)

    # Wait for a short duration before starting the fade-out effect
    time.sleep(1)

    # Get the height of the terminal window
    rows, columns = os.popen('stty size', 'r').read().split()

    # Fade out the message by re-printing it with reduced opacity
    for i in range(10, 0, -1):
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # Calculate the opacity
        opacity = i / 10.0

        # Print the message with reduced opacity
        print("\033[{};{}H\033[2;32;40m{}\033[0m".format(int(rows)//2, (int(columns) - len(message))//2, message))

        # Wait a short duration before re-printing the message
        time.sleep(0.1)

# Usage
fade_out("Welcome to the Python Fading Message!")
