import sys
sys.path.append('path_to_AirSim/PythonClient/')

import airsim
import time

# Connect to AirSim
client = airsim.MultirotorClient()
client.confirmConnection()

# Take off
client.enableApiControl(True)
client.armDisarm(True)
client.takeoffAsync().join()

# Simple move to a position
client.moveToPositionAsync(0, 0, -10, 5).join()
time.sleep(5)

client.moveToPositionAsync(0, 0, 100, 50).join()
time.sleep(5)

client.moveToPositionAsync(0, 0, -20, 50).join()

# Hover for 5 seconds
time.sleep(5)

# Land
client.landAsync().join()
client.armDisarm(False)
client.enableApiControl(False)
