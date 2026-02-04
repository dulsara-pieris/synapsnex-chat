def is_public_ip(ip):
        try:
                addr = ipaddress.ip_address(ip)
                return not addr.is_private
        except:
                return False
