from typing import Text
from requests_futures.sessions import FuturesSession



def send_request_at_the_same_time(max_workers,type_request,list_url,list_headers,list_timeout,list_data_post):
    '''
    type_request:
    1: get text
    2: get json
    3: post text
    4: post json
    '''
    session = FuturesSession(max_workers=max_workers)

    # Step 1: send request
    nb_request = len(list_url)
    list_future = []
    for i in range(nb_request):
        url = list_url[i]
        headers = list_headers[i]
        timeout = list_timeout[i]
        data_post = list_data_post[i]
        if type_request == 1:
            future = session.get(url,headers=headers,timeout=timeout)
        elif type_request == 2:
            future = session.get(url,headers=headers,timeout=timeout)
        elif type_request == 3:
            future = session.post(url,headers=headers,timeout=timeout,data=data_post)
        elif type_request == 4:
            future = session.get(url,headers=headers,timeout=timeout,json=data_post)
        list_future.append(future)

    # Step 2: get results
    list_status_code = []
    list_data = []
    for future in list_future:
        try:
            #get ket qua tra ve co the gay ra loi
            res = future.result()
            list_status_code.append(res.status_code)
            if type_request==1:
                list_data.append(res.text)
            elif type_request==2:
                list_data.append(res.json())
            elif type_request==3:
                list_data.append(res.text)
            elif type_request==4:
                list_data.append(res.json())
        except:
            list_status_code.append(404)
            list_data.append('')


    # Step 3: analysics
    nb_success_request = list_status_code.count(200)
    nb_fail_request = len(list_status_code)-nb_success_request
    return list_data,nb_success_request,nb_fail_request

if __name__ == "__main__":
    # problem: send 1000 request to this url
    max_workers = 100
    type_request = 4
    
    nb_request = 1000
    list_url = ['http://localhost:3009']*nb_request
    list_headers = [
        {
            'Connection':'keep-alive',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
        }
    ]*nb_request
    list_timeout = [5]*nb_request
    list_data_post = [
        {
            "name":i
        } for i in range(nb_request)
    ]
    list_data,nb_success_request,nb_fail_request = send_request_at_the_same_time(max_workers,type_request,list_url,list_headers,list_timeout,list_data_post)
