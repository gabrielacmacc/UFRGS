# -*- coding: utf-8 -*-
"""
Gabriela Copetti Maccagnan

Classificação e Pesquisa de Dados
Laboratório 3 - Radix Sort
"""

# FUNÇÕES
# Função do radix sort para o máximo dígito significativo
def msd(text, hi, d):
    if hi <= 1:
        return text
    
    sorted_text = []
    temp = [[] for x in range(27)]

    for i in range(hi):
        if d >= len(text[i]):
            sorted_text.append(text[i])
        else:
            temp[charAt(text[i], d)].append(text[i])
        
    temp = [msd(j, len(j), d + 1) for j in temp]

    for k in temp:
        for l in k:
            sorted_text.append(l)
    
    return sorted_text


# Função para adquirir o valor ASC de cada caracter
def charAt(word, d):
    if d < len(word):
        return ord(word[d]) - ord('A')


# Função para contar quantas vezes cada palavra aparece
def count_strings(text, hi):
    temp = []
    counter = []
    j = 0
    
    for i in range(hi):
        if text[i] not in temp:
            temp.append(text[i])
            counter.append(1)
            j += 1
        else:
            counter[j - 1] += 1
    return temp, counter


# Função para remover as palavras com tamanho menor que 4 caracteres
def remove_strings(text, hi):
    new_text = []
    
    for c in range(hi):
        if len(text[c]) >= 4:
            new_text.append(text[c])
    return new_text


# ABERTURA & ESCRITA ARQUIVOS
arq_fr = open("frankenstein_ordenado.txt", "w")
arq_wp = open("war_and_peace_ordenado.txt", "w")

# Funções principais
def radixsort_fr():
    with open('frankenstein_clean.txt') as entrada:
        text = entrada.readline()
        text = text.split()
        new_text = remove_strings(text, len(text))
        sorted_text = msd(new_text, len(new_text), 0)
        final_list, counter_list = count_strings(sorted_text, len(new_text))
        for i in range(len(final_list)):
            arq_fr.write(f"{final_list[i]} {counter_list[i]}\n")

def radixsort_wp():
    with open('war_and_peace_clean.txt') as entrada:
        text = entrada.readline()
        text = text.split()
        new_text = remove_strings(text, len(text))
        sorted_text = msd(new_text, len(new_text), 0)
        final_list, counter_list = count_strings(sorted_text, len(new_text))
        for i in range(len(final_list)):
            arq_wp.write(f"{final_list[i]} {counter_list[i]}\n")

radixsort_fr()
radixsort_wp()

# Fecha os arquivos
arq_fr.close()
arq_wp.close()