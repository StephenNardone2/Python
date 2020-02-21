''' Important:
        You will either need easy_install or pip to
        install the mechanize library. Mechanize will
        be discontinuing support for Python 2.X also.
'''
import mechanize 

# Retrieving a website's source code
'''def viewPage(url):
    browser = mechanize.Browser()
    page = browser.open(url)
    source_code = page.read()
    print source_code
viewPage('http://www.syngress.com/')
'''
# Anonymity - Adding Proxy
def testProxy(url, proxy):
    browser = mechanize.Browser()
    browser.set_proxies(proxy)
    page = browser.open(url)
    source_code = page.read()
    print (source_code)
url = 'http://ip.nefsc.noaa.gov'
hideMeProxy = {'http': '209.141.46.133:8080'}
testProxy(url, hideMeProxy)