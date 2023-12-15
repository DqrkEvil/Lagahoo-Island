'''Main fil'''

# Importer
import logging

import IO
import directions
import level
import text
from IO import standardPrint

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('app.log', 'w', encoding='UTF-8')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s in %(filename)s - line: %(lineno)-3d - %(levelname)-9s : %(message)s', '%Y-%m-%d %H:%M:%S')

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Funktioner
def main():
    ''''Main funktion'''

    # Starta upp programmet med objekt och variabler
    game_level = level.Level()
    current_tile = game_level.get_tile(1, 3)
    logger.info('Karta genererad')

    # 
    controls = IO.Controls()
    controls.add_hotkeys()
    logger.info('Kontroller skapade')

    # Börja skriva ut saker till användaren
    IO.printMainMenu()

    #TODO printa ut information om lore och kontroller
    pass
    
    # Spelets primära loop
    # logger.info('Startar loopen')
    while True:
        current_tile.explored = True
        standardPrint(current_tile.descriptions[0], *game_level.format_directions(current_tile))

        key = controls.await_input()

        logger.debug(f'User input taken: {key}')

        if key == 'info':
            standardPrint(text.controlInfo)
        
        elif key == 'map':
            #TODO Print map
            standardPrint('map opened')
        
        elif key == 'use item':
            #TODO Print numbered list of items in player inventory
            #TODO let player choose one with a number
            #TODO try using that item on tile
            standardPrint('item used')

        elif key == 'pickup':
            #TODO remove item from tile object
            #TODO add item to inventory
            standardPrint('item picked up')

        if key in current_tile.avalible_directions:
            if key == directions.up:
                current_tile = game_level.get_tile(current_tile.x, current_tile.y - 1)

            if key == directions.down:
                current_tile = game_level.get_tile(current_tile.x, current_tile.y + 1)

            if key == directions.right:
                current_tile = game_level.get_tile(current_tile.x + 1, current_tile.y)

            if key == directions.left:
                current_tile = game_level.get_tile(current_tile.x - 1, current_tile.y)

        # Om man trycker på en tangent som inte leder någonstans
        else:
            standardPrint('Du kan inte gå åt det hållet')

if __name__ == '__main__':
    main()
