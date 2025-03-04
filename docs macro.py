import time
import pyautogui

# The text to be typed into Google Docs
text = input('Enter you text:')
# Wait a few seconds before starting to give you time to switch to Google Docs
print("Switch to Google Docs and place your cursor in the document. Typing will start in 5 seconds...")
time.sleep(5)

# Type the text with a slight delay between characters
for line in text.split("\n"):
    pyautogui.write(line, interval=0.1)  # Adjust typing speed (0.02 = 20ms delay per character)
    pyautogui.press("enter")  # Simulate pressing Enter at the end of each paragraph

print("Typing complete!")
