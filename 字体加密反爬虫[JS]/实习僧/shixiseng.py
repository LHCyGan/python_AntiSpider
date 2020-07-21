import requests
from bs4 import BeautifulSoup

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}


def detail_url(url):
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    # 获取职位名称
    title = soup.title.text
    # 获取公司名称
    company_name = soup.select('.com_intro .com-name')[0].string
    # 获取薪资
    salary = soup.select('.job_money.cutom_font')[0].string.encode('utf-8')
    salary = salary.replace(b'\xee\x86\xa7', b'1')
    salary = salary.replace(b'\xef\xa3\xad', b'0')
    salary = salary.replace(b'\xef\x81\x9b', b'5')
    salary = salary.replace(b'\xef\x88\x9f', b'2')
    salary = salary.replace(b'\xef\x9f\xac', b'3')
    salary = salary.decode()
    print(title, company_name, salary, sep='\t')


def crawl():
    for i in range(1, 5):
        html = requests.get("https://www.shixiseng.com/interns?page={}&keyword=python".format(i),
                            headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')
        offers = soup.select('.intern-wrap.intern-item')
        for offer in offers:
            url = offer.select('.f-l .intern-detail__job a')[0].get('href')
            # print(url)
            detail_url(url)


if __name__ == '__main__':
    crawl()


