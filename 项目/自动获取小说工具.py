#发送请求
import requests
ur1="https://www.hen0.com/book/586367/121288178.html"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"}
resp=requests.get(ur1,headers=headers)
resp.encoding="utf-8"
#响应信息
print(resp.text)
#保存