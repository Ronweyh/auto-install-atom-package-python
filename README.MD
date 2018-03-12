- atom插件被墙, 应用内无法下载, 通过git来执行安装可以快速安装, 通过python来执行git命令并到相应目录安装插件依赖

### 安装插件
```bash
python3 installExtension.py
```
### 更新插件(默认更新所有通过conf文件安装的插件)
```bash
python3 updateExtension.py
```

**extension.json为配置文件**

1. PackageDir的address为atom的插件路径, Mac与windows有差别, 修改为正确路径即可(默认是个人Mac路径)
2. packageList是插件名(key)和仓库地址(value), 根据自己需求添加即可
3. git和npm建议设置代理, 不然依然很慢(git需要ss之类代理)
- npm config set registry https://registry.npm.taobao.org
- git config --global http.https://github.com.proxy socks5://127.0.0.1:1080

### 功能
- [x] 修改clone目录名, 防止插件无效
- [x] 更新插件
