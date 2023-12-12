# importar moduler
import keyboard
import time

x = ""

#funktioner för att ändra värdet på x så man kan ändra det med hjälp av keybinds för lambda behöver funktioner
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

#keybinds
keyboard.add_hotkey("w",  lambda: up())
keyboard.add_hotkey("up arrow",  lambda: up())

keyboard.add_hotkey("a",  lambda: left())
keyboard.add_hotkey("left arrow",  lambda: left())

keyboard.add_hotkey("s",  lambda: down())
keyboard.add_hotkey("down arrow",  lambda: down())

keyboard.add_hotkey("d",  lambda: right())
keyboard.add_hotkey("right arrow",  lambda: right())

# en lista på alla keybinds ifall spelaren glömmer av dom
keyboard.add_hotkey("i",  lambda: print("""
info om keybinds:

du håller i {} just nu                                        

wasd/pilarna för att gå runt
                                        
i för info
                                        
m för map
                                        
e för att använda itemet du håller i (om du kan)
                                        
q för att plocka upp items i ett rum
                                        
"""))


# loopar så att programmet alltid körs
while True:
    # ifall x har ett värde så printar det ut det
    if x != "":
        print(x)
        # väntar 5 sekunder för att förhindra att spelaren går vidare till nästa rum medans texten för nuvarande rummet printas ut
        time.sleep(5)
        #byter tillbaka värdet på x så den inte prinas ut flera gånger
        x = ""
        
    pass