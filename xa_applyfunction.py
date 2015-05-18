#!/usr/bin/python
import sys
import numpy as np
import extattrib as xa

xa.params = {
    'Input': 'Filter Input'}

def doCompute():
        x,y=np.loadtxt('C:\\Users\\zahup\\Desktop\\xa_examples\\function.csv',delimiter=',', unpack=True)
        while True:
                xa.doInput()
                xa.Output = xa.Input*np.interp(xa.Input,x,y, left=0, right=1)
                xa.doOutput()

xa.doCompute = doCompute
xa.run(sys.argv[1:])
