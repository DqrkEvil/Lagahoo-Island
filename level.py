'''Hanterar allting som har med kartan att göra'''

import items
import directions

# Classes
class Tile():
    '''Basklassen för alla tiles på kartan'''

    def __init__(self,
                 x: int,
                 y: int,
                 description: tuple[str, str],
                 avalible_directions: tuple,
                 useable_items: tuple = tuple(),
                 actions: tuple = tuple(),
                 findable_items: tuple = tuple()
                 ) -> None:
        '''
        :x: tile koordinat
        :y: tile koordinat
        :description: tuple med beskrivning av denna tilen som skrivs ut när spelaren kommer hit och ev. om man ser denna tile från en bredvid
        :avalible_directions: alla vägar att gå från denna tile
        :useable_items: items som går att använda på denna tile
        :actions: alla möjliga aktiviteter på denna tile
        :findable_items: saker som går att ta från denna tile'''

        self.x = x
        self.y = y

        self.description = description
        self.avalible_directions = avalible_directions
        self.useable_items = useable_items
        self.findable_items = findable_items
        self.actions = actions

        self.explored = False

class CavePuzzleTile(Tile):
    '''Subklass för pussel tiles i grottan'''

    def __init__(self,
                 x: int,
                 y: int,
                 description: tuple[str, str],
                 avalible_directions: tuple,
                 useable_items: tuple = tuple(),
                 actions: tuple = tuple(),
                 findable_items: tuple = tuple()
                 ) -> None:
        '''
        :x: tile koordinat
        :y: tile koordinat
        :description: tuple med beskrivning av denna tilen som skrivs ut när spelaren kommer hit och ev. om man ser denna tile från en bredvid
        :avalible_directions: alla vägar att gå från denna tile
        :useable_items: items som går att använda på denna tile
        :actions: alla möjliga aktiviteter på denna tile
        :findable_items: saker som går att ta från denna tile'''

        super().__init__(x, y, description, avalible_directions, useable_items, actions, findable_items)

        self.is_torch_lit = False

    def light_torch(self) -> None:
        '''Tänd facklan på tilen'''

        self.is_torch_lit = True

class Level():
    '''Klass för att hantera kartan'''

    def __init__(self) -> None:
        self.create_level()

    def create_level(self):
        '''Skapa kartan för spelet'''

        # Rad 1
        hall = Tile(
            2, 1,
            ('Du är i hallen av stugan', 'Du ser stugans hall %(direction)s'),
            (directions.right, directions.down))

        kitchen = Tile(
            3, 1,
            ('Du är i stugans kök', 'Det finns ett kök %(direction)s'),
            (directions.left,),
            findable_items=(items.torch,))

        # Rad 2
        turtle = Tile(
            1, 2,
            ('Du står på stranden, nära dig ligger en sköldpadda', '%(direction)s ligger en sköldpadda'),
            (directions.down,),
            (items.golden_seaweed,))

        cottege_entrance = Tile(
            2, 2,
            ('Du står i jungeln bredvid en liten stuga, dörren står på glänt', 'Det finns en stuga %(direction)s'),
            (directions.up, directions.down))

        lake = Tile(
            3, 2,
            ('beskrivning', 'en sjö glittrar %(direction)s från dig'),
            (directions.right, directions.down))
        
        parrot = Tile(
            4, 2,
            ('beskrivning', 'vad man ser från en närliggande tile'),
            (directions.left,),
            actions=('Prata med papegoja',))

        # Rad 3
        base = Tile(
            1, 3,
            ('beskrivning', 'vad man ser från en närliggande tile'),
            (directions.up, directions.down, directions.right))

        jungle1 = Tile(
            2, 3,
            ('beskrivning', 'vad man ser från en närliggande tile'),
            (directions.up, directions.down, directions.right, directions.left))

        monkey = Tile(
            3, 3,
            ('beskrivning', 'vad man ser från en närliggande tile'),
            (directions.up, directions.left),
            ('hatchet',),
            ('Prata med apan',))

        # Rad 4
        beach = Tile(
            1, 4,
            ('beskrivning', 'vad man ser från en närliggande tile'),
            (directions.up), (items.shovel))

        mountain = Tile(
            2, 4,
            ('beskrivning', 'vad man ser från en närliggande tile'),
            (directions.up, directions.right))

        cave_entrance = Tile(
            3, 4,
            ('beskrivning', 'vad man ser från en närliggande tile'),
            (directions.down, directions.right, directions.left))

        cave_1 = CavePuzzleTile(
            4, 4,
            ('beskrivning', 'vad man ser från en närliggande tile'),
            (directions.left,),
            (items.torch,))

        # Rad 5
        cave_2 = CavePuzzleTile(
            3, 5,
            ('beskrivning', 'vad man ser från en närliggande tile'),
            (directions.up,),
            (items.torch,))

        hidden_cave = Tile(
            4, 5,
            ('beskrivning', 'vad man ser från en närliggande tile'),
            (directions.up, directions.right),
            findable_items=(items.hatchet,))

        # Skapa kartan med alla tiles
        self.level = (
            (None, hall, kitchen, None),
            (turtle, cottege_entrance, lake, parrot),
            (base, jungle1, monkey, None),
            (beach, mountain, cave_entrance, cave_1),
            (None, None, cave_2, hidden_cave)
        )

    def get_tile(self, x: int, y: int) -> Tile | CavePuzzleTile:
        '''Tile objekt vid koordinat x, y. 1, 1 är övre vänstra hörnet'''

        return self.level[y-1][x-1]

    def format_directions(self, tile: Tile) -> tuple:
        '''Hämta beskrivningar från närliggande tiles'''

        descriptions = []

        for direction in tile.avalible_directions:

            # Hämta närliggande tile
            if direction == directions.up:
                adjacent_tile = self.get_tile(tile.x, tile.y - 1)

            elif direction == directions.down:
                adjacent_tile = self.get_tile(tile.x, tile.y + 1)

            elif direction == directions.right:
                adjacent_tile = self.get_tile(tile.x + 1, tile.y)

            elif direction == directions.left:
                adjacent_tile = self.get_tile(tile.x - 1, tile.y)

            # Om det inte finns någon beskrivning
            if not adjacent_tile.description[1]:
                continue

            descriptions.append(adjacent_tile.description[1] % {'direction': direction})

        return descriptions
