# HTTP API Test

- HTTP 协议
- 常见接口调用方式
- 使用requests 库调用

## HTTP 协议

最原始的协议:

```
GET / HTTP/1.1
Host: httpbin.org
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4
Cookie: _ga=GA1.2.475070272.1480418329; _gat=1
```



```
HTTP/1.1 200 OK
Server: nginx
Date: Tue, 29 Nov 2016 13:08:38 GMT
Content-Type: application/json
Content-Length: 203
Connection: close
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true

{
  "args": {},
  "headers": {
    "Host": "httpbin.org",
    "User-Agent": "Paw/2.3.1 (Macintosh; OS X/10.11.3) GCDHTTPRequest"
  },
  "origin": "13.75.42.240",
  "url": "https://httpbin.org/get"
}
```

其中：

- Host 是请求报头域，用于指定被请求资源的 Internet 主机和端口号，它通常从 HTTP URL 中提取出来；
- Connection 表示连接状态，keep-alive 表示该连接是持久连接（persistent connection），即 TCP 连接默认不关闭，可以被多个请求复用，如果客户端和服务器发现对方有一段时间没有活动，就可以主动关闭连接；
- Cache-Control 用于指定缓存指令，它的值有 no-cache, no-store, max-age 等，`max-age=秒`表示资源在本地缓存多少秒；
- User-Agent 用于标识请求者的一些信息，比如浏览器类型和版本，操作系统等；
- Accept 用于指定客户端希望接受哪些类型的信息，比如 text/html, image/gif 等；
- Accept-Encoding 用于指定可接受的内容编码；
- Accept-Language 用于指定可接受的自然语言；
- Cookie 用于维护状态，可做用户认证，服务器检验等

## HTTP 请求方法

|方法|描述|说明|
|GET|/url||
|POST|/url|with body|
|PUT|/url|with body|
|DELETE|/url||
|HEAD|/url||
|OPTIONS|/url||

- **状态行**
- **响应头**
- **响应报文**

```
HTTP/1.1 200 OK
```

其中，`200` 是状态码，表示客户端请求成功，`OK` 是相应的状态描述。

状态码是一个三位的数字，常见的状态码有以下几类：

- 1XX 消息 -- 请求已被服务接收，继续处理
- 2XX 成功 -- 请求已成功被服务器接收、理解、并接受
    - 200 OK
    - 201 Created 已创建
    - 202 Accepted 接收
    - 203 Non-Authoritative Information 非认证信息
    - 204 No Content 无内容
- 3XX 重定向 -- 需要后续操作才能完成这一请求
    - 301 Moved Permanently 请求永久重定向
    - 302 Moved Temporarily 请求临时重定向
    - 304 Not Modified 文件未修改，可以直接使用缓存的文件
    - 305 Use Proxy 使用代理
- 4XX 请求错误 -- 请求含有词法错误或者无法被执行
    - 400 Bad Request 由于客户端请求有语法错误，不能被服务器所理解
    - 401 Unauthorized 请求未经授权。这个状态代码必须和WWW-Authenticate报头域一起使用
    - 403 Forbidden 服务器收到请求，但是拒绝提供服务。服务器通常会在响应正文中给出不提供服务的原因
    - 404 Not Found 请求的资源不存在，例如，输入了错误的URL
- 5XX 服务器错误 -- 服务器在处理某个正确请求时发生错误
    - 500 Internal Server Error 服务器发生不可预期的错误，导致无法完成客户端的请求
    - 503 Service Unavailable 服务器当前不能够处理客户端的请求，在一段时间之后，服务器可能会恢复正常
    - 504 Gateway Time-out 网关超时

## 参考资料

- [超文本传输协议 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E8%B6%85%E6%96%87%E6%9C%AC%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE#HTTP.2F1.1)
- [HTTP 协议入门 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2016/08/http.html)
- [HTTP幂等性概念和应用 | 酷 壳 - CoolShell.cn](http://coolshell.cn/articles/4787.html)
- [Http协议详解 - 简书](http://www.jianshu.com/p/e83d323c6bcc)
- [When to use PUT or POST - The RESTful cookbook](http://restcookbook.com/HTTP%20Methods/put-vs-post/)
- [To PUT or POST?](https://stormpath.com/blog/put-or-post)
- [全面解读HTTP Cookie](http://www.webryan.net/2011/08/wiki-of-http-cookie/)
- [HTTP cookies 详解 | bubkoo](http://bubkoo.com/2014/04/21/http-cookies-explained/)
- [HTTP 接口设计指北](https://github.com/bolasblack/http-api-guide)


[tcp]: https://zh.wikipedia.org/wiki/%E4%BC%A0%E8%BE%93%E6%8E%A7%E5%88%B6%E5%8D%8F%E8%AE%AE