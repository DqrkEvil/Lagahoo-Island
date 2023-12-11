'''Tile klasser'''

import items

# Classes
class Tile():
    '''Basklassen för alla tiles på kartan'''

    def __init__(self,
                 avalible_directions: tuple,
                 useable_items: tuple = tuple(),
                 actions: tuple = tuple(),
                 findable_items: tuple = tuple()
                 ) -> None:

        self.avalible_directions = tuple(avalible_directions)
        self.useable_items = tuple(useable_items)
        self.findable_items = tuple(findable_items)
        self.actions = tuple(actions)

        self.explored = False

class CavePuzzleTile(Tile):
    '''Subklass för pussel tiles i grottan'''
    def __init__(self,
                 avalible_directions: tuple,
                 useable_items: tuple = tuple()
                 ) -> None:

        super().__init__(avalible_directions, useable_items)

        self.is_torch_lit = False

    def light_torch(self):
        '''Tänd facklan på tilen'''

        self.is_torch_lit = True

class level():
    '''Klass för att hantera kartan'''

    def __init__(self) -> None:
        self.create_level()

    def create_level(self):
        '''Skapa kartan för spelet'''

        hall = Tile(('right', 'down'))
        kitchen = Tile(('left'))

        turtle = Tile(('down'), (items.golden_seaweed))
        cottege_entrance = Tile(('up', 'down'))
        lake = Tile(('right', 'down'))
        parrot = Tile(('left'), actions='Prata med papegoja')

        base = Tile(('up', 'down', 'right'))
        jungle1 = Tile(('up', 'down', 'right', 'left'))
        monkey = Tile(('up', 'left'), ('hatchet'), ('Prata med apan'))

        beach = Tile(('up'), (items.shovel))
        mountain = Tile(('up', 'right'))
        cave_entrance = Tile(('down', 'right', 'left'))
        cave_1 = CavePuzzleTile(('left'), (items.torch))

        cave_2 = CavePuzzleTile(('up'), (items.torch))
        hidden_cave = Tile(('up', 'right'), findable_items=items.hatchet)
        
        self.level = (
            (None, hall, kitchen, None),
            (turtle, cottege_entrance, lake, parrot),
            (base, jungle1, monkey, None),
            (beach, mountain, cave_entrance, cave_1),
            (None, None, cave_2, hidden_cave)
        )

    def get_tile(self, x: int, y: int) -> Tile:
        '''Tile objekt vid koordinat x, y. 1, 1 är övre vänstra hörnet'''

        return self.level[y-1][x-1]
