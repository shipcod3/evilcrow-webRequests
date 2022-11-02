import requests

resp = requests.get("http://192.168.4.1/viewlog")
print(resp.content)
