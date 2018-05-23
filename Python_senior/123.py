# coding: utf-8
__author__ = 'lau.wenbo'

from netaddr import *


ip_cidr = "10.0.20.22/"
ip = IPNetwork(ip_cidr)
ip_list = list(ip)
print(ip_list)