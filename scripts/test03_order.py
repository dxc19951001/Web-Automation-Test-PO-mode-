import time
import unittest

from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_order import PageOrder
from base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


# 新建测试类 并 集成
class TestOrder(unittest.TestCase):
    # setup
    def setUp(self):
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 调用登录 PageLogin对象中，登录方法
        PageLogin(self.driver).page_login_success()
        # 实例化 PageOrder
        self.order = PageOrder(self.driver)
        # 回到首页
        self.order.page_click_index()

    # teardown
    def tearDown(self):
        # 关闭driver
        GetDriver().quit_driver()

    # 新建 订单测试方法
    def test_order(self):
        try:
            # 调用 下订单业务方法
            self.order.page_order()
            # 断言
            msg = self.order.page_get_submit_result()
            print("msg:", msg)
            self.assertIn("提交成功", msg)
        except Exception as e:
            # 截图
            self.order.base_get_image()
            # 日志
            log.error("错误：{}".format(e))
            raise

