import requests
pro ={'https':'',
      'http': ''} #Enter the proxy server ip between the inverted commas
url='https://httpbin.org/ip'
r=requests.get(url, proxies=pro)
print(r.json())
