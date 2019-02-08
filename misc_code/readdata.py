import smbus
import time
import json
bus = smbus.SMBus(1)

# bit field 		meaning
# 15:15  			1 - start single conversion
# 14:12				000 - differential input
# 11:09				111 - input range (+-0.256V)
# 08:08 			0 - continuous conversion
# 07:05 			100 - 128SPS (default)
# 04:01 			00011 - default comparator settings
bus.write_i2c_block_data(0x48,0x01,[0x88, 0x83])


f = int(input("what is f"))
while f == 1:
	#read data from ADC
	data = int.from_bytes(bus.read_i2c_block_data(0x48,0x00,2))
	#define dictionary
	data_dict = dict(time=time.ctime(),load=data)
	#json
	payload = json.dumps(data_dict)
	print(data)
	print(data_dict)
	f = int(input("what is f"))
