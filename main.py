from smbus2 import SMBus
import lsm6dso
import time
import signal
import sys

i2c = SMBus(2)
lsm = lsm6dso.LSM6DSO(i2c)

def handleCtrlC(signal, frame):
    i2c.close()
    sys.exit(130)

# This will capture exit when using Ctrl-C
signal.signal(signal.SIGINT, handleCtrlC)

while True:
    print(lsm.get())
    print(lsm.temperature())
    time.sleep(1)


# c = None
# response = []
# for i in range(255):
#     c = i2c.read_byte(0x44)
#     # i2c.read_byte_data
#     # print(c)
#     response.append(c)
# # time.sleep(1)
# for i in range(16):
#     print(response[i * 16 : i * 16 + 16])   
# # # breakpoint()