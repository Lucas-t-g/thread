import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

def thread_sum(vet1, vet2, start, end):
    global vetS
    for i in range(start, end):
        vetS[i] = vet1[i]+vet2[i]

if __name__ == "__main__":

    tam = 16
    passo1 = 3
    vet1 = list(range(0, passo1*tam, passo1))
    print(vet1)
    passo2 = 5
    vet2 = list(range(0, passo2*tam, passo2))
    print(vet2)
    vetS  = [0]*tam
    print(vetS)

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")

    num_thread = 8
    gap = int(tam/8)
    init = 0
    end = gap

    print(gap)

    for i in range(num_thread):
        x = threading.Thread(target=thread_sum, args=(vet1, vet2, init, end))
        print(i, init, gap)
        x.start()
        init += gap
        end += gap

    print(vetS)