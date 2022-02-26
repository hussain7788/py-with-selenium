from threading import *
from multiprocessing import Process
import time


# def squares(list1):
#     time.sleep(2)
#     for i in list1:
#         print("child thread::", i*i)


# b = time.time()
# l1 = [1, 2, 3, 4]
# s = Thread(target=squares, args=(l1,))
# s.start()
# s.join()
# e = time.time()
# print("Total time for thread:", e-b)
# print("Thread Name::", current_thread().getName())


def square(list1):
    time.sleep(2)
    for i in list1:
        print("child thread::", i*i)


if __name__ == "__main__":
    b = time.time()
    l1 = [1, 2, 3, 4]
    s = Process(target=square, args=(l1,))
    s.start()
    s.join()
    e = time.time()
    print("Total time for Process:", e-b)
    print("Thread Name::", current_thread().getName())
