from time import sleep

import keyboard
from rpa import excel
from rpa.ui.browser.browser import WebBrowser, BrowserType
from rpa.ui.element.element import *

# ********************


timeout_default = 10


# ********************
def find_key_in_dict(dict1, value):
    dic_key = list(dict1.keys())
    dic_value = list(dict1.values())
    for i in range(len(dic_value)):
        if dic_value[i] == value:
            return dic_key[i]
    raise Exception("字典中找不到对应值")


# 获取路径下保存的元素selector表
def get_ele_dict(path, name='元素.xlsx') -> dict:
    """获取路径下保存的元素selector表.
    Args:
        path: str 文件路径
        name: str 表名
    Returns:
        一个元素名称与selector的字典
        """
    try:
        tem_excel = excel.open(path + name)
        tem_sheet = tem_excel.get_sheet()
        ele_name = tem_sheet.read('A', skip=1)
        ele_selector = tem_sheet.read('B', skip=1)
        ele_start_by = tem_sheet.read('C', skip=1)
        tem_excel.close()
        tem_dic = {}
        for x in range(len(ele_name)):
            if ele_start_by[x] == '':
                ele_start_by[x] = '当前页面'
            if ele_selector[x] == '':
                log.warning('selector为空')
            inner_dict = {'selector': ele_selector[x], '父节点名称': ele_start_by[x]}
            tem_dic[ele_name[x]] = inner_dict
        return tem_dic
    except Exception as e:
        log.error("[%s] %s", "获取路径下保存的元素selector表", str(e))
        raise e


# 获取浏览器类型
def get_browser_type(str1) -> (str, object):
    """获取浏览器类型
    Args:
        str1: str 浏览器类型
    Returns:
        '不同浏览器专属的页面selector',WebBrowser
    Raises:
        未知的浏览器
        """
    if str1 == 'chrome' or str1 == 'Chrome':
        return ':scope > Pane[name="{} - Google Chrome"]', BrowserType.Chrome
    elif str1 == 'ie' or str1 == 'Ie' or str1 == 'IE':
        return ':scope > Window[name="{} - Internet Explorer"]', BrowserType.IE
    elif str1 == 'firefox' or str1 == 'Firefox':
        return ':scope > Window[name="{} — Mozilla Firefox"]', BrowserType.Firefox
    else:
        log.error('未知的浏览器类型')
        raise '未知的浏览器类型'


# 页面操作(快速模式)，需要完整selector
class WebAction:
    """基于UI的网页操作专用类（快速模式）
    Attributes:
        opened_pages: {页码:WebPage对象} 用于保存已经打开的页面
        ele_dict: {元素名称:{'selector':, '父节点名称':}} 自定义元素名称与selector以及父节点名称的字典
        browser_selector: str 不同浏览器窗口对应的selector
        browser_type: BrowserType 浏览器类型
        web_browser: WebBrowser 浏览器对象
        current_page: WebPage对象 当前操作页面
    """

    def __init__(self, url, path='', ele_dic=None, ele_dic_name='元素.xlsx', browser_type='chrome', launch_args="",
                 exe_path=""):
        """初始化，通常情况下，只需要传入元素.xlsx所在的路径path以及打开的网页url即可"""
        self.opened_pages = {}
        if not path == '':
            self.ele_dict = get_ele_dict(path, ele_dic_name)
        else:
            self.ele_dict = ele_dic
        self.browser_selector, self.browser_type = get_browser_type(browser_type)
        self.web_browser = WebBrowser.open_browser(self.browser_type, url, launch_args, exe_path)
        sleep(1)
        self.current_page = self.web_browser.get_current_page()
        self.opened_pages[len(self.opened_pages) + 1] = self.current_page

    # 去新的地址
    def to_new_url(self, url, is_new_page=True, is_wait_page_load=True) -> None:
        """去新的地址
        Args:
            url: str 将要去往的地址
            is_new_page: bool 是否打开个新页面
            is_wait_page_load: bool 是否等待网页加载完成
        """
        try:
            # 获取当前操作页
            page_num = find_key_in_dict(self.opened_pages, self.current_page)
            # 打开网页
            self.web_browser.open_page(is_new_page, url, is_wait_page_load)
            self.current_page = self.web_browser.get_current_page()
            if is_new_page:
                self.opened_pages[len(self.opened_pages) + 1] = self.current_page
            else:
                self.opened_pages[page_num] = self.current_page
            # log.debug('已去新的地址，新页面:{},等待网页加载完成:{},网页url:{}'.format(is_new_page, is_wait_page_load, url))
        except Exception as e:
            raise e

    # 关闭页面
    def close_page(self, page_num=0) -> None:
        """关闭页面
        Args:
            page_num: int 需要关闭哪个页面
        """
        # 默认关闭当前操作页面
        try:
            if page_num == 0:
                page_num = find_key_in_dict(self.opened_pages, self.current_page)
            # 关闭页面
            self.opened_pages[page_num].close_page()
            log.debug('已关闭第%d页', page_num)
            # 对已打开页面字典进行删减
            for i in range(page_num, len(self.opened_pages)):
                self.opened_pages[i] = self.opened_pages[i + 1]
            # 当前操作页面更新
            if page_num == len(self.opened_pages):
                page_num -= 1
            self.current_page = self.opened_pages[page_num]
            del self.opened_pages[len(self.opened_pages)]
            log.debug('当前正在操作第%d页', page_num)
        except Exception as e:
            log.error("[%s] %s", "关闭页面", str(e))
            raise e

    # 关闭浏览器
    def close_browser(self):
        self.web_browser.close_browser()

    # 切换操作网页
    def switch_page(self, page_num) -> None:
        """切换操作网页
        Args:
            page_num: 切换到第几个页面
            """
        try:
            self.opened_pages[page_num].switch_page()
            self.current_page = self.opened_pages[page_num]
            log.debug('已切换到第%d页', page_num)
        except Exception as e:
            log.error("[%s] %s", "切换操作网页", str(e))
            raise e

    # 点击元素
    def click_element(self, name, start_ele=None, click_type='message', timeout=timeout_default,
                      click_count=1, click_wait=1, click_button='left') -> None:
        """点击元素
        Args:
            name: str 需要点击的元素名称
            start_ele: UiElement 在哪个元素里遍历
            click_type: str 点击类型，message-系统消息，mouse-模拟鼠标
            timeout: int 超时计时
            click_count: int 点击次数
            click_wait: int 每次点击后等待的秒数
            click_button: str 模拟鼠标点击的按键,left;middle;right
            """
        try:
            # 如果为链接，则打开新网页
            try:
                url = self.run_js(name, '(target, kwargs) => {return target.href}')
                # 直接在当前页面转到新网页
                self.to_new_url(url, False)
            except Exception as e:
                log.debug('[%s无超链接] %s', name, str(e))
            # 普通点击，再根据点击类型作出不同动作
            if click_type == 'mouse':
                for i in range(click_count):
                    ele = wait_element(selector=self.ele_dict[name]['selector'], start_element=start_ele,
                                       timeout=timeout)
                    ele.click(button=click_button)
                    sleep(click_wait)
                    log.debug('已经点击%d次', i + 1)
            elif click_type == 'message':
                for i in range(click_count):
                    ele = wait_element(selector=self.ele_dict[name]['selector'], start_element=start_ele,
                                       timeout=timeout)
                    ele.invoke()
                    sleep(click_wait)
                    log.debug('已经点击%d次', i + 1)
            else:
                log.error('未知的click_type')
                raise '未知的click_type'
        except Exception as e:
            log.error("[%s] %s", "点击元素", str(e))
            raise e

    def wait_one_element(self, name, start_ele=None, timeout=timeout_default):
        return wait_element(self.ele_dict[name]['selector'], start_ele, timeout)

    # 获取同selector所有元素
    def get_all_element(self, name, start_ele=None, timeout=timeout_default) -> list:
        """获取同selector所有元素
                Args:
                    name: str 元素名称
                    start_ele: UiElement 父节点
                    timeout: int 超时计时
                Returns:
                    list
                """
        return query_element_all(self.ele_dict[name]['selector'], start_ele, timeout)

    def get_element_innerText(self, name, start_ele=None, timeout=timeout_default) -> str:
        script = "\r\n".join(['(target, kwargs) => {',
                              '  return {"res": target.innerText}'
                              '}', ])
        return self.current_page.run_script(self.ele_dict[name]['selector'], script, {})['res']

    # 获取输入框文本
    def get_input_box_text(self, name, start_ele=None, timeout=timeout_default) -> str:
        """获取输入框文本
        Args:
            name: str 元素名称
            start_ele: UiElement 父节点
            timeout: int 超时计时
        Returns:
            str 输入框文本
        """
        try:
            return wait_element(self.ele_dict[name]['selector'], start_ele, timeout).get_text()
        except Exception as e:
            log.error("[%s] %s", "获取输入框文本", str(e))
            raise e

    # 获取表格
    def get_table(self, name, start_ele=None, attr='name', transpose=False, timeout=timeout_default) -> list:
        """获取表格
        Args:
            name: str 表格元素名称
            start_ele: UiElement 父节点
            attr: str Object对象存内容的属性
            transpose: bool 是否转置结果
            timeout: int 超时计时
        Returns:
            一个存有表格的列表
            """
        try:
            return wait_element(self.ele_dict[name]['selector'], start_ele, timeout).get_grid_all_elements(attr,
                                                                                                           transpose)
        except Exception as e:
            log.error("[%s] %s", "获取表格", str(e))
            raise e

    def get_table2(self, name):
        script = "\r\n".join(['(target, kwargs) => {',
                              '  // Add your JavaScript here:',
                              '  // return your object to python;',
                              'function getTableContent(id){',
                              '    var mytable = id;',
                              '    var data = [];',
                              '    for(var i=0,rows=mytable.rows.length; i<rows; i++){',
                              '        for(var j=0,cells=mytable.rows[i].cells.length; j<cells; j++){',
                              '            if(!data[i]){',
                              '                data[i] = new Array();',
                              '            }',
                              '            data[i][j] = mytable.rows[i].cells[j].innerHTML;',
                              '        }',
                              '    }',
                              '    return data;',
                              '}',
                              'return {"res": getTableContent(target)}',
                              '}', ])
        return self.current_page.run_script(self.ele_dict[name]['selector'], script, {})['res']

    # 获取元素属性
    def get_ele_attr(self, name, attr, start_ele=None, timeout=timeout_default) -> str:
        """获取元素属性
        Args:
            name: str 元素名称
            attr: str 需要获取的属性
            start_ele: UiElement 父节点
            timeout: int 超时计时
        Returns:
            元素属性值(str)
        """
        try:
            return wait_element(self.ele_dict[name]['selector'], start_ele, timeout).get(attribute=attr)
        except Exception as e:
            log.error("[%s] %s", "获取元素属性", str(e))
            raise e

    # 获取复选框状态
    def get_toggle_state(self, name, start_ele=None, timeout=timeout_default) -> str:
        """获取元素复选框状态
        Args:
            name: str 元素名称
            start_ele: UiElement 父节点
            timeout: int 超时计时
        Returns:
            str 状态
        """
        try:
            return wait_element(self.ele_dict[name]['selector'], start_ele, timeout).get_toggle_state()
        except Exception as e:
            log.error("[%s] %s", "获取元素复选框状态", str(e))
            raise e

    # 获取元素选中项
    def get_ele_selection(self, name, start_ele=None, timeout=timeout_default) -> list:
        """获取元素选中项
        Args:
            name: str 元素名称
            start_ele: UiElement 父节点
            timeout: int 超时计时
        Returns:
            [UiElement]
        """
        try:
            return wait_element(self.ele_dict[name]['selector'], start_ele, timeout).get_selection()
        except Exception as e:
            log.error("[%s] %s", "获取元素选中项", str(e))
            raise e

    # 获取元素选中状态
    def get_ele_is_selected(self, name, start_ele=None, timeout=timeout_default) -> bool:
        """获取元素选中状态
        Args:
            name: str 元素名称
            start_ele: UiElement 父节点
            timeout: int 超时计时
        Returns:
            bool
        """
        try:
            return wait_element(self.ele_dict[name]['selector'], start_ele, timeout).get_is_selected()
        except Exception as e:
            log.error("[%s] %s", "获取元素选中状态", str(e))
            raise e

    # 设置输入框文本
    def set_input_box_text(self, name, input_text, set_type='message', click_before_input=True,
                           start_ele=None, timeout=timeout_default) -> None:
        """设置输入框文本
        Args:
            name: str 元素名称
            input_text: str 设置的文本
            set_type: str 输入方式 message-系统消息 keyboard-模拟键盘
            click_before_input: bool 输入前是否调用鼠标点击
            start_ele: UiElement 在哪个元素里遍历
            timeout: int 超时计时
        """
        try:
            if set_type == 'message':
                return wait_element(self.ele_dict[name]['selector'], start_ele, timeout).set_text(text=input_text)
            elif set_type == 'keyboard':
                if click_before_input:
                    self.click_element(name, start_ele)
                keyboard.write(input_text)
            log.debug("已通过{}方法向{}中输入{}".format(set_type, name, input_text))
        except Exception as e:
            log.error("[%s] %s", "设置输入框文本", str(e))
            raise e

    # 设置复选框状态
    def set_toggle_state(self, name, set_state='On', start_ele=None, timeout=timeout_default) -> None:
        """设置复选框状态
        Args:
            name: str 元素名称
            set_state: str 设置复选框状态
            start_ele: UiElement 在哪个元素里遍历
            timeout: int 超时计时
        """
        try:
            if self.get_toggle_state(name) != set_state:
                wait_element(self.ele_dict[name]['selector'], start_ele, timeout).toggle()
            log.debug("已设置{}复选框状态为{}".format(name, set_state))
        except Exception as e:
            log.error("[%s] %s", "设置输入框文本", str(e))
            raise e

    # 设置元素选中状态
    def set_ele_selected(self, name, start_ele=None, timeout=timeout_default) -> None:
        """设置元素选中状态
        Args:
            name: str 元素名称
            start_ele: UiElement 父节点
            timeout: int 超时计时
        """
        try:
            return wait_element(self.ele_dict[name]['selector'], start_ele, timeout).select()
        except Exception as e:
            log.error("[%s] %s", "设置元素选中状态", str(e))
            raise e

    # 展开元素
    def expend_ele(self, name, start_ele=None, timeout=timeout_default) -> None:
        """展开元素
        Args:
            name: str 元素名称
            start_ele: UiElement 父节点
            timeout: int 超时计时
        """
        try:
            wait_element(self.ele_dict[name]['selector'], start_ele, timeout).expand()
        except Exception as e:
            log.error("[%s] %s", "展开元素", str(e))
            raise e

    # 折叠元素
    def collapse_ele(self, name, start_ele=None, timeout=timeout_default) -> None:
        """折叠元素
        Args:
            name: str 元素名称
            start_ele: UiElement 父节点
            timeout: int 超时计时
        """
        try:
            wait_element(self.ele_dict[name]['selector'], start_ele, timeout).collapse()
        except Exception as e:
            log.error("[%s] %s", "折叠元素", str(e))
            raise e

    # 对当前页面的某个元素运行JavaScript
    def run_js(self, name, script, parameters=None) -> any:
        """对当前页面的某个元素运行JavaScript
        Args:
            name: str 元素名称
            script: str script语句
            parameters: Any 可被json序列化的对象
        Returns:
            运行结果
        """
        if parameters is None:
            parameters = {}
        try:
            return self.current_page.run_script(self.ele_dict[name]['selector'], script, parameters)
        except Exception as e:
            log.error("[%s] %s", "对当前页面的某个元素运行JavaScript", str(e))
            raise e
