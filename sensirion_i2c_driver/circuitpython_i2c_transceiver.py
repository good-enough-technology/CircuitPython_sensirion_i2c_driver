from adafruit_bus_device.i2c_device import I2CDevice
from .transceiver_v1 import I2cTransceiverV1

class CircuitPythonI2cTransceiver(I2cTransceiverV1):
    def __init__(self, i2c, device_address):
        super(CircuitPythonI2cTransceiver, self).__init__()
        self._device = I2CDevice(i2c, device_address)

    @property
    def description(self):
        return "CircuitPython I2C Transceiver"

    def transceive(self, slave_address, tx_data, rx_length, read_delay, timeout):
        if tx_data is not None:
            self.write(tx_data)
        if rx_length is not None:
            return self.STATUS_OK, None, self.read(rx_length)
        return self.STATUS_OK, None, bytearray()

    def write(self, data):
        data_bytes = bytearray(data) if isinstance(data, (bytes, bytearray, list, tuple)) else bytearray()
        with self._device as i2c_device:
            i2c_device.write(data_bytes)

    def read(self, count):
        read_buffer = bytearray(count)
        with self._device as i2c_device:
            i2c_device.readinto(read_buffer)
        return read_buffer
