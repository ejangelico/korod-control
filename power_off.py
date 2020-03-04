import Korod
import sys
import time

"""
Arguments input which supplies
get turned off, then turned on. 

Arg is "1,2,3" or "1" or "3,2" 
"""

ser_port = "/dev/ttyACM"

#argument parsing
strargs = sys.argv[1]
cycle_list = strargs.split(',')
ser_ports = [ser_port+str(int(_)) for _ in cycle_list]


#turn all off
for port in ser_ports:
    print "powering off supply number " + str(port)
    kor = Korod.Korod(port)
    kor.off()
    time.sleep(0.1)
    kor.close()

time.sleep(3)

