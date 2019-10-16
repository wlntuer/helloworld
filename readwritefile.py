# 生成 数组
list = [i * 11 for i in range(1,6)]
print(list)

# 写入数组到文件
file_name = 'listdata.dat'
file = open(file_name, 'w')
file.write(str(list))
file.close()

print("-------------------------")

# 从文件中读取数组
file = open(file_name, 'r')
print(file.readline())
file.close()