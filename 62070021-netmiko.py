from netmiko import ConnectHandler
import re

device_ip = '10.0.15.101'
username = 'admin' 
password = 'cisco'

device_params = {'device_type': 'cisco_ios',
                'ip': device_ip,
                'username': username,
                'password': password,
                }

createloop = ["int lo62070021",
              "ip add 192.168.1.1 255.255.255.0",
              "no sh"]

deleteloop = ["no int lo62070021"]

with ConnectHandler(**device_params) as ssh:
    result = ssh.send_command("sh ip int br")
    output = result.strip().split('\n')
    for line in output:
        if (line[23:34] != "192.168.1.1" and line[0:15] != "Loopback62070021"):
            result = ssh.send_config_set(createloop)
        else:
            ssh.send_config_set(deleteloop)
            print("already have")
        


# with ConnectHandler(**device_params) as ssh:
#     result = ssh.send_config_set(createloop)
#     print(result)