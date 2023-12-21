'''Hanterar allting som har med kartan att göra'''

from __future__ import annotations

from typing import Literal

import directions
import items


# Classes
class Tile():
    '''Basklassen för alla tiles på kartan'''

    def __init__(self,
                 x: int,
                 y: int,
                 descriptions: tuple[str],
                 available_directions: tuple,
                 useable_items: tuple = tuple(),
                 actions: tuple = tuple(),
                 findable_item: str | None = None
                 ) -> None:
        '''
        :x: tile koordinat
        :y: tile koordinat
        :descriptions: tuple med beskrivning av denna tilen som skrivs ut när spelaren kommer hit och ev. om man ser denna tile från en bredvid
        :available_directions: alla vägar att gå från denna tile
        :useable_items: items som går att använda på denna tile
        :actions: alla möjliga aktiviteter på denna tile
        :findable_items: saker som går att ta från denna tile'''

        self.x = x
        self.y = y

        self.descriptions = descriptions
        self.available_directions = available_directions
        self.useable_items = useable_items
        self.findable_item = findable_item
        self.actions = actions

        self.explored = False

    def edit_connections(self, method: Literal['add', 'remove'], new_direction: str, level: Level, oneway: bool = False):
        '''Ändra vilka kopplingar som finns mellan tiles'''

        if method == 'add':
            # Om  riktnigen redan finns
            if new_direction in self.available_directions:
                return

            # Lägg till riktningen på nuvarande tile
            self.available_directions = (*self.available_directions, new_direction)

            # Lägg till inversen av riktningen på tilen som riktningen leder till så att man kan gå tillbaka
            if not oneway:
                inverted_direction = directions.invert_directions((new_direction,))[0]
                adjacent_tile = level.get_tile(tile=self, direction=new_direction)

                adjacent_tile.edit_connections('add', inverted_direction, level)

        if method == 'remove':
            # Om riktningen inte finns
            if new_direction not in self.available_directions:
                return

            # Ta bort riktningen
            self.available_directions = tuple(direction for direction in self.available_directions if direction != new_direction)

            if not oneway:
                inverted_direction = directions.invert_directions((new_direction,))[0]
                adjacent_tile = level.get_tile(tile=self, direction=new_direction)

                adjacent_tile.edit_connections('remove', inverted_direction, level)

class Level():
    '''Klass för att hantera kartan'''

    def __init__(self) -> None:
        self.generate_level()

    def generate_level(self):
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
            findable_item=items.torch)

        # Rad 2
        turtle = Tile(
            1, 2,
            ('Du står på stranden, nära dig ligger en sköldpadda', '%(direction)s ligger en sköldpadda'),
            (directions.down,),
            (items.golden_seaweed,))

        cottege_entrance = Tile(
            2, 2,
            ('Du står i jungeln bredvid en liten stuga, dörren står på glänt', 'Det finns en stuga %(direction)s', 'Ytterdörren finns %(direction)s'),
            (directions.up, directions.down))

        lake = Tile(
            3, 2,
            ('Du står brevid en sjö', 'En sjö glittrar %(direction)s från dig'),
            (directions.right,))

        parrot = Tile(
            4, 2,
            ('Du ser en papegoja som ser väldigt prat glad ut \n*papegojan kanske ger dig något föremål om du hjälper han*', 'Du ser en papegoja %(direction)s om dig'),
            (directions.left,),
            actions=('Prata med papegoja',))

        # Rad 3
        base = Tile(
            1, 3,
            ('Du är tillbaka till där du vaknade upp brevid den nu slocknade lägerelden', 'Du ser en liten lägereld som nu har slocknat %(direction)s, det är där du vaknade upp'),
            (directions.up, directions.down, directions.right))

        jungle1 = Tile(
            2, 3,
            ('Du befinner dig i jungeln, det finns iget märkvärdigt här', 'Du ser en öppning bland träden till %(direction)s om dig'),
            (directions.up, directions.down, directions.right, directions.left),
            (items.hatchet,))

        monkey = Tile(
            3, 3,
            ('Du ser en apa som står på några lådor, \n*hmmm det kanske finns något i lådorna*', 'Du ser en apa som står på några lådor %(direction)s'),
            (directions.left,),
            (items.hatchet,),
            ('Prata med apan',))
        
        jungle2 = Tile(
            4, 3,
            ("Du ser en gravsten med en spade stickande ut från den","Du ser en gravsten %(direction)s"),
            (directions.left,),
            findable_item=items.shovel)

        # Rad 4
        beach = Tile(
            1, 4,
            ('Du ser inget speciellt förutom något du inte kan identifiera som sticker ut ur sanden \n *om jag har en spade kanske jag hade kunnat gräva upp det*', 'Stranden fortsätter %(direction)s'),
            (directions.up,),
            (items.shovel,))

        mountain = Tile(
            2, 4,
            ('Du finner dig högt upp i bergen, oj va kalt det var här', 'Du ser några höga berg %(direction)s om dig'),
            (directions.up, directions.right))

        cave_entrance = Tile(
            3, 4,
            ("du går in i grottan med din nyligt tända fackla", 'Du ser ingången till grottan %(direction)s'),
            (directions.down, directions.right, directions.left))

        cave_1 = Tile(
            4, 4,
            ('Du ser en ganska svag vägg här \n*jag hade säkert kunna spränga denna väggen om jag hade lite dynamit*', 'Grottan fortsätter %(direction)s'),
            (directions.left,),
            (items.dynamite,))

        # Rad 5
        spikes = Tile(
            2,5,
            ("Du hoppar ner för klippan och blir spetsad av spikarna där nere","Du kollar ner för klippan %(direction)s om dig och ser några spikar \n snälla hoppa inte"),
            (None,))

        cave_2 = Tile(
            3, 5,
            ('Du ser inget som hade kunnat hjälpa dig här, bäst att bara gå tillbaka', 'Grottan fortsätter %(direction)s'),
            (directions.up,))

        hidden_cave = Tile(
            4, 5,
            ('Du ser en yxa på en pedistal \n*denna kan man nog använda för att ta sönder obejekt gjort av trä*', 'Du ser ett litet rum %(direction)s som inte var där tidigare'),
            (directions.up,),
            findable_item=items.hatchet)

        # Skapa kartan med alla tiles
        self.level = (
            (None, hall, kitchen, None),
            (turtle, cottege_entrance, lake, parrot),
            (base, jungle1, monkey, jungle2),
            (beach, mountain, cave_entrance, cave_1),
            (None, spikes, cave_2, hidden_cave)
        )

    def get_tile(self, x: int | None = None, y: int | None = None, tile: Tile | None = None, direction: str | None = None) -> Tile:
        '''Tile objekt vid koordinat x, y eller åt ett håll från nuvarande. 1, 1 är övre vänstra hörnet'''

        if x and y:
            return self.level[y-1][x-1]
        
        elif tile and direction:
            if direction == directions.up:
                adjacent_tile = self.get_tile(tile.x, tile.y - 1)

            elif direction == directions.down:
                adjacent_tile = self.get_tile(tile.x, tile.y + 1)

            elif direction == directions.right:
                adjacent_tile = self.get_tile(tile.x + 1, tile.y)

            elif direction == directions.left:
                adjacent_tile = self.get_tile(tile.x - 1, tile.y)

            return adjacent_tile

    def format_directions(self, tile: Tile) -> tuple:
        '''Hämta beskrivningar från närliggande tiles'''

        descriptions = []
        
        # Hämta alla närliggande tiles
        for direction in tile.available_directions:

            adjacent_tile = self.get_tile(tile=tile, direction=direction)

            # Om det inte finns någon beskrivning
            if not adjacent_tile.descriptions[1]:
                continue

            #* Några speciella beskrivningar
            # Från insidan av huset mot utsidan
            if tile.x == 2 and tile.y == 1 and direction == directions.down:
                descriptions.append(adjacent_tile.descriptions[2] % {'direction': direction})
                continue
            
            #* Standard beskrivningar
            descriptions.append(adjacent_tile.descriptions[1] % {'direction': direction})

        # Stooooor bokstav (ifall beskrivningen börjar med "%(direction)s")
        descriptions = [i.capitalize() for i in descriptions]

        return descriptions
