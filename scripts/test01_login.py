import unittest

from base.get_driver import GetDriver
from page.page_login import PageLogin
from parameterized import parameterized
from tool.read_txt import read_txt
from base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


def get_data():
    arrs = []
    for data in read_txt("login.txt"):
        arrs.append(tuple(data.strip().split(",")))
    return arrs[1:]


# 新建 登录测试类 并 继承 unittest.TestCase
class TestLogin(unittest.TestCase):
    # 新建 setupClass
    @classmethod
    def setUpClass(cls):
        try:
            # 实例化 并获取driver
            cls.driver = GetDriver().get_driver()
            # 实例化 PageLogin()
            cls.login = PageLogin(cls.driver)
            # 点击登录连接
            cls.login.page_click_login_link()
        except Exception as e:
            log.error("错误：{}".format(e))
            # 截图
            cls.login.base_get_image()

    # 新建 tearDownClass
    @classmethod
    def tearDownClass(cls):
        # 关闭drier驱动对象
        GetDriver().quit_driver()

    # 新建 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, pwd, verify_code, expect_result, status):
        try:
            # 调用 登录业务方法
            self.login.page_login(username, pwd, verify_code)
            # 判断是否为正向
            if status == "true":
                # 断言是否登录成功
                try:
                    self.assertTrue(self.login.page_if_login_success())
                except Exception as e:
                    # 截图
                    self.login.base_get_image()
                    log.error("错误：{}".format(e))
                    raise  # 主动抛出异常，否则HTMLTestRunner无法显示该错误
                # 点击 安全退出
                self.login.page_click_logout_link()
                # 点击登录连接
                self.login.page_click_login_link()
            # 逆向用例
            else:
                # 获取错误提示信息
                msg = self.login.page_get_error_info()
                print("msg:", msg)
                try:
                    self.assertEqual(msg, expect_result)
                except Exception as e:
                    # 截图
                    self.login.base_get_image()
                    log.error("错误：{}".format(e))
                    raise
                # 点击错误提示框 确定按钮
                self.login.page_click_error_alert()
        except Exception as e:
            log.error("错误：{}".format(e))
            # 截图
            self.login.base_get_image()
            raise
