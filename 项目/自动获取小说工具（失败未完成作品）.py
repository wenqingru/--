#发送请求＆安装模块
#pip install requests
import requests

#发送目标
url="https://www.22biqu.com/biqu5669/5701978.html"
#伪装自己
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"}
#发送请求
resp=requests.get(url,headers=headers)
#设置编码
resp.encoding="utf-8"
#响应信息
print(resp.text)

