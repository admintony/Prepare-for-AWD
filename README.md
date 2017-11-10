# AWD线下赛脚本集合
## 目录结构
<code>
###########
├── Readme.md               // 帮助文档 
├── Attack                  // 批量&攻击型脚本
│   ├── 不死马.php          // PHP一直生成webshell
│   ├── 命令生成不死马.txt   // 用linux命令一直生成不死马
├── Defense                 //堡垒机防护脚本
|   |—— linux文件监控脚本.py //监控最近10分钟被修改的php文件并删除
|   |—— 克制不死马.txt       //克制不死马的方法
</code>

<code>
###########
├── Readme.md               //帮助文档 
├── console.py              //启动
├── core                    // 核心模块
│   ├── shells.py           //写入，读取，保存webshell
│   ├── flag.py             // 获取，提交flag
│   ├── iplist.py           // 生成ip列表   
│—— auxi                    //辅助模块
|   |—— upload.py           //webshell上传功能
|   |—— shell.php           //默认上传文件
|   |—— webshell.txt        //一句话储存路径  
</code>
