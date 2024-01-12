'''Hanterar allting som har med kartan att göra'''

from __future__ import annotations

import logging
from typing import Literal

import directions
import items

logger = logging.getLogger('__main__')

# Classes
class Tile():
    '''Basklassen för alla tiles på kartan'''

    def __init__(self,
                 x: int,
                 y: int,
                 descriptions: list[str],
                 available_directions: list,
                 usable_items: list | None = None,
                 findable_item: str | None = None
                 ) -> None:
        '''Skapa en ny tile
        :x: tile koordinat
        :y: tile koordinat
        :descriptions: lista med beskrivning av denna tilen som skrivs ut när spelaren kommer hit och ev. om man ser denna tile från en bredvid
        :available_directions: alla vägar att gå från denna tile
        :useable_items: items som går att använda på denna tile
        :findable_items: saker som går att ta från denna tile'''

        self.x = x
        self.y = y

        self.descriptions = descriptions
        self.available_directions = available_directions
        self.usable_items = usable_items if usable_items else []  # Måste vara en lista för att koden ska fungera
        self.findable_item = findable_item

        self.explored = False

    def set_explored(self, explored: bool) -> None:
        '''Denna tile har har besökts'''

        self.explored = explored

    def connections(self, method: Literal['add', 'remove'], direction: str, level: Level, one_way: bool = False):
        '''Ändra vilka kopplingar som finns mellan tiles
        
        :method: Lägg till eller ta bort koppling
        :direction: Åt vilket kopplingen ska vara från tilen
        :level: Den nuvarande kartan
        :one_way: Lägg bara till kopplingen åt ett håll'''

        if method == 'add':
            # Om  riktnigen redan finns
            if direction in self.available_directions:
                return

            # Lägg till riktningen på nuvarande tile
            self.available_directions.append(direction)
            logger.info(f'Path from {self.x},{self.y} added in direction: {direction}')

        if method == 'remove':
            # Om riktningen inte finns
            if direction not in self.available_directions:
                return

            # Ta bort riktningen
            self.available_directions.remove(direction)
            logger.info(f'Path from {self.x},{self.y} removed in direction: {direction}')

        # Ändra inversen av riktningen på tilen som riktningen leder till så att man kan gå tillbaka
        if not one_way:
            inverted_direction = directions.invert_directions((direction,))[0]
            adjacent_tile = level.get_tile(tile=self, direction=direction)

            adjacent_tile.connections(method, inverted_direction, level)

class Level():
    '''Klass för att hantera kartan'''

    def __init__(self, operation: Literal['new', 'load'] = 'new', level_data: dict | None = None) -> None:

        if operation == 'new':
            self.level = self.generate_level()

        elif operation == 'load':
            self.load_level(level_data)

    def generate_level(self) -> list[list[Tile | None]]:
        '''Skapa kartan för spelet'''

        # Rad 1
        parrot = Tile(
            2, 1,
            ['Du ser en papegoja som ser pratglad ut\n*papegojan kanske ger dig något föremål om du hjälper den*', 'Du ser en papegoja %(direction)s'],
            [directions.down]
            )

        jungle2 = Tile(
            3, 1,
            ['Det finns en gravsten med en spade som sticker fram","Du ser en gravsten %(direction)s'],
            [directions.down],
            findable_item=items.shovel
            )

        cave1 = Tile(
            4, 1,
            ['Du är djupare i grottan och ser en ganska svag vägg här\n*jag hade säkert kunna spränga denna om jag hade lite dynamit*', 'Grottan fortsätter %(direction)s'],
            [directions.down],
            [items.dynamite]
            )

        hidden_cave = Tile(
            5, 1,
            ['Du ser en yxa på en pedistal\n*denna kan man nog vara användbar*', 'Du ser ett litet rum %(direction)s som inte varit synligt tidigare'],
            [],
            findable_item=items.hatchet
            )

        # Rad 2
        kitchen = Tile(
            1, 2,
            ['Du är i stugans kök', 'Det finns ett kök %(direction)s'],
            [directions.down],
            findable_item=items.torch
            )

        lake = Tile(
            2, 2,
            ['Du står brevid en sjö', 'En sjö glittrar %(direction)s från dig'],
            [directions.up]
            )

        monkey = Tile(
            3, 2,
            ['Du ser en apa som står på några lådor\n*hmmm det kanske finns något i lådorna*', 'Du ser en apa som står på några lådor %(direction)s'],
            [directions.up, directions.down],
            [items.hatchet]
            )

        cave_entrance = Tile(
            4, 2,
            ["Du går in i grottan med din nyligt tända fackla", 'Du ser ingången till grottan %(direction)s'],
            [directions.up, directions.right]
            )

        cave2 = Tile(
            5, 2,
            ['Du ser inget som hade kunnat hjälpa dig här, bäst att bara gå tillbaka', 'Grottan fortsätter %(direction)s'],
            [directions.left]
            )

        # Rad 3
        hall = Tile(
            1, 3,
            ['Du är i hallen av stugan', 'Du ser stugans hall %(direction)s'],
            [directions.up, directions.right]
            )

        cottage = Tile(
            2, 3,
            ['Du står i jungeln bredvid en liten stuga, dörren står på glänt', 'Det finns en stuga %(direction)s', 'Ytterdörren finns %(direction)s'],
            [directions.left, directions.right]
            )

        jungle1 = Tile(
            3, 3,
            ['Du befinner dig i jungeln, det finns ett stort träd här som skulle gå att använda till en flotte\n*det hade säkert gått att hugga ner med en yxa*', 'Du ser en öppning bland träden %(direction)s om dig'],
            [directions.up, directions.down, directions.right, directions.left],
            [items.hatchet]
            )

        mountain = Tile(
            4, 3,
            ['Du finner dig högt upp i bergen, oj vad kallt det var här\nDet finns en mörk grotta framför dig\n*här skulle det vara bra att ha en fackla*', 'Du ser några höga berg %(direction)s om dig'],
            [directions.right, directions.left]
            )

        spikes = Tile(
            5, 3,
            ["Du hoppar ner för klippan och blir spetsad av spikarna där nere","Du kollar ner för klippan %(direction)s om dig och ser några spikar, snälla hoppa inte"],
            tuple()
            )

        # Rad 4
        turtle = Tile(
            2, 4,
            ['Du står på stranden, nära dig ligger en sköldpadda', '%(direction)s ligger en sköldpadda'],
            [directions.right],
            [items.golden_seaweed]
            )

        base = Tile(
            3, 4,
            ['Du är tillbaka till där du vaknade upp brevid den nu slocknade lägerelden', 'Du ser en liten lägereld som nu har slocknat %(direction)s, det är där du vaknade upp'],
            [directions.right, directions.left, directions.up]
            )

        beach = Tile(
            4, 4,
            ['Du ser inget speciellt förutom något du inte kan identifiera som sticker ut ur sanden\n*om jag har en spade kanske jag hade kunnat gräva upp det*', 'Stranden fortsätter %(direction)s'],
            [directions.left],
            [items.shovel],
            items.dynamite
            )

        # Returnera kartan med alla tiles
        return (
            (None, parrot, jungle2, cave1, hidden_cave),
            (kitchen, lake, monkey, cave_entrance, cave2),
            (hall, cottage, jungle1, mountain, spikes),
            (None, turtle, base, beach, None)
        )

    def load_level(self, saved_level_data: list[dict]):
        '''Ladda in kartan från sparfilen'''

        self.level = self.generate_level()

        # Gå igenom alla sparade tiles
        for saved_tile in saved_level_data:

            # Hämta tile från den nya kartan vid samma position
            new_tile = self.get_tile(saved_tile['x'], saved_tile['y'])

            # Gå igenom alla sparade ändringar och ändra på den riktiga kartan
            for attribute in set(saved_tile.keys()) - {'x', 'y'}:  # ChatGPT lärde mig om set operationer som

                setattr(new_tile, attribute, saved_tile[attribute])

    def get_tile(self, x: int | None = None, y: int | None = None, tile: Tile | None = None, direction: str | None = None) -> Tile:
        '''Tile objekt vid koordinat x, y eller åt ett håll från nuvarande. 1, 1 är övre vänstra hörnet'''

        if x and y:
            return self.level[y-1][x-1]

        if tile and direction:
            if direction == directions.up:
                adjacent_tile = self.get_tile(tile.x, tile.y - 1)

            elif direction == directions.down:
                adjacent_tile = self.get_tile(tile.x, tile.y + 1)

            elif direction == directions.right:
                adjacent_tile = self.get_tile(tile.x + 1, tile.y)

            elif direction == directions.left:
                adjacent_tile = self.get_tile(tile.x - 1, tile.y)

            return adjacent_tile

    def get_descriptions(self, tile: Tile) -> tuple:
        '''Hämta beskrivningar från närliggande tiles'''

        descriptions = []

        # Hämta alla närliggande tiles
        for direction in tile.available_directions:

            adjacent_tile = self.get_tile(tile=tile, direction=direction)

            # Om det inte finns någon beskrivning
            if not adjacent_tile.descriptions[1]:
                continue

            # Några speciella beskrivningar
            # Från insidan av huset mot utsidan
            if tile.x == 1 and tile.y == 3 and direction == directions.right:
                descriptions.append(adjacent_tile.descriptions[2] % {'direction': direction})
                continue

            # Standard beskrivningar
            descriptions.append(adjacent_tile.descriptions[1] % {'direction': direction})

        # Stooooor bokstav (ifall beskrivningen börjar med "%(direction)s")
        descriptions = [i.capitalize() for i in descriptions]

        return descriptions

    def compress_tiles(self) -> list:
        '''Komprimera alla tiles till en lista med tiles som bara inkluderar skillnader från en ny karta'''

        current_tiles = tuple(tile for row in self.level for tile in row) # lite cred till ChatGPT för en del av generatorn: (expression for outer_item in outer_sequence for inner_item in inner_sequence)
        new_tiles = tuple(tile for row in self.generate_level() for tile in row)
        saving_tiles = []

        for current_tile, new_tile in zip(current_tiles, new_tiles):

            # Om det finns ett tile objekt
            if current_tile:
                differences = ({'x': current_tile.x, 'y': current_tile.y})
                differences.update({key: value for key, value in current_tile.__dict__.items() if value != new_tile.__dict__[key]})

                saving_tiles.append(differences)

        return saving_tiles
