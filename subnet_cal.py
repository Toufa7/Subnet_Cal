
from operator import ne
import masks


def ipIsValid(ip):
    i = 0
    while (i < len(ip)):
        if ((ip[i] > '9' or ip[i] < '0') and ip[i] != '.'):
            return False
        if (ip[i] == '.' and i + 1 < len(ip) and ip[i + 1] =='.'):
            return False
        i += 1
    classes = list(ip.split('.'))
    if (len(classes) != 4):
        return False
    for e in classes:
        if (len(e) > 3 or int(e) < 0 or int(e) > 255):
            return False
    return True


def subnet(address, bit, n1='0', n2='1'):
    net = list()
    i = 0
    j = bit % 8
    while (i < int(bit / 8)):
        net.append(address[i])
        i += 1
    while (i < 4):
        if (i == 3):
            net.append(address[i][:j] + (n1 * (7 - j)) + n2)
        else:
            net.append(address[i][:j] + (n1 * (8 - j)))
        i += 1
        j = 0
    return net

def decimal(address):
    net = list()
    for e in address:
        net.append(int(e, 2))
    return net

def	binary(ip):
	i = 0
	while i < 4:
		ip[i] = "{0:b}".format(ip[i])
		diff = 8 - len(ip[i])
		ip[i] = ('0' * diff) + ip[i]
		i += 1



def subnet_calc(ip, bits):
    network = {}
    ip = list(map(int, ip.split('.')))
    binary(ip) # convert ip to binary
    if bits > 30:
        network['min host'] = '-'
        network['max host'] = '-'
        network['broadcast'] = '-'
        network['Wildcard Mask'] = '-'
        network['CIDR Notation'] = '-'
        network['No. of Hosts/Subnet'] = '-'
        network['Number of Subnets'] = '-'
        return network
    network['min host'] = str(decimal(subnet(ip, bits))).replace("[", "").replace(", ", ".").replace("]", "")
    network['max host'] = str(decimal(subnet(ip, bits, '1', '0'))).replace("[", "").replace(", ", ".").replace("]", "")
    network['No. of Hosts/Subnet'] = (2 ** (32 - bits)) - 2
    network['Number of Subnets'] = 2 ** bits
    network['broadcast'] = str(decimal(subnet(ip, bits, '1', '1'))).replace("[", "").replace(", ", ".").replace("]", "")
    network['Wildcard Mask'] = masks.wildcard_mask[str(bits)]
    network['CIDR Notation' ] = str(decimal(subnet(ip, bits, '0', '0'))).replace("[", "").replace(", ", ".").replace("]", "") + '/' + str(bits)
    return network



