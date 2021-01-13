# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:12:13 2021

@author: TORRES-SANNIER NICOLAS | AKTER VOLKAN | ROUSSEAU WILLIAM | QUENUM-SANFO DJIBRIL
"""


import numpy as np
import matplotlib.pyplot as plt
from pylab import *


# Fonctions utiles
def mat_Rotation_h(theta):
    mat = np.array(
        [
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1],
        ]
    )
    return mat


def mat_Rotation_Figure(theta):
    mat = np.array(
        [
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1],
        ]
    )
    return mat


def mat_Translation_h(tx, ty):
    mat = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
    return mat


def mat_Reflexion_axeAbscisse():
    mat = np.array(
        [
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1],
        ]
    )
    return mat


def mat_Reflexion_axeOrdonnes():
    mat = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
    return mat


def mat_Scale_h(sx, sy):
    mat = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
    return mat


def matP_homogene(matP):
    # la matrice des points écrits en coordonnées homogènes
    nP = matP.shape[1]
    matP_h = np.concatenate((matP, np.ones((1, nP))), 0)
    return matP_h


def visu_point(matPoint, style):
    # matPoint contient les coordonnées des points
    x = matPoint[0, :]
    y = matPoint[1, :]
    plt.plot(x, y, style, linewidth=10)

#N
N_abscisse = np.array([0, 0, 2, 2])
N_ordonnee = np.array([0, 4, 0, 4])
lettre_N = np.array([N_abscisse, N_ordonnee])
lettre_N = matP_homogene(lettre_N)

#E
E_abscisse = np.array([3, 6, 6, 3, 3, 6])
E_ordonnee = np.array([2, 2, 4, 4, 0, 0])
lettre_e = np.array([E_abscisse, E_ordonnee])
lettre_e = matP_homogene(lettre_e)

#W
M_abscisse = np.array([7, 7, 8.5, 8.5, 10])
M_ordonnee = np.array([4, 0, 4, 0, 4])
lettre_w = np.array([M_abscisse, M_ordonnee])
lettre_w = matP_homogene(lettre_w)

#N inversé
lettre_N_inv = np.dot(mat_Reflexion_axeAbscisse(), lettre_N)
lettre_N_inv = np.dot(mat_Translation_h(-9, -1), lettre_N_inv)
lettre_N_inv = np.dot(mat_Reflexion_axeOrdonnes(), lettre_N_inv)
visu_point(lettre_N, "k-")
visu_point(lettre_N_inv, "b-")

#E inversé
lettre_E_inv = np.dot(mat_Reflexion_axeAbscisse(), lettre_e)
lettre_E_inv = np.dot(mat_Translation_h(-9, -1), lettre_E_inv)
lettre_E_inv = np.dot(mat_Reflexion_axeOrdonnes(), lettre_E_inv)
visu_point(lettre_e, "k-")
visu_point(lettre_E_inv, "b-")

#W inversé
lettre_W_inv = np.dot(mat_Reflexion_axeAbscisse(), lettre_w)
lettre_W_inv = np.dot(mat_Translation_h(-9, -1), lettre_W_inv)
lettre_W_inv = np.dot(mat_Reflexion_axeOrdonnes(), lettre_W_inv)
visu_point(lettre_w, "k-")
visu_point(lettre_W_inv, "b-")

xlim(-5, 15)

plt.show()
