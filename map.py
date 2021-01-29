import pygame as pg
import numpy as np
import random as rd
import matplotlib.pyplot as plt

def cree_Carte(n=36,p=65):
  #les salles seront un nombre aléatoire entre 4 et 6
  #la taille des salles varie entre 5x6 et 7x10
  M=np.zeros((n,p),dtype='str')
  C=np.zeros((n,p),dtype='int')
  #crée les murs
  for i in range(n):
    C[i,0]=1
    C[i,p-1]=1
    M[i,0]='mur'
    M[i,p-1]='mur'
  for j in range(1,p-1):
    C[0,j]=1
    C[n-1,j]=1
    M[0,j]='mur'
    M[n-1,j]='mur'


  nbreSalle=rd.randint(4,6)
  ListeSalle=[]
  for i in range(nbreSalle):
    largeur=rd.randint(6,10)
    longueur=rd.randint(8,15)
    si,sj=cree_salle(longueur,largeur,C,M)
    ListeSalle.append((si,sj,longueur,largeur))
  return M,C,ListeSalle





def cree_salle(n,p,C,M):
  """crée une salle dans un endroit non occupé de la carte  IN PLACE"""
  def salle_Possible(pi,pj):
    for i in range(n):
      for j in range(p):
        if C[pi+i,pj+j]>0:
          return False
    return True

  tn,tp= M.shape
  nbrTest=10
  tester=True
  numTest=1
  while tester and numTest <= nbrTest:
    pi,pj=rd.randint(0,tn-1-n),rd.randint(0,tp-1-p)
    possible=salle_Possible(pi,pj)
    if possible:
      for i in range(n):
        C[i+pi,pj]=1
        C[i+pi,pj+p-1]=1
        M[i+pi,pj]='mur'
        M[i+pi,pj+p-1]='mur'
      for j in range(1,p-1):
        C[pi,pj+j]=1
        C[n-1+pi,pj+j]=1
        M[pi,pj+j]='mur'
        M[n-1+pi,pj+j]='mur'
      for i in range(1,n-1):
        for j in range(1,p-1):
          C[pi+i,pj+j]=2
          M[pi+i,pj+j]='salle'
      tester =False
    numTest+=1
  if numTest==11:
    print('pas réussi à placer la salle')

  return pi,pj

def cree_Chemin(listeSalle,M,C):
  #on trie la liste des salles selon l'ordre de lecture classique
  tri_bulle(listeSalle)
  def cree_Lien(S1,S2):
    if S1[1]<S2[1]:
      #chemin de en haut à droite à en haut à gauche
      dx=S2[1]-S1[1]-S1[4]
      dy=S1[0]-S2[0]
      for i in range(dx):
        C[S1[1]+i,S1[0]+1]=1
        M[S1[1]+i,S1[0]+1]='chemin'
      for j in range(dy-1):
        pass



    elif S1[1]>=S2[1]:
      #chemin de en bas à gauche à en haut droite
      dx=S1[1]-S2[1]-S2[4]
      dy=S1[0]-S2[0]








def tri_bulle(tab):
  def inferieur(e1,e2):
    if e1[0]<e2[0]:
      return True
    elif e1[0]>e2[0]:
      return False
    else:
      if e1[1]<e2[1]:
        return True
      else:
        return False

  n = len(tab)
  for i in range(n):
    for j in range(0, n-i-1):
      if not inferieur(tab[j],tab[j+1]):
        tab[j], tab[j+1] = tab[j+1], tab[j]



# in pixels
W, H = 65, 36
# in perso units
X, Y = 10, 10

BACKGROUND_COLOR = (0,0,0)
ROOM_COLOR = (255,255,255)
HALL_COLOR = (240,240,240)
WALL_COLOR = (100,100,100)
CHARACTER_COLOR = (255, 0, 0)

DIRECTIONS = {
    'DOWN': (0, 1*Y),
    'UP': (0, -1*Y),
    'RIGHT': (1*X, 0),
    'LEFT': (-1*X, 0),
}

pg.init()
screen = pg.display.set_mode((X*W, Y*H))

position = (X*10,Y*10)


C,M,L = cree_Carte()
C = C.T
M = M.T


def move_character(position, direction):
    x,y = position
    dx,dy = direction
    x2,y2 = (x+dx)//X,(y+dy)//Y
    if M[x2,y2] != 1:
      position = (x+dx,y+dy)
    return position

def draw_game(position):
    screen.fill(BACKGROUND_COLOR)

    #redessine la map
    for i in range (len(M)):
        for j in range (len(M[0])):
            if M[i,j] != 0:
                I = i*X
                J = j*X
                color = BACKGROUND_COLOR
                if M[i,j] == 1:
                    color = WALL_COLOR
                if M[i,j] == 2:
                    color = ROOM_COLOR
                if M[i,j] == 3:
                    color = HALL_COLOR
                rect = pg.Rect(I,J,X,Y)
                pg.draw.rect(screen,color,rect)

    #dessine le personnage
    x,y = position
    rect = pg.Rect(x, y, X, Y)
    pg.draw.rect(screen, CHARACTER_COLOR, rect)
    pg.display.update()

direction = (0,0)

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:
    draw_game(position)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        if event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False

            if event.key == pg.K_LEFT:
                direction = DIRECTIONS['LEFT']
            if event.key == pg.K_RIGHT:
                direction = DIRECTIONS['RIGHT']
            if event.key == pg.K_UP:
                direction = DIRECTIONS['UP']
            if event.key == pg.K_DOWN:
                direction = DIRECTIONS['DOWN']

    position = move_character(position,direction)
    direction = (0,0) 
            #on efface l'écran actuel
            #pygame.display.update() #on affiche
            #pygame.time.delay(100) #on attend un dixième de seconde



# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()