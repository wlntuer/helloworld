# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(host='localhost', user='wlntuer',
                               password='123456', database='world', auth_plugin='mysql_native_password')
cursor = conn.cursor()
# 创建user表:
cursor.execute(
    'create table if not exists user  (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)',
               ['121111', 'Michael'])
cursor.rowcount

# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('121111',))
values = cursor.fetchall()
print('results:')
print(values)  # [('1', 'Michael')]
# 关闭Cursor和Connection:
cursor.close()
conn.close()  # 记得正确关闭
