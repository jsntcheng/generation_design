#coding:utf-8
from actions.web_actions import *
from time import sleep
#Æô¶¯ä¯ÀÀÆ÷
dd=create_browser('https://www.baidu.com')
sleep(5)
#¹Ø±Õä¯ÀÀÆ÷
close_browser(dd)
