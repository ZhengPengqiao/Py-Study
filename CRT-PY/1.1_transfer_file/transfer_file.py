# $language = "python"
# $interface = "1.0"

import os
import sys

# 此方法表示你必须先登录一台服务器然后再去telnet到另外一台服务器
# 主机的ip
host = '192.168.137.3'
# 主机的用户名
user = 'zpq'
# 主机的密码
passwd = 'zpq'
# 本地文件名字
herefilename = crt.Arguments.GetArg(0)
# 主机中文件路径
routefilename = crt.Arguments.GetArg(1)


def main():
    crt.Screen.Send('rm '+ herefilename +' \r')
    crt.Screen.Send('ftpget -u '+user+' -p '+ passwd +' '+ host +'  '+ herefilename +' '+ routefilename +' \r')
    crt.Screen.Send('chmod 755 '+ herefilename +' \r')
    crt.Screen.Send('sync \r')
    crt.Dialog.MessageBox(herefilename + ' transfer ok!')

main()