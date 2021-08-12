import requests

def get_score(sbd):
    try:
        url = f'https://diemthi.vnanet.vn/Home/SearchBySobaodanh?code={sbd}&nam=2021'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
        }
        res = requests.get(url,headers=headers).json()['result'][0]
        
        toan = res['Toan']
        van = res['NguVan']
        anh = res['NgoaiNgu']
        return toan, van,anh
    except Exception as e:
        err_thi_sinh = f'Loi o thi sinh {sbd}: {e}'
        print(err_thi_sinh)
        return -1, -1,-1

def handle_one_row(row):

    print('current row',row)
    
    # Step1 : handle job = > get data
    sbd = row.sbd
    toan,van,anh = get_score(sbd)

    # Step 2: update data
    row.toan = toan
    row.van = van
    row.anh = anh
    row.save()

if __name__ =="__main__":
    sbd = '02010001'
    toan, van,anh = get_score(sbd)
