from selenium.webdriver.common.by import By
from common.Common_fun_APK import Common_fun


class my_tap_page(Common_fun):

    portrait_button = 'id=>csii.com.qny:id/img_touxiang'
    login_register_button = 'id=>csii.com.qny:id/tv_username'

    def enter_login_page(self):
        self.click_element(self.login_register_button)
