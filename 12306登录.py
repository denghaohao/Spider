from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options


# 修改 浏览器中的 window.navigator.webdriver  值为false
# 网站会检测 他的值不让你登录

opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')

web = Chrome(options=opt)
#验证方式已经改了
web.get('https://kyfw.12306.cn/otn/resources/login.html')

#拿到验证元素
# verify_element = web.find_element(By.XPATH, '//*[@id="slide"]/div')

#初始化超级鹰
# chaojiying = Chaojiying_Client('dengyi', 'qq1314', '941972')
# dic = chaojiying.PostPic(verify_element.screenshot_as_png, 1004)
# address = dic['pit_str']
#
# #选择操作
# for rs in address.split('|'):
#     rs_s = rs.split(',')
#     x = int(rs_s[0])
#     y = int(rs_s[1])
#
#     ActionChains(web).move_to_element_with_offset(verify_element, x, y).click().perform()


# 输入账户密码

web.find_element(By.XPATH, '//*[@id="J-userName"]').send_keys('15683836173')
web.find_element(By.XPATH, '//*[@id="J-password"]').send_keys('dhh20000105')

# 点击登录
web.find_element(By.XPATH, '//*[@id="J-login"]').click()
#这里如果不等待一会，下面的执行过快 找不到页面元素
time.sleep(2)
btn = web.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')

# 拖拽
ActionChains(web).drag_and_drop_by_offset(btn, 372, 0).perform()
time.sleep(10000)