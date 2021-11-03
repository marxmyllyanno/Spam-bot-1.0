import pyautogui, time
time.sleep(5)
s = open("spammessage", 'r')

for word in s:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

"""write literally ANYTHING you want to spam 
just a type: the more lines, the better. XD
you can use it to troll a friend on facebook or whatsapp, but know that problably you will make your friend's facebook crash if you use it.

I'll put SHREK script here as an example in "spammessage": """