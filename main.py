'''Main fil'''

# Importer
import logging
import time

import IO
import items
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

formatter = logging.Formatter('%(asctime)s in %(filename)s - line: %(lineno)-3d - %(levelname)-9s : %(message)s', '%Y-%m-%d %H:%M:%S')

# console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Funktioner
def main():
    ''''Main funktion'''

    # Starta upp programmet med objekt och variabler
    game_level = level.Level()
    current_tile = game_level.get_tile(1, 3)
    logger.info('Karta genererad')

    # Skapa kontroller
    controls = IO.Controls()
    controls.add_hotkeys()
    logger.info('Kontroller skapade')

    # Börja skriva ut saker till användaren
    IO.printMainMenu()

    #TODO printa ut information om lore och kontroller

    # Spelets primära loop
    # logger.info('Startar loopen')
    while True:
        current_tile.explored = True
        standardPrint(current_tile.descriptions[0], *game_level.format_directions(current_tile))

        key = controls.await_input()

        logger.debug(f'Now on tile {current_tile.x},{current_tile.y}')
        logger.info(f'User input taken: {key}')

        if key == 'info':
            standardPrint(text.controlInfo)

        elif key == 'map':
            #TODO Print map
            standardPrint('map opened WIP')
            logger.info('Opened map')

        elif key == 'use item':

            useable_items = []

            # Skapa en lista med alla items som går att använda
            for n, item in enumerate(items.inventory):
                if item in current_tile.useable_items:
                    useable_items.append(f'{n + 1}: {item.capitalize()}')

            # Om det fanns några användbara items, skriv ut dem
            if useable_items:
                standardPrint('Du kan använda:', *useable_items, add_dots=False)

                selected_index = IO.integer_input(tuple(range(1, len(current_tile.useable_items))))

                item = current_tile.useable_items[selected_index - 1]

                items.use_item(current_tile, item, game_level)
                logger.info(f'Used {item}')

        elif key == 'pickup':
            if current_tile.findable_item:
                item = items.pickup_item(current_tile)
                logger.info(f'Picked up {item}')
                standardPrint(f'Du plockade upp: {item}')

            else:
                standardPrint('Det finns inget att plocka upp här')

        # Sätt nuvarande tile till tile åt det valda hållet
        elif key in current_tile.available_directions:
            current_tile = game_level.get_tile(tile=current_tile, direction=key)

        # Om man trycker på en tangent som inte leder någonstans
        else:
            standardPrint('Du kan inte gå åt det hållet')
            time.sleep(1)

if __name__ == '__main__':
    main()
