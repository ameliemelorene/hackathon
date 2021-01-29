import numpy as np
import pygame
import random as rd
import matplotlib.pyplot as plt
#types de cellules et de méchants :
#... à lister ...

#mur 1
#salle 2
#chemin 3
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
    largeur=rd.randint(5,7)
    longueur=rd.randint(6,10)
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


M,C,L=cree_Carte()
plt.imshow(C)
plt.show()

