import time
import threading


def fun():
    print("子线程开始执行")
    time.sleep(4)
    print("子线程执行完毕")


print("主线程开始执行")

# 执行守护线程
t = threading.Thread(target=fun, args=())
t.start()

# 主线程休眠两秒
time.sleep(2)
print("主线程执行结束")
'''————————————————
版权声明：本文为CSDN博主「zuiziyoudexiao」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/zuiziyoudexiao/article/details/86751660'''
