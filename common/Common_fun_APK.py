# 初始化和封装一下基本方法
import logging
import os
import smtplib
import time
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import yaml
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

base_path = os.path.dirname(os.path.dirname(__file__))


class Common_fun(object):
    """
    封装公共方法
    """

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc):
        """
        找一个元素
        :param loc:元素地址
        :return:
        """
        if "=>" not in loc:
            raise NameError("Positioning syntax errors, lack of '=>'.")
        by = loc.split("=>")[0]
        value = loc.split("=>")[1]

        if by == 'id':
            element = self.driver.find_element_by_id(value)
        elif by == 'name':
            element = self.driver.find_element_by_name(value)
        elif by == 'class':
            element = self.driver.find_element_by_class(value)
        elif by == 'link_text':
            element = self.driver.find_element_by_link_text(value)
        elif by == 'xpath':
            element = self.driver.find_element_by_xpath(value)
        elif by == 'css':
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def get_window_size(self):
        """
        获取窗口大小
        :return:窗口长和宽
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipe_left(self):
        """
        向左滑
        :return:
        """
        logging.info("------swipe_left-------")
        l = self.get_window_size()
        x1 = int(l[0] * 0.1)
        x2 = int(l[0] * 0.9)
        y = int(l[1] * 0.5)
        return self.driver.swipe(x2, y, x1, y, 1000)

    def swipe_right(self):
        """
        向右滑
        :return:
        """
        logging.info("------swipe_right-------")
        l = self.get_window_size()
        x1 = int(l[0] * 0.1)
        x2 = int(l[0] * 0.9)
        y = int(l[1] * 0.5)
        return self.driver.swipe(x1, y, x2, y, 1000)

    def swipe_up(self):
        """
        向上滑
        :return:
        """
        logging.info("------swipe_up------")
        l = self.get_window_size()
        x = int(l[0] * 0.5)
        y1 = int(l[1] * 0.1)
        y2 = int(l[2] * 0.9)
        return self.driver.swipe(x, y1, x, y2, 1000)

    def swipe_down(self):
        """
        向下滑
        :return:
        """
        logging.info("------swipe_down------")
        l = self.get_window_size()
        x = int(l[0] * 0.5)
        y1 = int(l[1] * 0.1)
        y2 = int(l[2] * 0.9)
        return self.driver.swipe(x, y2, x, y1, 1000)

    def getTime(self):
        """
        获取当前时间
        """
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def get_Screen_Shot(self, module):
        """
        截图
        :param module:图片模式
        """
        time = self.getTime()
        image_file = base_path + '/screenshots/%s_%s.png' % (module, time)
        logging.info('====== get %s screenshot ======' % module)
        self.driver.get_screenshot_as_file(image_file)

    def click_element(self, loc):
        self.wait_element(loc)
        self.find_element(loc).click()

    def clear_element(self, loc):
        self.wait_element(loc)
        self.find_element(loc).clear()

    def type_element(self, loc, text):
        self.wait_element(loc)
        self.clear_element(loc)
        self.find_element(loc).send_keys(text)

    def wait_element(self, loc):
        if "=>" not in loc:
            raise NameError("Positioning syntax errors, lack of '=>'.")
        by = loc.split("=>")[0]
        value = loc.split("=>")[1]
        seconds = 10
        if by == 'id':
            WebDriverWait(self.driver, seconds).until(lambda x: x.find_element_by_id(value))
        elif by == 'name':
            WebDriverWait(self.driver, seconds).until(lambda x: x.find_element_by_name(value))
        elif by == 'class':
            WebDriverWait(self.driver, seconds).until(lambda x: x.find_element_by_class_name(value))
        elif by == 'link_text':
            WebDriverWait(self.driver, seconds).until(lambda x: x.find_element_by_link_text(value))
        elif by == 'xpath':
            WebDriverWait(self.driver, seconds).until(lambda x: x.find_element_by_xpath(value))
        elif by == 'css':
            WebDriverWait(self.driver, seconds).until(lambda x: x.find_element_by_css_selector(value))
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")

    def isElementExist(self, loc):

        element_text = self.find_element(loc).text

        try:
            self.wait_element(loc)
            print(element_text + '元素存在')
        except NoSuchElementException:
            print(element_text + '元素不存在')

    def get_text(self, loc):
        """

        :param loc:
        :return:
        """
        element_text = self.find_element(loc).text
        return element_text

    def isEnabled(self, loc):
        self.wait_element(loc)
        return self.find_element(loc).is_enabled()

    def isSelected(self, loc):
        self.wait_element(loc)
        return self.find_element(loc).is_selected()

    def get_title(self):
        return self.driver.title

    def get_currentUrl(self):
        return self.driver.current_url


    def alterAccept(self):
        self.driver.switch_to.alert.accept()

    def alterDismiss(self):
        self.driver.switch_to.alert.dismiss()

    def switchFrame(self, loc):
        self.driver.switch_to.frame(self.find_element(loc))

    def switchFrameOut(self):
        self.driver.switch_to.default_content()

    def select_by_value(self, loc, value):
        self.wait_element(loc)
        self.find_element(loc).select_by_value(value)

    def get_csv_data(self, csv_file, line):
        logging.info('=====get_csv_data======')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    def latest_report(report_dir):
        lists = os.listdir(report_dir)
        print(lists)
        lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
        print(lists[-1])
        file = os.path.join(report_dir, lists[-1])
        return file

    def send_mail(latest_report):
        f = open(latest_report, 'rb')
        mail_content = f.read()
        f.close()
        yamlfile = base_path + '/config/' + 'email.yaml'
        file = open(yamlfile, encoding='utf-8')
        data = yaml.load(file, Loader=yaml.FullLoader)

        smtpserver = data['smtpserver']

        user = data['user']
        password = data['password']

        sender = data['sender']
        receives = data['receives']

        subject = data['subject']
        filename = data['filename']
        msg = MIMEMultipart()
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = sender
        msg['To'] = receives
        msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        text_msg = MIMEText('查看自动化测试请下载附件', 'plain', 'utf-8')
        msg.attach(text_msg)
        file_msg = MIMEApplication(mail_content)
        file_msg.add_header('content-disposition', 'attchment', filename=filename + '.html')

        msg.attach(file_msg)

        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        smtp.helo(smtpserver)
        smtp.ehlo(smtpserver)
        smtp.login(user, password)

        print("Start send email....")
        smtp.sendmail(sender, receives, msg.as_string())
        smtp.quit()
        print("Send email end")
