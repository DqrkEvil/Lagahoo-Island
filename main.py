'''Main fil'''

# Importer
import logging
import os
import time

import IO
import items
import events
import level
import saving
import text
from IO import standardPrint

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('app.log', 'w', encoding='UTF-8')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s in %(filename)-13s - line: %(lineno)-3d - %(levelname)-9s : %(message)s', '%Y-%m-%d %H:%M:%S')

# console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Funktioner
def main():
    ''''Main funktion'''

    # Börja skriva ut saker till användaren
    IO.printMainMenu()

    #TODO printa ut information om lore och kontroller

    save_data, game_slot = saving.select_slot()
    os.system('cls')

    if save_data:
        items.inventory = save_data['inventory']
        logger.info('Inventory loaded')

        game_level = level.Level('load', save_data['level'])
        logger.info('Map loaded')

    # Skapa en ny karta om det inte finns spardata
    else:
        game_level = level.Level()
        logger.info('New map generated')

    # Skapa kontroller
    controls = IO.Controls()
    controls.add_hotkeys()
    logger.info('Controls initiated')

    # Spelets primära loop
    # logger.info('Startar loopen')
    while True:
        current_tile = game_level.current_tile

        logger.debug(f'Now on tile {current_tile.x},{current_tile.y}')
        current_tile.set_explored(True)

        standardPrint(current_tile.descriptions[0], *game_level.get_descriptions(current_tile))
        events.tile_event(current_tile, game_level, game_slot)

        key = controls.await_input()

        logger.info(f'User input taken: {key}')

        if key == 'info':
            logger.debug('Info print triggered')
            standardPrint(text.controlInfo)

        elif key == 'map':
            logger.debug('Open map triggered')
            #TODO Print map
            standardPrint('map opened WIP')

        elif key == 'use item':
            logger.debug('Item usage triggered')
            items.use_item(current_tile, game_level)

        elif key == 'pickup':
            logger.info('Item pickup triggered')
            items.pickup_item(current_tile, game_level)

        # Sätt nuvarande tile till tile åt det valda hållet
        elif key in current_tile.available_directions:
            logger.debug('Movement triggered')
            game_level.current_tile = game_level.get_tile(tile=current_tile, direction=key)

        # Om man trycker på en tangent som gör något
        else:
            standardPrint('Du kan inte gå åt det hållet')
            time.sleep(1)

        logger.debug('End of main loop')

if __name__ == '__main__':
    main()
