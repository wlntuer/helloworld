import time
import _thread
# 任务1


def work1():
    print("任务1开始了：{0}\n".format(time.ctime()))
    time.sleep(4)
    print("任务1结束了：", time.ctime())
# 任务2


def work2():
    print("任务2开始了：{0}\n".format(time.ctime()))
    time.sleep(2)
    print("任务2结束了：", time.ctime())

# 主程序


def main():
    print("主函数开始了：", time.ctime())
    # 开启两个线程来分别执行两个任务
    _thread.start_new_thread(work1, ())
    _thread.start_new_thread(work2, ())
    print("主函数结束了：", time.ctime())

    # 主程序等待20秒再退出，防止两个线程还没开始执行整个程序就终止了
    for i in range(20):
        time.sleep(1)


main()
