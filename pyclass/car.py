class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):   # 返回汽车的描述信息
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):    # 打印汽车的里程
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):     # 更新汽车的里程
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):    # 增加汽车里程
        self.odometer_reading += miles


'''————————————————
版权声明：本文为CSDN博主「不睡觉的怪叔叔」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_35732147/article/details/83084774'''


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")


class ElectricCar(Car):     # 必须在括号内指定父类的名称
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):      # 接受创建Car实例所需的信息
        """初始化父类的属性"""
        super().__init__(make, model, year)     # 帮助Python将父类和子类关联起来
        self.battery = Battery()         # 将实例用作属性


my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
