import re
import requests


# 数据清洗
def filter_html(html_str):
    # 小尾巴
    tips = '<p>—— 来自TesterHome官方 <a href="http://fir.im/p9vs" target="_blank">安卓客户端</a></p>'
    # 处理换行
    re_br = re.compile('<br\s*?/?>')
    # HTML标签
    re_h = re.compile('</?\w+[^>]*>')
    # url链接
    re_url = re.compile('[a-zA-z]+://[^\s]*')
    # 转义字符
    char_ = {'&lt;': '<', '&gt;': '>', '&amp;': '&', '&quot;': '"'}
    html_str = html_str.replace(tips, " ")
    html_str = re_br.sub(" ", html_str)
    html_str = re_h.sub(" ", html_str)
    html_str = re_url.sub(" ", html_str)
    for key_, values_ in char_.iteritems():
        html_str = html_str.replace(key_, values_)
    return html_str


# 获取精华帖列表:  /topics.json ()
# 接口返回分页有问题，放弃用这个接口
# topics_by_excellent_url = "https://testerhome.com/api/v3/topics.json"
# params = dict()
# params["type"] = "popular"
# params["offset"] = 20
# params["limit"] = 20
# topics_by_excellent_resp = requests.get(url=topics_by_excellent_url, timeout=30)
# topics_by_excellent_json = json.loads(topics_by_excellent_resp.content)
# print topics_by_excellent_json

def get_topic_number():
    base_url = 'https://testerhome.com/topics.json'
    base_resp = requests.get(url=base_url, timeout=30)
    if str(base_resp.status_code) != '200':
        raise Exception("返回值不是200,网络异常")
    else:
        html = base_resp.content
        print(type(html))
        re_type = re.compile(r'<li class="list-group-item">帖子数:(.*?)个</li>')
        print(str(html))
        result_list = re_type.findall(str(html))
        return len(result_list)


def get_excellent_topics(topic_number):
    pass


if __name__ == '__main__':
    print(get_topic_number())
