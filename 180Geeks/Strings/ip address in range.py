ipRange = '10.10.0.0'
ipAddress = '10.10.2.3'

# def check(range,ip_address):
#     range_1 = range.split(".")
#     ip_address = range.split(".")
#
#     for i in range
#
#     # print(range_1, ip_address)
#
# check(range, ip_address)
#
# from ipaddress import ip_network, ip_address
#
# net = ip_network("1.1.0.0/16")
# print(ip_address("1.1.2.2") in net)


def isIPInRange(ipRange, ipAddress):
    new_ipRange = ipRange.split(".")
    new_ipRange2 = []
    for i in range(len(new_ipRange)):
        if new_ipRange[i] == '0':
            new_ipRange2.append('255')
        else:
            new_ipRange2.append(new_ipRange[i])

    new_ipRange = '.'.join(new_ipRange)
    new_ipRange2 = '.'.join(new_ipRange2)

    if ipAddress >= new_ipRange and ipAddress <= new_ipRange2:
        return True
    else:
        return False

isIPInRange(ipRange,ipAddress)

# def convert_ipv4(ip):
#     return tuple(int(n) for n in ip.split('.'))
#
# def check_ipv4_in(ip_address, start, end):
#     return convert_ipv4(start) < convert_ipv4(ip_address) < convert_ipv4(end)
#
# print(check_ipv4_in(ip_address, range[0], range[1]))