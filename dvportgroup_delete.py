#! /usr/bin/env python

from vsphere import vSphere
from vsphere import credentials


dportgroup = raw_input("Distributed port group to be deleted: ")

# Read the credentials for vShere from YAML fiel and input dialog
inputs = 'inputs/vsphere_lab.yml'


# Create an instance of Class vSphere
cred = credentials(inputs)
vmw = vSphere(*cred)

# Delete port group
vmw.del_dvPort_group(dportgroup)
