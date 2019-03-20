# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:35:03 2019

@author: Robin
"""

import numpy as np
import project_part1 as pp1
import math

sudoku = np.load("sudoku.npy")
possibleValues = [1,2,3,4,5,6,7,8,9]

temp = []
i = 1
for line in range(9):
    temp.append([])
    for column in range(9):
        temp[line].append(i)
        i+=1
matrice = np.array(temp)



def whichSquare(n):
    """
    Return a tuple
    The first element of the tuple is in which of the 9 submatrix of the sudoku belongs the random variable n
    The second element is a list containing the values we also know of the submatrix
    """
    rowIndex, columnIndex = np.where(matrice == n)
    l = []
    if(0 <= rowIndex[0] <= 2):
        if(0 <= columnIndex[0] <= 2):
            for i in range(0,3):
                for j in range(0,3):
                    if sudoku[i][j] != 0:
                        l.append(sudoku[i][j])
            return 1, l
        elif(3 <= columnIndex[0] <= 5):
            for i in range(0,3):
                for j in range(3,6):
                    if sudoku[i][j] != 0:
                        l.append(sudoku[i][j])
            return 2, l
        elif(6 <= columnIndex[0] <= 8):
            for i in range(0,3):
                for j in range(6,9):
                    if sudoku[i][j] != 0:
                        l.append(sudoku[i][j])
            return 3, l
    elif(3 <= rowIndex[0] <= 5):
        if(0 <= columnIndex[0] <= 2):
            for i in range(3,6):
                for j in range(0,3):
                    if sudoku[i][j] != 0:
                        l.append(sudoku[i][j])
            return 4, l
        elif(3 <= columnIndex[0] <= 5):
            for i in range(3,6):
                for j in range(3,6):
                    if sudoku[i][j] != 0:
                        l.append(sudoku[i][j])
            return 5, l
        elif(6 <= columnIndex[0] <= 8):
            for i in range(3,6):
                for j in range(6,9):
                    if sudoku[i][j] != 0:
                        l.append(sudoku[i][j])
            return 6, l
    elif(6 <= rowIndex[0] <= 8):
        if(0 <= columnIndex[0] <= 2):
            for i in range(6,9):
                for j in range(0,3):
                    if sudoku[i][j] != 0:
                        l.append(sudoku[i][j])
            return 7, l
        elif(3 <= columnIndex[0] <= 5):
            for i in range(6,9):
                for j in range(3,6):
                    if sudoku[i][j] != 0:
                        l.append(sudoku[i][j])
            return 8, l
        elif(6 <= columnIndex[0] <= 8):
            for i in range(6,9):
                for j in range(6,9):
                    if sudoku[i][j] != 0:
                        l.append(sudoku[i][j])
            return 9, l
    

def createRV(n):
    """
    This function create the random variable number n
    """
    rowIndex, columnIndex = np.where(matrice == n)
    rvValues = [item for item in possibleValues if (item not in sudoku[rowIndex[0]]) and (item not in sudoku[:, columnIndex[0]]) and (item not in whichSquare(n)[1])]
    rv = [0,0,0,0,0,0,0,0,0]
    if(sudoku[rowIndex[0]][columnIndex[0]] == 0):
        for e in rvValues:
            rv[e-1] = 1/len(rvValues)
    else:
        rv[sudoku[rowIndex[0]][columnIndex[0]]-1] = 1
    return rv

temp = []
i = 1
for line in range(81):
    temp.append(createRV(i))
    i+=1
randomVariables = np.array(temp)#An array of all the random variables

def entropyOfUnsolvedSudoku():
    """
    This function return the entropy of the unsolved sudoku
    """
    entropy = 0
    for i in range(81):
        entropy += pp1.entropy(randomVariables[i])
    return entropy

def firstSquareToFill():
    entropy = 0
    maxEntropy = 0
    maxIndex = -1
    for i in range(81):
        entropy = pp1.entropy(randomVariables[i])
        if(entropy > maxEntropy):
            maxEntropy = entropy
            maxIndex = i
    return maxIndex+1

if __name__ == "__main__":
    print(sudoku)
    """What is the entropy of a single square independantly of others ?"""
    X1 = [1/9,1/9,1/9,1/9,1/9,1/9,1/9,1/9,1/9]
    print("Question 13 : " + str(pp1.entropy(X1)))
    
    """What is the entropy of the following subgrid ? pas correct"""
    X1 = [1/6,1/6,1/6,1/6,1/6,1/6]
    entropy = pp1.entropy(X1)*6
    print("Question 14 : " + str(entropy))
    
    """What is the entropy of the unsolved sudoku grid ?"""
    print("Question 15 : " + str(entropyOfUnsolvedSudoku()))
    
    """Question 17"""
    print("Question 17 : " + str(firstSquareToFill()))
    
    r = createRV(81)
    print(r)
    print(pp1.entropy(r))
    print(4*((-0.25)*math.log2(0.25)))