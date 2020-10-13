import yaml
from selenium.webdriver.common.by import By

from common.Common_fun_APK import Common_fun
from common.Common_fun_APK import base_path


class login_page(Common_fun):
    account_yaml_path = base_path + '/config/account.yaml'
    with open(account_yaml_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    username_box = 'id=>csii.com.qny:id/edt_username'
    password_box = 'id=>csii.com.qny:id/edt_paypwd'
    login_button = 'id=>csii.com.qny:id/btn_login'
    username = data['username']
    password = data['password']

    def login(self):
        # self.find_element(*self.username_box).send_keys(self.username)
        self.click_element(self.password_box)
        self.driver.press_keycode(10)
        self.driver.press_keycode(9)
        self.driver.press_keycode(16)
        self.driver.press_keycode(10)
        self.driver.press_keycode(9)
        self.driver.press_keycode(16)

        self.click_element(self.login_button)
