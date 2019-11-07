import time
import threading


def work1(in1):
    print("任务1开始啦：{0}\n".format(time.ctime()))
    print("我是参数", in1)
    time.sleep(4)
    print("任务1结束了：{0}".format(time.ctime()))


def work2(in1, in2):
    print("任务1开始啦：{0}\n".format(time.ctime()))
    print("我是参数", in1, in2)
    time.sleep(2)
    print("任务2结束了：{0}".format(time.ctime()))


def main():
    print("主程序开始啦：{0}".format(time.ctime()))
    # 创建子线程
    t1 = threading.Thread(target=work1, args=("二狗子",))
    t2 = threading.Thread(target=work2, args=("傻子", "大笨蛋"))

    # 启动子线程
    t1.start()
    t2.start()

    # 等子线程执行完毕再退出
    t1.join()
    t2.join()
    print("主程序结束了：{0}".format(time.ctime()))


main()

'''————————————————
版权声明：本文为CSDN博主「zuiziyoudexiao」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/zuiziyoudexiao/article/details/86751660'''
