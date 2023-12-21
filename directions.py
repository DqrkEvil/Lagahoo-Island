'''Fil för standardiserade riktningar'''

up = 'till vänster'
down = 'till höger'
right = 'framåt'
left = 'bakåt'

def invert_directions(directions: tuple) -> tuple:
    '''Motsatsen till alla riktningar i en tuple'''

    return tuple(up if direction == down else down if direction == up else right if direction == left else left for direction in directions)
