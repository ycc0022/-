import requests

base_url = 'http://13.126.64.70:8090/noise/ffit/userInfo/getUserInfo'
r = requests.post(base_url)
code = r.status_code
text = r.text
print(code)
print(text)·