#coding:utf-8
from actions.web_actions import *
from actions.excel_actions import *
from actions.email_action import *
from actions.code_actions import *
#启动浏览器
browser=create_browser('http://www.weather.com.cn/')

#点击元素
click_element(browser,'//*[@id="txtZip"]')

#设置输入框
set_input(browser,'//*[@id="txtZip"]','shanghai')

#点击元素
click_element(browser,'//*[@id="txtZip"]')

#延迟执行
sleep_time(1)

#点击元素
click_element(browser,'//*[@id="show"]/ul/li')

#延迟执行
sleep_time(1)

#切换操作页面
switch_page(browser,2)

#点击元素
click_element(browser,'//*[@id="someDayNav"]/li[2]/a')

#获取元素内文字
weather=get_element_txt(browser,'//*[@id="7d"]/ul/li[1]')

#打印变量
print_mem(weather)

#发送邮件
send_emails(['694625452@qq.com'],weather,'shanghai_weather')

#关闭浏览器
close_browser(browser)
