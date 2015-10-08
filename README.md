# NameCheap Dynamic DNS Updater (ncddnsupdater.py)

A little Python script to update the DNS records for a NameCheap domain with
dynamic DNS enabled. Requires Python 3 and requests to run (pip3 install requests).

Usage:

```
$ ./ncddnsupdater.py -h
usage: ncddnsupdater.py [-h] -H HOSTS -p PASSWORD -d DOMAIN

Update DNS entries for a NameCheap hosted domain with dynamic DNS enabled.

optional arguments:
  -h, --help            show this help message and exit
  -H HOSTS, --hosts HOSTS
                        The subdomains to update separated by commas ('@' for
                        root domain).
  -p PASSWORD, --password PASSWORD
                        Your NameCheap dynamic DNS password.
  -d DOMAIN, --domain DOMAIN
                        The root domain to update.
```
