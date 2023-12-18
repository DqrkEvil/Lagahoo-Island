'''Fil för alla föremål'''

import level

inventory = []

# Föremål
golden_seaweed = 'guldigt sjögräs'
shovel = 'spade'
torch = 'fackla'
dynamite = 'dynamit'
hatchet = 'yxa'

# Funktioner
def pickup_item(current_tile: level.Tile) -> str:
    '''Pickup item from tile'''

    # Take item from tile and put in inventory
    item = current_tile.findable_item
    inventory.append(item)
    current_tile.findable_item = None

    return item
