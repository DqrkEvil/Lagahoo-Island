'''Förvarar alla större textbitar och ascii art för spelet'''

import directions

mainMenuText = r'''




                            ┌───────────────────────────────────────────────────────────────────────────────┐
                            │                                                                               │
                            │  __          ___       _______      ___       __    __    ______     ______   │
                            │ |  |        /   \     /  _____|    /   \     |  |  |  |  /  __  \   /  __  \  │
                            │ |  |       /  ^  \   |  |  __     /  ^  \    |  |__|  | |  |  |  | |  |  |  | │
                            │ |  |      /  /_\  \  |  | |_ |   /  /_\  \   |   __   | |  |  |  | |  |  |  | │
                            │ |  `----./  _____  \ |  |__| |  /  _____  \  |  |  |  | |  `--'  | |  `--'  | │
                            │ |_______/__/     \__\ \______| /__/     \__\ |__|  |__|  \______/   \______/  │
                            │                                                                               │
                            │          __       _______. __          ___      .__   __.  _______            │
                            │         |  |     /       ||  |        /   \     |  \ |  | |       \           │
                            │         |  |    |   (----`|  |       /  ^  \    |   \|  | |  .--.  |          │
                            │         |  |     \   \    |  |      /  /_\  \   |  . `  | |  |  |  |          │
                            │         |  | .----)   |   |  `----./  _____  \  |  |\   | |  '--'  |          │
                            │         |__| |_______/    |_______/__/     \__\ |__| \__| |_______/           │
                            │                                                                               │
                            └───────────────────────────────────────────────────────────────────────────────┘

                            
'''

startGameText = '                                                      Tryck ENTER för att starta spelet'

# ASCII art tagen från https://www.reddit.com/r/ASCII_Archive/comments/ewsf5g/the_night_sky/
preGameLore = '''
.　　　　　　　　　　 ✦ 　　　　   　 　　　˚　　　　　　　　　　　　　　　　　　　　   
　　　　　　　　　　　　　.　　　☄　　　　　　　　 　　　. 　　 　　　　　　　 ✦ 　　　　　　　　　　 
‍ ‍ ‍ ‍ 　　　　 　　　　　　　　　　　　,　　   　 .　　　　　　　　　　　　　.　　　ﾟ　  　　　.　　　　　　　　　　　　　
✦ 　　　　　　,　　　　　　　.　　　　　　    　　　　 　　　　　　　　　　　　　　　　　　  . 
　　　　　　　　　　　　　　　　　　    　      　　　　　        　　　　　　　　　　　　　.
　　　　　　　　　　　　　 　           　　　　　　　　　　　　　　　　　　　. ˚　　　 　   . ,
　　　　　　　　　　　       　    　　　　　　　　　　　　　. .　　　  　　    ✦　 ✦　　　　 
　　　　　.　　　　　　　　　　　　　.　　　　　✦　　　　　　　　　　
‍ ‍ ‍ ,　 　　　　　　　　　　　　　　* .　　　　　 　　　　　　　　　　　　　　.　　　　　　　　　　
✦ 　　　　   　 　　　˚　　　　　　　　　　　　　　*　　　　　　  
　　　　　　　　　　　　　　　.　　　　　　　　　　　　　　 ✦
　　　　　　　　　　　　　 　           　　　　　　　　　　　　　　　　　　　. ˚　　　 　   . ,
　　　　　　　　　　　  　　　　 　　,　　　 ‍ ‍ ‍ ‍ 　 　　　　　　　　　　　　.　　　　　 　　 　　　

Du ligger på den fuktiga sanden, den tropiska luften fyller dina lungor medans du stirrar upp i det djupt mörkblå eviga tomrum fullt av stjärnor. 
Tankarna väller fram; 
Vad hände med de andra, är det saken som vi skulle undersöka som är anledningen till att de har försvunnit? 
Hur ska jag komma tillbaka till fastlandet?
Är jag den enda överlevaren?
Desto mer du ligger och tänker desto tyngre blir ögonlocken.
Till slut blir det svart.'''

postGameLore = {
    'turtle': 'Du kommer hem efter att ha varit på ön i flera veckor med sköldpaddan vid din sida. Din första tankte är vart din familj är och när du öppnar dörren så ser du en annan familj i ditt hus. Åh nej du har inte betalat ränta och har blivit av med ditt hus. Men det är lungt för sköldpaddan låter dig bo med den så ni lever lyckliga i alla era dar',
    'raft': 'Du kommer hem och din familj är överlyckliga att se dig. Dom har varit så oroliga och tagit hand om ditt hus och din katt åt dig.'
}

controlInfo = f'''Information:

Använd WASD eller piltangenterna för att gå runt:
W / pil upp: {directions.up}
A / pil vänster: {directions.left}
S / pil neråt: {directions.down}
D / pil höger: {directions.right}

i: information

e: använd föremål

q: plocka upp föremål

f: lista föremål du har

Spelet sparas varje gång du återvänder till startplatsen på stranden'''

slotSelection = '''%(slot_selection)s
 .-------------------.    .-------------------.    .-------------------. 
| .-----------------. |  | .-----------------. |  | .-----------------. |
| |       __        | |  | |      _____      | |  | |      ______     | |
| |      /  |       | |  | |     / ___ `.    | |  | |     / ____ `.   | |
| |      `| |       | |  | |    |_/___) |    | |  | |     `'  __) |   | |
| |       | |       | |  | |     .'____.'    | |  | |     _  |__ '.   | |
| |      _| |_      | |  | |    / /____      | |  | |    | \____) |   | |
| |     |_____|     | |  | |    |_______|    | |  | |     \______.'   | |
| |                 | |  | |                 | |  | |                 | |
| |  Senast använt: | |  | |  Senast använt: | |  | |  Senast använt: | |
| |  %(slot1)-12s   | |  | |  %(slot2)-12s   | |  | |  %(slot3)-12s   | |
| '-----------------' |  | '-----------------' |  | '-----------------' |
 '-------------------'    '-------------------'    '-------------------' '''

parrot_riddle = ('Vad har fyra ben på dagen men sex ben på natten?(lämna svaret tomt för att gå tillbaka)', ('sängen', 'en säng', 'säng', 'sängar','segnen', 'en segn', 'seng', 'sengar','sägnen', 'en sägn', 'sägn', 'sägnar','segnen', 'en segn', 'segn', 'segnar'))
