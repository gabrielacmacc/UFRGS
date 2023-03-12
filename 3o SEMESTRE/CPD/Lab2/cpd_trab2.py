# -*- coding: utf-8 -*-
"""
Gabriela Copetti Maccagnan

Classificação e Pesquisa de Dados
Laboratório 2 - QuickSort
"""

# BIBLIOTECAS
from math import floor
from statistics import median
import time
import random

# CONSTANTES
swaps_ml = recur_ml = 0
swaps_al = recur_al = 0
swaps_mh = recur_mh = 0
swaps_ah = recur_ah = 0

# FUNÇÕES
# Função para o particionamento de Lomuto
def lomuto_partition(seq, start, end, swap):
    pivot = seq[end]
    i = start
    for j in range(start, end):
        if seq[j] <= pivot:
            exchange(seq, i, j, swap)
            i += 1
    exchange(seq, i, end, swap)
    return i


# Função para o particionamento de Hoare
def hoare_partition(seq, start, end, swap):
    pivot = seq[start]
    esq = True
    while start < end:
        if esq:
            if pivot >= seq[end]:
                seq[start] = seq[end]
                counter(swap)
                start += 1
                esq = False
            else:
                end -= 1
        else:
            if pivot < seq[start]:
                seq[end] = seq[start]
                counter(swap)
                end -= 1
                esq = True
            else:
                start += 1
    k = start
    seq[k] = pivot
    return k


# Função para a escolha do particionador por mediana de 3
def median_partition(mode, seq, start, end, swap):
    # Pega a posição do meio
    middle = floor((end - start) / 2)

    # Pega os valores de cada posição
    first = seq[start]
    stop = seq[middle]
    last = seq[end]
    
    # Cria um vetor
    data = [first, stop, last]
    # Ordena o vetor
    sorted(data)
    # Acha a mediana
    mediana = median(data)
    # Pega o index da mediana 
    m_index = data.index(mediana)

    if m_index == 0: 
        m_index = start
    elif m_index == 1: 
        m_index = middle
    elif m_index == 2:
        m_index = end
    
    exchange(seq, start, m_index, swap)
    
    # Checa qual vai ser o partionamento e manda para a função específica
    if mode == "lomuto":
        return lomuto_partition(seq, start, end, swap)
    elif mode == "hoare":
        return hoare_partition(seq, start, end, swap)


# Função para a escolha do particionador randômico
def random_partition(mode, seq, start, end, swap):
    r_index = random.randint(start + 1, end)
    
    exchange(seq, start, r_index, swap)
    
    # Checa qual vai ser o partionamento e manda para a função específica
    if mode == "lomuto":
        return lomuto_partition(seq, start, end, swap)
    elif mode == "hoare":
        return hoare_partition(seq, start, end, swap)

# Função para troca de posição
def exchange(seq, pos1, pos2, swap):
    # Soma no counter
    counter(swap)
    # Faz a troca
    temp = seq[pos1]
    seq[pos1] = seq[pos2]
    seq[pos2] = temp
 

# Função para contagem dos swaps
def counter(swap):
    # Variáveis globais para os counters específicos
    global swaps_ml
    global swaps_al
    global swaps_mh
    global swaps_ah
    
    if swap == "swaps_ml":
        swaps_ml += 1
    elif swap == "swaps_al":
        swaps_al += 1
    elif swap == "swaps_mh":
        swaps_mh += 1
    elif swap == "swaps_ah":
        swaps_ah += 1

# Função do quicksort para Lomuto com particionador por mediana de 3
def lomuto_median(seq, start, end):
    # Calcula as recursões
    global recur_ml
    recur_ml += 1
    
    if int(end) > int(start):
        pivot_index = median_partition("lomuto", seq, int(start), int(end), "swaps_ml") # Escolhe o particionador
        lomuto_median(seq, start, pivot_index - 1) # Ordena os elementos antes do particionador 
        lomuto_median(seq, pivot_index + 1, end) # Ordena os elementos depois do particionador 


# Função do quicksort para Lomuto com particionador randômico
def lomuto_random(seq, start, end):
    # Calcula as recursões
    global recur_al
    recur_al += 1
    
    if int(end) > int(start):
        pivot_index = random_partition("lomuto", seq, int(start), int(end), "swaps_al") # Escolhe o particionador
        lomuto_random(seq, start, pivot_index - 1) # Ordena os elementos antes do particionador 
        lomuto_random(seq, pivot_index + 1, end) # Ordena os elementos depois do particionador 


# Função do quicksort para Hoare com particionador por mediana de 3
def hoare_median(seq, start, end):
    # Calcula as recursões
    global recur_mh
    recur_mh += 1
    
    if end > start:
        pivot_index = median_partition("hoare", seq, start, end, "swaps_mh") # Escolhe o particionador
        hoare_median(seq, start, pivot_index - 1) # Ordena os elementos antes do particionador 
        hoare_median(seq, pivot_index + 1, end) # Ordena os elementos depois do particionador 


# Função do quicksort para Hoare com particionador randômico
def hoare_random(seq, start, end):
    # Calcula as recursões
    global recur_ah
    recur_ah += 1

    if end > start: 
        pivot_index = random_partition("hoare", seq, start, end, "swaps_ah") # Escolhe o particionador
        hoare_random(seq, start, pivot_index - 1) # Ordena os elementos antes do particionador 
        hoare_random(seq, pivot_index + 1, end) # Ordena os elementos depois do particionador 


# ABERTURA & ESCRITA ARQUIVOS
stats_mh = open("stats-mediana-hoare.txt", "w")
stats_ml = open("stats-mediana-lomuto.txt", "w")
stats_ah = open("stats-aleatorio-hoare.txt", "w")
stats_al = open("stats-aleatorio-lomuto.txt", "w")

# Função principal
def quicksort():
    with open('entrada-quicksort.txt') as entrada:
        for line in entrada.readlines():
            # Transforma a lista de strings em ints
            line = [int(i) for i in line.split()]
            # Primeiro elemento é o tamanho do vetor 
            n = line[0]
            
            # Quicksort Lomuto com particionador escolhido por mediana de 3
            stats_ml.write(f"TAMANHO ENTRADA {n}\n")
            # Começa o temporizador
            start_timer = time.process_time()
            lomuto_median(line[1:], 0, n - 1)
            #Calcula o tempo total de processamento
            end_timer = time.process_time() - start_timer
            stats_ml.write(f"SWAPS {swaps_ml}\n")
            stats_ml.write(f"RECURSOES {recur_ml}\n")
            stats_ml.write(f"TEMPO {end_timer} EM SEGUNDOS\n")
            
            # Quicksort Lomuto com particionador escolhido aleatoriamente
            stats_al.write(f"TAMANHO ENTRADA {n}\n")
            start_timer = time.process_time()
            lomuto_random(line[1:], 0, n - 1)
            end_timer = time.process_time() - start_timer
            stats_al.write(f"SWAPS {swaps_al}\n")
            stats_al.write(f"RECURSOES {recur_al}\n")
            stats_al.write(f"TEMPO {end_timer} EM SEGUNDOS\n")

            # Quicksort Hoare com particionador escolhido por mediana de 3
            stats_mh.write(f"TAMANHO ENTRADA {n}\n")
            start_timer = time.process_time()
            hoare_median(line[1:], 0, n - 1)
            end_timer = time.process_time() - start_timer
            stats_mh.write(f"SWAPS {swaps_mh}\n")
            stats_mh.write(f"RECURSOES {recur_mh}\n")
            stats_mh.write(f"TEMPO {end_timer} EM SEGUNDOS\n")
            
            # Quicksort Hoare com particionador escolhido aleatoriamente
            stats_ah.write(f"TAMANHO ENTRADA {n}\n")
            start_timer = time.process_time()
            hoare_random(line[1:], 0, n - 1)
            end_timer = time.process_time() - start_timer
            stats_ah.write(f"SWAPS {swaps_ah}\n")
            stats_ah.write(f"RECURSOES {recur_ah}\n")
            stats_ah.write(f"TEMPO {end_timer} EM SEGUNDOS\n")
            

quicksort()

# Fecha os arquivos
stats_mh.close()
stats_ml.close()
stats_ah.close()
stats_al.close()
