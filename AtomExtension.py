import os
from configparser import ConfigParser

def install(packageDir):
    os.chdir(packageDir)
    dirList = os.listdir()
    for dir in dirList:
        if os.path.isdir(dir) and dir.startswith('.') == False:
            print(dir + '插件安装中...')
            installCommand = 'cd ' + dir + ' && npm install'
            os.system(installCommand)

def readConfig(file='extension.conf'):
    print('配置读取中...')
    cfg = ConfigParser()
    cfg.read(file)
    packageDir = cfg.get('PackageDir', 'address')
    extensionList = cfg.get('ExtensionAddress', 'address').split(',')
    print('切换到atom插件目录--->')
    os.chdir(packageDir)
    for extension in extensionList:
        gitCommand = 'git clone ' + extension
        os.system(gitCommand)
    install(packageDir)

if __name__=='__main__':
    readConfig()
