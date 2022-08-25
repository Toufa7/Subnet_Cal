def ipIsValid(ip):
    i = 0
    while (i < len(ip)):
        if ((ip[i] > '9' or ip[i] < '0') and ip[i] != '.'):
            return False
        if (ip[i] == '.' and i + 1 < len(ip) and ip[i + 1] =='.'):
            return False
        i += 1
    classes = list(ip.split('.'))
    for e in classes:
        if (len(e) > 3 or int(e) < 0 or int(e) > 255):
            return False
    return True
