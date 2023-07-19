from threading import Thread, Lock


def synchronized(f):
    lock = Lock()
    value = 0

    def increment(func):
        def ret(*args, **kwargs):
            lock.acquire()
            nonlocal value
            value += 1
            # lock.acquire()
            lock.release()
            return func(*args, **kwargs)
        return ret

    return increment(f)


a = 0


@synchronized
def f():
    global a
    for i in range(300000):
        a = a + 1


t = Thread(target=f)
s = Thread(target=f)

t.start()
s.start()

t.join()
s.join()

print(" *** ", a)
