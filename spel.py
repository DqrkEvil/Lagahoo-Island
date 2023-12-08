
import keyboard

keyboard.add_hotkey("w",  lambda: print("upp"))
keyboard.add_hotkey("up arrow",  lambda: print("upp"))

keyboard.add_hotkey("a",  lambda: print("vänster"))
keyboard.add_hotkey("left arrow",  lambda: print("vänster"))

keyboard.add_hotkey("s",  lambda: print("ner"))
keyboard.add_hotkey("down arrow",  lambda: print("ner"))

keyboard.add_hotkey("d",  lambda: print("höger"))
keyboard.add_hotkey("right arrow",  lambda: print("höger"))


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

    pass