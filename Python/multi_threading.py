from threading import *
import time

# with threading calculating execution time


# def double(list1):
#     for i in list1:
#         time.sleep(1)
#         print("double value::", 2*i)


# def squares(list1):
#     for i in list1:
#         time.sleep(1)
#         print("square value::", i*i)


# list1 = [1, 2, 3, 4, 5, 6]
# begin = time.time()
# t1 = Thread(target=double, args=(list1,))
# t2 = Thread(target=squares, args=(list1,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end = time.time()
# print("the total time::", end-begin)

#############################################################

# with out threading calculating execution time


# def double(list1):
#     for i in list1:
#         time.sleep(1)
#         print("double value::", 2*i)


# def squares(list1):
#     for i in list1:
#         time.sleep(1)
#         print("square value::", i*i)


# list1 = [1, 2, 3, 4, 5, 6]
# begin = time.time()
# double(list1)
# squares(list1)
# end = time.time()
# print("the total time::", end-begin)

###############################################################
# # finding threading names

# def m1():
#     print("Child thread::", current_thread().getName())


# def m2():
#     print("Child thread 2::", current_thread().getName())


# t = Thread(target=m1)
# t1 = Thread(target=m2)
# t.start()
# t1.start()
# # after start() method the main thread will execute before start method child threads will executes
# print("Main thread::", current_thread().getName())

###################################################################
# # passing the thread names when calling

# def display():
#     print(current_thread().name, '......started')
#     time.sleep(1)
#     print(current_thread().name, '......ended')


# t1 = Thread(target=display, name="ChildThread_1")
# t2 = Thread(target=display, name="ChildThread_2")
# t1.start()
# t2.start()
# print(t1.name, "is alive", t1.is_alive())
# print(t2.name, "is alive", t2.is_alive())
# time.sleep(10)

# # after 10 seconds the thread will die .so result is False
# print(t1.name, "is alive", t1.is_alive())
# print(t2.name, "is alive", t2.is_alive())


################################################################
### set name and get name

# def get():
#     print(current_thread().getName())
#     time.sleep(2)
#     current_thread().setName(name="hussain")
#     print(current_thread().getName())
# get()

# ## count the present threads which are running.. MainThread is always running 
# print(active_count())
# ## the identitiy number of thread ..it will change every time
# print(current_thread().ident)

####################################################################