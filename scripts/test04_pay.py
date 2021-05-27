import unittest

from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_pay import PagePay
from base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class TestPay(unittest.TestCase):
    # setup
    def setUp(self):
        # 获取 driver
        self.driver = GetDriver().get_driver()
        # 登录 成功
        PageLogin(self.driver).page_login_success()
        # PagePay 类
        self.pay = PagePay(self.driver)
        # 回到首页
        self.pay.base_index()

    # teardown
    def tearDown(self):
        # 关闭driver
        GetDriver().quit_driver()

    # 新建支付测试方法
    def test_pay(self):
        try:
            # 调用支付方法
            self.pay.page_pay()
            # 断言
            print("获取的支付结果：", self.pay.page_get_payment_result())
            self.assertIn("订单提交成功", self.pay.page_get_payment_result())
        except Exception as e:
            # 截图
            self.pay.base_get_image()
            # 日志
            log.error(e)
            raise