# -*- coding: utf-8 -*-
"""
Gabriela Copetti Maccagnan

Biologia Computacional
Trabalho 2
"""
 
#BIBLIOTECAS
import numpy as np

#FUNÇÕES
def neighbour_joining(matrix, labels):
    initial_lengh = len(labels) 
    
    while len(labels) > 1:
        x, y, u = lowest_cell_np(matrix, labels, initial_lengh)
        join_table_np(matrix, x, y, u)
        join_labels(labels, x, y)
    
    return labels[0]


def upgma(matrix, labels):
    while len(labels) > 1:
        x, y = lowest_cell_up(matrix)
        join_table_up(matrix, x, y)
        join_labels(labels, x, y) 

    return labels[0]


def lowest_cell_np(matrix, labels, n):
    min_cell = float("inf")
    x, y = 0, 0
    
    u = []

    for i in range(len(matrix)):
        soma = 0
        for j in range(len(matrix[i])):
            soma += (matrix[i][j] / (n - 2)) 
            if matrix[i][j] < min_cell and matrix[i][j] > 0:
                min_cell = matrix[i][j]
        u.append(soma)
    
    Q = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0:
                Q[i][j] = matrix[i][j] - u[i] - u[j] 

    min_q_cell = float("inf")
    for i in range(len(Q)):
        for j in range(len(Q[i])):
            if Q[i][j] < min_q_cell and matrix[i][j] > 0:
                min_q_cell = Q[i][j]
                x, y = i, j

    return x, y, u


def lowest_cell_up(matrix):
    min_cell = float("inf")
    x, y = 0, 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_cell:
                min_cell = matrix[i][j]
                x, y = i, j

    return x, y


def join_table_np(matrix, x, y,u):
    if y < x:
        x, y = y, x
    
    dist = matrix[x][y] / 2 + (u[x] - u[y]) / 2
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0:
                matrix[i][j] -= dist
    
    del matrix[y]
    
    for i in matrix:
        del i[y]
    print("\nNew matrix:\n", matrix)


def join_table_up(matrix, x, y):
    if y < x:
        x, y = y, x

    row = []
    for i in range(x):
        row.append((matrix[x][i] + matrix[y][i]) / 2)
    matrix[x] = row
    
    for i in range(x + 1, y):
        matrix[i][x] = (matrix[i][x] + matrix[y][i]) / 2
        
    for i in range(y + 1, len(matrix)):
        matrix[i][x] = (matrix[i][x] + matrix[i][y]) / 2
        del matrix[i][y]

    del matrix[y]
    print("\nNew matrix:\n", matrix)


def join_labels(labels, x, y):
    if y < x:
        x, y = y, x

    labels[x] = "(" + labels[x] + ", " + labels[y] + ")"
    
    del labels[y]
    print("\nNew labels:\n", labels)
    

def needleman_wunsch(seq_1, seq_2, match, gap, mismatch):
    size_1 = len(seq_1)
    size_2 = len(seq_2)
    
    main_matrix = np.zeros((size_1 + 1, size_2 + 1))
    main_matrix[:,0] = np.linspace(0, size_1 * gap, size_1 + 1)
    main_matrix[0,:] = np.linspace(0, size_2 * gap, size_2 + 1)
    
    for i in range(1, size_1 + 1):
        for j in range(1, size_2 + 1):
            if seq_1[i-1] == seq_2[j-1]:
                main_matrix[i][j] = max(main_matrix[i-1][j-1] + match, main_matrix[i-1][j] + gap, main_matrix[i][j-1] + gap)
            else:
                main_matrix[i][j] = max(main_matrix[i-1][j-1] + mismatch, main_matrix[i-1][j] + gap, main_matrix[i][j-1] + gap)
    
    temp_1 = len(seq_1)
    temp_2 = len(seq_2)
    score = 0
    
    while(temp_1 > 0 and temp_2 > 0):
        if temp_1 > 0 and temp_2 > 0 and main_matrix[temp_1][temp_2] == main_matrix[temp_1-1][temp_2-1] + match:
            temp_1 -= 1
            temp_2 -= 1
            score += match
        elif temp_1 > 0 and temp_2 > 0 and main_matrix[temp_1][temp_2] == main_matrix[temp_1-1][temp_2-1] + mismatch:
            temp_1 -= 1
            temp_2 -= 1
            score += mismatch
        elif temp_1 > 0 and main_matrix[temp_1][temp_2] == main_matrix[temp_1-1][temp_2] + gap:
            temp_1 -= 1
            score += gap
        elif temp_2 > 0 and main_matrix[temp_1][temp_2] == main_matrix[temp_1][temp_2-1] + gap:
            temp_2 -= 1
            score += gap
    
    return score


############### QUESTÃO 1 ###############
# Matriz de distância
dist_matrix = [
              [0.0000, 0.1890, 0.1100, 0.1130, 0.2150],
              [0.1890, 0.0000, 0.1790, 0.1920, 0.2110],
              [0.1100, 0.1790, 0.0000, 0.0940, 0.2050],
              [0.1130, 0.1920, 0.0940, 0.0000, 0.2140],
              [0.2150, 0.2110, 0.2050, 0.2140, 0.0000]
              ]

for i in range(len(dist_matrix)):
    for j in range(len(dist_matrix[i])):
        dist_matrix[i][j] *= 10000

# Implementação do Neighbour Joining 
labels = ["Gorila", "Orangotango", "Humano", "Chimpanzé", "Gibão"]

arvore = neighbour_joining(dist_matrix, labels)
print(arvore)
print("\n")

############### QUESTÃO 2 ###############
# Implementação do Needleman Wunsch
match = 1
gap = -2
mismatch = -1
score = []

# Comparação das sequências
seq_cut = [[9482, 9732], [177903, 178153], [3519919, 3520169], [1490249, 1490499], [731123, 731373], [682942, 683192], [454284, 454434], [15079, 15329], [234103, 234353], [253, 503]]

for i in range(1, 10):
    first_sequence = ""
    
    with open(f'seq_{i}.txt') as entrada:
        for line in entrada.readlines():
            first_sequence += line
        first_sequence.replace(" ", "")
        first_sequence = first_sequence[seq_cut[i - 1][0]:seq_cut[i - 1][1]]
        
    for j in range(i + 1, 11):
        second_sequence = ""

        with open(f'seq_{j}.txt') as entrada:
            for line in entrada.readlines():
                second_sequence += line
            second_sequence.replace(" ", "")
            second_sequence = second_sequence[seq_cut[j - 1][0]:seq_cut[j - 1][1]]
        score.append(needleman_wunsch(first_sequence, second_sequence, match, gap, mismatch))
        print(f"seq_{i} vs seq_{j}: {score[len(score) - 1]}")

# Matriz de distâncias
dist_matrix = [
              [],
              [score[0]],
              [score[1], score[9]],
              [score[2], score[10], score[17]],
              [score[3], score[11], score[18], score[24]],
              [score[4], score[12], score[19], score[25], score[30]],
              [score[5], score[13], score[20], score[26], score[31], score[35]],
              [score[6], score[14], score[21], score[27], score[32], score[36], score[39]],
              [score[7], score[15], score[22], score[28], score[33], score[37], score[40], score[42]],
              [score[8], score[16], score[23], score[29], score[34], score[38], score[41], score[43], score[44]]
              ]

print("\n")
print(dist_matrix)

# Implementação do UPGMA 
labels = ["seq_1", "seq_2", "seq_3", "seq_4", "seq_5", "seq_6", "seq_7", "seq_8", "seq_9", "seq_10"]

arvore = upgma(dist_matrix, labels)

print("\n")
print(arvore)
