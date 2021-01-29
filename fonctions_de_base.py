import numpy as np
import pygame
import random as rd
import matplotlib.pyplot as plt
from math import *
#types de cellules et de méchants :
#... à lister ...

#mur 1
#salle 2
#chemin 3
#escalier 4
def cree_Carte(n=36,p=65):
  #les salles seront un nombre aléatoire entre 4 et 6
  #la taille des salles varie entre 6x8 et 10x15
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

  def cree_un_chemin(S1,S2):
    g1x=S1[1]
    d1x=S1[1]+S1[3]
    g2x=S2[1]
    d2x=S2[1]+S2[3]
    h1y=S1[0]
    b1y=S1[0]+S1[2]
    h2y=S2[0]
    b2y=S2[0]+S2[2]
    if d1x<g2x:
      dx=g2x-d1x
      for p in range(-1,dx+1):
        C[h1y+1,d1x+p]=3
        M[h1y+1,d1x+p]='chemin'
    elif d1x==g2x:
      C[h1y+1,d1x-1]=3
      M[h1y+1,d1x-1]='chemin'
      C[h1y+1,d1x]=3
      M[h1y+1,d1x]='chemin'
    else:
      if d2x<g1x:
        dx=g1x-d2x
        for p in range(-1,dx+1):
          C[h2y+1,d2x+p]=3
          M[h2y+1,d2x+p]='chemin'
      elif d2x==g1x:
        C[h2y+1,d2x]=3
        M[h2y+1,d2x]='chemin'
        C[h2y+1,d2x-1]=3
        M[h2y+1,d2x-1]='chemin'

    if b1y<h2y:
      dy=h2y-b1y
      for p in range(-1,dy+1):
        C[b1y+p,g1x+1]=3
        M[b1y+p,g1x+1]='chemin'
    elif b1y==h2y:
      C[b1y-1,g1x+1]=3
      M[b1y-1,g1x+1]='chemin'
      C[b1y,g1x+1]=3
      M[h1y,g1x+1]='chemin'
    else:
      if b2y<h1y:
        dy=h1y-b2y
        for p in range(-1,dy+1):
          C[b2y+p,g2x+1]=3
          M[b2y+p,g2x+1]='chemin'
      elif b2y==h1y:
        C[b2y,g2x+1]=3
        M[b2y,g2x+1]='chemin'
        C[b2y-1,g2x+1]=3
        M[b2y-1,g2x+1]='chemin'

  nSalle=len(listeSalle)
  for k in range(nSalle-1):
    voisin=k+1
    dist=distance_salle(listeSalle[k],listeSalle[k+1])
    for j in range(k+1,nSalle):
      dist2=distance_salle(listeSalle[k],listeSalle[j])
      if dist2<dist:
        voisin=j
    cree_un_chemin(listeSalle[k],listeSalle[voisin])




# def table_des_liens(listeSalle):
#   n=len(listeSalle)
#   M=np.eye((n),dtype='object')
#   for i in range(n):
#     for j in range(i,n):
#       M[i,j]=distance_salle(listeSalle[i],listeSalle[j])
#
#   return M

def distance_salle(S1,S2):
  g1x=S1[1]
  d1x=S1[1]+S1[3]
  g2x=S2[1]
  d2x=S2[1]+S2[3]
  if d1x<g2x:
    dx=g2x-d1x
  elif d1x==g2x:
    dx=0
  else:
    if d2x<g1x:
      dx=g1x-d2x
    elif d2x==g1x:
      dx=0
    else:
      dx=0

  h1y=S1[0]
  b1y=S1[0]+S1[2]
  h2y=S2[0]
  b2y=S2[0]+S2[2]
  if b1y<h2y:
    dy=h2y-b1y
  elif b1y==h2y:
    dy=0
  else:
    if b2y<h1y:
      dy=h1y-b2y
    elif b2y==h1y:
      dy=0
    else:
      dy=0

  return dx+dy

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
cree_Chemin(L,M,C)
plt.imshow(C)

plt.show()

