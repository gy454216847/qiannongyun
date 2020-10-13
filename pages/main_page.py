from selenium.webdriver.common.by import By

from common.Common_fun_APK import Common_fun


class main_page(Common_fun):
    my_tap = 'id=>csii.com.qny:id/iv_user'
    home_tap = 'id=>csii.com.qny:id/iv_home'
    shop_tap = 'id=>csii.com.qny:id/iv_shop'
    e_dai_tap = 'id=>csii.com.qny:id/iv_work'
    live_tap = 'id=>csii.com.qny:id/iv_njl'
    search_box = 'xpath=>/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextSwitcher/android.widget.TextView'
    scan_button = 'id=>csii.com.qny:id/img_sys'
    pay_button = 'id=>csii.com.qny:id/img_pay'
    wealth_button = 'id=>csii.com.qny:id/img_getmoney'
    my_account_button = 'id=>csii.com.qny:id/img_qned'
    transfer_account_button = 'xpath=>/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.ImageView'

    live_pay_fee_button = 'xpath=>/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[2]/android.widget.ImageView'
    transfer_by_phone_number_button = 'xpath=>/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[3]/android.widget.ImageView'
    transfer_by_myself_button = 'xpath=>/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[4]/android.widget.ImageView'
    smart_transport_button = 'xpath=>/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[5]/android.widget.ImageView'
    save_product_button = 'xpath=>/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[6]/android.widget.ImageView'
    money_management_product_button = 'xpath=>/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[7]/android.widget.ImageView'
    more_function_button = 'xpath=>/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[8]/android.widget.ImageView'

    def click_my_tap(self):
        self.click_element(self.my_tap)

    def click_home_tap(self):
        self.click_element(self.home_tap)

    def click_shop_tap(self):
        self.click_element(self.shop_tap)

    def click_e_dai_tap(self):
        self.click_element(self.e_dai_tap)

    def click_live_tap(self):
        self.click_element(self.live_tap)
