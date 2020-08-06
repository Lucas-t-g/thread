import logging
import threading
from time import sleep
import datetime
import numpy as np
#simulação 1
#['tamanho da matriz: 256 || numero de threads: 1 -> 2020-04-03 16:32:07.818454 - 2020-04-03 16:32:07.818470 = 0:00:00.000016', 
# 'tamanho da matriz: 256 || numero de threads: 2 -> 2020-04-03 16:32:07.830233 - 2020-04-03 16:32:15.266738 = 0:00:07.436505', 
# 'tamanho da matriz: 512 || numero de threads: 1 -> 2020-04-03 16:32:15.313746 - 2020-04-03 16:32:15.313889 = 0:00:00.000143', 
# 'tamanho da matriz: 512 || numero de threads: 2 -> 2020-04-03 16:32:15.360202 - 2020-04-03 16:33:17.866223 = 0:01:02.506021']



#simulação 2
#tamanho da matriz: 64 || numero de threads: 1 ->   2020-04-03 17:03:25.717168 - 2020-04-03 17:03:25.717178 = 0:00:00.000010
#tamanho da matriz: 64 || numero de threads: 2 ->   2020-04-03 17:03:25.717970 - 2020-04-03 17:03:25.849200 = 0:00:00.131230
#tamanho da matriz: 64 || numero de threads: 4 ->   2020-04-03 17:03:25.850374 - 2020-04-03 17:03:26.001136 = 0:00:00.150762
#tamanho da matriz: 64 || numero de threads: 8 ->   2020-04-03 17:03:26.001922 - 2020-04-03 17:03:26.129224 = 0:00:00.127302
#tamanho da matriz: 64 || numero de threads: 16 ->  2020-04-03 17:03:26.130020 - 2020-04-03 17:03:26.256661 = 0:00:00.126641

#tamanho da matriz: 128 || numero de threads: 1 ->  2020-04-03 17:03:26.259602 - 2020-04-03 17:03:26.259614 = 0:00:00.000012
#tamanho da matriz: 128 || numero de threads: 2 ->  2020-04-03 17:03:26.262444 - 2020-04-03 17:03:27.243848 = 0:00:00.981404
#tamanho da matriz: 128 || numero de threads: 4 ->  2020-04-03 17:03:27.246675 - 2020-04-03 17:03:28.338962 = 0:00:01.092287
#tamanho da matriz: 128 || numero de threads: 8 ->  2020-04-03 17:03:28.341848 - 2020-04-03 17:03:29.558436 = 0:00:01.216588
#tamanho da matriz: 128 || numero de threads: 16 -> 2020-04-03 17:03:29.561268 - 2020-04-03 17:03:30.886031 = 0:00:01.324763

#tamanho da matriz: 256 || numero de threads: 1 ->  2020-04-03 17:03:30.902403 - 2020-04-03 17:03:30.902426 = 0:00:00.000023
#tamanho da matriz: 256 || numero de threads: 2 ->  2020-04-03 17:03:30.915706 - 2020-04-03 17:03:38.492960 = 0:00:07.577254
#tamanho da matriz: 256 || numero de threads: 4 ->  2020-04-03 17:03:38.504667 - 2020-04-03 17:03:46.649369 = 0:00:08.144702
#tamanho da matriz: 256 || numero de threads: 8 ->  2020-04-03 17:03:46.661413 - 2020-04-03 17:03:56.699113 = 0:00:10.037700
#tamanho da matriz: 256 || numero de threads: 16 -> 2020-04-03 17:03:56.710600 - 2020-04-03 17:04:08.536388 = 0:00:11.825788

#tamanho da matriz: 512 || numero de threads: 1 ->  2020-04-03 17:04:08.590993 - 2020-04-03 17:04:08.591018 = 0:00:00.000025
#tamanho da matriz: 512 || numero de threads: 2 ->  2020-04-03 17:04:08.639635 - 2020-04-03 17:05:10.948035 = 0:01:02.308400
#tamanho da matriz: 512 || numero de threads: 4 ->  2020-04-03 17:05:11.005488 - 2020-04-03 17:06:13.639368 = 0:01:02.633880
#tamanho da matriz: 512 || numero de threads: 8 ->  2020-04-03 17:06:13.684163 - 2020-04-03 17:07:28.821520 = 0:01:15.137357
#tamanho da matriz: 512 || numero de threads: 16 -> 2020-04-03 17:07:28.869559 - 2020-04-03 17:09:11.078292 = 0:01:42.208733


def np_matriz(linhas, colunas, elem = 1): #função que cria uma matriz de numpy arrays, é n bem melhor de trabalhar com matrizes numpy
    aux = [elem]*colunas
    matriz = []
    for i in range(linhas):
        matriz.append(aux)
    matriz = np.array(matriz)
    return matriz

def thread_multiplica_matriz(matriz_1, matriz_2, ini_i, fim_i):
    #print("i'm here")
    colunas = len(matriz_1[0])
    linhas =  len(matriz_1)
    global matriz_saida

    if( colunas == linhas ):

        for i in range(ini_i, fim_i):
            for j in range(colunas):
                soma = 0
                for k in range(linhas):
                    soma += matriz_1[i][k]*matriz_2[k][i]
                
                matriz_saida[i][j] = soma
        return matriz_saida

    else:
        print("matrizes de tamanhos incompativeis para a multiplicação")

def threads_are_working(threads_list):#função que verifica se aainda tem threads trabalhando
    for thread in threads:
        if ( thread.isAlive() ):
            #print("thread viva")
            return True
    print("threads mortas")
    return  False

if __name__ == "__main__":
    resultados = []
    cont = 0
    qte_threads = [1, 2, 4, 8, 16]
    o = 16 #variavel que define o quanto o tamanho da matriz será reduzida
    tam_matriz = [int(1024/o), int(2048/o), int(4096/o), int(8192/o)]
    while (cont < len(tam_matriz)): #varia o tamanho da matriz
        cont2 = 0
        while (cont2 < len(qte_threads)):  #varia o numero de threads
            print("nova simulação")
            num_linhas = tam_matriz[cont]
            num_colunas = num_linhas
            num_thread = qte_threads[cont2]
            gap = int(num_linhas/num_thread)
            init = 0
            end = gap
            print("threads", num_thread, "\n", num_linhas, num_colunas)

            matriz_1 = np_matriz(num_linhas, num_colunas, 1)    #cria uma matriz toda composta por '1'
            matriz_2 = np_matriz(num_linhas, num_colunas, 2)    #cria uma matriz toda composta por '2'
            matriz_saida = np_matriz(num_linhas, num_colunas, 0)#cria uma matriz toda composta por '0' para guardar o resultado

            #print(matriz_1)
            #print(matriz_2)
            #matriz = thread_multiplica_matriz(matriz_1, matriz_2, 0, num_colunas)

            threads = []
            tempo_inicial = datetime.datetime.now()

            while (end < num_linhas):
                x = threading.Thread(target=thread_multiplica_matriz, args=(matriz_1, matriz_2, init, end))
                #print(i, init, gap)
                x.start()
                threads.append(x)
                init += gap
                end += gap

            u = 0
            while (threads_are_working(threads)):
                u+=1
            
            #print(matriz)
            tempo_final = datetime.datetime.now()
            resultados.append("tamanho da matriz: {} || numero de threads: {} -> {} - {} = {}".format(num_linhas, num_thread, tempo_inicial, tempo_final, tempo_final - tempo_inicial ))
            #print("numero de threads: ", num_thread, "->", tempo_final, " - ", tempo_inicial," = ",tempo_final - tempo_inicial)
            cont2 += 1
        cont += 1
    for elem in resultados:
        print(elem)