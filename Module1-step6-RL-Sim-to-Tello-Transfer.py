from djitellopy import Tello
import numpy as np
from stable_baselines3 import PPO
import time

# Connect to the DJI Tello drone
tello = Tello()
tello.connect()

# Load the trained PPO model
model = PPO.load("ppo_drone_model")

# Function to get the drone's current state and format it as an observation
def get_observation():
    # Retrieve Tello's state (for simplicity, we'll just use some basic state info)
    state = tello.get_state()
    
    # Example observation: roll, pitch, yaw (you can adjust this based on your environment)
    observation = np.array([state.roll, state.pitch, state.yaw])
    
    # If using more advanced sensors like the camera, you could add the camera feed here
    return observation

# Takeoff the drone
tello.takeoff()

# Define an action mapping to control the Tello drone
def execute_action(action):
    # Assuming the PPO model outputs actions like 0: forward, 1: rotate, etc.
    if action == 0:
        tello.move_forward(100)  # Move forward by 100 cm
    elif action == 1:
        tello.rotate_clockwise(90)  # Rotate clockwise by 90 degrees
    elif action == 2:
        tello.move_left(50)  # Move left by 50 cm
    elif action == 3:
        tello.move_right(50)  # Move right by 50 cm
    elif action == 4:
        tello.move_back(100)  # Move back by 100 cm
    elif action == 5:
        tello.move_up(50)  # Move up by 50 cm
    elif action == 6:
        tello.move_down(50)  # Move down by 50 cm

# Run the drone for a fixed number of steps using the PPO model to choose actions
for step in range(100):  # You can adjust this number based on your needs
    # Get the current observation from the drone
    obs = get_observation()
    
    # Use the trained PPO model to predict the next action
    action, _states = model.predict(obs)
    
    # Execute the predicted action on the drone
    execute_action(action)
    
    # Sleep for a bit to give the drone time to complete the action
    time.sleep(2)  # Adjust based on how fast you want to run actions

# Land the drone after the steps are complete
tello.land()

# End the Tello session
tello.end()
