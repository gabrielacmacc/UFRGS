# -*- coding: utf-8 -*-
"""
Gabriela Copetti Maccagnan

Biologia Computacional
Trabalho 1
"""

#BIBLIOTECAS
import sys
import numpy as np

np.set_printoptions(threshold=sys.maxsize)
arquivo = open("alinhamentos.txt", "w")

#FUNÇÕES
def needleman_wunsch(seq_1, seq_2, match, gap, mismatch):
    arquivo.write(f"NEEDLEMAN {match}, {gap}, {mismatch}:\n")
    size_1 = len(seq_1)
    size_2 = len(seq_2)
    
    # Inicialização da matriz
    main_matrix = np.zeros((size_1 + 1, size_2 + 1))
    # Preenchimento dos valores de gap acumulado
    main_matrix[:,0] = np.linspace(0, size_1 * gap, size_1 + 1)
    main_matrix[0,:] = np.linspace(0, size_2 * gap, size_2 + 1)
    
    # Preenchimento do resto da matriz
    for i in range(1, size_1 + 1):
        for j in range(1, size_2 + 1):
            # Caso os valores sejam iguais
            if seq_1[i-1] == seq_2[j-1]:
                main_matrix[i][j] = max(main_matrix[i-1][j-1] + match, main_matrix[i-1][j] + gap, main_matrix[i][j-1] + gap)
            # Caso sejam diferentes
            else:
                main_matrix[i][j] = max(main_matrix[i-1][j-1] + mismatch, main_matrix[i-1][j] + gap, main_matrix[i][j-1] + gap)
    
    # Condições de parada, se acabar a sequência, acaba o laço
    temp_1 = len(seq_1)
    temp_2 = len(seq_2)
    # String pras sequências alinhadas
    aligned_1 = ""
    aligned_2 = ""
    # Variável de score
    score = 0
    
    # Percorre a matriz
    while(temp_1 > 0 and temp_2 > 0):
        # Caso match
        if temp_1 > 0 and temp_2 > 0 and main_matrix[temp_1][temp_2] == main_matrix[temp_1-1][temp_2-1] + match:
            aligned_1 = seq_1[temp_1 - 1] + aligned_1
            aligned_2 = seq_2[temp_2 - 1] + aligned_2
            temp_1 -= 1
            temp_2 -= 1
            score += match
        # Caso mismatch
        elif temp_1 > 0 and temp_2 > 0 and main_matrix[temp_1][temp_2] == main_matrix[temp_1-1][temp_2-1] + mismatch:
            aligned_1 = seq_1[temp_1 - 1] + aligned_1
            aligned_2 = seq_2[temp_2 - 1] + aligned_2
            temp_1 -= 1
            temp_2 -= 1
            score += mismatch
        # Caso gap na sequência 2
        elif temp_1 > 0 and main_matrix[temp_1][temp_2] == main_matrix[temp_1-1][temp_2] + gap:
            aligned_1 = seq_1[temp_1 - 1] + aligned_1
            aligned_2 = "-" + aligned_2
            temp_1 -= 1
            score += gap
        # Caso gap na sequência 1
        elif temp_2 > 0 and main_matrix[temp_1][temp_2] == main_matrix[temp_1][temp_2-1] + gap:
            aligned_1 = "-" + aligned_1
            aligned_2 = seq_2[temp_2 - 1] + aligned_2
            temp_2 -= 1
            score += gap

    arquivo.write(f"{main_matrix}\n")
    return aligned_1, aligned_2, score

def smith_waterman(seq_1, seq_2, match, gap, mismatch):
    arquivo.write("SMITH {match}, {gap}, {mismatch}:\n")
    size_1 = len(seq_1) 
    size_2 = len(seq_2)
    
    # Inicializa a matriz
    main_matrix = np.zeros((size_1 + 1, size_2 + 1))
    
    # Preechimento da matriz
    for i in range(1, size_1 + 1):
        for j in range(1, size_2 + 1):
            # Caso os valores sejam iguais
            if seq_1[i-1] == seq_2[j-1]:
                main_matrix[i][j] = max(main_matrix[i-1][j-1] + match, main_matrix[i-1][j] + gap, main_matrix[i][j-1] + gap, 0)
            # Caso sejam diferentes
            else:
                main_matrix[i][j] = max(main_matrix[i-1][j-1] + mismatch, main_matrix[i-1][j] + gap, main_matrix[i][j-1] + gap, 0)
    
    temp_matrix = np.array(main_matrix)
    m_index = np.where(temp_matrix == temp_matrix.max())
    
    temp_1 = m_index[0][0]
    temp_2 = m_index[1][0]
    aligned_1 = ""
    aligned_2 = ""
    score = (temp_1, temp_2)
    
    while(temp_1 > 0 and temp_2 > 0):
        if temp_1 > 0 and temp_2 > 0 and main_matrix[temp_1][temp_2] > 0:
            aligned_1 = seq_1[temp_1 - 1] + aligned_1
            aligned_2 = seq_2[temp_2 - 1] + aligned_2
            temp_1 -= 1
            temp_2 -= 1
        elif main_matrix[temp_1][temp_2] == 0:
            temp_1 = 0
            temp_2 = 0

    arquivo.write(f"{main_matrix}")
    return aligned_1, aligned_2, score

############### QUESTÃO 1 ###############
chimpanzee_seq = "MTENSTSAPAAKPKRAKASKKSTDHPKYSDMIVAAIQAEKNRAGSSRQSIQKYIKSHYKVGENADSQIKLSIKRLVTTGVLKQTKGVGASGSFRLAKSDEPKKSVAFKKTKKEIKKVATPKKASKPKKAASKAPTKKPKATPVKKAKKKLAATPKKAKKPKTVKAKPVKASKPKKAKPVKPKAKSSAKRAGKKK"
homo_sapiens_seq = "MTENSTSAPAAKPKRAKASKKSTDHPKYSDMIVAAIQAEKNRAGSSRQSIQKYIKSHYKVGENADSQIKLSIKRLVTTGVLKQTKGVGASGSFRLAKSDEPKKSVAFKKTKKEIKKVATPKKASKPKKAASKAPTKKPKATPVKKAKKKLAATPKKAKKPKTVKAKPVKASKPKKAKPVKPKAKSSAKRAGKKK"
cow_seq = "MTENSTSTPAAKPKRAKASKKSTDHPKYSDMIVAAIQAEKNRAGSSRQSIQKYIKSHYKVGENADSQIKLSIKRLVTTGVLKQTKGVGASGSFRLAKSDEPKRSVAFKKTKKEVKKVATPKKAAKPKKAASKAPSKKPKATPVKKAKKKPAATPKKTKKPKTVKAKPVKASKPKKTKPVKPKAKSSAKRTGKKK"
rat_seq = "MSETAPVPQPASVAPEKPAATKKTRKPAKAAVPRKKPAGPSVSELIVQAVSSSKERSGVSLAALKKSLAAAGYDVEKNNSRIKLGLKSLVNKGTLVQTKGTGAAGSFKLNKKAESKASTTKVTVKAKASGAAKKPKKTAGAAAKKTVKTPKKPKKPAVSKKTSSKSPKKPKVVKAKKVAKSPAKAKAVKPKAAKVKVTKPKTPAKPKKAAPKKK"

match = 2
gap = -5
mismatch = -2

aligned_hu1, aligned_ch, score1 = needleman_wunsch(homo_sapiens_seq, chimpanzee_seq, match, gap, mismatch)
print("GLOBAL SEQUENCE ALIGNMENT:")
print(aligned_hu1)
print(aligned_ch)
print(f"ALIGNMENT SCORE: {score1}\n")

aligned_hu2, aligned_co, score2 = needleman_wunsch(homo_sapiens_seq, cow_seq, match, gap, mismatch)
print("GLOBAL SEQUENCE ALIGNMENT:")
print(aligned_hu2)
print(aligned_co)
print(f"ALIGNMENT SCORE: {score2}\n")

aligned_hu3, aligned_ra, score3 = needleman_wunsch(homo_sapiens_seq, rat_seq, match, gap, mismatch)
print("GLOBAL SEQUENCE ALIGNMENT:")
print(aligned_hu3)
print(aligned_ra)
print(f"ALIGNMENT SCORE: {score3}\n")

############### QUESTÃO 2 ###############
seq_1 = "AGGTCTCA"
seq_2 = "GGCCA"

match = 7
gap = -4
mismatch = -3

aligned_1, aligned_2, score = needleman_wunsch(seq_1, seq_2, match, gap, mismatch)
print("GLOBAL SEQUENCE ALIGNMENT:")
print(aligned_1)
print(aligned_2)
print(f"ALIGNMENT SCORE: {score}\n")

############### QUESTÃO 3 ###############
bacillus_lentus_seq = "AQSVPWGISRVQAPAAHNRGLTGSGVKVAVLDTGISTHPDLNIRGGASFVPGEPSTQDGNGHGTHVAGTIAALNNSIGVLGVAPSAELYAVKVLGASGSGSVSSIAQGLEWAGNNGMHVANLSLGSPSPSATLEQAVNSATSRGVLVVAASGNSGAGSISYPARYANAMAVGATDQNNNRASFSQYGAGLDIVAPGVNVQSTYPGSTYASLNGTSMATPHVAGAAALVKQKNPSWSNVQIRNHLKNTATSLGSTNLYGSGLVNAEAATR"
bacillus_halodurans_seq = "MRQSLKVMVLSTVALLFMANPAAASEEKKEYLIVVEPEEVSAQSVEESYDVDVIHEFEEIPVIHAELTKKELKKLKKDPNVKAIEKNAEVTISQTVPWGISFINTQQAHNRGIFGNGARVAVLDTGIASHPDLRIAGGASFISSEPSYHDNNGHGTHVAGTIAALNNSIGVLGVAPSADLYAVKVLDRNGSGSLASVAQGIEWAINNNMHIINMSLGSTSGSSTLELAVNRANNAGILLVGAAGNTGRQGVNYPARYSGVMAVAAVDQNGQRASFSTYGPEIEISAPGVNVNSTYTGNRYVSLSGTSMATPHVAGVAALVKSRYPSYTNNQIRQRINQTATYLGSPSLYGNGLVHAGRATQ"

match = 1
gap = -2
mismatch = -1

aligned_1, aligned_2, score = smith_waterman(bacillus_lentus_seq, bacillus_halodurans_seq, match, gap, mismatch)
print("LOCAL SEQUENCE ALIGNMENT:")
print(aligned_1)
print(aligned_2)
print(f"START POSITION FOR LOCAL ALIGNMENT: {score}\n")
arquivo.close()
