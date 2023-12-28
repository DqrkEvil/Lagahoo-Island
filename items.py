'''Fil för alla föremål'''

import logging

import directions
import IO
import level

logger = logging.getLogger('__main__')

# Föremål
golden_seaweed = 'guldigt sjögräs'
shovel = 'spade'
torch = 'fackla'
dynamite = 'dynamit'
hatchet = 'yxa'
materials = "plankor och lianer"

# Spelarens inventory
inventory = []

# Funktioner
def pickup_item(current_tile: level.Tile) -> str:
    '''Pickup item from tile'''

    # Take item from tile and put in inventory
    item = current_tile.findable_item
    inventory.append(item)
    current_tile.findable_item = None

    return item

def use_item(current_tile: level.Tile, item: str, game_level: level.Level):
    '''Use item on tile'''

    #vad olika items gör när man använder dom på tiles där man kan använda dom
    if item == golden_seaweed:
        IO.standardPrint("Sköldpaddan blev väldid glad och hjälpte dig komma tillbaka till fastland genom att låta dig rida på sig \n Grattis, Du vann spelet!!!")

    elif item == shovel:
        IO.standardPrint("Du gräver upp en dynamit")
        inventory.append(dynamite)

    #TODO göra så att man bara kan gå till tilen "hiddenCave" om man spränger dynamiten
    elif item == dynamite:
        IO.standardPrint("Du la ner dynamiten, du kanske borde gå iväg så du inte sprängs med den")


    elif item == hatchet and current_tile.x == 2:
        IO.standardPrint("Du hugger ner trädet och får plankor och lianer\n *detta är perfekt att bygga en flotte av*")
        inventory.append(materials)

    elif item == hatchet and current_tile.x == 3:
        IO.standardPrint("Du förstörde lådorna som apan står på så apan kan få bananerna som var inuti dom, som tack flyttade apan ur vägen så du nu kan gå vidare")
        current_tile.edit_connections('add', directions.up, game_level)
        logger.info('Path to lake added')
