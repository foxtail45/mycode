#!/usr/bin/env python3
"""Showing how to move files into ceph_storage/"""


# standard library imports

import shutil

import os

os.chdir('/home/student/mycode/')

shutil.move('raynor.obj', 'ceph_storage/')

xname = input('What is the new name for kerrigan.obj? ')

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main() # this calls our main function

