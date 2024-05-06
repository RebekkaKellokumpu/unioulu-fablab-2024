from PiicoDev_MPU6050 import PiicoDev_MPU6050
from PiicoDev_Unified import sleep_ms
import bluetooth
from ble_simple_peripheral import BLESimplePeripheral

motion = PiicoDev_MPU6050()
previousValue = 0
repCount = 0

# Create a BLE object
ble = bluetooth.BLE()

# Create an instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble)


# Start an infinite loop
while True:
    accel = motion.read_accel_data() # read the accelerometer
    aX = accel["x"] #Read the accel value with x
    print("x:" + str(aX))
    if aX < 0 and previousValue >= 0: #This will do the actual counting
        repCount += 1
    previousValue = aX
    print(repCount)
    sleep_ms(100)
    msg = "Number of repetitions: " + str(repCount)
    if sp.is_connected():  # Check if a BLE connection is established
        #Sends the message to the bluetooth device
        sp.send(msg)

    