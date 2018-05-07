import threading
import os


def print_cube(num):
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
    print("Cube: {}".format(num*num*num))


def print_square(num):
    print("Task 2 assigned to thread {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))
    print("Square: {}".format(num * num))


if __name__ == "__main__":

    t1 = threading.Thread(target=print_cube, args=(10,))
    t2 = threading.Thread(target=print_square, args=(10,))

    print("ID of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.main_thread().name))


    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!!")
