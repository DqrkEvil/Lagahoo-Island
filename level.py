'''Tile klasser'''

import items
import directions

# Classes
class Tile():
    '''Basklassen för alla tiles på kartan'''

    def __init__(self,
                 tile_description: tuple[str, str],
                 avalible_directions: tuple,
                 useable_items: tuple = tuple(),
                 actions: tuple = tuple(),
                 findable_items: tuple = tuple()
                 ) -> None:
        '''
        :tile_description: tuple med beskrivning av denna tilen som skrivs ut när spelaren kommer hit och ev. beskrivningen av tiles man kan gå till
        :avalible_directions: alla vägar att gå från denna tile
        :useable_items: items som går att använda på denna tile
        :actions: alla möjliga aktiviteter på denna tile
        :findable_items: saker som går att ta från denna tile'''

        self.tile_description = tuple(tile_description)
        self.avalible_directions = tuple(avalible_directions)
        self.useable_items = tuple(useable_items)
        self.findable_items = tuple(findable_items)
        self.actions = tuple(actions)

        self.explored = False

class CavePuzzleTile(Tile):
    '''Subklass för pussel tiles i grottan'''

    def __init__(self, tile_description: tuple[str, str],
                 avalible_directions: tuple,
                 useable_items: tuple = tuple(),
                 actions: tuple = tuple(),
                 findable_items: tuple = tuple()) -> None:
        '''
        :tile_description: tuple med beskrivning av denna tilen som skrivs ut när spelaren kommer hit och ev. beskrivningen av tiles man kan gå till
        :avalible_directions: alla vägar att gå från denna tile
        :useable_items: items som går att använda på denna tile
        :actions: alla möjliga aktiviteter på denna tile
        :findable_items: saker som går att ta från denna tile'''

        super().__init__(tile_description, avalible_directions, useable_items, actions, findable_items)

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

        hall = Tile(('Du är i hallen av stugan', 'Du ser en stuga %(direction)s'),
                    (directions.right, directions.downward))

        kitchen = Tile(('Dur är i stugans kök', 'Det finns ett kök %(direction)s'),
                       (directions.left),
                       findable_items=(items.torch))

        # Ny rad
        turtle = Tile(('Du står på stranden, nära dig ligger en sköldpadda', '%(direction)s ligger en sköldpadda'),
                      (directions.downward),
                      (items.golden_seaweed))

        cottege_entrance = Tile(('Du står i jungeln bredvid en liten stuga, dörren står lite på glänt', 'Det finns en stuga %(direction)s om dig'),
                                (directions.forward, directions.downward))

        lake = Tile(('beskrivning', 'vad man ser från närliggande tile'),
                    (directions.right, directions.downward))
        parrot =            Tile('', ('left'), actions='Prata med papegoja')

        # Ny rad
        base = Tile(('beskrivning', 'vad man ser från närliggande tile'),
                    (directions.forward, directions.downward, directions.right))

        jungle1 = Tile(('beskrivning', 'vad man ser från närliggande tile'),
                       (directions.forward, directions.downward, directions.right, 'left'))

        monkey = Tile(('beskrivning', 'vad man ser från närliggande tile'),
                      (directions.forward, 'left'), ('hatchet'), ('Prata med apan'))

        # Ny rad
        beach = Tile(('beskrivning', 'vad man ser från närliggande tile'),
                     (directions.forward), (items.shovel))

        mountain = Tile(('beskrivning', 'vad man ser från närliggande tile'),
                        (directions.forward, directions.right))

        cave_entrance = Tile(('beskrivning', 'vad man ser från närliggande tile'),
                             (directions.downward, directions.right, 'left'))

        cave_1 = CavePuzzleTile(('beskrivning', 'vad man ser från närliggande tile'),
                                ('left'), (items.torch))
        
        # Ny rad
        cave_2 = CavePuzzleTile(('beskrivning', 'vad man ser från närliggande tile'),
                                (directions.forward), (items.torch))

        hidden_cave = Tile(('beskrivning', 'vad man ser från närliggande tile'),
                           (directions.forward, directions.right), findable_items=items.hatchet)

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
