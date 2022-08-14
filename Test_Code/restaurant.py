'''
类和函数的知识点，首先只要定义了类和函数，就用空两行，然后类的名字首字母大写，函数与变量都小写
初始化必须有，初始化是一个函数
方法用到属性，变量添加self
构造函数是两条下划线
不管有没有参数self必须给
'''


class Restaurant():

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuision_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuision_type)

    def open_restaurant(self):
        print("\n")
         
    def set_number(self, number_served):
        self.number_served = number_served


german_restaurant = Restaurant('german', 'germany', 10)
german_restaurant.describe_restaurant()
