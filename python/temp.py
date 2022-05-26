#coding:utf-8
from actions.web_actions import *
from actions.excel_actions import *
#启动浏览器
driver=create_browser('https://www.baidu.com')

#切换操作页面
switch_page(driver,2)

#刷新页面
refresh_page(driver)

#获取所有元素
elements=get_all_element(driver,'//*/)

#关闭浏览器
close_browser(driver)

#打开Excel文件
book=open_excel('D://test1,xlsx')

#写入内容
insert_into_excel(book,'A1','hhh')
