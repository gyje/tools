# 单进程顺序执行,目前没有对写入的json做美化,json直接压缩了

import requests,time,json,base64
#apikey请自己申请
ss_png=["http://api.wwei.cn/dewwei.html?data=http://freess.org/images/servers/jp01.png&apikey=xxx","http://api.wwei.cn/dewwei.html?data=http://freess.org/images/servers/jp02.png&apikey=xxx","http://api.wwei.cn/dewwei.html?data=http://freess.org/images/servers/jp03.png&apikey=xxx","http://api.wwei.cn/dewwei.html?data=http://freess.org/images/servers/us01.png&apikey=xxx","http://api.wwei.cn/dewwei.html?data=http://freess.org/images/servers/us02.png&apikey=xxx","http://api.wwei.cn/dewwei.html?data=http://freess.org/images/servers/us03.png&apikey=xxx"]
info_list=[]
def get_info(url):
	a=requests.get(url).json()
	ss_info=base64.b64decode(a["data"]["raw_text"][5:]).decode()
	temp=ss_info.split(":",1)
	ss_encrypt=temp[0]
	ss_password=temp[1].split("@")[0]
	ss_username=temp[1].split("@")[1].split(":")[0]
	ss_port=temp[1].split("@")[1].split(":")[1].strip("\n")
	info_dict={}
	info_dict["server"]=ss_username
	info_dict["server_port"]=ss_port
	info_dict["password"]=ss_password
	info_dict["method"]=ss_encrypt
	info_dict["remarks"]=url[69:73]#freess图片url提取服务器信息
	info_dict["timeout"]=5
	info_list.append(info_dict)
s=time.time()
for i in range(6):
	get_info(ss_png[i])
#修改为自己的ss配置文件路径
with open("F:\Myfile\SS\Shadowsocks-4.0.4\gui-config.json","r") as origin_fob:
	content=json.loads(origin_fob.read())
	content["configs"]=info_list
with open("F:\Myfile\SS\Shadowsocks-4.0.4\gui-config.json","w") as new_fob:
	new_fob.write(json.dumps(content))
print (time.time()-s)
