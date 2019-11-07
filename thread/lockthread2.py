import threading
import time
lock1 = threading.Lock()
lock2 = threading.Lock()


def work1():
    print("-----线程1开始运行")
    lock1.acquire()
    print("线程1申请了锁1")
    time.sleep(1)
    print("线程1等待其他线程释放锁2")
    lock2.acquire()
    print("线程1申请了锁2")
    # time.sleep(1);

    lock2.release()
    print("线程1释放了锁2")
    lock1.release()
    print("线程1释放了锁1")


def work2():
    print("-----线程2开始运行")
    lock2.acquire()
    print("线程2申请了锁2")
    time.sleep(1)
    print("线程2等待其他线程释放锁1")
    lock1.acquire()
    print("线程2申请了锁1")
    # time.sleep(2);

    lock2.release()
    print("线程2释放了锁1")
    lock1.release()
    print("线程2释放了锁2")


if __name__ == '__main__':
    print("主程序启动")
    t1 = threading.Thread(target=work1, args=())
    t2 = threading.Thread(target=work2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("主程序结束")
