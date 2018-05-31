import re


def ip_to_bits(ip):
    """Returns 32 bits when provided an IP"""
    current = 1
    bits = ""
    octet = {}
    octet[1] = re.search("(?<!\d)\d*(?=\.)", ip).group()
    octet[2] = re.search("(?<=" + octet[1] + "\.)\d*(?=\.)", ip).group()
    octet[3] = re.search("(?<=" + octet[1] + "\." + octet[2] + "\.)\d*(?=\.)", ip).group()
    octet[4] = re.search("(?<=" + octet[1] + "\." + octet[2] + "\." + octet[3] + "\.)\d*(?!=(\.|\d))", ip).group()
    for x in range(1, 5):
        octet[x] = int(octet[x])
        value = 256
        for y in range(0, 8):
            value = value / 2
            if octet[x] >= value:
                octet[x] -= value
                bits = bits + "1"
            else:
                bits = bits + "0"
    return bits


def bits_to_ip(bits):
    '''
    Returns an IP when provided 32 bits
    :param bits: str
    :return: str
    '''
    value = 128
    current = 1
    octet = {'1': '0', '2': '0', '3': '0', '4': '0'}
    for x in range(0, 32):
        if bits[x] == "1":
            octet[str(current)] = int(octet[str(current)]) + value
        if value == 1:
            value = 128
            current += 1
            continue
        value = value / 2
    return str(int(octet["1"])) + "." + str(int(octet["2"])) + "." + str(int(octet["3"])) + "." + str(int(octet["4"]))


def ip_broadcastip(target, subnet):
    """Returns the broadcast IP in a subnet."""
    t_res = []
    net_res = []
    bc_res = []
    for x in ip_to_bits(target): t_res.append(x)
    for x in ip_to_bits(subnet): net_res.append(x)
    for x in range(0, 32):
        if net_res[x] == "1":
            bc_res.append(t_res[x])
        if net_res[x] == "0":
            bc_res.append("1")
    return bits_to_ip(bc_res)


def wc_compare(target, wc_net, wc_mask):
    """Determines if a target IP exists in a wildcard network and mask."""
    t_res = []
    net_res = []
    mask_res = []
    match = True
    for x in ip_to_bits(target): t_res.append(x)
    for x in ip_to_bits(wc_net): net_res.append(x)
    for x in ip_to_bits(wc_mask): mask_res.append(x)
    for y in range(0, 32):
        if t_res[y] != net_res[y] and mask_res[y] != "0":
            match = False
            break
    return match


def network_id(ip_cidr):
    ip, cidr = ip_cidr.split('/')
    ip_bits = ip_to_bits(ip)[:int(cidr)] + '0' * (32 - int(cidr))
    return '{}/{}'.format(bits_to_ip(ip_bits), cidr)
