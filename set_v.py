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
supplyno = int(sys.argv[1])
setv = float(sys.argv[2])
#turn all off
kor = Korod.Korod(ser_ports[supplyno])
print "Setting V = " + sys.argv[2] + "to Supply #" + str(supplyno)
kor.setV(setv)
time.sleep(0.3)
print "Now measures at " + str(kor.getV())

