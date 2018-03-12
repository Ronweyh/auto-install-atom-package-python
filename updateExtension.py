import os
import sys
import json

def updateAllPackage(packageDir, updateList):
    os.chdir(packageDir)
    for dir in updateList:
        if os.path.isdir(dir) and dir.startswith('.') == False:
            print(dir + ' -- 插件更新中...')
            installCommand = 'cd ' + dir + ' && git checkout -f && git pull && npm install'
            os.system(installCommand)


def update(select="1", file="extension.json"):
    print('配置读取中...')
    cfg = ''
    with open(file, 'r', encoding='utf-8') as file:
        cfg = json.loads(file.read())
    packageDir = cfg['packageDir']
    extensionList = cfg['packageList'] # 读取配置
    exNames = extensionList.keys()
    print('切换到atom插件目录--->')
    os.chdir(packageDir)
    # install(packageDir)
    updateAllPackage(packageDir, exNames)

if __name__ == '__main__':
    args = sys.argv
    length = len(args) # 获取命令行参数，从1开始
    update(args[1] if length > 1 and args[1] != None else '1')
