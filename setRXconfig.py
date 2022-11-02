import requests

crow_url = "http://192.168.4.1:80/setrx"
crow_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://192.168.4.1", "Connection": "close", "Referer": "http://192.168.4.1/rxconfig", "Upgrade-Insecure-Requests": "1"}
crow_data = {"module": "1", "mod": "2", "frequency": "433.92", "setrxbw": "58", "deviation": "0", "datarate": "5", "configmodule": "4"}
requests.post(crow_url, headers=crow_headers, data=crow_data)