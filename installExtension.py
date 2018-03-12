import os
import json

def onlyInstallNew(packageDir, newExtensionList):
    os.chdir(packageDir)
    for dir in newExtensionList:
        if os.path.isdir(dir) and dir.startswith('.') == False:  # 如果这个名称是一个文件夹并且不是以.开头
            print(dir + '插件安装中...')
            installCommand = 'cd ' + dir + ' && npm install'
            os.system(installCommand)


def installPackage(file='extension.json'):
    print('配置读取中...')
    newExtensionList = []  # 定义的需要安装的包
    cfg = ''
    with open(file, 'r', encoding='utf-8') as file: # 读取文件
        cfg = json.loads(file.read())
    packageDir = cfg['packageDir']  # 获取atom的插件安装路径
    extensionList = cfg['packageList']  # 获取json文件中packageList
    print('切换到atom插件目录--->')
    os.chdir(packageDir)
    '''
    1. 如果当前已存在安装文件夹，删除这个文件夹或者跳过这个插件安装？？？
    2. 让conf只需要添加插件路径而不需要修改，在代码里管理哪些应该安装
  '''
    dirList = os.listdir()
    for name in extensionList:
        # 插件名: name
        packageAddress = extensionList[name]  # 插件地址
        if name not in dirList:
            gitCommand = 'git clone ' + packageAddress + ' ' + name + '&& cd ' + name + ' && npm install' # 执行git clone
            os.system(gitCommand)
    # onlyInstallNew(packageDir, extensionList)


if __name__ == '__main__':
    installPackage()
