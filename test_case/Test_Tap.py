import logging

from common.myunit import StartEnd
from pages.main_page import main_page
from pages.my_tap_page import my_tap_page
from pages.e_dai_tap_page import e_dai_tap_page
from pages.live_tap_page import live_tap_page
from pages.shop_tap_page import shop_tap_page
from common.Common_fun_APK import Common_fun


class Test_Tap(StartEnd, Common_fun):

    def test_tap(self):
        logging.info('======test tap======')
        main_page(self.driver).click_shop_tap()
        self.isElementExist(shop_tap_page.AD_loc)
        main_page(self.driver).click_e_dai_tap()
        main_page(self.driver).click_live_tap()
        self.assertEqual(self.get_text(live_tap_page.Title_loc), '生活')
        main_page(self.driver).click_my_tap()
        self.isElementExist(my_tap_page.login_register_button)
