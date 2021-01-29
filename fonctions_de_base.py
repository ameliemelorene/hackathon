import numpy as np
import pygame
import random as rd

#types de cellules et de méchants :
#... à lister ...


def cree_Carte(n=50,p=100):
  #les salles seront un nombre aléatoire entre 3 et 6
  #la taille des salles varie entre 4x4 et 6x10
  M=np.zeros((n,p),dtype='string')
  C=cases_occupes(M)
  nbreSalle=rd.randint(3,6)
  for i in range(nbreSalle):
    largeur=rd.randint(4,6)
    longueur=rd.randint(4,10)
    cree_salle(longueur,largeur,C)

  return M

def cases_occupes(M):
  n,p=M.shape
  C=np.zeros((n,p))
  return C

def cree_salle(n,p,C,M):
   """crée une salle dans un endroit non occupé de la carte  IN PLACE"""
  tn,tp=C.shape
  nbrTest=10
  tester=True
  numTest=1
  while tester and numTest <= nbrTest:
    pi,pj=rd.randint(0,tn-1),rd.randint(0,tp-1)
    possible=salle_Possible(pi,pj)
    if possible:
      for i in range(n):
        for j in range(p):
          C[pi+i,pj+j]=1
          M[pi+i,pj+j]='salle'
      tester =False
    numTest+=1
  if numTest==11:
    print('pas réussi à placer la salle')




  def salle_Possible(pi,pj):
    for i in range(n):
      for j in range(p):
        if C[pi+i,pj+j]==1:
          return False
    return True

  while test

def dans_une_salle((i,j,k))



def cree_Passage(salle):
  """ crée un passage sur les bords d'une salle"""


def cree_Monstre()
