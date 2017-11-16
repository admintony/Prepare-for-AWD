# AWD线下赛脚本集合
## 目录结构
<pre><code>
###########
├── Readme.md               // 帮助文档 
├── Attack                  // 批量&攻击型脚本
│   ├── GetFlag.py          //用shell来批量getflag
│   ├── upload_shell.py     //批量上传不死马并激活
│   ├── 命令生成不死马_批量版.py  //调用system函数来执行shell命令生成不死马
│   ├── 隐藏不死马测试版.php     //生成并隐藏文件
│   ├── 不死马.php          // PHP一直生成webshell
│   ├── 命令生成不死马.txt   // 用linux命令一直生成不死马
│   ├── ListCreate.php      //生成本集合中脚本所需要的list
├── Defense                 //堡垒机防护脚本
|   |—— linux文件监控脚本.py //监控最近10分钟被修改的php文件并删除
|   |—— 克制不死马.txt       //克制不死马的方法
|   |—— Web日志安全分析工具+v2.0.rar  //可以直接导入apache等日志进行分析
|   |—— waf.php             //记录所有的敏感请求-别人的
├── attack_python           //攻击模块集合
|—————— plugin	            //攻击插件目录
|   |—— awd_attack.py	      //主程序
|   |—— shell.php	          //upload上传的马，只支持普通马
|   |—— shell1.php	        //upload1上传的马，只支持不是马
|   |—— tips.txt	          //比赛中要修改的点
|   |—— webshell.txt        //shell_list的样本
</code></pre>

