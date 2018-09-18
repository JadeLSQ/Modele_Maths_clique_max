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
    sommetMaxDgr = 1
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

