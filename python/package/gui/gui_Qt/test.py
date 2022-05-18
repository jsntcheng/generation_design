#code
import os

temp_file = open('temp.py', 'w', encoding='gbk')
temp_file.write('print("hello world")')
path = os.path.dirname(__file__)
import os
path2 = path
path.strip('package\gui\gui_Qt')
os.system('cd '+path2)
os.system(path + ' python' +' test.py')