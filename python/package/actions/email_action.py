from python.package.email.smtp_sender import SMTPSender


def send_emails(to_address,data,title = 'RPA自动化系统',file=None):
    '''
    发送邮件
    :param to_address: 接收方邮箱列表
    :param data: 邮件内容
    :param title: 主题
    :param file: 附件文件路径列表
    :return:
    '''
    if file:
        SMTPSender.get_instance().send_mail({
            'subject': title,
            'recipient': to_address,
            'content': data,
            'filenames': file
        })
    else:
        SMTPSender.get_instance().send_mail({
            'subject': title,
            'recipient': to_address,
            'content': data
        })
# def get_doc(func):
#     '''
#     获取方法内的说明文字
#     :param func: 方法
#     :return: str 说明文字
#     '''
#     txt_dict = {'send_email':send_email.__doc__.split('\n    ')
#                 }
#     temp_list = txt_dict[func]
#     result = ""
#     for i in temp_list:
#         if i[0:6] == ':param':
#             result += i.replace(':param ','')+'  '
#     return result

if __name__ == '__main__':
    send_emails(['694625452@qq.com'],'测试',file=['D:/test1.xlsx'])
