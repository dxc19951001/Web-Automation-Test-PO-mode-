import time
import page
from selenium.webdriver.support.wait import WebDriverWait
from base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class Base:

    def __init__(self, driver):
        log.info("[base]: 正在获取初始化driver对象:{}".format(driver))
        self.driver = driver

    # 查找元素方法 封装
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info("[base]: 正在定位:{} 元素，默认定位超时时间为: {}".format(loc, timeout))
        # 使用显示等待 查找元素
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击元素 方法封装
    def base_click(self, loc):
        log.info("[base]: 正在对:{} 元素实行点击事件".format(loc))
        self.base_find(loc).click()
        # self.driver.execute_script("arguments[0].click();", self.base_find(loc))

    # 输入元素 方法封装
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空
        log.info("[base]: 正在对:{} 元素实行清空".format(loc))
        el.clear()
        # 输入
        el.send_keys(value)

    # 获取文本信息 方法封装
    def base_get_text(self, loc):
        log.info("[base]: 正在获取:{} 元素文本值".format(loc))
        return self.base_find(loc).text

    # 截图 方法封装
    def base_get_image(self):
        log.info("[base]: 断言出错，调用截图")
        self.driver.get_screenshot_as_file("./image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 判断元素是否存在 方法封装
    def base_element_is_exist(self, loc):
        try:
            self.base_find(loc, timeout=5)
            log.info("[base]: {} 元素查找成功，存在页面".format(loc))
            return True  # 代表元素存在
        except Exception as e:
            log.error("[base]：发生错误{}，{} 元素查找失败，不存在当前页面".format(e, loc))
            return False  # 代表元素不存在

    # 回到首(页购物车、下订单、支付)都需要用到此方法
    def base_index(self):
        time.sleep(5)
        self.driver.get(page.URL)

    # 切换frame表单方法
    def base_switch_frame(self, name):
        self.driver.switch_to.frame(name)

    # 回到默认目录方法
    def base_default_content(self):
        self.driver.switch_to.default_content()

    # 切换窗口 方法 调用此方法
    def base_switch_to_window(self, title):
        log.info("正在执行切换title值为：{}窗口 ".format(title))
        self.driver.switch_to.window(self.base_get_title_handle(title))

    # 获取指定title页面的handle方法
    def base_get_title_handle(self, title):
        # 获取当前页面所有的handles
        for handle in self.driver.window_handles:
            log.info("正在遍历handles：{}-->{}".format(handle, self.driver.window_handles))
            # 切换 handle
            self.driver.switch_to.window(handle)
            log.info("切换 :{} 窗口".format(handle))
            # 获取当前页面title 并判断 是否等于 指定参数title
            log.info("判断当前页面title:{} 是否等于指定的title:{}".format(self.driver.title, title))
            if self.driver.title == title:
                log.info("条件成立！ 返回当前handle{}".format(handle))
                # 返回 handle
                return handle
