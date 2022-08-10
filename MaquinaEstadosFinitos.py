### Feito por: Thiago Krügel

"""
Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a linguagem Python, C ou C++.
Este programa, quando executado, irá determinar se uma string de entrada faz parte da linguagem 𝐿 definida  por
𝐿 = {𝑥 | 𝑥 ∈ {𝑎,𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo o alfabeto  Σ={𝑎,𝑏,𝑐}.
O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) contendo várias strings.
A primeira linha do arquivo indica quantas strings estão no arquivo de texto de entrada. As linhas subsequentes contém
uma string por linha.  A seguir está um exemplo das linhas que podem existir em um arquivo de testes para o programa
que você irá desenvolver:
3
abbaba
abababb
bbabbaaab
Neste  exemplo  temos  3  strings  de  entrada.  O  número  de  strings em  cada  arquivo  será representado  por  um
número  inteiro  positivo.  A  resposta  do  seu  programa  deverá  conter  uma, e somente uma linha de saída para cada
string. Estas linhas conterão a string de entrada e o resultado da validação conforme o formato indicado a seguir:
abbaba: não pertence.
A  saída  poderá  ser  enviada  para  um  arquivo  de  textos,  ou  para  o  terminal  padrão  e  será composta de uma
linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída.
"""


import os, glob ### bibliotecas para abrir os arquivos automaticamente



def contagemChar():

    cont = 0
    charAt = 0
    quantidade = 0
    palavrasChecadas = 0
    inicioArquivo = False
    path = "./textos" ### pasta onde estão os arquivos de texto

    for nomeArquivo in glob.glob(os.path.join(path, '*.txt')): ### verificação do tipo do arquivo (somente lerá .txt)
        inicioArquivo = False
        quantidade = 0
        palavrasChecadas = 0
        arq = open(os.path.join(os.getcwd(), nomeArquivo), 'r')
        ###print("Arquivo: " + nomeArquivo) 
            

        for i in arq:
            if inicioArquivo == False:
                quantidade = int(i[0])
                inicioArquivo = True
            else:
                word = str(i)
                dividir = word.split("\n")
                palavra = str(dividir[0])
                for letra in palavra:
                    if letra == "a":
                        try:
                            if palavra[charAt + 1] != "b" or palavra[charAt + 2] != "b":                    
                                cont += 1
                                charAt += 1
                            else:
                                charAt += 1
                        except IndexError: ### quando a letra "a" estiver em uma das duas últimas posições a palavra já não pertencerá
                            cont += 1
                            continue                            
                    elif letra != "a" and letra != "b" and letra != "c":
                        cont += 1
                        charAt += 1
                    else:
                        charAt += 1

                if cont != 0:
                    print(palavra + ": não pertence")  
                    cont = 0
                    charAt = 0 
                    palavrasChecadas += 1
                    if palavrasChecadas >= quantidade:
                        break
                else:
                    print(palavra + ": pertence")
                    cont = 0
                    charAt = 0
                    palavrasChecadas += 1
                    if palavrasChecadas >= quantidade:
                        break

contagemChar()
