import os
from configparser import ConfigParser

# 此函数废弃
def install(packageDir):
  os.chdir(packageDir)
  dirList = os.listdir()
  for dir in dirList:
    if os.path.isdir(dir) and dir.startswith('.') == False:
      print(dir + '插件安装中...')
      installCommand = 'cd ' + dir + ' && npm install'
      os.system(installCommand)

def onlyInstallNew(packageDir, newExtensionList):
    os.chdir(packageDir)
    for dir in newExtensionList:
      if os.path.isdir(dir) and dir.startswith('.') == False: # 如果这个名称是一个文件夹并且不是以.开头
        print(dir + '插件安装中...')
        installCommand = 'cd ' + dir + ' && npm install'
        os.system(installCommand)

def installPackage(file = 'extension.conf'):
  print('配置读取中...')
  newExtensionList = [] # 定义的需要安装的包
  cfg = ConfigParser()
  cfg.read(file) # 读取文件
  packageDir = cfg.get('PackageDir', 'address') # 获取atom的插件安装路径
  extensionList = cfg.items('ExtensionList') # 获取conf文件中ExtensionList
  print('切换到atom插件目录--->')
  os.chdir(packageDir)
  ''' 
    1. 如果当前已存在安装文件夹，删除这个文件夹或者跳过这个插件安装？？？
    2. 让conf只需要添加插件路径而不需要修改，在代码里管理哪些应该安装
  '''
  dirList = os.listdir()
  for ex in extensionList:
    dirname = ex[0] # 插件名
    packageAddress = ex[1] # 插件地址
    if dirname not in dirList:
      print(dirname)
      newExtensionList.append(dirname) # 把插件名称添加到单独数组中
      gitCommand = 'git clone ' + packageAddress + ' ' + dirname # 执行git clone
      os.system(gitCommand)
  onlyInstallNew(packageDir, newExtensionList) # 

if __name__=='__main__':
  installPackage()
