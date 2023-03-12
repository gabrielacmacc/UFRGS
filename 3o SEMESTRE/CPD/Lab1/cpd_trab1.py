# -*- coding: utf-8 -*-
"""
Gabriela Copetti Maccagnan

Classificação e Pesquisa de Dados
Laboratório 1 - ShellSort 
"""

# BIBLIOTECAS
import numpy as np
import time

# CONSTANTES
seqShell = np.array([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576])

seqKnuth = np.array([1,4,13,40,121,364,1093,3280,9841,29524,88573,265720,797161,2391484])

seqCiura = np.array([1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711])

# SHELLSORT

# FUNÇÕES
def calculaH(n):
    hS = 0
    hK = 0
    hC = 0
    
    i = 0
    while(seqShell[i] < n):
        i += 1
    hS = i - 1
    if seqShell[hS] >= n:
        hS -= 1
    
    j = 0
    while(seqKnuth[j] < n):
        j += 1
    hK = j - 1
    if seqKnuth[hK] >= n:
        hK -= 1
        
    k = 0
    while(seqCiura[k] < n):
        k += 1
    hC = k - 1
    if seqCiura[hC] >= n:
        hC -= 1
    
    return hS, hK, hC

def ordenamento(n, seqO, h, seqE, modo):
    saida.write(f"{' '.join(seqO)} SEQ={modo}\n")
    while(h >= 0):
        for i in range(seqE[h], n):
            temp = seqO[i]
            j = i
            while (j >= seqE[h]) and (int(temp) < int(seqO[j - seqE[h]])):
                seqO[j] = seqO[j - seqE[h]]
                j -= seqE[h]
            seqO[j] = temp
        saida.write(f"{' '.join(seqO)} INCR={seqE[h]}\n")
        h -= 1

saida = open("saida1.txt", "w")

def shellSort():
    with open('entrada1.txt') as entrada:
        for line in entrada.readlines():
            line = line.split()
            n = int(line[0])
            hS, hK, hC = calculaH(n)
            ordenamento(n, line[1:], hS, seqShell, "SHELL")
            ordenamento(n, line[1:], hK, seqKnuth, "KNUTH")
            ordenamento(n, line[1:], hC, seqCiura, "CIURA")

shellSort()
    
saida.close() 

# TESTES DE ESCALA

# FUNÇÕES
    
def ordenamentoCronometrado(n, seqO, h, seqE, modo):
    start = time.process_time()
    while(h >= 0):
        for i in range(seqE[h], n):
            temp = seqO[i]
            j = i
            while (j >= seqE[h]) and (int(temp) < int(seqO[j - seqE[h]])):
                seqO[j] = seqO[j - seqE[h]]
                j -= seqE[h]
            seqO[j] = temp
        h -= 1
    end = time.process_time() - start
    saida2.write(f"{modo}, {n}, {end}\n")
    
saida2 = open("saida2.txt", "w")

def testeEscala():
    with open('entrada2.txt') as entrada2:
        for line in entrada2.readlines():
            line = line.split()
            n = int(line[0])
            hS, hK, hC = calculaH(n)
            ordenamentoCronometrado(n, line[1:], hS, seqShell, "SHELL")
            ordenamentoCronometrado(n, line[1:], hK, seqKnuth, "KNUTH")
            ordenamentoCronometrado(n, line[1:], hC, seqCiura, "CIURA")
    
testeEscala()

saida2.close() 
