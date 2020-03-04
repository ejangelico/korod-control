import Korod

k1 = Korod.Korod("/dev/ttyACM0")
k2 = Korod.Korod("/dev/ttyACM1")
k3 = Korod.Korod("/dev/ttyACM2")

print k1.getV()
print k2.getV()
print k3.getV()
