# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import numpy.linalg as alg

N = 7;

def init(taille):
    return np.zeros((taille, taille))

def ajoutArt(matrice, x, y):
    matrice[x, y] = 1
    matrice[y, x] = 1

''' retourner le sommet qui a le plus degre'''

def sommetMaxDegre(myMatrice):
    maxDegre = 0
    sommetMaxDgr = 0
    for i in range(len(myMatrice[0])):
        if sum(myMatrice[i]) > maxDegre:
            maxDegre = sum(myMatrice[i])
            sommetMaxDgr = i
    return sommetMaxDgr


def voisin(x, G):
    P = []
    for i in range(7):
        if G[x][i] == 1:
            P.append(i);
    return P


''' tester '''
G = init(7);
ajoutArt(G, 0, 1);
ajoutArt(G, 0, 2);
ajoutArt(G, 0, 3);
ajoutArt(G, 1, 2);
ajoutArt(G, 2, 3);
ajoutArt(G, 2, 4);
ajoutArt(G, 3, 4);
ajoutArt(G, 3, 5);
ajoutArt(G, 5, 6);
print("\nmatrice adjacence : ")
print (G)

print("\nle sommet qui a le plus degre : ")
K = sommetMaxDegre(G);
print (K)

print("\nles voisins du sommet qui a le plus degre : ")
P = voisin(sommetMaxDegre(G), G)
print (P)


def maxClique(myMatrice, myClique, myC):
    if myC == []:
        '''print("\n*****************")'''
        print(myClique)
        return myClique
    else:
        for sommet in myC:
            maxClique(myMatrice, myClique + [sommet], np.intersect1d(myC,voisin(sommet,myMatrice),0).tolist())

kInit = [K]
cInit = voisin(sommetMaxDegre(G),G)
'''
maxCliquesTrouves = maxClique(G,cliqueInit,cInit)
print("\nclique maximale : ")
print(maxCliquesTrouves)
'''

print("\nLes cliques maximales sont  : ")
maxClique(G,kInit,cInit)

'''Fin fonction MaxClique'''

def maxClique2(G,K,C,A):
    if C == []:
        print (K)
        return 0
    else:
        while A != [] :
            x = A[0]
            maxClique2(G,K + [x], np.intersect1d(C,voisin(x,G),0).tolist(), np.intersect1d(A,voisin(x,G),0).tolist())
            A.remove(x)

kInit2 = [K]
cInit2 = voisin(K,G)
aInit2 = voisin(K,G)

print("\nAvec l'amélioration,les cliques maximales sont  : ")
maxClique2(G,kInit2,cInit2,aInit2)


def degre(x,myMatrice):
    return sum(myMatrice[x])

'''je stock les sommets blanc de G dans une liste'''
'''Liste = [[numSommet,numCouleur]]'''
'''Et je le range par ordre de dégrés décroissants'''

def initG(matrice):
    '''stock les sommets blanc'''
    l = []
    for i in range(len(matrice)) :
        l.append(i)
    '''Créer un liste qui stock le dregre de sommet, et le ranger en décroissant'''
    tmp = []
    for j in range(len(l)):
        tmp.append((degre(l[j], matrice), l[j]))
    tmp.sort(reverse=True)
    '''mise à jour la liste finale avec la liste de degre'''
    for k in range(len(tmp)):
        l[k] = tmp[k][1]
    return l

print ("\nOn range les sommet dans l'ordre décroissant")
L = initG(G)

'''Pour simplifier, je vois une couleur commeun nombre : 1,2,3,4...'''

def adjacent(l,x,G):
    adj=False
    for i in range(len(l)) :
        if G[l[i]][x]==1:
            adj=True
    return adj

def colorier(G):
    l = initG(G)
    carteColeur = []
    i=0
    taille = len(l)
    while l!= []:
        couleur = []
        couleur.append(l[0])
        l.remove(l[0])
        j=0

        while l!=[] and j<len(l):
            if not adjacent(couleur,l[j],G) :
                couleur.append(l[j])
                l.remove(l[j])
                j-=1
            j+=1
        carteColeur.append(couleur)
    return carteColeur


print ("\nOn colorie le graphe G :")
carteCouleur = colorier(G)
print (carteCouleur)