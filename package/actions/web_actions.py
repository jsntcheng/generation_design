from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def create_browser(url):
    if url[0:4] != 'http':
        raise Exception('请输入正确的网址(带http(s)://)')
    try:
        driver = webdriver.Remote(
            command_executor="101.35.49.209:4444",
            desired_capabilities=DesiredCapabilities.CHROME.copy()
        )
        driver.get(url)
        print('成功启动浏览器')
        return driver
    except:
        driver.quit()
        raise Exception('启动浏览器失败')

def close_browser(driver):
    driver.quit()
    print('已退出浏览器')

def switch_page(driver, page_num):
    '''
    切换操作页面
    :param driver: web_driver
    :param page_num: 切换到第几页
    :return:
    '''
    try:
        page_list = driver.handles
        driver.switch_to.window(page_list[page_num+1])
        print(f'成功切换到第{page_num+1}页')
    except:
        driver.quit()
        raise Exception('切换操作页面失败')

def refresh_page(driver):
    '''
    刷新页面
    :param driver: web_driver
    :return:
    '''
    try:
        driver.refresh()
        print('刷新页面成功')
    except:
        driver.quit()
        raise Exception('刷新页面失败')

def wait_element(driver, selector, start_element = None, timeout = 10):
    '''
    等待元素出现
    :param driver: web_driver
    :param selector: Xpath
    :param start_element: 起始元素
    :param timeout: 超时时间
    :return: Web_Element
    '''
    count = 0
    while count < timeout:
        try:
            if not start_element:
                return  driver.find_element(by = By.XPATH, value = selector)
            else:
                return start_element.find_element(by = By.XPATH, value = selector)
        except:
            sleep(1)
            count += 1
    driver.quit()
    raise Exception('等待元素超时')

def get_all_element(driver, selector, start_element = None, timeout = 10):
    '''
    获取同selector的所有元素
    :param driver: web_driver
    :param selector: xpath
    :param start_element: 起始元素
    :param timeout: 超时时间
    :return: list[Web_Element]
    '''
    count = 0
    while count < timeout:
        try:
            if  not start_element:
                return driver.find_elements(by=By.XPATH, value=selector)
            else:
                return start_element.find_elements(by=By.XPATH, value=selector)
        except:
            count += 1
    driver.quit()
    raise Exception('获取元素超时')

def click_element(driver, selector, start_element = None, timeout = 10):
    '''
    点击元素
    :param driver: Web_driver
    :param selector: Xpath
    :param start_element: 起始元素
    :param timeout: 超时时间
    :return:
    '''
    try:
        wait_element(driver, selector,start_element,timeout).click()
    except:
        driver.quit()
        raise Exception('点击元素失败')

def get_element_attr(driver, selector, attr, start_element = None, timeout = 10):
    '''
    获取元素元素
    :param driver: web_driver
    :param selector: xpath
    :param attr: 需要获取的属性
    :param start_element: 起始元素
    :param timeout: 超时时间
    :return: str 属性值
    '''
    try:
        return wait_element(driver, selector, start_element, timeout)[attr]
    except:
        driver.quit()
        raise Exception('获取元素属性失败')

def get_element_txt(driver, selector, start_element = None, timeout = 10):
    '''
    获取元素内所有文字
    :param driver: web_driver
    :param selector: xpath
    :param start_element: 起始元素
    :param timeout: 超时时间
    :return: str 元素内文字
    '''
    wait_element(driver,selector,start_element,timeout)

def get_doc(func):
    '''
    获取方法内的说明文字
    :param func: 方法
    :return: str 说明文字
    '''

    temp_list = func.__doc__.split('\n    ')
    result = ""
    for i in temp_list[2:-2]:
        result += i.replace(':param ','')+'  '
    return result

driver = create_browser('https://www.baidu.com')

str1 = get_element_txt.__doc__
print(get_element_txt.__doc__)
print(111)