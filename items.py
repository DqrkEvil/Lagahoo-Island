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
def pickup_item(current_tile: level.Tile, game_level: level.Level) -> None:
    '''Pickup item from tile'''

    item = current_tile.findable_item

    # Om det finns ett item att plocka här
    if item:
        inventory.append(item)
        current_tile.findable_item = None

        # Lägg till väg till grottan om man plockar upp fackla
        if item == torch:
            mountain_tile = game_level.get_tile(4, 3)
            mountain_tile.descriptions[0] = 'Du finner dig högt upp i bergen, oj vad kallt det var här.'
            mountain_tile.connections('add', directions.up, game_level)

        if item == shovel:
            current_tile.descriptions[0] = '\nDu ser en gravsten'

        logger.info(f'Picked up {item}')
        IO.standardPrint(f'Du plockade upp: {item}')

    else:
        IO.standardPrint('Det finns inget att plocka upp här')

def use_item(current_tile: level.Tile, game_level: level.Level) -> None:
    '''Använd item på tile'''

    # Kolla om något item i inventory går att använda här (https://stackoverflow.com/questions/740287/how-to-check-if-one-of-the-following-items-is-in-a-list)
    if any(item in current_tile.usable_items for item in inventory):

        # Skapa en lista med alla items i inventory
        useable_items = []

        for n, item in enumerate(inventory):
            useable_items.append(f'{n + 1}: {item.capitalize()}')

        IO.standardPrint('Du har:', *useable_items, '(välj med nummer och sedan enter)', add_dots=False)

        # Tills man valt ett item som går att använda
        while True:
            selected_index = IO.integer_input(*range(1, len(useable_items)))

            if selected_index in current_tile.usable_items:
                break

        item = inventory[selected_index - 1]

        # Vad olika items gör när man använder dom på tiles där man kan använda dom
        if item == golden_seaweed:
            IO.standardPrint("Sköldpaddan blev väldigt glad och hjälpte dig komma tillbaka till fastlandet genom att låta dig rida.\nGrattis, Du vann spelet!!!")

        elif item == shovel:
            IO.standardPrint("Du gräver upp en dynamit")

            # Uppdatera tile attribut
            current_tile.usable_items.remove(shovel)
            current_tile.findable_item = None
            inventory.append(dynamite)

        elif item == dynamite:
            IO.standardPrint("Du la ner dynamiten, du kanske borde gå iväg så du inte sprängs med den")

            # Uppdatera tile attribut
            current_tile.usable_items.remove(dynamite)
            current_tile.descriptions[0] = 'Du är djupare i grottan, det ligger grus och större stenblock på golvet'
            current_tile.connections('add', directions.right, game_level)

        elif item == hatchet and current_tile.y == 3:
            IO.standardPrint("Du hugger ner trädet och får plankor och lianer.\n*detta är perfekt att bygga en flotte av*")

            # Uppdatera tile attribut
            current_tile.usable_items.remove(hatchet)
            current_tile.descriptions[0] = 'Du befinner dig i jungeln'
            inventory.append(materials)

        elif item == hatchet and current_tile.y == 2:
            # Om man använder yxan på tile med apan och lådorna
            IO.standardPrint("Du förstörde lådorna som apan står på så apan kan få bananerna som var inuti dom, som tack flyttade apan ur vägen så du nu kan gå vidare")

            # Uppdatera tile attribut
            current_tile.usable_items.remove(hatchet)
            current_tile.descriptions = ['Du ser apan som du hjälpte sitta och äta bananer från lådorna', 'Du ser en apa som äter bananer %(direction)s']
            current_tile.connections('add', directions.left, game_level)

        logger.info(f'Used {item} on {current_tile.x},{current_tile.y}')

    else:
        IO.standardPrint('Du kan inte använda något här')
