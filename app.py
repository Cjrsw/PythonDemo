"""
精度案例
"""
# name="传智播客"
# stock_price=19.99
# stock_code="003032"
# stock_price_daily_growth_factor=1.2
# growth_days=7
# print(f"公司:{name},股票代码:{stock_code},当前股价:{stock_price}")
# print("每日增长系数是:%.1f,经过%d天增长后,股价达到%.2f"%(stock_price_daily_growth_factor,growth_days,stock_price*stock_price_daily_growth_factor**growth_days))

"""
输入注释
"""
# name=input("hello world\n")
# print(name)

"""
==比较值
is比较地址
"""
# a='1'
# b='1'
# print(a==b)


"""
条件判断案例
"""
# high=int(input("欢迎来到黑马动物园\n请输入身高(cm):"))
# if high>=120:
#     print("您的身高超出120cm,游玩需要购票10元\n祝您购票愉快")
# else:
#     print("您的身高低于120cm,可以免费游玩\n祝您游玩愉快")

# import random
# num=random.randint(1,10)
# print(num)
# num1=int(input("请输入1-10的数字:"))
# if num1==num:
#     print("恭喜你猜对了")
# else:
#     if num1>num:
#         print("猜的数字太大")
#     elif num1<num:
#         print("猜的数字太小")
#     num1 = int(input("请输入1-10的数字:"))
#     if num1 == num:
#         print("恭喜你猜对了")
#     else:
#         if num1 > num:
#             print("猜的数字太大")
#         elif num1 < num:
#             print("猜的数字太小")
#         num1 = int(input("请输入1-10的数字:"))
#         if num1 == num:
#                 print("恭喜你猜对了")
#         else:
#             print("游戏失败")


"""
循环案例
"""

# import random
# num=random.randint(1,100)
# nums=int(input("请输入1-100的数字:"))
# i=0
# while nums!=num:
#     if nums>num:
#         print("猜的数字太大")
#     elif nums<num:
#         print("猜的数字太小")
#     nums=int(input("请输入1-100的数字:"))
#     i+=1
# print(f"恭喜你花了{i+1}次答对了")


"""
九九乘法表
"""

# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print(f"{j}*{i}={i*j}\t",end='')
#         j+=1
#     print()
#     i+=1

"""
for案例
"""
# i=0
# for x in "itheima is a brand of itcast":
#     if x=='a':
#         i=i+1
# print(i)

"""
range案例
"""

# num=int(input("请输入一个整数"))
# x=0
# for i in range(1,num):
#     if i%2==0:
#         x=x+1
# print(x)

"""
循环综合案例
"""
# import random
# all_money=10000
# for i in range(1,21):
#     if all_money<=0:
#         break
#     else:
#         x=random.randint(1,10)
#         if x<5:
#             print(f"员工{i},绩效{x}分，低于5分,不发工资,下一位")
#             continue
#         else:
#             all_money=all_money-1000
#             print(f"向员工{i}发放工资1000元，账户余额还剩余{all_money}元")
# print("工资发完了下个月领取吧")

"""
类案例
"""
# class Clock:
#     id=None
#     price=None
#     def ring(self):
#         import winsound
#         winsound.Beep(2000,3000)
# clock_1=Clock()
# clock_1.id=1
# clock_1.price=100
# print(clock_1.id)
# print(clock_1.price)
# clock_1.ring()
# clock_2=Clock()
# print(clock_2.id)
# print(clock_2.price)
# clock_2.ring()

"""
魔术方法案例
"""
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     # __str__魔术方法
#     def __str__(self):
#         return f"Name:{self.name},Age:{self.age}"
#     # __lt__魔术方法
#     def __lt__(self, other):
#         return self.age<other.age
#     # __le__魔术方法
#     def __le__(self,other):
#         return self.age<=other.age
#     # __eq__魔术方法
#     def __eq__(self,other):
#         return self.age==other.age
# #__str__魔术方法
# stu=Student("cjr", 18)
# print(stu)
# print(str(stu))#输出内存地址
# # __lt__魔术方法
# stu1=Student("cjr", 10)
# stu2=Student("cjr", 1)
# print(stu1<stu2)
# print(stu1>stu2)
# # __le__魔术方法
# print(stu1>=stu2)
# print(stu1<=stu2)
# # __eq__魔术方法
# print(stu1==stu2)


"""
封装案例
"""
# class Phone:
#     __is_5g_enable=False
#     def __check_5g(self):
#         if self.__is_5g_enable:
#             print("5g开启")
#         else:
#             print("5g关闭,使用4g网络")
#     def call_by_5g(self):
#         self.__check_5g()
#         print("正在通话中")
#     def __init__(self,is_5g):
#         self.__is_5g_enable = is_5g
# phone=Phone(True)
# phone.call_by_5g()

"""
多态案例
"""
# class Animal:
#     def speak(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         print("汪汪")
# class Cat(Animal):
#     def speak(self):
#         print("喵喵")
# def make_noise(animal:Animal):
#     animal.speak()
# dog = Dog()
# make_noise(dog)
# cat = Cat()
# cat.speak()

"""
函数条件变量作用域
"""
# c=1
# def a():
#     b=2
#     global c
#     c=3
#     print(b,c)
#     return b
# print(c)
# a()
# print(c)

### 函数案例
# money=0
# def find():
#     print(money)
# def get():
#     gets=int(input("请输入取款金额"))
#     global money
#     money-=gets
#     print(f"周杰伦你好，您取款{gets}成功\n您的余额剩余{money}")
# def put():
#     puts=int(input("请输入存款金额"))
#     global money
#     money+=puts
#     print(f"周杰伦你好，您存款{puts}成功\n您的余额剩余{money}")
#
# print("-----------------主菜单-----------------")
# print("周杰伦，你好，欢迎来到黑马银行ATM，请选择操作：\n查询余额\t[输入1]\n存款\t\t[输入2]\n取款\t\t[输入3]\n退出\t\t[输入4]\n请输入你的选择：")
# src=int(input())
# while(src!=4):
#     if src==1:
#         find()
#     elif src==2:
#         put()
#     elif src==3:
#         get()
#     else:
#         break
#     src=int(input())
# print("已退出")


#循环定义列表
list1=[]
index=0
while index<len(list1):
    print(list1[index])
    index+=1
for i in list1:
    print(i)
#for 临时变量 in 数据容器
#    对临时变量进行处理
#差别：for不能自定义循环条件，无限循环，while可以