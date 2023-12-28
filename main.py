'''Main fil'''

# Importer
import logging
import os
import time

import IO
import items
import saving
# import directions
# import actions
import level
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

    #TODO ladda in data från den valda platsen

    # Skapa en 'tom' karta
    game_level = level.Level()
    current_tile = game_level.get_tile(1, 3)
    logger.info('New map generated')

    # Skapa kontroller
    controls = IO.Controls()
    controls.add_hotkeys()
    logger.info('Controls initiated')

    # Spelets primära loop
    # logger.info('Startar loopen')
    while True:
        logger.info(f'Now on tile {current_tile.x},{current_tile.y}')

        if current_tile.x == 1 and current_tile.y == 3:

            # Spara alla tiles och deras egenskaper
            tiles = tuple(tile.__dict__ if tile else tile for row in game_level.level for tile in row) # lite cred till ChatGPT för en del av generatorn: (expression for row in game_level.level for tile in row)
            logger.debug(f'Current map ready for saving, first tiles preview: {tiles[0:6]}')

            saving.save_save(
                game_slot,
                inventory=items.inventory,
                level=tiles)

        current_tile.explored = True
        standardPrint(current_tile.descriptions[0], *game_level.get_descriptions(current_tile))

        key = controls.await_input()

        logger.info(f'User input taken: {key}')

        if key == 'info':
            logger.info('Info print triggered')
            standardPrint(text.controlInfo)

        elif key == 'map':
            logger.info('Open map triggerd')
            #TODO Print map
            standardPrint('map opened WIP')

        elif key == 'use item':
            logger.info('Item usage triggered')

            useable_items = []

            # Skapa en lista med alla items som går att använda
            for n, item in enumerate(items.inventory):
                if item in current_tile.useable_items:
                    useable_items.append(f'{n + 1}: {item.capitalize()}')

            # Om det fanns några användbara items, skriv ut dem
            if useable_items:
                standardPrint('Du kan använda:', *useable_items, add_dots=False)

                selected_index = IO.integer_input(*range(1, len(current_tile.useable_items)))

                item = current_tile.useable_items[selected_index - 1]

                items.use_item(current_tile, item, game_level)
                logger.info(f'Used {item}')

        elif key == 'pickup':
            logger.info('Item pickup triggered')
            if current_tile.findable_item:
                item = items.pickup_item(current_tile)
                logger.info(f'Picked up {item}')
                standardPrint(f'Du plockade upp: {item}')

            else:
                standardPrint('Det finns inget att plocka upp här')

        # Sätt nuvarande tile till tile åt det valda hållet
        elif key in current_tile.available_directions:
            logger.info('Movement triggerd')
            current_tile = game_level.get_tile(tile=current_tile, direction=key)

        # Om man trycker på en tangent som inte leder någonstans
        else:
            standardPrint('Du kan inte gå åt det hållet')
            time.sleep(1)

        logger.debug('End of main loop')

if __name__ == '__main__':
    main()
