'''Hanterar all sparning av saker man gjort'''

import datetime
import json
import logging
import os

import IO
import text

logger = logging.getLogger('__main__')

def save(slot: str, **data) -> None:
    '''Sparar allt spelaren har gjort än så länge till en slot'''

    # Ladda från filen om den finnns
    if os.path.isfile('saves.json'):
        with open('saves.json', 'r', encoding='UTF-8') as file:
            saved_data = json.load(file)

    # Annars skapa en tom
    else:
        saved_data = {slot: {}}

    # Lägg till datun när sparfilen använts
    data.update({'date': str(datetime.datetime.now()).split(' ', maxsplit=1)[0]})

    # Lägg till datan och skriv den till filen
    saved_data[slot].update(data)

    with open('saves.json', 'w', encoding='UTF-8') as file:
        json.dump(saved_data, file, ensure_ascii=False, indent=4, sort_keys=True)

def load() -> dict:
    '''Ladda in all spardata'''

    with open('saves.json', 'r', encoding='UTF-8') as file:
        saved_data = json.load(file)

    return saved_data

def select_slot() -> (dict, str):
    '''Användaren får välja en slot
    
    :return: data från vald slot och slotnummer'''

    # Ladda in data om det finns någon annars tom dict
    if os.path.isfile('saves.json'):
        data = load()

    else:
        data = {}

    # Skapa en dict med datum när sparplatsen senaste användes
    save_dates = tuple(data[str(n)]['date'] if str(n) in data else 'Aldrig' for n in range(1, 4))

    # Ge bara möjligheten om det finns ett sparat spel
    if data:
        IO.standardPrint('Vad vill du göra?', '1. Nytt spel', '2. Ladda spel', add_dots=False)
        mode = IO.integer_input(1, 2)

    else:
        mode = 1

    # Nytt spel läge
    if mode == 1:
        print(text.slotSelection %
                {'slot_selection': 'Välj en siffra att spara ditt spel på:',
                'slot1': save_dates[0],
                'slot2': save_dates[1],
                'slot3': save_dates[2]})

        game_slot = IO.integer_input(1, 2, 3)

        # Skapa eller töm den valda platen
        data.update({str(game_slot): {}})

    # Ladda in spel läge
    elif mode == 2:
        print(text.slotSelection %
                    {'slot_selection': 'Välj en siffra att ladda ditt spel ifrån:',
                    'slot1': save_dates[0],
                    'slot2': save_dates[1],
                    'slot3': save_dates[2]})

        # Bara platser som är använda får väljas
        game_slot = IO.integer_input(*(n + 1 for n, date in enumerate(save_dates) if date != 'Aldrig'))

    # En key måste vara str i json format
    game_slot = str(game_slot)
    logger.debug(f'Slot selected: {game_slot}')

    return data[game_slot], game_slot
