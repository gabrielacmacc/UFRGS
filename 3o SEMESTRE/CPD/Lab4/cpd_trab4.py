# -*- coding: utf-8 -*-
"""
Gabriela Copetti Maccagnan

Classificação e Pesquisa de Dados
Laboratório 4 - Tabelas Hash
"""

# BIBLIOTECAS
import numpy as np
from statistics import mean

# CONSTANTES
keys = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W":23, "X": 24, "Y": 25, "Z": 26,
        "a": 27, "b": 28, "c": 29, "d": 30, "e": 31, "f": 32, "g": 33, "h": 34, "i": 35, "j": 36, "k": 37, "l": 38, "m": 39, "n": 40, "o": 40, "p": 41, "q": 42, "r": 43, "s": 44, "t": 45, "u": 46, "v": 47, "w": 48, "x": 49, "y": 50, "z": 51}

# FUNÇÕES
# Função para construção e inserção dos nomes na tabela hash
def build_hash(names, m):
    hash_table = [[] for x in range(m)]
    
    for name in names:
        hash_key = horner_keys(0, name, m)
        hash_table[hash_key].append(name)
    return hash_table


# Função para gerar um valor numérico inteiro (chave) para cada nome 
def horner_keys(hash_key, name, m):
    # 53 para ser um valor maior que o máximo do vetor keys (51) 
    p = 53

    for d in range(len(name)):
        hash_key = (p * hash_key + letter_key(name, d)) % m
    return hash_key


# Função para pegar o valor de cada letra do nome a partir do vetor keys
def letter_key(name, d):
    if name[d] in keys:
        return keys[name[d]]
    else:
        return 0


# Função para gerar as estatísticas da tabela hash
def stats_hash(table):
    table_sizes = []
    non_empty_items = list(filter(None, table))
    empty_items = len(table) - len(non_empty_items)
    
    for i in range(len(non_empty_items)):
        table_sizes.append(len(non_empty_items[i])) 
    
    exp.write("PARTE 1: ESTATISTICAS DA TABELA HASH\n")
    exp.write(f"NUMERO DE ENTRADAS DA TABELA USADAS {len(non_empty_items)}\n")
    exp.write(f"NUMERO DE ENTRADAS DA TABELA VAZIAS {empty_items}\n")
    exp.write(f"TAXA DE OCUPACAO {len(non_empty_items) / len(table)}\n")
    exp.write(f"MINIMO TAMANHO DE LISTA {min(table_sizes)}\n")
    exp.write(f"MAXIMO TAMANHO DE LISTA {max(table_sizes)}\n")
    exp.write(f"MEDIO TAMANHO DE LISTA {mean(table_sizes)}\n")


# Função para gerar as estatísticas das consultas
def stats_consults(table, names, m):
    acessos = np.zeros(len(names))

    exp.write("\nPARTE 2: ESTATISTICAS DAS CONSULTAS\n")
    
    for i in range(len(names)):
        hash_key = horner_keys(0, names[i], m)
        if names[i] in table[hash_key]:
            for k in range(len(table[hash_key])):
                acessos[i] += 1
                if names[i] == table[hash_key][k]:
                    break
            exp.write(f"{names[i]} HIT {acessos[i]}\n")
        else:
            acessos[i] = -1
            exp.write(f"{names[i]} MISS\n")
    
    hit_items = list(filter(lambda acesso: acesso > -1, acessos))

    exp.write(f"MINIMO NUMERO DE TESTES POR NOME ENCONTRADO {min(hit_items)}\n")
    exp.write(f"MAXIMO NUMERO DE TESTES POR NOME ENCONTRADO {max(hit_items)}\n")
    exp.write(f"MEDIA NUMERO DE TESTES POR NOME ENCONTRADO {mean(hit_items)}\n")
    exp.write(f"MEDIA {mean(acessos)}")


# CHAMADAS DE FUNÇÕES & LEITURA DOS ARQUIVOS
# Chamada para criação da tabela hash
def parte_1(m):
    with open('nomes_10000.txt') as entrada:
        names = []
        for name in entrada.readlines():
            names.append(name.replace("\n", ""))
        hash_table = build_hash(names, m)
        stats_hash(hash_table)
    return hash_table


# Chamada para a consulta da tabela hash
def parte_2(hash_table, m):
    with open('consultas.txt') as entrada:
        names = []
        for name in entrada.readlines():
            names.append(name.replace("\n", ""))
        stats_consults(hash_table, names, m)


# Chamada para os experimentos de tabelas com tamanhos diferentes
m_sizes = [503, 2503, 5003, 7507]
for m in m_sizes:
    exp = open(f"experimento{m}.txt", "w")
    hash_table = parte_1(m)
    parte_2(hash_table, m)
    exp.close()
