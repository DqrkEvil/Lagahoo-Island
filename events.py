'''Plats för alla events'''

import logging
import keyboard
import time

import IO
import items
import level
import saving
import text

logger = logging.getLogger('__main__')

def tile_events(tile: level.Tile, game_level: level.Level, game_slot: int) -> bool:
    '''Om det finns något event på tile, annars gör inget. Returnera True om spelet ska hoppa till nästa iteration av main loopen'''

    # Vissa event gör att programmet borde hoppa frampåt en iteration
    skip = False

    # base
    if tile.x == 3 and tile.y == 4:
        # Spara spel
        tiles = game_level.compress_tiles()
        logger.debug(f'Current inventory to save: {items.inventory}')
        logger.debug(f'Current map ready for saving, first tile preview: {tiles[0]}')

        saving.save(
            game_slot,
            inventory=items.inventory,
            level=tiles)

    # parrot, om man inte har sjögräset än
    elif tile.x == 2 and tile.y == 1 and items.golden_seaweed not in items.inventory:
        while True:
            IO.standardPrint('Papegojan börjar prata med dig och ställer en gåta:\n', text.parrot_riddle[0], add_dots=False)

            answer = input().lower().strip()

            if answer in text.parrot_riddle[1]:
                IO.standardPrint(f'\nDu hade rätt!\nPapegojan gav dig {items.golden_seaweed}')
                items.inventory.append(items.golden_seaweed)
                tile.descriptions[0] = '\nPapegojan är glad att du kunde svaret till dens gåta.\n*Sköldpaddan vid stranden skulle nog uppskatta sjögräset*'
                break

        # Tile attribut har ändrats, hoppa till nästa
        skip = True

    elif tile.x == 5 and tile.y == 3:
        IO.standardPrint('Varför hoppade du ner på spikarna?.\nDet var ett dåligt val, men vi är snälla och placerar dig tillbaka där du vaknade')
        game_level.current_tile = game_level.get_tile(3, 4)

        # Hoppa till nästa loop för att fortsätta vid 3, 4
        skip = True

    return skip

def ending():
    for n in range(15, -1, -1):
        time.sleep(1)
        print(f' {n} ', end='\r')

    # keyboard.send("windows+d")
    # time.sleep(0.5)
    keyboard.send("alt+F4")
    # time.sleep(0.5)
    # keyboard.send("enter")
