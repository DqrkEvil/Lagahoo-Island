'''Main fil'''

# Importer
import logging

import items
import level
import IO
from IO import standardPrint

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('app.log', 'w', encoding='UTF-8')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(filename)s - line: %(lineno)-3d - %(levelname)-9s : %(message)s') # logging format: https://stackoverflow.com/questions/57204920/how-to-properly-format-the-python-logging-formatter

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Funktioner
def main():
    ''''Main funktion'''

    # Starta upp programmet med objekt och variabler
    game_level = level.level()
    current_tile = game_level.get_tile(2, 1)
    logger.info('level created')

    # Börja skriva ut saker till användaren
    IO.printMainMenu()

    #TODO printa ut information om kontroller och allt annat som ska vara med
    # standardPrint()

    #TODO
    # Skriv ut nuvarande tile och ev. information om vilka som ligger i närheten
    standardPrint(current_tile.description[0], *game_level.format_directions(current_tile))

    # Spelets primära loop
    # logger.info('Startar loopen')
    # while True:
        # current_tile.explored = True
    #     pass

if __name__ == '__main__':
    main()
