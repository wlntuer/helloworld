import  math
def isprime(n): #判断素数
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i == 0:
                return False
        return True
 
def thonsand(n) : #生成若干个素数，返回素数list
    a = []
    for i in range(1,n+1):
        if isprime(i):
            a.append(i)
    return a
"""利用前面的两个函数生成n范围内的素数列表
两层for循环，两个迭代变量之和如果等于参数n就加入列表中
循环完所有的情况后返回列表，并打印输出。
"""
def gdbh(n): 
    a =[]
    ls = thonsand(n)
    for i in ls:
        for j in ls:
            if n == i+j:
                a.append(i)
                a.append(j)
    return a
                
ls2 = gdbh(12)
ls3 = gdbh(152)
print(ls2)
print(ls3)
'''————————————————
版权声明：本文为CSDN博主「bingoCoder」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/bingocoder/article/details/80384633'''