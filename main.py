'''Main fil'''

# Importer
import logging
import os
import time

import IO
import items
import directions
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

    # Skapa en 'tom' karta om det inte finns spardata
    else:
        game_level = level.Level()
        logger.info('New map generated')

    current_tile = game_level.get_tile(3, 4)

    # Skapa kontroller
    controls = IO.Controls()
    controls.add_hotkeys()
    logger.info('Controls initiated')

    # Spelets primära loop
    # logger.info('Startar loopen')
    while True:
        logger.debug(f'Now on tile {current_tile.x},{current_tile.y}')
        current_tile.set_explored(True)

        if current_tile.x == 3 and current_tile.y == 4:

            # Spara alla tiles och ändrade attribut
            tiles = game_level.compress_tiles()
            logger.debug(f'Current map ready for saving, first tiles preview: {tiles[0:6]}')
            logger.debug(f'Current inventory to save: {items.inventory}')

            saving.save(
                game_slot,
                inventory=items.inventory,
                level=tiles)
            
            logger.info(f'Progress saved to slot {game_slot}')

        standardPrint(current_tile.descriptions[0], *game_level.get_descriptions(current_tile))

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

            useable_items = []

            # Skapa en lista med alla items som går att använda
            for item in items.inventory:
                if item in current_tile.usable_items:
                    useable_items.append(f'{len(useable_items) + 1}: {item.capitalize()}')

            # Om det fanns några användbara items, skriv ut dem
            if useable_items:
                standardPrint('Du kan använda:', *useable_items, add_dots=False)

                selected_index = IO.integer_input(*range(1, len(current_tile.usable_items)))

                item = current_tile.usable_items[selected_index - 1]

                items.use_item(current_tile, item, game_level)
                logger.info(f'Used {item} on {current_tile.x},{current_tile.y}')

        elif key == 'pickup':
            logger.info('Item pickup triggered')
            if current_tile.findable_item:
                item = items.pickup_item(current_tile)

                # Lägg till väg till grottan om man plockar upp fackla
                if item == items.torch:
                    
                    mountain_tile = game_level.get_tile(4, 3)
                    mountain_tile.descriptions[0] = 'Du finner dig högt upp i bergen, oj vad kallt det var här'
                    mountain_tile.connections('add', directions.up, game_level)
                
                logger.info(f'Picked up {item}')
                standardPrint(f'Du plockade upp: {item}')

            else:
                standardPrint('Det finns inget att plocka upp här')

        # Sätt nuvarande tile till tile åt det valda hållet
        elif key in current_tile.available_directions:
            logger.debug('Movement triggered')
            current_tile = game_level.get_tile(tile=current_tile, direction=key)

        # Om man trycker på en tangent som inte leder någonstans
        else:
            standardPrint('Du kan inte gå åt det hållet')
            time.sleep(1)

        logger.debug('End of main loop')

if __name__ == '__main__':
    main()
