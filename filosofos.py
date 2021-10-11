import time
import random
import threading
import queue

queue = queue.Queue(maxsize=5)
print("Cinco filósofos sentados en una mesa hacen cola para comer")
def productor():
    while True:
        if not queue.full():    
            item = random.randint(1,5)
            queue.put(item)
            print("\nFilósofo: ", item, "Comiendo")

            time.sleep(random.randint(1,3))


def consumidor():
    while True:
        if not queue.empty():    
            item = queue.get()
            queue.task_done()

            print("\nFilósofo : ", item, "ha terminado de comer")

            time.sleep(random.randint(1,3))


if __name__=="__main__":
    
    thread_productor = threading.Thread(target=productor)
    thread_consumidor = threading.Thread(target=consumidor)

    thread_productor.start();
    thread_consumidor.start();
    thread_productor.join();
    thread_consumidor.join();



