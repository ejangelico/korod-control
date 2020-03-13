import Korod
import sys
import time
from serial_ports import ser_ports
"""
Arguments input which supplies
are read. 

Arg is "0,1,2,3" or "1" or "3,2" 
"""


#argument parsing
strargs = sys.argv[1]
read_list = strargs.split(',')
read_list = [int(_) for _ in read_list]

#turn all off
for c in read_list:
    if(c == ''):
        continue
    kor = Korod.Korod(ser_ports[c])
    print "Supply #" + str(c),
    i = kor.getI()
    v = kor.getV()
    print str(v) + "V, " + str(i) + "A" 
    time.sleep(0.1)

