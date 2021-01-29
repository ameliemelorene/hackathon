import numpy as np
import pygame
import random as rd

#types de cellules et de méchants :
#... à lister ...


def cree_Carte(n=100,p=50):
  #les salles seront un nombre aléatoire entre 3 et 6
  #la taille des salles varie entre 4x4 et 6x10
  M=np.zeros((n,p),dtype='string')
  C=cases_occupes(M)
  nbreSalle=rd.randint(3,7)
  for i in range(nbreSalle):
    largeur=rd.randint(4,7)
    longueur=rd.randint(4,11)
    cree_salle(longueur,largeur)

  return M

def cases_occupes(M):
  n,p=M.shape
  C=np.zeros((n,p))
  return C

def cree_salle((n,p)):
  """crée une salle dans un endroit non occupé de la carte"""


def dans_une_salle((i,j,k))



def cree_Passage(salle):
  """ crée un passage sur les bords d'une salle"""


def cree_Monstre()

# je teste des choses