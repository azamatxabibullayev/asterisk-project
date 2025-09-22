import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:8088/ari/asterisk/info"
auth = HTTPBasicAuth('ariuserA', 'aripassA')

r = requests.get(url, auth=auth)
print(r.json())
