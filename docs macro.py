import time
import pyautogui


text = input('Enter you text:')

print("Switch to Google Docs and place your cursor in the document. Typing will start in 5 seconds...")
time.sleep(5) #5 seconds until macro starts

for line in text.split("\n"):
    pyautogui.write(line, interval=0.1)  
    pyautogui.press("enter") 
print("Typing complete!")
