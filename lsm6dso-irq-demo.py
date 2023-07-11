from smbus2 import SMBus
import lsm6dso
import time

i2c = SMBus(2)
lsm = lsm6dso.LSM6DSO(i2c)
lsm.ax()
lsm.get_a()
lsm.get()

def tim_irq(t):
    print(lsm.get(), lsm.temperature())

while True:
    tim_irq(1)
    time.sleep(1)