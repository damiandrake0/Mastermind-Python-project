#librerie
import random

#fuzioni
def choice_f(c1, c2, choice2): #funzione per inserire il codice da indovinare da tastiera
    scelta = input("\nScrivi il codice da indovinare: ")
    choice2 = []
    #ciclo
    while c1 <= 10:
        choice2.append(scelta[c1:c2])
        c1 += 2
        c2 += 2
    print(choice2) #istruzione per stampare a video il codice inserito dall'utente
    correctElements(choice2, code)

def correctElements(choice3, codice):
    if choice3 == codice: #se il codice inserito dall'utente è uguale a quello generato
        win() #si passa alla funzione win()
    else: #altrimenti stampo i "pioli" bianchi e neri attraverso il carattere "|"
        print('Elementi corretti al posto giusto: ', end = '')
        for i in range(len(codice)):
            if choice3[i] == codice[i]:
                print('|', end = ' ')

        print('\nElementi corretti al posto sbagliato: ', end = '')
        for i in range(len(codice)):
            if choice3[i] in codice and choice3[i] != codice[i]:
                print('|', end = ' ')
        print()

def win(): #funzione per stampare a video il messaggio di vittoria della partita contro il computer
    print('HAI VINTO!')
    vittoria = True
    input()

#Inizio programma principale

#variabili
cont1 = 0
cont2 = 2
vittoria = False
tent = 1

#liste
colori = ["Ro", "Ar", "Ve", "Bl", "Vi", "Gi"]
choice = [1, 2, 3, 4, 5, 6]
code = []

#ciclo che crea il codice segreto
for i in range(len(colori)):
    num = random.randint(0, 5)
    code.append(colori[num])

#Start!
while vittoria == False and tent <= 9:
    choice_f(cont1, cont2, choice)
    tent += 1

print('\nHai perso!')
