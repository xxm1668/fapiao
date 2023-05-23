import json
import urllib.parse
import urllib.request
import requests
url = "http://172.16.19.81:8024/onlyou/m_classify_fapiao"  # 11.10.10.2 根据实际启动配 置的ip设置
urldict = dict()
urldict['text'] = '苹果'
data = bytes(urllib.parse.urlencode(urldict), encoding='utf8')
# response = urllib.request.urlopen(url, data=urldict)
response = requests.post(url, data=urldict)
res_dict = json.loads(response.text.decode('utf-8'))
print('res_dict', res_dict)
