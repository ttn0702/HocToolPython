import requests
from bs4 import BeautifulSoup
from peewee import *

# huond dan cho mysql nam o localhost
host='localhost'
db_name = 'btvn11'
db_user='root'
db_pass=''
db = MySQLDatabase(db_name,host=host, user=db_user, passwd=db_pass)

# model tuong ung voi table
class crawl_nghiahsgs(Model):
    link = CharField()
    title = TextField()
    class Meta:
        database=db

page_number = 1
list_url_total = []
list_title_total = []

while True:
    url =f'http://nghiahsgs.com/page/{page_number}/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Cookie': '_ga=GA1.2.1345430268.1624012111; _gid=GA1.2.1521922581.1626064523'
    }
    data = requests.get(url,headers=headers).text
    soup = BeautifulSoup(data,'lxml')
    list = soup.findAll("h2",{"class":"entry-title"})
    if(len(list) == 0 ):
        break
    else:
        for i in list:
            url = i.a.get("href")
            title = i.a.text
            list_url_total.append(url)
            list_title_total.append(title)
    page_number += 1

for i in range(0,len(list_title_total)):
    # insert rows to table
    link1 = list_url_total[i]
    title1 = list_title_total[i]
    instance = crawl_nghiahsgs(link= link1,title= title1)
    instance.save()