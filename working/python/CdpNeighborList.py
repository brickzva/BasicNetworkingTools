from easysnmp import Session

'''
EasySnmp does support SNMPv1/v2c/3 implementations.  
This was a simple test of using a common SNMPv2c implementation.
From CLI example output:
Give me an IP to search for neighbors: 192.168.1.2
----------
Name                          IP Address          Platform                      
AP-down2                      192.168.1.169       cisco AIR-CAP3702I-A-K9       
AP-down                       192.168.1.167       cisco AIR-CAP3702I-A-K9       
WLC_HOME                      192.168.1.239       AIR-CT2504-K9                 
test-sw.home.here             192.168.1.3         cisco WS-C2960C-8TC-L         
'''

table = '{0:30}{1:20}{2:30}'

newname = []
newip = []
newplat = []


def cdpname(h, c):
    i = 0
    session = Session(hostname=h, community=c, version=2)
    cname = session.walk('1.3.6.1.4.1.9.9.23.1.2.1.1.6')

    while i < len(cname):
        s_name = cname[i].value
        i = i + 1
        newname.append(s_name)
    return


def cdpip(h, c):
    i = 0
    session = Session(hostname=h, community=c, version=2)
    cip = session.walk('1.3.6.1.4.1.9.9.23.1.2.1.1.4')

    while i < len(cip):
        s_ip = cip[i].value
        s_ip = ' '.join(['%0.2x' % ord(_) for _ in s_ip])
        n_ip = s_ip.split(' ')
        ip_0 = int(n_ip[0], 16)
        ip_1 = int(n_ip[1], 16)
        ip_2 = int(n_ip[2], 16)
        ip_3 = int(n_ip[3], 16)
        converted_ip = str('{0}.{1}.{2}.{3}'.format(ip_0, ip_1, ip_2, ip_3))
        i = i + 1
        newip.append(converted_ip)
    return


def cdpplat(h, c):
    i = 0
    session = Session(hostname=h, community=c, version=2)
    cplat = session.walk('1.3.6.1.4.1.9.9.23.1.2.1.1.8')

    while i < len(cplat):
        s_plat = cplat[i].value
        i = i + 1
        newplat.append(s_plat)
    return


if __name__ == "__main__":
    cmnty = 'public' # set correct community for your network device
    newhost = input("Give me an IP to search for neighbors: ")
    cdpname(newhost, cmnty)
    cdpip(newhost, cmnty)
    cdpplat(newhost, cmnty)
    #
    print("-" * 10)
    print(table.format("Name", "IP Address", "Platform"))
    for aa, bb, cc in zip(newname, newip, newplat):
        print(table.format(aa, bb, cc))
