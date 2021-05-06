#!/usr/bin/env python3

from lib.configparser import parseConfig

host, port = parseConfig('ini/config.ini')

print(host, port)


