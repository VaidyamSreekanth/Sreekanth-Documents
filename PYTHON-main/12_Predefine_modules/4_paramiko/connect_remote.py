'''
1. Praramiko module is used to do operations on remote machine.
2. used to run commands on remote host and copy file from local to remote and remote to local.
1. To install module ==> python -m pip install paramiko
'''
import paramiko

h_name = '10.122.32.135'
u_name ='smellamp'
p_word = '8Aug2019'
port_no = 22   # ssh port

# To create ssh object
ssh = paramiko.SSHClient()

## To Add unknown host automaticllay 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# To create a connection on remote machine
ssh.connect(h_name, username=u_name, password=p_word, port=port_no)

# To run commnd on remote host 
stdin, stdout, stderr = ssh.exec_command('ls /home/smellam')

## To get command output
print(' \n stdout is ::', stdout.readlines())

## To get error message if any failures 
print(' \n stderr is ::', stderr.read())
ssh.close()

