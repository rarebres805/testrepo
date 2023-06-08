import multiprocessing as mp
from multiprocessing import Manager
import time

def cube(x):
    #time.sleep(2)
    return x**mylist[0]

manager = Manager()
mylist = manager.list()
mylist[0] = 2
list = []
for i in range(10000):
        list.append(i)

pool = mp.Pool(processes=4)
results = pool.map(cube, list)
print(results)

