'''Main fil'''

# Imports
import logging

import items
import level

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

# Fucntions
def main():
    ''''Main funktion'''

    game_level = level.level()
    current_tile = game_level.get_tile(1, 3)
    logger.info('level created')

if __name__ == '__main__':
    main()
