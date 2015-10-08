#!/usr/bin/env python3
import argparse
import requests

def parse_args():
    p = argparse.ArgumentParser(description="Update the dynamic DNS entry for a NameCheap hosted domain.")
    p.add_argument("-H", "--hosts", required=True, help="The subdomains to update ('@' for root domain)")
    p.add_argument("-p", "--password", required=True, help="Your NameCheap dynamic DNS password.")
    p.add_argument("-d", "--domain", required=True, help="The root domain to update.")
    return p.parse_args()

def main():
    args = parse_args()
    args.hosts = args.hosts.split(",")

    ip = requests.get("https://dynamicdns.park-your-domain.com/getip").text

    for host in args.hosts:
        print("Updating {} to {}".format(host, ip))
        response = requests.get("https://dynamicdns.park-your-domain.com/update", params = {
            'domain': args.domain,
            'host': host,
            'password': args.password,
            'ip': ip,
        })

        if "<ErrCount>0</ErrCount>" not in response.text:
            print("ERROR! Could not update domain {}! Full Response:\n".format(host))
            print(response.text)
            sys.exit(-1)

if __name__ == '__main__':
    main()
