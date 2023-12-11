
import keyboard
import time

x = ""
def up():

    global x
    x = "upp"

def left():
    global x
    x = "vänster"

def right():
    global x
    x = "höger"

def down():
    global x
    x = "ner"

keyboard.add_hotkey("w",  lambda: up())
keyboard.add_hotkey("up arrow",  lambda: up())

keyboard.add_hotkey("a",  lambda: left())
keyboard.add_hotkey("left arrow",  lambda: left())

keyboard.add_hotkey("s",  lambda: down())
keyboard.add_hotkey("down arrow",  lambda: down())

keyboard.add_hotkey("d",  lambda: right())
keyboard.add_hotkey("right arrow",  lambda: right())


keyboard.add_hotkey("i",  lambda: print("""
info om keybinds:

du håller i {} just nu                                        

wasd/pilarna för att gå runt
                                        
i för info
                                        
m för map
                                        
e för att använda itemet du håller i
                                        
q för att plocka upp items i ett rum
                                        
"""))



while True:
    if x != "":
        print(x)
        time.sleep(5)
        x = ""
        
    pass