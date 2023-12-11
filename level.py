'''Tile klasser'''

import items

# Classes
class Tile():
    '''Basklassen för alla tiles på kartan'''

    def __init__(self,
                 avalible_directions: tuple,
                 useable_items: tuple = tuple(None),
                 actions: tuple = tuple(None),
                 findable_items: tuple = tuple(None)
                 ) -> None:

        self.avalible_directions = avalible_directions
        self.useable_items = useable_items
        self.findable_items = findable_items
        self.actions = actions

class CaveTile(Tile):
    '''Subklass för pussel tiles i grottan'''
    def __init__(self,
                 avalible_directions: tuple,
                 useable_items: tuple = tuple(None)
                 ) -> None:
        
        super().__init__(avalible_directions, useable_items)

        self.is_torch_lit = False

    def light_torch(self):
        '''Tänd facklan på tilen'''

        self.is_torch_lit = True

# Functions
def create_level() -> tuple[tuple]:
    '''Skapa kartan för spelet'''

    hall = Tile(('right', 'down'))
    kitchen = Tile(('left'))

    turtle = Tile(('down'), (items.goldenSeaweed))
    cottege_entrance = Tile(('up', 'down'))
    lake = Tile(('right', 'down'))
    parrot = Tile(('left'), actions=('Prata med papegoja'))

    base = Tile(('up', 'down', 'right'))
    jungle1 = Tile(('up', 'down', 'right', 'left'))
    monkey = Tile(('up', 'left'), ('hatchet'), ('Prata med apan'))

    beach = Tile(('up'), (items.shovel))
    mountain = Tile(('up', 'right'))
    cave_entrance = Tile(('down', 'right', 'left'))
    cave_1 = CaveTile(('left'), (items.torch))

    cave_2 = CaveTile(('up'), (items.torch))
    hidden_cave = Tile(('up', 'right'), findable_items=(items.hatchet))

    return (
        (None, hall, kitchen, None),
        (turtle, cottege_entrance, lake, parrot),
        (base, jungle1, monkey, None),
        (beach, mountain, cave_entrance, cave_1),
        (None, None, cave_2, hidden_cave)
    )
