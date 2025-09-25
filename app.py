name="传智播客"
stock_price=19.99
stock_code="003032"
stock_price_daily_growth_factor=1.2
growth_days=7
print(f"公司:{name},股票代码:{stock_code},当前股价:{stock_price}")
print("每日增长系数是:%.1f,经过%d天增长后,股价达到%.2f"%(stock_price_daily_growth_factor,growth_days,stock_price*stock_price_daily_growth_factor**growth_days))
name=input("hello world\n")
print(name)
a='1'
b='1'
print(a==b)