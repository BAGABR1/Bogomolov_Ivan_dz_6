def searcher():
    a = []
    ip_s = []
    with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
        line = file.readline()
        while line:
            ip = line.split(' ')[0]
            ip_s.append(ip)
            b = (ip, line.split('"')[1].split('/')[0][:-1], line.split('"')[1].split(' ')[1])
            a.append(b)
            line = file.readline()
    print(a)
    ip_lst = []
    dif_ip = set()
    for i in ip_s:
        dif_ip.add(i)
    dif_ip_list = list(dif_ip)
    for i in dif_ip_list:
        ip_lst.append(ip_s.count(i))
    maxim = max(ip_lst)
    print(f'ip: {dif_ip_list[ip_lst.index(maxim)]}-- {maxim}')


searcher()
