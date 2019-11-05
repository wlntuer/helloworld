
def f(n):
    list = []
    for i in range(2, n + 1):
        for j in range(2, int(i / 2)):
            if i % j == 0 and j <= (i / j):
                list.append(j)
                list.append(i / j)
        if sum(list) + 1 == i:
            print(i)
        list = []
n = 56789
f(n)
