import os, glob ### bibliotecas para abrir os arquivos automaticamente



def contagemChar():

    cont = 0
    charAt = 0
    path = "./textos" ### pasta onde estão os arquivos de texto

    for nomeArquivo in glob.glob(os.path.join(path, '*.txt')): ### verificação do tipo do arquivo (somente lerá .txt)
        arq = open(os.path.join(os.getcwd(), nomeArquivo), 'r')
        ###print("Arquivo: " + nomeArquivo) 
            

        for i in arq:
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
            else:
                print(palavra + ": pertence")
                cont = 0
                charAt = 0

contagemChar()