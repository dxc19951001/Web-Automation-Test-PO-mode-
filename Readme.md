# Web自动化测试框架

​		本项目是以Tpshop开源商城作为web自动化测试对象，使用Unittest+Selenium+HTMLTestRunner基于PO模式实现的web自动化测试，可实现异常截图、日志输出和HTML包括生成等功能

项目结构如下所示

```
Web-Automation-Test-PO-mode-
├─ base   封装公共方法
│  ├─ base.py   封装查找、点击、输入、获取文本、截图、切换frame和窗口等方法
│  ├─ get_driver.py   以单例模式封装driver
│  ├─ get_logger.py   以单例模式封装log，log可输出至文本及控制台
├─ data
│  └─ login.txt   测试数据已txt文本存放
├─ image   存放异常截图
├─ log   存放log日志
├─ page   存放个功能模块逻辑，包括登录、购物车、下订单和支付
│  ├─ page_cart.py
│  ├─ page_login.py
│  ├─ page_order.py
│  ├─ page_pay.py
│  ├─ __init__.py  相关配置信息
├─ report   生成的测试报告存放地址
├─ run_main.py   主程序入口，运行此文件进行自动化测试
├─ scripts   执行测试用例
│  ├─ test01_login.py
│  ├─ test02_cart.py
│  ├─ test03_order.py
│  ├─ test04_pay.py
└─ tool   放置所需工具
   ├─ HTMLTestRunner.py   生成HTML测试报告
   ├─ read_txt.py   读取测试数据
```

tpshp安装教程可自取

链接：https://pan.baidu.com/s/1KZDrV5RdhaF5icjRq3kTBQ 
提取码：0n1e 
