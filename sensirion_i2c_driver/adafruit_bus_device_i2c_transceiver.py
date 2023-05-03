from adafruit_bus_device.i2c_device import I2CDevice

class AdafruitBusDeviceI2cTransceiver:
    def __init__(self, i2c_bus, device_address):
        self._i2c_device = I2CDevice(i2c_bus, device_address)

    def read(self, count):
        read_buffer = bytearray(count)
        with self._i2c_device as i2c:
            i2c.readinto(read_buffer)
        return read_buffer

    def write(self, data):
        with self._i2c_device as i2c:
            i2c.write(data)
