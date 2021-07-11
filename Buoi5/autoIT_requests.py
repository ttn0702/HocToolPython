import requests 

# GET (cookie, user-agent)
url = 'https://autoitvn.com/'
headers_get = {
    'cookie': '__gads=ID=8a4ba8c3016a3881-226fbdec36ca0075:T=1625757636:RT=1625757636:S=ALNI_MZjZTQq8AoUfh9ZagQor6veo8DUSA; xf_session=120df9f23354670f7880f9149fb7d502',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
res = requests.get(url,headers = headers_get )
data = res.text
status_code_get = res.status_code
print('status_code_get ',status_code_get)

# POST -- cần truyền vào data login (login,password)
url_requests = 'https://autoitvn.com/login/login'
headers_post = {
    'cookie': '__gads=ID=8a4ba8c3016a3881-226fbdec36ca0075:T=1625757636:RT=1625757636:S=ALNI_MZjZTQq8AoUfh9ZagQor6veo8DUSA; xf_session=fa14f338041d4346d1739d449c7adeb3',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
form_data = {
    'login': 'tansang7171@gmail.com',
    'password': 'trungnghia11'
}
res_post = requests.post(url_requests,headers=headers_post,data = form_data)
data_post = res_post.text
status_code_post = res_post.status_code
print('status_code_post ',status_code_post)