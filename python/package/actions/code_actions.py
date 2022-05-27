from time import sleep
def create_mem(info):
    '''
    新建变量
    :param info:变量初始化内容
    :return:
    '''
    return info

def print_mem(mem):
    '''
    打印变量
    :param mem:变量名
    :return:
    '''
    print(mem)

def set_value(info):
    '''
    赋值操作
    :param info: 赋值内容
    :return:
    '''
    return info

def sleep_time(second):
    '''
    延迟执行
    :param second: 秒数
    :return:
    '''
    sleep(second)
# def get_doc(func):
#     '''
#     获取方法内的说明文字
#     :param func: 方法
#     :return: str 说明文字
#     '''
#     txt_dict = {'create_mem':create_mem.__doc__.split('\n    '),
#                 'print_mem':print_mem.__doc__.split('\n    '),
#                 'set_value':set_value.__doc__.split('\n    '),
#                 'get_doc':get_doc.__doc__.split('\n    ')
#                 }
#     temp_list = txt_dict[func]
#     result = ""
#     for i in temp_list:
#         if i[0:6] == ':param':
#             result += i.replace(':param ','')+'  '
#     return result