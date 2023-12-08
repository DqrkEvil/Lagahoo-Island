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

class CavePuzzle(Tile):
    def __init__(self, avalibleDirections: tuple, useableItems: tuple = tuple(None)) -> None:
        super().__init__(avalibleDirections, useableItems)

        self.isTorchLit = False

    def light_torch(self):
        self.isTorchLit = True

# Functions
def createLevel() -> tuple:
    hall = Tile(('right', 'down'))
    kitchen = Tile(('left'))

    turtle = Tile(('down'), (items.goldenSeaweed))
    cottege_entrance = Tile(('up', 'down'))
    lake = Tile(('right', 'down'))
    parrot = Tile(('left'), actions=('Prata med papegoja'))
    
    base = Tile(('up', 'down', 'right'))
    jungle1 = Tile(('up', 'down', 'right', 'left'))
    monkey = Tile(('up', 'left'), ('hatchet'), ('Prata med apan'))
    
    beach = Tile(('up'), (items.showel))
    mountain = Tile(('up', 'right'))
    caveEntrance = Tile(('down', 'right', 'left'))
    cave1 = CavePuzzle(('left'), (items.torch), )

    return (
        (None, hall, kitchen, None),
        (turtle, cottege_entrance, lake, parrot),
        (base, jungle1, monkey, None),
        (beach, mountain, caveEntrance),
        (None)
    )
