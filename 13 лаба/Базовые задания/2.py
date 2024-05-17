import queue
from multiprocessing import Lock, Process, Queue, current_process
import time

def multiplication(tasks_to_accomplish, tasks_that_are_done):
    while True:
        try:
            task = tasks_to_accomplish.get_nowait()
        except queue.Empty:
            break
        else:
            line, column = task
            count = 0
            for i in range(len(line)):
                count += line[i] * column[i]
            tasks_that_are_done.put(count)
            print(str(task) + ' is done by ' + current_process().name)
    return True


def main():

    Matrix1 = [[1, 2, 3], 
            [4, 5, 6],
            [7, 8, 9]]

    Matrix2 = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

    tasks_to_accomplish, tasks_that_are_done = Queue(), Queue()

    MatrixT = [[] for i in range(len(Matrix2[0]))]

    for i in range(len(Matrix2[0])):
        for j in range(len(Matrix2)):
            MatrixT[i].append(Matrix2[j][i])

    for i in range(len(Matrix1)):
        for j in range(len(MatrixT)):
            tasks_to_accomplish.put((Matrix1[i], MatrixT[j]))

    number_of_processes = 4
    processes = []

    for i in range(number_of_processes):

        p = Process(target=multiplication, args=(tasks_to_accomplish, tasks_that_are_done))
        p.start()
        processes.append(p)


    for p in processes:
        p.join()

    ans = [[] for i in range(len(Matrix1))]
    s = 0
    c = len(Matrix1)
    while not tasks_that_are_done.empty():
        ans[s//c].append(tasks_that_are_done.get())
        s += 1

    print(ans)


if __name__ == '__main__':
    main()