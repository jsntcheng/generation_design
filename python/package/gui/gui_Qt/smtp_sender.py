import os
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import *


class SMTPSender:
    """邮件通知"""
    _instance = None

    @classmethod
    def get_instance(cls):
        """单例模式"""
        if SMTPSender._instance is None:
            SMTPSender._instance = SMTPSender()
        return SMTPSender._instance

    def __init__(self):
        self.message = None
        self.client = None
        self.use_ssl = Config.get_instance().get_email_base_info().get('user_ssl', '')
        self._connect()
        self._login()

    def __del__(self):
        try:
            if self.client:
                self.client.quit()
                self.client = None
        except:
            pass

    def _connect(self):
        """连接服务器"""
        mail_base_info = Config.get_instance().get_email_base_info()

        if self.use_ssl:
            self.client = smtplib.SMTP_SSL(mail_base_info['address'], mail_base_info['port'])
        else:
            self.client = smtplib.SMTP(mail_base_info['address'], mail_base_info['port'])

        try:
            # outlook 需要starttls 否则无法发送邮件  其他的不需要
            self.client.starttls()
        except:
            pass

    def _login(self):
        """登录邮箱"""
        mail_base_info = Config.get_instance().get_email_base_info()
        self.user = mail_base_info['user']
        self.client.login(mail_base_info['user'], mail_base_info['password'])

    def set_smtp_header(self, sender, receivers, subject, cc=[], bcc=[]):
        """设置协议头"""
        self.message['From'] = sender
        self.message['To'] = Header(','.join(receivers))
        self.message['Subject'] = Header(subject)
        self.message['Cc'] = Header(','.join(cc))
        self.message['Bcc'] = Header(','.join(bcc))

    def set_smtp_content(self, content, content_type, encoding):
        """设置正文内容"""
        alternative = MIMEMultipart('alternative')
        text_html = MIMEText(content, _subtype=content_type, _charset=encoding)
        alternative.attach(text_html)
        self.message.attach(alternative)

    def set_smtp_attachment(self, filepath, display_name=None):
        """设置单个附件"""
        attachment = MIMEApplication(open(filepath, 'rb').read())
        attachment.add_header("Content-Type", 'application/octet-stream')
        if display_name is None:
            display_name = os.path.basename(filepath)
        attachment.add_header('Content-Disposition', 'attachment', filename=Header(display_name).encode())
        self.message.attach(attachment)

    def set_smtp_attachments(self, filepaths, display_names=None):
        """设置附件"""
        for i in range(len(filepaths)):
            filepath = filepaths[i]
            display_name = display_names[i] if display_names else None
            self.set_smtp_attachment(filepath, display_name)

    def create_smtp_message(self,
                            receivers,
                            cc=[],
                            bcc=[],
                            subject="",
                            content=None,
                            content_type='utf-8',
                            file_paths=[],
                            display_names=[]):
        """构造邮箱报文"""
        self.message = MIMEMultipart('mixed')
        self.set_smtp_header(self.user, receivers, subject, cc, bcc)
        if content:
            self.set_smtp_content(content, 'html', content_type)
        if file_paths:
            self.set_smtp_attachments(file_paths, display_names)

    def send_mail(self, content):
        """发送 邮件  subject、recipient、content 属于必填项
            content:{
            'subject': '*标题',
            'recipient': ['*收件人邮箱1', '收件人邮箱2'],
            'cc': ['抄送邮箱1'， ’抄送邮箱2‘],
            'bcc': ['密送邮箱1', '密送邮箱2'],
            'content': '*正文  支持html',
            'filenames': ['文件路径列表']
            }
        """
        mail_base_info = Config.get_instance().get_email_base_info()
        cc = content.get('cc', [])
        bcc = content.get('bcc', [])
        receivers = content['recipient']

        self.create_smtp_message(receivers=receivers,
                                 cc=cc,
                                 bcc=bcc,
                                 subject=content['subject'],
                                 content=content['content'],
                                 file_paths=content.get('filenames', []))
        self.client.sendmail(mail_base_info['user'], receivers + cc + bcc, self.message.as_string())


if __name__ == '__main__':
    SMTPSender.get_instance().send_mail({
        'subject': '测试邮箱标题',
        'recipient': ['694625452@qq.com'],
        'content': '测试邮件正文'
    })
