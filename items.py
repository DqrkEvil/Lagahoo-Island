'''Fil för alla föremål'''

import logging

import directions
import IO
import text
import level

logger = logging.getLogger('__main__')

# Föremål
golden_seaweed = 'guldigt sjögräs'
shovel = 'spade'
torch = 'fackla'
dynamite = 'dynamit'
hatchet = 'yxa'
materials = 'plankor och lianer'

# Spelarens inventory
inventory = []

# Funktioner
def pickup_item(current_tile: level.Tile, game_level: level.Level) -> None:
    '''Pickup item from tile'''

    item = current_tile.findable_item

    # Om det finns ett item att plocka här
    if item:
        inventory.append(item)
        current_tile.findable_item = None

        # Lägg till väg till grottan om man plockar upp fackla
        if item == torch:
            current_tile.descriptions[0] = '\nDu är i stugans kök'

            mountain_tile = game_level.get_tile(4, 3)
            mountain_tile.descriptions[0] = 'Du finner dig högt upp i bergen, oj vad kallt det var här.'
            mountain_tile.connections('add', directions.up, game_level)

        if item == shovel:
            current_tile.descriptions[0] = '\nDu ser en gravsten'

        if item == hatchet:
            current_tile.descriptions[0] = '\nDet finns en tom pedistal här'

        logger.info(f'Picked up {item}')
        IO.standardPrint(f'Du plockade upp: {item}')

    else:
        IO.standardPrint('Det finns inget att plocka upp här')

def use_item(current_tile: level.Tile, game_level: level.Level) -> None:
    '''Använd item på tile'''

    if current_tile.usable_item in inventory:

        item = current_tile.usable_item

        # Vad olika items gör när man använder dom på tiles där man kan använda dom
        if item == golden_seaweed:
            IO.standardPrint(text.postGameLore['turtle'])
            game_level.current_tile = game_level.get_tile(3, 4)

        elif item == materials:
            IO.standardPrint(text.postGameLore['raft'])
            game_level.current_tile = game_level.get_tile(3, 4)

        elif item == shovel:
            IO.standardPrint('Du använder spaden för att gräva upp en dynamit')

            # Uppdatera tile attribut
            current_tile.usable_item = materials
            current_tile.descriptions[0] = '\nDet är bara en tom strand här, och ett hål där dynamiten var.\n*Jag skulle kunna sjösätta en flotte här*'

            inventory.append(dynamite)

        elif item == dynamite:
            IO.standardPrint('Du tände dynamiten och placerade den nära väggen. Efter ljudet av en explosion går du tillbaka')

            # Uppdatera tile attribut
            current_tile.usable_item = None
            current_tile.descriptions[0] = 'Du är djupare i grottan, det ligger grus och större stenblock på golvet'
            current_tile.connections('add', directions.right, game_level)

        elif item == hatchet and current_tile.y == 3:
            IO.standardPrint('Du hugger ner trädet och får plankor och lianer.\n*detta är perfekt att bygga en flotte av*')

            # Uppdatera tile attribut
            current_tile.usable_item = None
            current_tile.descriptions[0] = 'Du befinner dig i jungeln'
            inventory.append(materials)

        elif item == hatchet and current_tile.y == 2:
            # Om man använder yxan på tile med apan och lådorna
            IO.standardPrint('Du förstörde lådorna som apan står på så apan kan få bananerna som var inuti dem, som tack flyttade apan ur vägen så du nu kan gå vidare')

            # Uppdatera tile attribut
            current_tile.usable_item = None
            current_tile.descriptions = ['Du ser apan som du hjälpte sitta och äta bananer från lådorna', 'Du ser en apa som äter bananer %(direction)s']
            current_tile.connections('add', directions.left, game_level)

        logger.info(f'Used {item} on {current_tile.x},{current_tile.y}')

    else:
        IO.standardPrint('Du har inget att använda här')

def list_items() -> None:
    '''Lista alla föremål man har'''

    IO.standardPrint('Du har:', *inventory, add_dots=False)
