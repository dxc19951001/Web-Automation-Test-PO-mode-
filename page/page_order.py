from time import sleep

import page
from base.base import Base
from base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class PageOrder(Base):
    # 打开首页
    def page_click_index(self):
        log.info("[page_order] 执行打开首页操作")
        self.base_index()

    # 点击 我的购物车
    def page_click_my_cart(self):
        log.info("[page_order] 点击{} 元素，执行进入购物车操作".format(page.order_my_cart))
        self.base_click(page.order_my_cart)

    # 点击 全选复选框
    def page_click_all_select(self):
        # 判断 如果没选中 就进行点击操作
        if not self.base_find(page.order_all).is_selected():
            log.info("[page_order] 点击{} 元素，执行全选操作".format(page.order_all))
            self.base_click(page.order_all)

    # 点击 去结算
    def page_click_account(self):
        log.info("[page_order] 点击{} 元素，执行去结算操作".format(page.order_account))
        self.base_click(page.order_account)

    # 若收货人和自提点不加载完成直接提交订单将报错
    # 备用 查找收货人 -->动态 解决 收货人加载慢的问题
    def page_find_person(self):
        log.info("[page_order] 查找{} 元素".format(page.order_person))
        self.base_find(page.order_person)

    # 备用 查找自提点 -->动态 解决 自提点加载慢的问题
    def page_find_fetch_address(self):
        log.info("[page_order] 查找{} 元素".format(page.order_fetch_address))
        self.base_find(page.order_fetch_address)

    # 点击 提交订单
    def page_click_submit_order(self):
        log.info("[page_order] 点击{}，执行提交订单操作".format(page.order_submit))
        self.base_click(page.order_submit)

    # 获取 订单提交结果
    def page_get_submit_result(self):
        log.info("[page_order] 通过{}元素，得到订单提交结果".format(page.order_submit_result))
        return self.base_get_text(page.order_submit_result)

    # 组装订单业务方法
    def page_order(self):
        self.page_click_my_cart()
        self.page_click_all_select()
        self.page_click_account()
        # 注意：此处有一个坑，默认收货人在页面加载完成3秒后才出现；解决方式1：使用sleep(5)
        # sleep(5)
        # 找到收货人，说明异步加载完成，收货人信息出现，直接可以继续执行提交订单；
        # 解决方式2 ：使用显示等待等待时长机制，实现，推荐：
        self.page_find_person()
        self.page_find_fetch_address()
        self.page_click_submit_order()
