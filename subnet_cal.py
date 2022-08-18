
from operator import ne
import masks

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
    network['No. of Hosts/Subnet'] = (2 ** (32 - bits)) - 2
    network['Number of Subnets'] = 2 ** bits
    if bits > 30:
        network['host range'] = '-'
        network['broadcast'] = '-'
        network['Wildcard Mask'] = '-'
        network['CIDR Notation'] = '-'
        return network
    network['host range'] = str(decimal(subnet(ip, bits))).replace("[", "").replace(", ", ".").replace("]", "") + ' - ' + str(decimal(subnet(ip, bits, '1', '0'))).replace("[", "").replace(", ", ".").replace("]", "")
    network['broadcast'] = str(decimal(subnet(ip, bits, '1', '1'))).replace("[", "").replace(", ", ".").replace("]", "")
    network['Wildcard Mask'] = masks.wildcard_mask[str(bits)]
    network['CIDR Notation' ] = str(decimal(subnet(ip, bits, '0', '0'))).replace("[", "").replace(", ", ".").replace("]", "") + '/' + str(bits)
    return network



