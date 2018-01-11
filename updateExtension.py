import os
from configparser import ConfigParser

def updateAllPackage(packageDir, updateList):
  os.chdir(packageDir)
  for dir in updateList:
    if os.path.isdir(dir) and dir.startswith('.') == False:
      print(dir + ' -- 插件更新中...')
      installCommand = 'cd ' + dir + ' git checkout . && git pull && npm install'
      os.system(installCommand)

def update(select = 1, file = 'extension.conf'):
  print('配置读取中...')
  updateList = []
  cfg = ConfigParser()
  cfg.read(file)
  packageDir = cfg.get('PackageDir', 'address')
  extensionList = cfg.items('ExtensionList' if select == 1 else 'UpdateList')
  print('切换到atom插件目录--->')
  os.chdir(packageDir)
  for ex in extensionList:
    dirname = ex[0]
    updateList.append(dirname)
  # install(packageDir)
  updateAllPackage(packageDir, updateList)

if __name__=='__main__':
  update()
