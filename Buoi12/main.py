import requests
from utils_db import *
from File_Class import File_Interact

File_Interact1 = File_Interact('Log.txt')
# city_code: 1 - 64
# code: 1 - ...

list_sbd = []
for i in range(1,65):
    city_code = format(i,"0>2d")
    ma_thi_sinh = 1
    count = 0
    while True:
        try:
            code = format(ma_thi_sinh, "0>6d")
            sbd = '%s%s'%(city_code,code)
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
                except Exception as err:
                    loi = f'Loi: {err}'
                    File_Interact1.write_file_line(loi)
                finally:
                    list_sbd = []

            if count < 100:
                continue
            else:
                break

        except Exception as err:
            loi = f'Loi o thi sinh {sbd}: {err}'
            File_Interact1.write_file_line(loi)
            continue

    
            