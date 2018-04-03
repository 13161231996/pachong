from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse
from tianmao.items import TianmaoItem

class Tianmaomiddlewares(object):
        def __init__(self):
                self.driver = webdriver.PhantomJS()

        def process_request(self,request,spider):
                if request.meta.get('phantonjs',True):
                        self.driver.get(request.url)
                        time.sleep(1)
                        html = self.driver.page_source

                        return HtmlResponse(url=request.url,body=html,encoding='utf-8',request=request)