import pygame, sys, random
from pygame.locals import *

pygame.init() #inizializza una nuova finestra di pygame

#immagini: qui vengono caricate tutte le immagini necessarie
icon = pygame.image.load('images\icon.png')
wallpaper = pygame.image.load('images\wallpaper.jpg')
logo = pygame.image.load('images\logopixel.png')
logo_tiny = pygame.image.load('images\logotiny.png')
start_btn = pygame.image.load('btn.png')
exit_btn = pygame.image.load('btn.png')
rules_btn = pygame.image.load('btn.png')
info_btn = pygame.image.load('btn.png')
rosso = pygame.image.load('images\ROSSO.png')
blu = pygame.image.load('images\BLU.png')
giallo = pygame.image.load('images\GIALLO.png')
viola = pygame.image.load('images\VIOLA.png')
verde = pygame.image.load('images\VERDE.png')
arancione = pygame.image.load('images\ARANCIONE.png')
info_text = pygame.image.load('images\info.png')
rules_text = pygame.image.load('rules.png')

#schermo: qui vengono stabilite la risoluzione, l'icona e lo sfondo
window = pygame.display.set_mode((1280, 720))
pygame.display.set_icon(icon)
window.blit(wallpaper,(0, 0))
pygame.display.update()

class Button(): #inizio classe Button() con la definizione di alcune variabili utili

	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)

		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):

		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):

		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):

		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

def get_font(size): #funzione responsabile del caricamento del codice

    return pygame.font.Font("font/font.ttf", size)

def start(): #funzione che viene invocata quando si preme il tasto "Start"

        pygame.display.set_caption('Mastermind - Play') #imposta come nome della finestra "Mastermind - Play"

        #variabili e liste (contatori e liste dei colori possibili)
        tent = 1
        cont1 = 0
        cont2 = 0
        cont3 = 0
        cont4 = 0
        cont5 = 0
        cont6 = 0
        n_pioli_bianchi = 0
        n_pioli_neri = 0

        colori = [rosso, blu, giallo, viola, verde, arancione]
        coloriCheck = ['Ro', 'Bl', 'Gi', 'Vi', 'Ve', 'Ar']
        codeCheck = []
        choiceCheck = ['Ro', 'Ro', 'Ro', 'Ro', 'Ro', 'Ro']

        #ciclo che crea il codice segreto
        for i in range(len(colori)):
                num = random.randint(0, 5)
                codeCheck.append(coloriCheck[num])
        #print(codeCheck) istruzione "di servizio" utile per debug
        
        while True: #ciclo per gestire i tentativi (pioli bianchi e neri)
                    #e gli elementi corretti al posto giusto e quelli al posto sbagliato

                playMousePos = pygame.mouse.get_pos()

                window.blit(wallpaper, (0, 0))
                window.blit(logo_tiny, (10, 10)) #mostra il logo Mastermind in alto a sinistra

                playText1 = get_font(10).render("Elementi corretti al posto giusto: ", True, "black")
                playRect1 = playText1.get_rect(center = (200, 550))
                window.blit(playText1, playRect1)

                numText1 = get_font(10).render(str(n_pioli_bianchi), True, "black")
                numRect1 = numText1.get_rect(center = (400, 550))
                window.blit(numText1, numRect1)

                playText2 = get_font(10).render("Elementi corretti al posto sbagliato: ", True, "black")
                playRect2 = playText2.get_rect(center = (220, 600))
                window.blit(playText2, playRect2)

                numText2 = get_font(10).render(str(n_pioli_neri), True, "black")
                numRect2 = numText2.get_rect(center = (440, 600))
                window.blit(numText2, numRect2)

                tentText1 = get_font(13).render("Tentativo n° ", True, "black")
                tentRect1 = tentText1.get_rect(center = (1150, 100))
                window.blit(tentText1, tentRect1)

                tentText2 = get_font(13).render(str(tent), True, "black")
                tentRect2 = tentText2.get_rect(center = (1250, 100))
                window.blit(tentText2, tentRect2)

                if cont2 == 6:
                        cont2 = 0
                if cont3 == 6:
                        cont3 = 0
                if cont4 == 6:
                        cont4 = 0
                if cont5 == 6:
                        cont5 = 0
                if cont6 == 6:
                        cont6 = 0
                
                el1 = Button(image = colori[cont1], pos = (240, 360), text_input = None, font = get_font (30), base_color = "White", hovering_color = "Gray")

                el2 = Button(image = colori[cont2], pos = (400, 360), text_input = None, font = get_font (30), base_color = "White", hovering_color = "Gray")

                el3 = Button(image = colori[cont3], pos = (560, 360), text_input = None, font = get_font (30), base_color = "White", hovering_color = "Gray")

                el4 = Button(image = colori[cont4], pos = (720, 360), text_input = None, font = get_font (30), base_color = "White", hovering_color = "Gray")

                el5 = Button(image = colori[cont5], pos = (880, 360), text_input = None, font = get_font (30), base_color = "White", hovering_color = "Gray")

                el6 = Button(image = colori[cont6], pos = (1040, 360), text_input = None, font = get_font (30), base_color = "White", hovering_color = "Gray")

                playCheck = Button(image = start_btn, pos = (640, 550), text_input = "CHECK", font = get_font (40), base_color = "White", hovering_color = "Gray")

                playBack = Button(image = None, pos = (1220, 700), text_input = "BACK", font = get_font (20), base_color = "White", hovering_color = "Gray")

                playCheck.changeColor(playMousePos)
                playCheck.update(window)

                playBack.changeColor(playMousePos)
                playBack.update(window)

                for button in [el1, el2, el3, el4, el5, el6]:
                    button.update(window)
                
                for event in pygame.event.get(): #controllo tasti del mouse e X in alto a destra per uscire dal programma
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if playBack.checkForInput(playMousePos):
                                menu()
                        if el1.checkForInput(playMousePos):
                                choiceCheck.pop(0)
                                cont1 += 1
                                if cont1 == 6:
                                        cont1 = 0
                                choiceCheck.insert(0, coloriCheck[cont1])
                        if el2.checkForInput(playMousePos):
                                choiceCheck.pop(1)
                                cont2 += 1
                                if cont2 == 6:
                                        cont2 = 0
                                choiceCheck.insert(1, coloriCheck[cont2])
                        if el3.checkForInput(playMousePos):
                                choiceCheck.pop(2)
                                cont3 += 1
                                if cont3 == 6:
                                        cont3 = 0
                                choiceCheck.insert(2, coloriCheck[cont3])
                        if el4.checkForInput(playMousePos):
                                choiceCheck.pop(3)
                                cont4 += 1
                                if cont4 == 6:
                                        cont4 = 0
                                choiceCheck.insert(3, coloriCheck[cont4])
                        if el5.checkForInput(playMousePos):
                                choiceCheck.pop(4)
                                cont5 += 1
                                if cont5 == 6:
                                        cont5 = 0
                                choiceCheck.insert(4, coloriCheck[cont5])
                        if el6.checkForInput(playMousePos):
                                choiceCheck.pop(5)
                                cont6 += 1
                                if cont6 == 6:
                                        cont6 = 0
                                choiceCheck.insert(5, coloriCheck[cont6])
                        if playCheck.checkForInput(playMousePos):
                                n_pioli_bianchi = 0
                                n_pioli_neri = 0
                                #print(choiceCheck) istruzione "di servizio" utile per il debug
                                if choiceCheck == codeCheck:
                                        win()
                                for i in range(len(colori)):
                                        if choiceCheck[i] == codeCheck[i]:
                                                n_pioli_bianchi += 1
                                        if choiceCheck[i] != codeCheck[i] and choiceCheck[i] in codeCheck:
                                                n_pioli_neri += 1
                                tent += 1
                                if tent > 9:
                                        lose()
                pygame.display.update()

def info(): #funzione che viene invocata quando si preme il tasto "Info"

    pygame.display.set_caption('Mastermind - Info') #imposta come nome della finestra "Mastermind - Info"

    while True:
        infoMousePos = pygame.mouse.get_pos()

        window.blit(wallpaper, (0, 0))
        window.blit(info_text, (5, 5))

        infoBack = Button(image = None, pos= (640, 660), text_input="BACK", font = get_font (30), base_color = "black", hovering_color = "Gray")

        infoBack.changeColor(infoMousePos)
        infoBack.update(window)

        for event in pygame.event.get(): #controllo tasti del mouse e X in alto a destra per uscire dal programma
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if infoBack.checkForInput(infoMousePos):
                    menu()
        pygame.display.update()

def rules(): #funzione che viene invocata quando si preme il tasto "Rules"

    pygame.display.set_caption('Mastermind - Rules') #imposta come nome della finestra "Mastermind - Rules"

    while True:
        rulesMousePos = pygame.mouse.get_pos()

        window.blit(wallpaper, (0, 0))
        window.blit(rules_text, (5, 5))

        rulesBack = Button(image=None, pos= (640, 660), text_input="BACK", font = get_font (30), base_color = "black", hovering_color = "Gray")

        rulesBack.changeColor(rulesMousePos)
        rulesBack.update(window)

        for event in pygame.event.get(): #controllo tasti del mouse e X in alto a destra per uscire dal programma
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rulesBack.checkForInput(rulesMousePos):
                    menu()
        pygame.display.update()

def menu(): #funzione responsabile della gestione del menù di gioco

    pygame.display.set_caption('Mastermind') #imposta come nome della finestra "Mastermind"

    while True: #ciclo per gestire il wallpaper, il logo e i 4 tasti nel menù principale
        window.blit(wallpaper, (0, 0))

        menuMousePos = pygame.mouse.get_pos()

        menuWallpaper = logo
        menuRect = menuWallpaper.get_rect(center=(640, 180))
        window.blit(menuWallpaper, menuRect)

        playB = Button(image = start_btn, pos = (206, 430), text_input= "Play", font = get_font (45), base_color = "White", hovering_color = "black")

        infoB = Button(image = info_btn, pos = (492, 430), text_input= "Info", font = get_font (45), base_color = "White", hovering_color = "black")

        rulesB = Button(image = rules_btn, pos = (778, 430), text_input= "Rules", font = get_font (45), base_color = "White", hovering_color = "black")

        exitB = Button(image = exit_btn, pos = (1064, 430), text_input= "Exit", font = get_font (45), base_color = "White", hovering_color = "black")

        window.blit(menuWallpaper, menuRect)

        for button in [playB, infoB, rulesB, exitB]:
            button.changeColor(menuMousePos)
            button.update(window)

        for event in pygame.event.get(): #controllo tasti del mouse e X in alto a destra per uscire dal programma
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playB.checkForInput(menuMousePos):
                    start()
                    pygame.display.update()
                if infoB.checkForInput(menuMousePos):
                    info()
                    pygame.display.update()
                if rulesB.checkForInput(menuMousePos):
                    rules()
                    pygame.display.update()
                if exitB.checkForInput(menuMousePos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def win(): #funzione che viene invocata in caso di vittoria
        while True: #ciclo responsabile della stampa a video di "YOU WIN!" in caso di vittoria
                winMousePos = pygame.mouse.get_pos()

                window.blit(wallpaper, (0, 0))

                winText = get_font(45).render("YOU WIN!", True, "black")
                winRect = winText.get_rect(center=(640, 260))
                window.blit(winText, winRect)

                winBack = Button(image=None, pos= (640, 460), text_input="BACK", font = get_font (30), base_color = "black", hovering_color = "Gray")

                winBack.changeColor(winMousePos)
                winBack.update(window)

                for event in pygame.event.get(): #controllo tasti del mouse e X in alto a destra per uscire dal programma
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if winBack.checkForInput(winMousePos):
                            menu()
                pygame.display.update()

def lose(): #funzione che viene invocata in caso di perdita
        while True: #ciclo responsabile della stampa a video di "YOU LOSE!" in caso di perdita
                loseMousePos = pygame.mouse.get_pos()

                window.blit(wallpaper, (0, 0))

                loseText = get_font(45).render("YOU LOSE!", True, "black")
                loseRect = loseText.get_rect(center=(640, 260))
                window.blit(loseText, loseRect)

                loseBack = Button(image=None, pos= (640, 460), text_input="BACK", font = get_font (30), base_color = "black", hovering_color = "Gray")

                loseBack.changeColor(loseMousePos)
                loseBack.update(window)

                for event in pygame.event.get(): #controllo tasti del mouse e X in alto a destra per uscire dal programma
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if loseBack.checkForInput(loseMousePos):
                            menu()
                pygame.display.update()

menu() #lancio della funzione menu per visualizzare il menù principale
