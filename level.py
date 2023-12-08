'''All tile classes'''

import items

# Classes
class Tile():
    '''Base tile for the map'''

    def __init__(self,
                 avalibleDirections: tuple,
                 useableItems: tuple = tuple(None),
                 actions: tuple = tuple(None)
                 ) -> None:

        self.avalibleDirections = avalibleDirections
        self.actions = actions
        self.useableItems = useableItems


# Functions
def createLevel() -> tuple:
    hall = Tile(('right', 'down'))
    kitchen = Tile(('left'))

    turtle = Tile(('down'), (items.goldenSeaweed))
    cottege_entrance = Tile(('up', 'down'))
    lake = Tile(('right', 'down'))
    parrot = Tile(('left'), actions=('Prata med papegoja'))
    base = Tile(('up', 'down', 'right'))

    return (
        (None, hall, kitchen, None),
        (turtle, cottege_entrance, lake, parrot),
        (base),
        (None),
        (None)
    )
