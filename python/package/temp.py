import time

import os

from actions.web_actions import *


#启动浏览器
driver=create_browser('https://www.baidu.com')

#设置输入框
set_input(driver,'//*[@id="kw"]','中国天气网')

#点击元素
click_element(driver,'//*[@id="su"]')


time.sleep(5)
close_browser(driver)