### EXAMPLE
> atom插件被墙, 应用内无法下载, 通过git来执行安装可以快速安装, 通过python来执行git命令并到相应目录安装插件依赖

**extension.conf为配置文件**
1. PackageDir的address为atom的插件路径, Mac与windows有差别, 修改为正确路径即可(默认是Mac路径)
2. ExtensionAddress的address为插件git仓库地址, 以逗号形式隔开, 根据自己需求添加即可
3. git和npm建议设置代理, 不然依然很慢