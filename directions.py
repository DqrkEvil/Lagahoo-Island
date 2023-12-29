'''Fil för standardiserade riktningar'''

up = 'framåt'
down = 'bakåt'
right = 'till höger'
left = 'till vänster'

def invert_directions(directions: list) -> list:
    '''Motsatsen till alla riktningar i en tuple'''

    return [up if direction == down else down if direction == up else right if direction == left else left for direction in directions]
