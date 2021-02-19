import smbus2
import time

bus = smbus2.SMBus(1)
si_addr = 0x40
def temp_and_hum():

    temp = bus.read_i2c_block_data(si_addr, 0xE3,2)

    Temp = ((temp[0] * 256 + temp[1]) * 175.72 / 65536.0) - 46.85
    time.sleep(0.1)



    rh = bus.read_i2c_block_data(si_addr, 0xE5, 2)


    humidity = ((rh[0] * 256 + rh[1]) * 125 / 65536.0) - 6
    time.sleep(0.1)

    return Temp,humidity

