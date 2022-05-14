import os
import time
import zipfile
from rpa import log
from datetime import datetime, date, timedelta

def get_date(form = "%Y-%m-%d", delta = 0):
    try:
        return (date.today() + timedelta(days = delta)).strftime(form)
    except Exception as e:
        log.error("获取时间错误，错误明细是", e)

def get_time(form = "%Y-%m-%d"):
    try:
        now_time = time.strftime(form, time.localtime())
        return now_time
    except Exception as e:
        log.error("获取今天时间错误，错误明细是", e)

def day_diff(time1, time2):
    """获取两个日期的相差天数"""
    try:
        time_array1 = time.strptime(time1, "%Y-%m-%d")
        timestamp_day1 = int(time.mktime(time_array1))
        time_array2 = time.strptime(time2, "%Y-%m-%d")
        timestamp_day2 = int(time.mktime(time_array2))
        result = (timestamp_day2 - timestamp_day1) // 60 // 60 // 24
        if result < 0:
            result = 0 - result
        return result
    except Exception as e:
        log.error(e)


def date_in_range(this_date, start_date, end_date):
    """判断一个日期是否在日期范围内"""
    try:
        if start_date == '' or start_date == ' ':
            start_date = '1971-1-1'
        if end_date == '' or end_date == ' ':
            end_date = '2050-1-1'
        big_arr = time.strptime(end_date, "%Y-%m-%d")
        big = int(time.mktime(big_arr))
        small_arr = time.strptime(start_date, "%Y-%m-%d")
        small = int(time.mktime(small_arr))
        now_arr = time.strptime(this_date, "%Y-%m-%d")
        now = int(time.mktime(now_arr))
        if now > big:
            return 'too new'
        if now < small:
            return 'too old'
        return 'in'
    except Exception as e:
        log.error(e)


def zip_files(work_path, save_name, filename=None, filespath=''):
    try:
        if filename is None:
            filename = []
        zp = zipfile.ZipFile(work_path + save_name, 'w', zipfile.ZIP_DEFLATED)
        if filespath != '':
            for path, dirnames, filenamess in os.walk(work_path + filespath):
                # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
                fpath = path.replace(work_path, '')
                for filenames in filenamess:
                    zp.write(os.path.join(path, filenames), os.path.join(fpath, filenames))
                # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        if filename:
            for i in filename:
                zp.write(os.path.join(work_path, i), os.path.join('', i))
        zp.close()
    except Exception as e:
        log.error(e)
