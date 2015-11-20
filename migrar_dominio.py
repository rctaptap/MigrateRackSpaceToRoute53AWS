#!/usr/bin/env python

import boto.route53
import clouddns
import time
from sys import argv

script, dominio = argv

dns_clasificados = clouddns.connection.Connection('usuarioRackSpace','Password')
domain=dns_clasificados.get_domain(name=dominio)

conn = boto.connect_route53()
zone = conn.get_zone(dominio)

for record in domain.get_records():
        time.sleep(1)
        #print '(%s) %s -> %s' % (record.type, record.name, record.data)
        route53 = zone.find_records(record.name, record.type, desired=9, all=False, identifier=None)
        print route53
        if route53 == None:
                if record.type != "TXT":
                        if record.type != "NS":
                                try:
                                        result = zone.add_record(record.type, record.name, record.data)
                                        print '(%s) %s -> %s' % (record.type, record.name, record.data)
                                        print result

                                except Exception,e: print str(e)

