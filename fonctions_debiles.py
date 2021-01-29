##
def mignot(n):
  return n*'mignot'

def pauline(n):
    for i in range(n):
        print ("TA GUEULE PAULINE")

def main_point_cépépé():
    annee = input("Entrez votre année de naissance : ")
    mois = input("Entrez votre mois de naissance : ")
    jour = input("Entrez votre jour de naissance : ")
    age = 2020 - int(annee)
    if (int(mois) <= 1) and (int(jour) <= 29):
        age += 1
    print("Vous avez", age, "ans")

def karaoke():
    import time
    def passer_secondes(n):
        fin = time.time() + n
        while time.time()<fin:
            pass
    print("Alors comme ça tu m'as trompé")
    passer_secondes(3)
    print("T'as cru qu'j'allais pas capter?")
    passer_secondes(3)
    print("Et t'as changé d'parfum, d'numéro")
    passer_secondes(3)
    print("Comme si par les keufs t'étais recherché")
    passer_secondes(3)
    print("Apparemment tu n'm'aimes pas")
    passer_secondes(3)
    print("C'est une autre que t'aimes")
    passer_secondes(3)
    print("Tu parles avec une Anissa")
    passer_secondes(3)
    print("Mais moi j'm'appelle Wejdene")
    passer_secondes(3)

def stade_rennais():
    import random
    liste_joueurs = ["Eduardo Camavinga","Steven Nzonzi", "Faitout Maouassa","Hamari Traoré","Clément Grenier", "Damien Da Silva","Nayef Aguerd","Alfred Gomis","Jérémy Doku","Martin Terrier","Serhou Guirassy"]
    i = random.randint(0,10)
    return liste_joueurs[i]

## déplacements
for event in pygame.event.get():
    if event.type in (QUIT, KEYDOWN):
        sys.exit() #si l'utilisateur le dit, on quitte le programme
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if screen[position[O],position[1]-1] == "mur":
                print("Impossible ! Il y a un mur")
            print("Vous vous déplacez vers la gauche")
            screen.blit(background,position,position)
            position[1]-=1
            screen.blit(player,position)
        if event.key == pygame.K_RIGHT:
            if screen[position[0],position[1]+1] == "mur":
                print("Impossible ! Il y a un mur")
            print("Vous vous déplacez vers la droite")
            screen.blit(background,position,position)
            position[1]+=1
            screen.blit(player,position)
        if event.key == pygame.K_UP:
            if screen[position[0]-1,position[1]] == "mur":
                print("Impossible ! Il y a un mur")
            print("Vous vous déplacez vers le haut")
            screen.blit(background,position,position)
            position[0]-=1
            screen.blit(player,position)
        if event.key == pygame.K_DOWN:
            if screen[position[0]+1,position[1]] == "mur":
                print("Impossible ! Il y a un mur")
            print("Vous vous déplacez vers le bas")
            screen.blit(background,position,position) #on efface l'écran actuel
            position[0]+=1 #on déplace le joueur
            screen.blit(player,position) #on place le joueur sur la carte
        pygame.display.update() #on affiche
        pygame.time.delay(100) #on attend un dixième de seconde
