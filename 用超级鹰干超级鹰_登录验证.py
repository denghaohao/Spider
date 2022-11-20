from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.by import By
import time
web = Chrome()
web.get('http://www.chaojiying.com/user/login/')

#处理验证码

#直接截屏 screenshot 保存成二进制
img = web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png



# chaojiying = Chaojiying_Client('超级鹰用户名', '超级鹰用户名的密码', '96001')	#用户中心>>软件ID 生成一个替换 96001
chaojiying = Chaojiying_Client('dengyi', 'qq1314', '941972')
dic = chaojiying.PostPic(img, 1004)
print(dic)
verify_code = dic['pic_str']
time.sleep(2)
#模拟登录
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('dengyi')
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('qq1314')
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)
time.sleep(5)
#点击登录
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()

time.sleep(5)
