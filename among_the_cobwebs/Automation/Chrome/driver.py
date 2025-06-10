from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import socket
from pathlib import Path
from among_the_cobwebs.Automation.WebDriver.Chrome.entrance import CHROME, CHROMEDRIVER
from datetime import datetime
from typing import Optional
from selenium.common.exceptions import WebDriverException


class ParameterMapping(object):
    def __init__(self):
        self._service_mapping = {
            'executable_path': 'to_do',
            'log_output': 'log',
            'part': 'part',
        }
        self._options_mapping = {
            '--headless': 'no_head',  # 无头浏览器模式
            '--disable-gpu': 'no_gpu',  # 禁用gpu加速
            '--window-size=1900,1080': 'window[1900,1080]',  #自定义分辨率
            'start-maximized': 'max_win',  # 启动时最大化窗口
            '--user-agent=xxx': 'xxxx',  # 用户代理
            '--disable-infobars': 'hidden',  # 禁用自动化提示栏
            "'excludeSwitches', ['enable-automation']": 'hidden',  #
            '--incognito': '无痕',
            '--disable-blink-features=AutomationControlled': '禁用自动化控制特性',
            'blink-settings=imagesEnabled=false': '禁用图片和视频加载',
            '--disable-javascript': '禁用javascript',
            '--proxy-server=http://129:..': '通过代理服务器访问目标网站',
            ''
        }


class LogConfig(object):
    __slots__ = ['_enabled', '_dir']
    def __init__(self) ->None:
        self._enabled: bool = False
        self._dir: Optional[str] = None

    @property
    def enabled(self) ->bool:
        return self._enabled

    @property
    def dir(self) ->str or None:
        return self._dir

    @enabled.setter
    def enabled(self, value: str) ->None:
        self._enabled = value

    @dir.setter
    def dir(self, value: str) ->None:
        if self._enabled:
            self._dir = value


class ServiceConfig(LogConfig):
    def __init__(self) ->None:
        super().__init__()
        self._service:Service = Service()
        self._cfg: dict = {
            ''
        }

    @property
    def is_exist_service(self) ->bool:
        if self._service:
            return True
        else:
            return False

    @property
    def cfg(self):
        return self._cfg

    @is_exist_service.setter
    def is_exist_service(self, value) ->None:
        if not self._service:
            self._cfg = None
        else:







class Driver(object):
    __slots__ = ['driver', 'chrome', 'chromedriver', 'service', 'log_output', 'options']
    def __init__(self):
        self.chrome = CHROME
        self.chromedriver = CHROMEDRIVER
        self.log_output = None
        self.service = Service(executable_path=self.chromedriver, log_output=self.log_output, port=4444)
        self.options = Options()
        self.options.binary_location = self.chrome
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def to(self, url: str) ->None:
        self.driver.get(url)
        return

    def by(self, chrome_path=None, chromedriver_path=None, enable_log=False, log_output=None, port=None, **kwargs) ->None:
        if chromedriver_path:
            self.chrome = chrome_path
        if chromedriver_path:
            self.chromedriver = chromedriver_path
        try:
            if enable_log and log_output:
                if os.path.exists(log_output):
                    self.log_output = log_output
                else:
                    os.makedirs(log_output, exist_ok=True)
                    self.log_output = log_output
            if enable_log and log_output is None:
                current_dir_parent = Path(__file__).parent
                now = datetime.now()
                default_log_output = os.path.join(current_dir_parent,
                                                   f"{now.strftime("%Y-%m-%d %H:%M:%S")}"
                )
                self.log_output = default_log_output
            if enable_log is False and log_output:
                raise




d = Driver()
d.to('https://www.baidu.com')














