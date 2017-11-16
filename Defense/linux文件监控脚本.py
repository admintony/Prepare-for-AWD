#!/usr/bin/python
#coding=utf-8
#Usage ：python demo.py
#Code by : AdminTony
#QQ : 78941695
#注意：要将此文件放在有读写权限的目录以及所有修改过的php必须在此目录或者该目录的子目录中。
#作用：读取被修改过的文件，然后将文件的地址加上内容全部存放在txt



import sys,subprocess,os
#查找最近10分钟被修改的文件
def scanfile():
	#command: find -name '*.php' -mmin -10
	command = "find -name \'*.php\' -mmin -10"
	su = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	STDOUT,STDERR = su.communicate()
	list = STDOUT.split("\n")
	#print str(list)
	#将文件处理成list类型然后返回。
	return list

#读取文件：
def loadfile(addr):
	data = ""
	#如果文件不存在就跳出函数
	try :
		file = open(addr,'r')
		data = file.read()
	except : 
		return 0
	all_data = addr+"\n"+data+"\n\n"
	file1 = open("shell.txt",'a+')
	#避免重复写入
	try:
		shell_content = file1.read()
	except:
		shell_content = "null"
	#如果文件内容不为空再写入，避免写入空的。
	#print shell_content
	if data :
		if all_data not in shell_content:
			file1.write(all_data)
	file.close()
	file1.close()
	rm_cmd = "rm -rf "+addr
	su = subprocess.Popen(rm_cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	su.communicate()
	print "loadfile over : "+addr

if __name__ == '__main__':
	while True:

		list = scanfile()
		if list :
			for i in range(len(list)):
				#如果list[i]为空就不读取了
				if list[i]:
					loadfile(str(list[i]))
		else : pass
