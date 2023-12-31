import time
from time import sleep
import os
from dma_heap import *
import mmap
import numpy as np

dmaHeap = DmaHeap()

frame_size = 1024 * 1024 * 1024

fd = dmaHeap.alloc(f"test", frame_size)
memory = mmap.mmap(fd.get(), frame_size, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE)
arr = np.ndarray(shape=(1024, 1024, 1024), dtype=np.uint8, buffer=memory)

fd_alt = dmaHeap.alloc(f"test", frame_size)
memory_alt = mmap.mmap(fd_alt.get(), frame_size, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE)
arr_alt = np.ndarray(shape=(1024, 1024, 1024), dtype=np.uint8, buffer=memory_alt)

print(fd.get())
print(fd_alt.get())
print(os.getpid())

while True:
    rand_arr = np.random.randint(0, 255, size=(1024, 1024, 1024), dtype=np.uint8)
    to = time.monotonic_ns()
    arr[:] = rand_arr[:]
    # print()
    # print(frame_size / (time.monotonic_ns() - to))
    # print(arr[:10, :10])
    # print(arr_alt[:10, :10])
