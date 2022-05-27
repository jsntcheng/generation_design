import xlwings as xw

def open_excel(path):
    '''
    打开excel
    :param path:文件路径
    :return: excel 对象
    '''
    return xw.Book(path)

def create_excel(name,path):
    '''
    新建excel
    :param name:文件名
    :param path: 保存路径
    :return: excel 对象
    '''
    app = xw.App(visible=False, add_book=False)
    workbook = app.books.add()  # 新建工作簿
    workbook.save(path+'\\'+name+'.xlsx')  # 保存工作簿
    return workbook

def save_excel(excel,name,path):
    '''
    保存excel
    :param excel:excel 对象
    :param name: 文件名（不带.xlsx)
    :param path: 保存路径
    :return
    '''
    excel.save(path+'\\'+name+'.xlsx')

def create_sheet(excel,name):
    '''
    新建Sheet页
    :param excel:excel 对象
    :param name: Sheet 名称
    :return: excel 对象
    '''
    excel.sheets.add(name)
    excel.save(excel.fullname)
    return excel

def del_sheet(excel,sheet):
    '''
    删除Sheet页
    :param excel:excel 对象
    :param sheet: 需要删除的Sheet名称
    :return: excel 对象
    '''
    for i in excel.sheets:
        if i.name == sheet:
            i.delete()
    excel.save(excel.fullname)
    return excel

def merge_cells(excel,start,end,sheet = 1):
    '''
    合并单元格
    :param excel:excel 对象
    :param start: 起始位置
    :param end: 结束位置
    :param sheet: 第几张工作簿(默认为当前)
    :return
    '''
    sht = excel.sheets[sheet-1]
    sht.range(start+":"+end).api.merge()

def insert_into_excel(excel,cell,data,sheet = 1):
    '''
    excel写入数据
    :param excel: excel 对象
    :param cell: 写入位置
    :param data: 写入数据
    :param sheet: 第几张工作簿(默认为当前)
    :return:
    '''
    sht = excel.sheets[sheet-1]
    sht.range(cell).value = data
    excel.save(excel.fullname)

def read_excel(excel,start,end,sheet = 1):
    '''
    excel读取数据
    :param excel: excel 对象
    :param start: 起始位置
    :param end: 结束位置
    :param sheet: 第几张工作簿(默认为当前)
    :return:读取到的数据
    '''
    sht = excel.sheets[sheet-1]
    return sht.range(start+':'+end).value

def color_cell(excel,cell,color,sheet = 1):
    '''
    excel写入数据
    :param excel: excel 对象
    :param cell: 操作位置
    :param color: 颜色
    :param sheet: 第几张工作簿(默认为当前)
    :return:
    '''
    sht = excel.sheets[sheet-1]
    sht.range(cell).color = color
    excel.save(excel.fullname)

# def get_doc(func):
#     '''
#     获取方法内的说明文字
#     :param func: 方法
#     :return: str 说明文字
#     '''
#     txt_dict = {'open_excel':open_excel.__doc__.split('\n    '),
#                 'create_excel':create_excel.__doc__.split('\n    '),
#                 'save_excel':save_excel.__doc__.split('\n    '),
#                 'create_sheet':create_sheet.__doc__.split('\n    '),
#                 'del_sheet':del_sheet.__doc__.split('\n    '),
#                 'merge_cells':merge_cells.__doc__.split('\n    '),
#                 'insert_into_excel':insert_into_excel.__doc__.split('\n    '),
#                 'read_excel':read_excel.__doc__.split('\n    '),
#                 'color_cell':color_cell.__doc__.split('\n    ')
#                 }
#     temp_list = txt_dict[func]
#     result = ""
#     for i in temp_list:
#         if i[0:6] == ':param':
#             result += i.replace(':param ','')+'  '
#     return result
if __name__ == '__main__':
    wb = create_excel('test1','D://')
    create_sheet(wb,'tt')