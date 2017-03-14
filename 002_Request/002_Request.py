#encoding:utf-8

def requests_GET():
    """requests
        GET
    """

    import requests

    kw = {"wd": "Guibs"}

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}

    # params 接收一个字典或者字符串的查询参数, 字典类型自动转换为 url 编码, 不需要 urlencode()
    # requests.get() requests.request() 发送 GET 方法
    response = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)

    # 查看响应内容
    # response.content 返回字节流格式数据
    print response.content
    # response.text 返回 Unicode 格式的数据
    print response.text

    # 查看完整 url 地址
    print response.url

    # 查看响应头字符编码
    print response.encoding

    # 查看响应码
    print response.status_code

def requests_POST():
    """requests
        POST
    """

    import requests

    formdata = {
        "type": "AUTO",
        "i": "Why So Serious",
        "doctype": "json",
        "xmlVersion": "1.8",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_ENTER",
        "typoResult": "true"
    }

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}

    response = requests.post(url, data=formdata, headers=headers)

    print "response.text: %s" % response.text

    # 如果返回结果是 json, 则可以直接调用 .json() 返回
    print "response.json(): %s" % response.json()

def requests_proxy():
    """requests
        proxies
    """

    import requests

    # 根据协议类型, 选择不同代理
    # 公用代理
    proxies = {
        "http": "http://xx.xx.xx.xxx:xxxx",
        "https": "https://xx.xx.xx.xxx:xxxx",
    }
    # 私密代理
    p_proxies = {
        "http": "username:password@xx.xxx.xxx.xxx:xxxx"
    }

    response = requests.get("http://www.xxx.com", proxies=proxies)

    print response.text

def reqeusts_web_auth():
    """requests
        Web 客户端验证
    """

    import requests

    auth = ("username", "password")

    response = requests.get('http://xxx.xxx.xxx.xxx', auth=auth)

    print response.text

def requests_cookie():
    """requests
        cookies
    """

    import requests

    response = requests.get("http://www.renren.com/")

    # 获得 cookie 对象
    cookiejar = response.cookies

    # 将 cookie 对象转换为字典
    cookies_dir = requests.utils.dict_from_cookiejar(cookiejar)

    print "cookie: %s" % cookiejar
    print "cookie_dir: %s" % cookies_dir

def requests_session():
    """requests
        session
    """

    import requests

    # 创建 session 对象, 可以保存 cookie
    session = requests.session()

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}

    data = {"email": "xxxxx@qq.com", "password": "xxxxxxx"}

    session.post("http://www.renren.com/PLogin.do", data=data)

    response = session.get("http://www.renren.com")

    print response.text

def requests_ssl():
    """requests
        ssl
    """

    import requests

    # verify=False 忽略 ssl 证书验证
    response = requests.get("https://www.12306.cn/mormhweb/", verify=False)

    print response.text

if __name__ == '__main__':
    requests_ssl()
