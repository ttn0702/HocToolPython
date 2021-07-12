import requests
from File_Class import *
from bs4 import BeautifulSoup

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

#Luu du lieu vao file data.xlsx
File_Excel1 = File_Excel('data.xlsx')
sheet_name = 'Sheet1'
File_Excel1.update_cell(sheet_name,'A1','URL')
File_Excel1.update_cell(sheet_name,'B1',"Title")
for i in range(1,len(list_url_total)):
        url = list_url_total[i]
        title = list_title_total[i]
        cell_name_url ="A%s"%(i+1)
        cell_name_title ="B%s"%(i+1)
        File_Excel1.update_cell(sheet_name,cell_name_url,url)
        File_Excel1.update_cell(sheet_name,cell_name_title,title)