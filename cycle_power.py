import Korod
import sys
import time
from serial_ports import ser_ports

"""
Arguments input which supplies
get turned off, then turned on. 

Arg is "1,2,3" or "1" or "3,2" 
"""


#argument parsing
strargs = sys.argv[1]
cycle_list = strargs.split(',')
cycle_list = [int(_) for _ in cycle_list]


#turn all off
for c in cycle_list:
    if(c == ''):
        continue
    print "powering off supply " + str(c)
    kor = Korod.Korod(ser_ports[c])
    kor.off()
    time.sleep(0.1)
    kor.close()

time.sleep(3)

#turn all on
for c in cycle_list:
    if(c == ''):
        continue

    print "powering on supply " + str(c)
    kor = Korod.Korod(ser_ports[c])
    kor.on()
    time.sleep(0.1)
    kor.close()

