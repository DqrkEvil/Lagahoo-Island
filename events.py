'''Plats för alla events'''

import logging

import level
import saving
import text
import items
import IO

logger = logging.getLogger('__main__')

def tile_event(current_tile: level.Tile, game_level: level.Level, game_slot: int):
    '''Om det finns något event på tile, annars gör inget'''

    x = current_tile.x
    y = current_tile.y

    # base
    if x == 3 and y == 4:
        # Spara spel
        tiles = game_level.compress_tiles()
        logger.debug(f'Current inventory to save: {items.inventory}')
        logger.debug(f'Current map ready for saving, first tiles preview: {tiles[:4]}')

        saving.save(
            game_slot,
            inventory=items.inventory,
            level=tiles)

    # hidden cave
    elif x == 5 and y == 1:
        # Om man inte har yxan än
        if items.hatchet not in items.inventory:
            IO.standardPrint('Du plockar upp yxan')

            current_tile.findable_item = None
            items.inventory.append(items.hatchet)

    # parrot
    elif x == 2 and y == 1:
        # Om man inte har sjögräset än
        if items.golden_seaweed not in items.inventory:

            while True:
                IO.standardPrint(text.parrot_riddle[0])

                answer = input().lower().strip()

                if answer in text.parrot_riddle[1]:
                    IO.standardPrint(f'Du hade rätt.\nPapegojan gav dig {items.golden_seaweed}')
                    items.inventory.append(items.golden_seaweed)
                    break

                if not answer:
                    return

    elif x == 5 and y == 3:
        IO.standardPrint('Varför hoppade du ner på spikarna?.\nDet var ett dåligt val, men vi är snälla och placerar dig tillbaka där du vaknade')
        game_level.current_tile = game_level.get_tile(3, 4)
