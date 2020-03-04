import serial
import time

global delay
delay = 0.2 #seconds to wait after sending bits before an input flush

class Korod:
	def __init__(self, usbport='/dev/ttyUSB0'):
		self.ser = serial.Serial(usbport, 9600)
		if(self.ser.isOpen()):
                        pass
			#print "Opened serial comms with Korod"

		else:
			print "Was unable to open serial comms with Korod"

	def close(self):
		self.ser.close()

	def open(self):
		self.ser.open()

	def read_cmd(self, cmd, byterange):
		self.ser.reset_input_buffer()
		time.sleep(delay)
		self.ser.write(cmd)
		time.sleep(delay)
		iw = self.ser.inWaiting()
		#sometimes serial coms fails and 
		#is inconsistent. Ignore Null returns
		if(min(byterange) <= iw <= max(byterange)):
			output = self.ser.read(iw)
			return output
		else:
			return None




	def on(self):
		self.ser.write("OUT1")
		time.sleep(delay)
		self.ser.reset_output_buffer()

	def off(self):
		self.ser.write("OUT0")
		time.sleep(delay)
		self.ser.reset_output_buffer()

	def setV(self, v):
		self.ser.write("VSET1:"+str(v))
		time.sleep(delay)
		self.ser.reset_output_buffer()

	def getVset(self):
		output = self.read_cmd("VSET1?", [4, 10])
		return float(output)

	def getV(self):
		output = self.read_cmd("VOUT1?", [4, 10])
		return float(output)

	def setI(self, i):
		self.ser.write("ISET1:"+str(i))
		time.sleep(delay)
		self.ser.reset_output_buffer()

	def getIset(self):
		output = self.read_cmd("ISET1?", [4, 10])
		return float(output.split('\x00')[0])

	def getI(self):
		output = self.read_cmd("IOUT1?", [4, 10])
		return float(output)
