import paramiko
import sys
import threading
def ssh(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=0.5)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        #print('This is stdin:',stdin)
        #print('This is stderr:',stderr)
        for x in stdout.readlines():
            print('%s\t%s'%(ip,x),end='')
    except:
        print('%s\terror'%(ip))

cmd=input('请输入你想执行的命令:')
#f=open('mac.xls','w')
#sys.stdout=f
#threads=[]
#username='root'
#passwd='123456'
#cmd='cat /sys/class/net/eth0/address'
for i in range(220,230):
    ip='192.168.31.'+str(i)
    ssh(ip,'root','123456',cmd)
print('执行完毕..')
#f.close() 
