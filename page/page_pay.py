import page
from base.base import Base
from base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class PagePay(Base):
    # 点击 我的订单连接
    def page_click_my_order_link(self):
        log.info("[page_pay] 点击{} 元素，执行进入我的订单操作".format(page.pay_my_order))
        self.base_click(page.pay_my_order)

    # 点击 立即支付
    def page_click_now_payment(self):
        # 必须先切换窗口
        log.info("[page_pay] 切换窗口至支付页面")
        self.base_switch_to_window(page.pay_my_order_title)
        # 点击立即支付
        log.info("[page_pay] 点击{} 元素，执行立即支付操作".format(page.pay_now_payment))
        self.base_click(page.pay_now_payment)

    # 点击 货到付款
    def page_click_pay_on_delivery(self):
        # 必须切换窗口
        log.info("[page_pay] 切换窗口至付款页面")
        self.base_switch_to_window(page.pay_payment_title)
        # 点击货到付款
        log.info("[page_pay] 点击{} 元素，执行选择货到付款操作".format(page.pay_on_delivery))
        self.base_click(page.pay_on_delivery)

    # 确认支付方式
    def page_click_payment_mode(self):
        log.info("[page_pay] 点击{} 元素，执行确认支付操作".format(page.pay_confirm_payment))
        self.base_click(page.pay_confirm_payment)

    # 获取支付结果
    def page_get_payment_result(self):
        log.info("[page_pay] 通过{}元素，得到订单提交结果".format(page.pay_payment_result))
        return self.base_get_text(page.pay_payment_result)

    # 组合业务方法
    def page_pay(self):
        self.page_click_my_order_link()
        self.page_click_now_payment()
        self.page_click_pay_on_delivery()
        self.page_click_payment_mode()
