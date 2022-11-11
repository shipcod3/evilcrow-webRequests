import requests

crow_url = "http://192.168.4.1:80/setjammer"
crow_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://192.168.4.1", "Connection": "close", "Referer": "http://192.168.4.1/jammer", "Upgrade-Insecure-Requests": "1"}
crow_data = {"module": "1", "frequency": "434.17", "powerjammer": "1", "configmodule": "2"}
requests.post(crow_url, headers=crow_headers, data=crow_data)