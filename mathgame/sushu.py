from math import sqrt
#定义素数判断函数
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
#for循环输出素数 
for i in range(1, 100):
    if is_prime(i):
        print(i)
'''————————————————
版权声明：本文为CSDN博主「Fireman1994」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fireman1994/article/details/78491523'''