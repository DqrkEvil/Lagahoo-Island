import logging

import fade
import keyboard

import directions
import text

logger = logging.getLogger('__main__')

# Inputs
class Controls():
    '''Klass för att hantera spelarens inputs'''

    def __init__(self) -> None:
        self.add_hotkeys()

        self.last_key = None

    def await_input(self) -> str:
        '''Vänta tills användaren ger en input'''

        # Spara den senast nedtryckta knappen
        last_key = self.last_key

        # Vänta tills en annan knapp trycks ner
        while True:
            if self.last_key != last_key:
                return self.last_key

    def change_key(self, key: str) -> None:
        '''Uppdatera variablen med den senaste nedtryckta knappen'''

        self.last_key = key

    def add_hotkeys(self) -> None:
        '''Lägg till hotkeys för att kontrollera'''

        keyboard.add_hotkey("w", lambda: self.change_key(directions.up))
        keyboard.add_hotkey("up arrow", lambda: self.change_key(directions.up))

        keyboard.add_hotkey("s", lambda: self.change_key(directions.down))
        keyboard.add_hotkey("down arrow", lambda: self.change_key(directions.down))

        keyboard.add_hotkey("d", lambda: self.change_key(directions.right))
        keyboard.add_hotkey("right arrow", lambda: self.change_key(directions.right))

        keyboard.add_hotkey("a", lambda: self.change_key(directions.left))
        keyboard.add_hotkey("left arrow", lambda: self.change_key(directions.left))

        keyboard.add_hotkey("i", lambda: self.change_key("info"))

        keyboard.add_hotkey("m", lambda: self.change_key("map"))

        keyboard.add_hotkey("e", lambda: self.change_key("use item"))

        keyboard.add_hotkey("q", lambda: self.change_key("pickup"))

# Outputs
def printMainMenu():
    """Skriv ut main menyn och vänta tills spelaren vill börja"""

    standardPrint(fade.greenblue(text.mainMenuText))
    input(text.startGameText)

def standardPrint(*sections):
    """Standardiserad print funktion för hela programmet
    
    :*sections: sektioner med all information som ska skrivas ut"""

    for section in sections:
        print(section)

    print('\n')
