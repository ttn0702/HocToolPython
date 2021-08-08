from peewee import *
import requests
from File_Class import File_Interact

host='149.28.145.242'
db_name = 'btvn_nghia'
db_user='nghiahsgs4'
db_pass='123456'
db = MySQLDatabase(db_name,host=host, user=db_user, passwd=db_pass)

# model tuong ung voi table
class Score(Model):
    sbd = CharField()
    toan = FloatField()
    van = FloatField()
    anh = FloatField()
    is_run = IntegerField(default=0)
    class Meta:
        database=db


File_Interact1 = File_Interact('Log.txt')
# city_code: 1 - 64
# code: 1 - ...
def crawl_data(city_code):
    # 100 ma thi sinh lien tiep khong co du lieu thi dung o tinh do
    limit_check = 100
    list_sbd = []
    city_code_format = format(city_code,"0>2d")
    ma_thi_sinh = 1
    count = 0
    while True:
        try:
            code = format(ma_thi_sinh, "0>6d")
            sbd = '%s%s'%(city_code_format,code)
            url = f'https://diemthi.vnanet.vn/Home/SearchBySobaodanh?code={sbd}&nam=2021'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
            }
            res = requests.get(url,headers=headers).json()['result']
        
            ma_thi_sinh += 1
            if len(res) != 0:
                list_sbd.append(sbd)
                count = 0
                print(sbd)
            else:
                count += 1
        except Exception as err:
            err_thi_sinh = f'Loi o thi sinh {sbd}: {err}'
            File_Interact1.write_file_line(err_thi_sinh)
            continue

        if len(list_sbd) == 10000:
            try:
                data_source = [
                    {
                        'sbd' : i 
                    }
                    for i in list_sbd
                ]

                for batch in chunked(data_source,10000):
                    Score.insert_many(batch).execute()
                list_sbd = []

            except Exception as err:
                err_db = f'Loi: {err} tinh {city_code}'
                File_Interact1.write_file_line(err_db)
                
        if count < limit_check:
            continue
        else:
            break

    # Truong hop khong du so data con lai cua 1 tinh < 10000
    if len(list_sbd) != 0:
        try:
                data_source = [
                    {
                        'sbd' : i 
                    }
                    for i in list_sbd
                ]

                for batch in chunked(data_source,10000):
                    Score.insert_many(batch).execute()
                list_sbd = []

        except Exception as err:
            err_db = f'Loi: {err} tinh {city_code}'
            File_Interact1.write_file_line(err_db)

if __name__ == "__main__":
    Score.create_table()

