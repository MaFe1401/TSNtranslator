import json, time
import paramiko

#Get lldp data by ssh
def getLldp():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("192.168.4.51", username='sys-admin', password='sys-admin')
    
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('sudo lldpcli show neighbors -f json ',get_pty=True ) #ask for lldp neighbors
    ssh_stdin.write('sys-admin'+'\n')
    ssh_stdin.flush()
    time.sleep(1)
    data = ssh_stdout.readlines()
    error = ssh_stderr.readlines()
    del data[0:5]
    for line in data:
        print(line)
            
        
exec = getLldp()

#Get IP address from NIC-TSN
#def getNicIp():
    