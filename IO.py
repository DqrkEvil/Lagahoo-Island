import fade

mainMenuText = r"""




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

                            
"""
startGameText = "                                                      Press enter to start game"

def printMainMenu():
    """Skriv ut main menyn och vänta tills spelaren vill börja"""

    standardPrint(fade.greenblue(mainMenuText))
    input(startGameText)

def standardPrint(*sections):
    """Standardiserad print funktion för hela programmet
    
    :*sections: sektioner med all information som ska skrivas ut"""

    for section in sections:
        print(section)

    print('\n')
