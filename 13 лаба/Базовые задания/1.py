import queue
from multiprocessing import Lock, Process, Queue, current_process
import time

def scalar_multiplication(tasks_to_accomplish, tasks_that_are_done):
    while True:
        try:
            task = tasks_to_accomplish.get_nowait()
        except queue.Empty:
            break
        else:
            a, b = task
            tasks_that_are_done.put(a*b)
            print(str(task) + ' is done by ' + current_process().name)
    return True
    
def main():

    a = (1, 2, 3, 4)
    b = (1, 5, 6, 7, 8)

    tasks_to_accomplish, tasks_that_are_done = Queue(), Queue()

    number_of_processes = 4
    processes = []
    for i in range(-1, -min(len(a), len(b))-1, -1):
        tasks_to_accomplish.put((a[i], b[i]))

    for i in range(number_of_processes):
        p = Process(target=scalar_multiplication, args=(tasks_to_accomplish, tasks_that_are_done))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

    ans = 0
    while not tasks_that_are_done.empty():
        ans += tasks_that_are_done.get()
    print(f'Результат: {ans}')

if __name__ == '__main__':
    main()