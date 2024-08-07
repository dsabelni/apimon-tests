#!/usr/bin/env python3
import openstack
import sys
from otcextensions import sdk

openstack.enable_logging(True)
conn = openstack.connect()
sdk.register_otc_extensions(conn)

# openstack.enable_logging(debug=True, http_debug=True)

container_name = sys.argv[1]

# create container
headers = {'x-amz-bucket-type': 'SFS', 'x-obs-az-redundancy': '3az'}
conn.obs.create_container(name=container_name, headers=headers)
