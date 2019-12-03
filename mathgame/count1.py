import math
while (1):
    print('请输入一个正整数(如果需要结束，请输入0):')
    a = input()
    a = int(float(a))
    b = a  # 记录原始值
    i = 0
    while(1):
        if (a % 2 == 1):
            i = i+1
        a = math.floor(a/2)
        if (a <= 0):
            break
    print('%d 的2进制中1的个数是 %d' % (b, i))  # 打印带参数的格式1
    if (b == 0):
        break
print('输入为0，程序结束')
