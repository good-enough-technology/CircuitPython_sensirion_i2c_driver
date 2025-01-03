Quick Start
===========

Following example code shows how the driver is intended to use:

.. note::

    This is just a short example to get an idea how the driver is used.
    If you plan to implement a new device driver, please also read the
    :ref:`guidelines for implementing device drivers <device_driver_guidelines>`.


.. sourcecode:: python

    from struct import pack
    from circuitpython_sensirion_i2c_driver import I2cTransceiver, I2cConnection, \
        I2cDevice, SensirionI2cCommand, CrcCalculator


    # Implement a command
    class MyI2cCmdReadSerialNumber(SensirionI2cCommand):
        def __init__(self):
            super(MyI2cCmdReadSerialNumber, self).__init__(
                command=0xD033,
                tx_data=[],
                rx_length=48,
                read_delay=0,
                timeout=0,
                crc=CrcCalculator(8, 0x31, 0xFF),
            )

        def interpret_response(self, data):
            raw_response = SensirionI2cCommand.interpret_response(self, data)
            return str(raw_response.decode('utf-8').rstrip('\0'))


    # Implement a device
    class MyI2cDevice(I2cDevice):
        def __init__(self, connection, slave_address=0x69):
            super(MyI2cDevice, self).__init__(connection, slave_address)

        def read_serial_number(self):
            return self.execute(MyI2cCmdReadSerialNumber())


    # Usage
    # I2cTransceiver import is Automatically switched between Linux/CircuitPython
    with I2cTransceiver('/dev/i2c-1') as transceiver:
        device = MyI2cDevice(I2cConnection(transceiver))
        print("Serial Number: {}".format(device.read_serial_number()))
