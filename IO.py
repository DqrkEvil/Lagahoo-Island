'''Hanterar all input och output för spelet'''

import logging
import os
import sys
import time

import fade
import keyboard

import directions
import text

logger = logging.getLogger('__main__')

#* Inputs
class Controls():
    '''Klass för alla hotkeys'''

    def __init__(self) -> None:
        '''Lägg till alla hotkeys'''
        self.add_hotkeys()

        self.key = None

    def await_input(self) -> str:
        '''Vänta tills användaren ger en input'''

        # Återställ variabeln
        self.key = None

        # Vänta tills esn annan knapp trycks ner
        logger.info('Awaiting keyboard input')
        while True:
            if self.key is not None:
                return self.key

            # Sakta ner loopen för att använda mindre resurser
            time.sleep(0.1)

    def key_pressed(self, key: str) -> None:
        '''Uppdatera variablen med den senaste nedtryckta knappen'''

        self.key = key

    def add_hotkeys(self) -> None:
        '''Lägg till hotkeys för att kontrollera'''

        keyboard.add_hotkey('w', lambda: self.key_pressed(directions.up))
        keyboard.add_hotkey('up arrow', lambda: self.key_pressed(directions.up))

        keyboard.add_hotkey('a', lambda: self.key_pressed(directions.left))
        keyboard.add_hotkey('left arrow', lambda: self.key_pressed(directions.left))

        keyboard.add_hotkey('s', lambda: self.key_pressed(directions.down))
        keyboard.add_hotkey('down arrow', lambda: self.key_pressed(directions.down))

        keyboard.add_hotkey('d', lambda: self.key_pressed(directions.right))
        keyboard.add_hotkey('right arrow', lambda: self.key_pressed(directions.right))

        keyboard.add_hotkey('i', lambda: self.key_pressed('info'))

        keyboard.add_hotkey('e', lambda: self.key_pressed('use item'))

        keyboard.add_hotkey('q', lambda: self.key_pressed('pickup'))

        keyboard.add_hotkey('f', lambda: self.key_pressed('list inventory'))

def integer_input(*acceptable_values, error_text: str = 'Det där var inte ett möjligt val') -> int:
    '''Tar en input från avnändaren som måste vara en int'''

    while True:
        integer = input().strip()

        if integer.isdigit() and (not acceptable_values or int(integer) in acceptable_values):
            return int(integer)

        standardPrint(error_text)

#* Outputs
def printMainMenu():
    '''Skriv ut main menyn och vänta tills spelaren vill börja'''

    os.system('cls')
    print(fade.greenblue(text.mainMenuText))
    time.sleep(1.4)
    input(text.startGameText)
    os.system('cls')

def printLore():
    '''Skriv ut bakgrundsinformation om storyn till spelet'''

    print(text.preGameLore[0])
    time.sleep(1)
    standardPrint(text.preGameLore[1])
    input('\nTryck ENTER för att fortsätta')

def printControls():
    '''Skriv ut kontrollerna och vänta tills spelaren vill börja'''

    print(f'\n{text.controlInfo}')

def standardPrint(*sections, add_dots: bool = True, explored: bool = False):
    '''Standardiserad print funktion för hela programmet
    
    :*sections: sektioner med all information som ska skrivas ut
    :add_dots: Lägg till punkter mellan sektionerna'''

    section_end = '. ' if add_dots else ''
    char_delay = 0.02 if explored else 0.04

    for section in sections:
        if section:
            for char in section:
                # https://replit.com/talk/ask/How-to-make-your-text-appear-fluidly-instead-of-one-big-chunk-in-Python/111394
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(char_delay)
            print(section_end)

    print('\n')
