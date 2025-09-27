# name="传智播客"
# stock_price=19.99
# stock_code="003032"
# stock_price_daily_growth_factor=1.2
# growth_days=7
# print(f"公司:{name},股票代码:{stock_code},当前股价:{stock_price}")
# print("每日增长系数是:%.1f,经过%d天增长后,股价达到%.2f"%(stock_price_daily_growth_factor,growth_days,stock_price*stock_price_daily_growth_factor**growth_days))


# name=input("hello world\n")
# print(name)


# a='1'
# b='1'
# print(a==b)



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

import random
num=random.randint(1,100)
nums=int(input("请输入1-100的数字:"))
i=0
while nums!=num:
    if nums>num:
        print("猜的数字太大")
    elif nums<num:
        print("猜的数字太小")
    nums=int(input("请输入1-100的数字:"))
    i+=1
print(f"恭喜你花了{i+1}次答对了")

