#encoding:utf-8

def urllib2_urlpoen():
    """urllib2
        urlopen
    """
    # 导入 urllib2 模块
    import urllib2

    # 指定 url 发送请求, 返回响应的类文件对象
    response = urllib2.urlopen("http://www.baidu.com")

    # read() 读取类文件对象全部内容, 返回字符串
    html = response.read()

    # 打印字符串
    print html

def urllib2_Request():
    """urllib2
        Request
            使用 Request 对象可以构建一个更为复杂的请求, 比如增加 HTTP 报头
        url: 目标路径
        data: 默认空, 伴随 url 提交的数据, 若传入改参数, 则 HTTP 请求将从 GET 方式变为 POST
        headers: 默认空, 是一个字典, 包含了要发送的 HTTP 报头的键值对
    """

    import urllib2

    # url 作为 Request() 方法的参数, 构造并返回一个 Request 对象
    request = urllib2.Request("http://www.baidu.com")

    # Request 对象作为 urlopen() 参数, 发送给服务器并接收响应
    response = urllib2.urlopen(request)

    html = response.read()

    print html

def urllib2_User_Agent():
    """urllib2

    """

    import urllib2

    url = "http://news.baidu.com/"

    # Chrome Mac User-Agent
    ua_header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}

    # url 连同 headers, 一起构建 Request 请求
    request = urllib2.Request(url, headers=ua_header)

    # 向服务器发送这个请求
    response = urllib2.urlopen(request)

    html = response.read()

    print html

def urllib2_Headers():
    """urllib2
        Request.add_header() 添加/修改 Header
        Request.get_header() 查看已有 Header
    """

    import urllib2
    import random

    url = "http://news.baidu.com/"

    # header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}

    ua_list = [
        # Chrome Mac User-Agent
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
        # Safari Mac User-Agent
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8",
    ]

    # 随机 User-Agent
    user_agent = random.choice(ua_list)

    request = urllib2.Request(url)

    request.add_header("User-Agent", user_agent)

    # 调用 Request.add_header() 添加/修改一个特定 header
    request.add_header("Connection", "keep-alive")

    # 调用 Req.get_header(headerName) 查看 header 信息
    print request.get_header("User-agent") # 第一个字母大写, 后面的小写

    response = urllib2.urlopen(request)

    print response.code # 查看响应状态码

    html = response.read()

    print html

def urllib2_GET_POST():
    """urllib
        GET POST 请求
        urlencode(): 用来将 key:value 转换成 key=value 这样的 GET 查询字符串
        unquote(): 用来解码
    """

    import urllib
    import urllib2

    # GET

    word = {"wd": "桂布斯"}

    # 通过 urlencode() 进行字典的 URL 编码转换
    word = urllib.urlencode(word)
    print word

    # GET 请求的目标 url
    url = "http://www.baidu.com/s"
    url = url + "?" + word

    # 通过 unquote 解码
    word = urllib.unquote(word)
    print word

    request = urllib2.Request(url)

    request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8")

    resposne = urllib2.urlopen(request)

    print resposne.read()

    # POST
    # Content - Length: 144： 是指发送的表单数据长度为144，也就是字符个数是144个。
    # X - Requested - With: XMLHttpRequest ：表示Ajax异步请求。
    # Content - Type: application / x - www - form - urlencoded ： 表示浏览器提交 Web 表单时使用，表单数据会按照 name1 = value1 & name2 = value2 键值对形式进行编码。

    # POST 请求的目标 url
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8"}

    formadata = {
        "type": "AUTO",
        "i": "Why So Serious",
        "doctype": "json",
        "xmlVersion": "1.8",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_ENTER",
        "typoResult": "true"
    }

    data = urllib.urlencode(formadata)

    request = urllib2.Request(url, data=data, headers=headers)
    resposne = urllib2.urlopen(request)

    print resposne.read()

def urllib2_AJAX():
    """urllib2
        AJAX
    """

    import urllib
    import urllib2

    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8"}

    formdata = {
        'start': '0',
        'limit': '10'
    }

    data = urllib.urlencode(formdata)

    request = urllib2.Request(url, data=data, headers=headers)

    response = urllib2.urlopen(request)

    print response.read()

def urllib2_SSL():
    """urllib2
        SSL
    """

    import urllib
    import urllib2
    import ssl

    url = "https://www.12306.cn/mormhweb/"

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8"}

    request = urllib2.Request(url, headers=headers)

    # 构建 context, 表示忽略未经核实的 SSL 证书认证
    context = ssl._create_unverified_context()

    response = urllib2.urlopen(request, context=context)

    print response.read()

def urllib2_opener():
    """urllib2
        1. 使用相关的 Handler 处理器, 来创建特定功能的处理器对象
        2. 通过 urllib2.build_opener() 方法使用这些处理器对象, 创建自定义 opener 对象
        3. 使用自定义 opener 对象, 调用 open() 方法发送请求

        如果程序所有的请求都使用自定义的 opener, 可以使用urllib2.install_opener() 将自定义的 opener 对象定义为全局 opener
    """

    import urllib2

    # 构建一个 HTTPHandler 处理器对象, 支持处理 HTTP 请求
    http_handler = urllib2.HTTPHandler()

    # 构建一个 HTTPSHandler 处理器对象, 支持处理 HTTPS 请求
    # debuglevel 默认为0 1: 开启 Debug Log
    https_handler = urllib2.HTTPSHandler(debuglevel=1)

    # 调用urllib2.build_opener() 方法, 创建自定义 opener 对象
    http_opener = urllib2.build_opener(http_handler)
    https_opener = urllib2.build_opener(https_handler)

    # 构建 Request 请求
    request = urllib2.Request("http://www.baidu.com")

    # 调用自定义 opener 对象的 open() 方法, 发送 request 请求
    response = http_opener.open(request)

    # 获取服务器响应
    print response.read()

def urllib2_ProxyHandler():
    """urllib2
        ProxyHandler 处理器(代理设置)
    """

    import urllib2
    import random

    proxyList = [
        {"http": "124.88.67.52:843"},
        {"http": "218.76.106.78:3128"}
    ]

    proxy = random.choice(proxyList)

    # 构建了两个 Handler, 一个有 IP 代理, 一个没有
    http_proxy_handler = urllib2.ProxyHandler(proxy)
    http_no_proxy_handler = urllib2.ProxyHandler({})

    proxySwitch = True # 代理开关

    if proxySwitch:
        opener = urllib2.build_opener(http_proxy_handler)
    else:
        opener = urllib2.build_opener(http_no_proxy_handler)

    request = urllib2.Request("http://www.baidu.com")

    response = opener.open(request)

    print response.read()

def urllib2_ProxyBasicAuthHandler():
    """urllib2
        私密代理
        HTTPPasswordMgrWithDefaultRealm(): 保存私密代理的用户名密码
        ProxyBasicAuthHandler(): 处理代理的身份验证
    """

    import urllib
    import urllib2

    # 私密代理用户名密码
    user = "username"
    pwd = "password"

    # 私密代理 IP
    proxyserver = "xxx.xxx.xxx.xxx:xxxx"

    # 1. 构建一个密码管理对象, 用来保存登录信息
    passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # 2. 添加私密代理信息
    passwdmgr.add_password(None, proxyserver, user=user, passwdmgr=pwd)

    # 3. 构建基于 ProxyBasicAuthHandler 的 opener
    proxy_auth_handler = urllib2.ProxyBasicAuthHandler(passwdmgr)

    # 4. 通过 build_opener() 创建自定义 opener
    opener = urllib2.build_opener(proxy_auth_handler)

    request = urllib2.Request('http://www.baidu.com')

    response = opener.open(request)

    print response.read()

def urllib2_HTTPBasicAuthHandler():
    """urllib2
        Web 客户端授权验证
        HTTPBasicAuthHandler
    """

    import urllib2

    # 登录信息
    user = "username"
    pwd = "password"
    webserver = "http://xxx.xxx.xxx.xxx"

    # 1. 构建一个密码管理对象, 用来保存登录信息
    passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # 2. 添加私密代理信息
    passwdmgr.add_password(None, webserver, user=user, passwdmgr=pwd)

    # 3. 构建基于 HTTPBasicAuthHandler 处理器对象
    http_auth_handler = urllib2.HTTPBasicAuthHandler(passwdmgr)

    # 4. 通过 build_opener() 创建自定义 opener
    opener = urllib2.build_opener(http_auth_handler)

    # 5. 通过 install_opener() 方法定义 opener 为全局 opener
    urllib2.install_opener(opener)

    # 6. 构建 Request 对象
    request = urllib2.Request(webserver)

    # 7. 定义 opener 为全局后, 可以直接使用 urlopen() 发送请求
    response = urllib2.urlopen(request)

    print response.read()

def urllib2_cookie():
    """urllib2
        cookie
    """

    import urllib2

    headers = {
        "Host": "www.renren.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "http://www.renren.com/",
        # "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cookie": "xxxxxxxxxxxx",
    }

    request = urllib2.Request("http://www.renren.com/", headers=headers)

    resposne = urllib2.urlopen(request)

    print resposne.read()

def urllib2_cookielib():
    """urllib2
        cookielib: 提供用于存储 cookie 的对象
        HTTPCookieProcessor: 构建处理 cookie 对象的 handler
    """

    import urllib2
    import cookielib

    # 构建一个 CookieJar 对象用于保存 cookie
    cookiejar = cookielib.CookieJar()

    # 使用 HTTPCookieProcessor() 来创建 cookie 处理器对象
    handler = urllib2.HTTPCookieProcessor(cookiejar)

    # 构建 opener 对象
    opener = urllib2.build_opener(handler)

    # 以 GET 访问页面, 访问后 cookie 会保存到 cookiejar 中
    opener.open("http://www.renren.com")

    # 打印 cookie
    cookieStr = ""

    for item in cookiejar:
        cookieStr = cookieStr + item.name + "=" + item.value + ";"

    print cookieStr

def urllib2_URLError():
    """urllib2
        URLError
    """

    import urllib2

    request = urllib2.Request('http://www.jklasfj.com')

    try:
        urllib2.urlopen(request, timeout=5)
    except urllib2.URLError, err:
        print err

def urllib2_HTTPError():
    """urllib2
        HTTPError
    """

    import urllib2

    request = urllib2.Request("http://www.jksdfjsal.com")

    try:
        urllib2.urlopen(request)
    except urllib2.HTTPError, err:
        print err.code
        print err
    except urllib2.URLError, err:
        print err



if __name__ == '__main__':
    urllib2_HTTPError()















