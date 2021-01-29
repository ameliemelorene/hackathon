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

def cree_salle(n,p,C):
  tn,tp=C.shape
  """crée une salle dans un endroit non occupé de la carte"""
  i,j=rd.randint(0,n-1),rd.randint(0,p-1)
  while test

def dans_une_salle((i,j,k))



def cree_Passage(salle):
  """ crée un passage sur les bords d'une salle"""


def cree_Monstre()
