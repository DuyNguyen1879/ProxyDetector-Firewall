#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import argparse

try:
    from proxy_detector_firewall import ProxyDetectorFirewall
except ImportError:
    from proxydetectorfirewall.proxy_detector_firewall import ProxyDetectionFirewall

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input',type=str, required=True, help="File containing an ip list")
    parser.add_argument('-f', '--firewall',type=str, required=True, choices=['iptables', 'mikrotik', 'cisco-acl','cidr','ciscobitbucket','juniperjunos'], help="Firewall, output format for the rules.")
    parser.add_argument('-o', '--output', type=str, default='Output.txt', help="Output file with the rules to block the ips detected as a proxy.")
    
    args = parser.parse_args()

    af = ProxyDetectorFirewall()
    af.detect_anonymous(args.input, args.firewall, args.output)