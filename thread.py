
import time

# 定义任务1


def work1():
    print("任务1开始了：", time.ctime())
    time.sleep(4)
    print("任务1结束了：", time.ctime())
# 定义任务2


def work2():
    print("任务2开始了：", time.ctime())
    time.sleep(2)
    print("任务2结束了：", time.ctime())
# 定义主程序 在主程序中依次执行两个任务


def main():
    print("主函数开始了：", time.ctime())
    work1()
    work2()
    print("主函数结束了：", time.ctime())


# 执行主程序
main()

'''————————————————
版权声明：本文为CSDN博主「zuiziyoudexiao」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https: // blog.csdn.net/zuiziyoudexiao/article/details/86751660*'''
