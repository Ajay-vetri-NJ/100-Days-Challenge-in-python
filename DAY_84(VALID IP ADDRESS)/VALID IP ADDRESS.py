import re

def validate_ip_address(ip):
    ipv4_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    ipv6_pattern = re.compile(r'^(([0-9a-fA-F]{1,4}):){7}([0-9a-fA-F]{1,4})$')
    
    if ipv4_pattern.match(ip):
        return "IPv4"
    elif ipv6_pattern.match(ip):
        return "IPv6"
    else:
        return "Neither"

ip_address = input("Enter an IP address to validate: ")

result = validate_ip_address(ip_address)
print(f"The IP address is: {result}")
