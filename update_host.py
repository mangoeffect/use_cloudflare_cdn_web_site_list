import argparse
import re

def get_parser():
    parser = argparse.ArgumentParser("srcipt for update host")
    parser.add_argument("--ip", help="update ip")
    parser.add_argument('--domain', help="domain list filename")
    return parser

def IsDomain(domain):
    ds = re.findall('^(?=^.{3,255}$)[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+$', domain)
    if(len(ds) != 0):
        return True
    else:
        return False


def update(ip, domain_file_path):
    dns_list = ["#cloudflare host\n"]
    dns_list.append("#https://github.com/mangosroom/use_cloudflare_cdn_web_site_list\n")
    with open(str(domain_file_path),'r') as fr:
        line =fr.readline()
        while line:
            if (IsDomain(line)):
                dns_list.append(ip + "\t\t" + line)
            else:
                dns_list.append(" \n")
            line=fr.readline()
    fr.close()
    with open('./hosts_file/shenzhen_ctcc_1.txt', 'w') as fw:
        for dns in dns_list:
            fw.writelines(dns)
    fw.close()

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    ip = args.ip
    domain_file = args.domain
    update(ip, domain_file)