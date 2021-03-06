#
import threading

count = 0
# 创建一个lock对象
lock = threading.Lock()


def work1():
    global count
    for i in range(0, 1000000):
        # 申请锁
        lock.acquire()
        count = count + 1
        # 释放锁
        lock.release()
        # print("任务1：count={0}\n".format(count));


def work2():
    global count
    for i in range(0, 1000000):
        # 申请锁
        lock.acquire()
        count = count - 1
        # 释放锁
        lock.release()
        # print("任务2：count={0}\n".format(count));


t1 = threading.Thread(target=work1, args=())
t2 = threading.Thread(target=work2, args=())

# 启动子线程
t1.start()
t2.start()

# 等子线程执行完毕再退出
t1.join()
t2.join()

print("最终结果：{0}".format(count))
'''————————————————
版权声明：本文为CSDN博主「zuiziyoudexiao」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https: // blog.csdn.net/zuiziyoudexiao/article/details/86751660'''
