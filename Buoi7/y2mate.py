import requests
from File_Class import *
import shutil

link_direct = []
link_path = []
list_link = File_Interact('link.txt').read_file_list()

def download_video(url_download,file_name):
    file = url_download.split("file=")[-1]
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    data ={
        'file': file
    }
    res = requests.get(url_download, stream=True,timeout=10,headers=headers,data=data,verify=False)
    file_path = f".\\Video\\{file_name}"
    with open(file_path,'wb') as out_file:
        shutil.copyfileobj(res.raw,out_file)
    del res
    return file_path.replace('\\','/')

for index,link in enumerate(list_link):
    url_ajax = 'https://www.y2mate.com/mates/en56/analyze/ajax'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    data_ajax = {
        'url': link,
        'q_auto': 0,
        'ajax': 1
    }
    res_ajax = requests.post(url_ajax,headers=headers,data=data_ajax).text
    res_ajax = res_ajax.replace('\\','')

    String_Interact1 = String_Interact()
    _id = String_Interact1.regex_one_value('k__id = "(.*?)"',res_ajax)
    v_id = String_Interact1.regex_one_value('k_data_vid = "(.*?)"',res_ajax)
    fquality = String_Interact1.regex_many_value('<a href="#" rel="nofollow"> (.*?)p',res_ajax)

    url_convert = 'https://www.y2mate.com/mates/en56/convert'
    data_convert = {
        'type': 'youtube',
        '_id': _id,
        'v_id': v_id,
        'ajax': 1,
        'ftype': 'mp4',
        'fquality': fquality[0]
    }
    
    res_convert = requests.post(url_convert,headers=headers,data = data_convert).text
    res_convert = res_convert.replace('\\','')
    link = String_Interact1.regex_one_value('<a href="(.*?)"',res_convert)
    link_direct.append(link)
    name = 'video%s.mp4'%(index+1)
    path = download_video(link,name)
    link_path.append(path)

File_Excel1 = File_Excel('data.xlsx')
sheet_name = 'Sheet1'
File_Excel1.update_cell(sheet_name,'A1','Link Youtube')
File_Excel1.update_cell(sheet_name,'B1',"Direct Link")
File_Excel1.update_cell(sheet_name,'C1',"Link Path")

for index,link in enumerate(link_direct):
    link = list_link[index]
    direct = link_direct[index]
    path = link_path[index]
    cell_name_link ="A%s"%(index+2)
    cell_name_direct ="B%s"%(index+2)
    cell_name_path ="C%s"%(index+2)
    File_Excel1.update_cell(sheet_name,cell_name_link,link)
    File_Excel1.update_cell(sheet_name,cell_name_direct,direct)
    File_Excel1.update_cell(sheet_name,cell_name_path,path)