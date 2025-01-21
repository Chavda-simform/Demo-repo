import threading
import time

def func1(r):
    print("numbers ")
    for x in range(r) :
        print(x)
        time.sleep(0.5)
def func2(A,Z):
    print("Alfabets")
    for i in range(ord(A), ord(Z)):
        print(chr(i))
        time.sleep(0.5)
time1 = time.perf_counter()
# func1()
# func2()
t1 = threading.Thread(target=func1, args=[10])
t2 = threading.Thread(target=func2, args=['A', 'Z'])

t1.start()
t2.start()

t1.join()
t2.join()
time2 = time.perf_counter()
print(time2 - time1)