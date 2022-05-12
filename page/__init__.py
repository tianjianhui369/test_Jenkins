"""配置数据都写到这里"""
from selenium.webdriver.common.by import By

"""以下为通讯录首界面的配置数据"""
index_add = By.ID,"com.android.contacts:id/floating_action_button"

"""以下为人员新增界面的配置数据"""
add_name = By.XPATH,"//*[@text='姓名']"
add_phone = By.XPATH,"//*[@text='电话']"
add_back = By.CLASS_NAME,"android.widget.ImageButton"