import logging
import threading
import time
import datetime

#simulação 1
#tamanho do vetor: 1024 || numero de threads: 1 ->  2020-04-03 17:16:55.675763 - 2020-04-03 17:16:55.676680 = 0:00:00.000917
#tamanho do vetor: 1024 || numero de threads: 2 ->  2020-04-03 17:16:55.677038 - 2020-04-03 17:16:55.677948 = 0:00:00.000910
#tamanho do vetor: 1024 || numero de threads: 4 ->  2020-04-03 17:16:55.678166 - 2020-04-03 17:16:55.678927 = 0:00:00.000761
#tamanho do vetor: 1024 || numero de threads: 8 ->  2020-04-03 17:16:55.679012 - 2020-04-03 17:16:55.679750 = 0:00:00.000738
#tamanho do vetor: 1024 || numero de threads: 16 -> 2020-04-03 17:16:55.679822 - 2020-04-03 17:16:55.680562 = 0:00:00.000740

#tamanho do vetor: 2048 || numero de threads: 1 ->  2020-04-03 17:16:55.680667 - 2020-04-03 17:16:55.680896 = 0:00:00.000229
#tamanho do vetor: 2048 || numero de threads: 2 ->  2020-04-03 17:16:55.681015 - 2020-04-03 17:16:55.681297 = 0:00:00.000282
#tamanho do vetor: 2048 || numero de threads: 4 ->  2020-04-03 17:16:55.681388 - 2020-04-03 17:16:55.681792 = 0:00:00.000404
#tamanho do vetor: 2048 || numero de threads: 8 ->  2020-04-03 17:16:55.681897 - 2020-04-03 17:16:55.682480 = 0:00:00.000583
#tamanho do vetor: 2048 || numero de threads: 16 -> 2020-04-03 17:16:55.682750 - 2020-04-03 17:16:55.683747 = 0:00:00.000997

#tamanho do vetor: 4096 || numero de threads: 1 ->  2020-04-03 17:16:55.684017 - 2020-04-03 17:16:55.684482 = 0:00:00.000465
#tamanho do vetor: 4096 || numero de threads: 2 ->  2020-04-03 17:16:55.684772 - 2020-04-03 17:16:55.685695 = 0:00:00.000923
#tamanho do vetor: 4096 || numero de threads: 4 ->  2020-04-03 17:16:55.686286 - 2020-04-03 17:16:55.687597 = 0:00:00.001311
#tamanho do vetor: 4096 || numero de threads: 8 ->  2020-04-03 17:16:55.688328 - 2020-04-03 17:16:55.689795 = 0:00:00.001467
#tamanho do vetor: 4096 || numero de threads: 16 -> 2020-04-03 17:16:55.690196 - 2020-04-03 17:16:55.691687 = 0:00:00.001491

#tamanho do vetor: 8192 || numero de threads: 1 ->  2020-04-03 17:16:55.692840 - 2020-04-03 17:16:55.693922 = 0:00:00.001082
#tamanho do vetor: 8192 || numero de threads: 2 ->  2020-04-03 17:16:55.694368 - 2020-04-03 17:16:55.695448 = 0:00:00.001080
#tamanho do vetor: 8192 || numero de threads: 4 ->  2020-04-03 17:16:55.696155 - 2020-04-03 17:16:55.699155 = 0:00:00.003000
#tamanho do vetor: 8192 || numero de threads: 8 ->  2020-04-03 17:16:55.699805 - 2020-04-03 17:16:55.701129 = 0:00:00.001324
#tamanho do vetor: 8192 || numero de threads: 16 -> 2020-04-03 17:16:55.701501 - 2020-04-03 17:16:55.703152 = 0:00:00.001651

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

def thread_sum(vet1, vet2, start, end):
    global vetS
    for i in range(start, end):
        vetS[i] = vet1[i]+vet2[i]

def threads_are_working(threads_list): #função que verifica se aainda tem threads trabalhando
    for thread in threads:
        if ( thread.isAlive() ):
            #print("thread viva")
            return True
    print("threads mortas")
    return  False

if __name__ == "__main__":
    resultados = []
    tam_vetor = [1024, 2048, 4096, 8192]
    qte_threads = [1, 2, 4, 8, 16]
    cont = 0
    while ( cont < len(tam_vetor)):
        cont2 = 0
        while ( cont2 < len(qte_threads)):
            print("nova simulação")
            tam = tam_vetor[cont]
            passo1 = 3
            vet1 = list(range(0, passo1*tam, passo1))
            #print(vet1)
            passo2 = 5
            vet2 = list(range(0, passo2*tam, passo2))
            #print(vet2)
            vetS  = [0]*tam
            #print(vetS)

            num_thread = qte_threads[cont2]
            gap = int(tam/num_thread)
            init = 0
            end = gap
            print("threads", num_thread, "\n", tam)


            threads = []
            tempo_inicial = datetime.datetime.now()

            for i in range(num_thread):
                x = threading.Thread(target=thread_sum, args=(vet1, vet2, init, end))
                #print(i, init, gap)
                x.start()
                threads.append(x)
                init += gap
                end += gap

            #print(vetS)

            u = 0
            while (threads_are_working(threads)):
                u+=1

            tempo_final = datetime.datetime.now()
            resultados.append("tamanho do vetor: {} || numero de threads: {} -> {} - {} = {}".format(tam , num_thread, tempo_inicial, tempo_final, tempo_final - tempo_inicial ))
            cont2 += 1
        cont += 1
    for elem in resultados:
        print(elem)