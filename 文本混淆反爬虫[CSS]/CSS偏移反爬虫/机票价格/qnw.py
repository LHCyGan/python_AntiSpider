import requests
import re
from parsel import Selector

def get_price():
    url = "http://www.porters.vip/confusion/flight.html"
    resp = requests.get(url)
    soup = Selector(resp.text)
    em = soup.css("em.rel").extract()
    # 定位b标签和p标签
    for element in em:
        element = Selector(element)
        # 定位所有b标签
        element_b = element.css('b').extract()
        b1 = Selector(element_b.pop(0))
        # 获取第一个<b>标签中的值（列表）
        base_price = b1.css("i::text").extract()
    # 提取其他b标签的偏移量和数字
    alternate_price = []
    for eb in element_b:
        eb = Selector(eb)
        # 提取b标签的style的属性值
        style = eb.css('b::attr("style")').get()
        # 获得具体位置
        position = ''.join(re.findall('left:(.*?)px', style))
        # 获取该标签下的数字
        value = eb.css("b::text").get()
        # 将b标签的位置信息和数字以字典的格式添加到替补票价列表中
        alternate_price.append({'position': position, 'value':value})
    # 根据偏移量决定基准数据列表的覆盖元素
    for al in alternate_price:
        position = int(al.get('position'))
        value = al.get('value')
        # 判断位置的数值是否为正数
        plus = True if position >= 0 else False
        # 计算下标，以16px为基准
        index = int(position / 16)
        # 替换第一对b标签值列表中的元素，完成值覆盖操作
        base_price[index] = value
    print(base_price)


if __name__ == '__main__':
    get_price()