import numpy as np
import pygame
import random as rd
import matplotlib.pyplot as plt
#types de cellules et de méchants :
#... à lister ...


def cree_Carte(n=36,p=65):
  #les salles seront un nombre aléatoire entre 4 et 6
  #la taille des salles varie entre 5x6 et 7x10
  M=np.zeros((n,p),dtype='str')
  C=np.zeros((n,p),dtype='int')
  nbreSalle=rd.randint(4,6)
  for i in range(nbreSalle):
    largeur=rd.randint(5,7)
    longueur=rd.randint(6,10)
    cree_salle(longueur,largeur,C,M)

  return M,C


def cree_salle(n,p,C,M):
  compteur=0
  """crée une salle dans un endroit non occupé de la carte  IN PLACE"""
  def salle_Possible(pi,pj):
    for i in range(n):
      for j in range(p):
        if C[pi+i,pj+j]==1:
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
        for j in range(p):
          print(compteur)
          compteur+=1
          C[pi+i,pj+j]=1
          M[pi+i,pj+j]='salle'
      tester =False
    numTest+=1
  if numTest==11:
    print('pas réussi à placer la salle')

# def dans_une_salle((i,j,k))
#
#
#
# def cree_Passage(salle):
#   """ crée un passage sur les bords d'une salle"""
#
#
# def cree_Monstre()M=
