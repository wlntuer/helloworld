import time
import threading

# 重写run方法


class mythread(threading.Thread):
    def __init__(self, arg):
        threading.Thread.__init__(self)
        self.arg = arg

    def run(self):
        time.sleep(2)
        print("这是第%d个线程。" % self.arg)


for i in range(5):
    t = mythread(i)
    t.start()
    t.join()

print("主线程执行完毕！")
