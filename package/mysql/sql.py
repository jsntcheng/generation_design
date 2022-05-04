import re

import pymysql
import logging as log


class SqlAction():
    def __init__(self):
        try:
            self.database = pymysql.connect(host='101.35.49.209',
                                            user='root',
                                            password='543049601',
                                            database='Generation')
            self.cursor = self.database.cursor()
            self.cursor.execute('SELECT VERSION()')
            log.info('Database Version:', self.cursor.fetchone())
            log.info('数据库连接成功')
        except Exception as e:
            log.error('数据库连接失败')
            raise e

    def check_table_exist(self, table) -> None:
        '''
        判断表是否存在
        :param table: str 表名
        '''
        sql = "show tables"
        self.cursor.execute(sql)
        tables = self.cursor.fetchall()
        # print(tables)
        tables_list = re.findall('(\'.*?\')', str(tables))
        # print(tables_list)
        tables_list = [re.sub("'", '', each) for each in tables_list]
        # print(tables_list)
        if table not in tables_list:
            log.error(f'{table}不存在')
            raise Exception

    def checak_connection(self) -> None:
        '''
        确认连接未断开，否则重连
        '''
        self.database.ping()
        self.cursor = self.database.cursor()

    def inser_into_mysql(self, table, values, condition='') -> None:
        '''
        写入数据到数据库
        :param table: str 表名
        :param values: tuple 值
        :param condition: str 条件
        '''
        self.checak_connection()
        self.check_table_exist(table)
        if condition == '':
            sql = f"""INSERT INTO {table}
         VALUES {values}"""
        else:
            sql = f"""INSERT INTO {table}
            VALUES {values} WHERE {condition}"""
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.database.commit()
            log.info('写入数据库成功')
        except:
            # 如果发生错误则回滚
            self.database.rollback()
            log.error('写入数据库出错，已回滚')
            raise Exception
