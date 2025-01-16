print("Connecting via SSH => show interface status (brief)")
from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="devnetsandboxiosxe.cisco.com",
    port="22",
    username="admin",
    password="C1sco12345"
    )
output=sshCli.send_command("show ip interface brief")
print(output)
