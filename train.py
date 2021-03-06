#!/usr/bin/python
# Runs somoclu initializing with the codelist of the previous epoch

import os
from subprocess import call

first = '2012-05-13'
initialcb = 'initial-codebook.wts'
path = '/home/amp/ssd/mats'
suffix = '-mat.out.sorted'
previous = '2012-05-13'
out_suffix = suffix + '.rgb.wts'
this_suffix = '.rgb'

for dirname, firnmaes, filenames in os.walk(path):
    for filename in sorted(filenames):
        if filename.endswith(suffix):
            if first not in filename:
                call('somoclu -k 2 -x 25 -y 15 -c ' + previous + out_suffix + ' -l 0.05 -e 3 -t exponential -m toroid -r 5 ' + filename + ' ' + filename + this_suffix, shell=Tru\
e)
                # print 'somoclu -k 2 -x 25 -y 15 -c ' + previous + out_suffix + ' -l 0.05 ' + filename + ' ' + filename + this_suffix
            else:
                call('somoclu -k 2 -x 25 -y 15 -c ' + initialcb + ' -l 0.1 -e 10 -t exponential -m toroid -r 5 ' + filename + ' ' + filename + this_suffix, shell=True)
            previous = filename[0:10]
