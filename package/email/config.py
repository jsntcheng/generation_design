import json
from constant import *


class Config:
    __instance = None

    @classmethod
    def get_instance(cls):
        if Config.__instance is None:
            Config.__instance = Config()
        return Config.__instance

    def __init__(self):
        self.data = {}
        # try:
        #     with open(CONFIG_PATH, 'rb') as f:
        #         self.data = json.loads(f.read())
        # except Exception as e:
        #     raise Exception(f'配置文件内容错误，请核对\n{e}')

    def get_email_base_info(self):
        return self.data.get('邮箱信息', DEFAULT_MAIL_INFO)
