import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 查询除权除息信息####
# 查询2015年除权除息信息
rs_list = []
rs_dividend_2017 = bs.query_dividend_data(code="sz.000001", year="2017", yearType="report")
while (rs_dividend_2017.error_code == '0') & rs_dividend_2017.next():
    rs_list.append(rs_dividend_2017.get_row_data())

# 查询2016年除权除息信息
rs_dividend_2018 = bs.query_dividend_data(code="sz.000001", year="2018", yearType="report")
while (rs_dividend_2018.error_code == '0') & rs_dividend_2018.next():
    rs_list.append(rs_dividend_2018.get_row_data())

# 查询2017年除权除息信息
rs_dividend_2019 = bs.query_dividend_data(code="sz.000001", year="2019", yearType="report")
while (rs_dividend_2019.error_code == '0') & rs_dividend_2019.next():
    rs_list.append(rs_dividend_2019.get_row_data())

result_dividend = pd.DataFrame(rs_list, columns=rs_dividend_2019.fields)
# 打印输出
print(result_dividend)

#### 结果集输出到csv文件 ####
result_dividend.to_csv("D:\\history_Dividend_data.csv", encoding="gbk",index=False)

#### 登出系统 ####
bs.logout()
