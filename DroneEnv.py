import gym
from gym import spaces
import numpy as np
import airsim

class DroneEnv(gym.Env):
    def __init__(self):
        super(DroneEnv, self).__init__()
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()

        # Define action and observation space
        self.action_space = spaces.Box(low=-1, high=1, shape=(3,), dtype=np.float32)
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(3,), dtype=np.float32)

    def step(self, action):
        # Apply action
        pitch, roll, yaw = action
        self.client.moveByAngleThrottleAsync(pitch, roll, yaw, 1).join()

        # Return new state, reward, done
        obs = self.client.getMultirotorState().kinematics_estimated.position
        reward = -np.linalg.norm(obs)  # Reward based on proximity to target (0, 0, 0)
        done = False
        return np.array([obs.x_val, obs.y_val, obs.z_val]), reward, done, {}

    def reset(self):
        self.client.reset()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)
        self.client.takeoffAsync().join()
        return np.array([0.0, 0.0, -10.0])

    def render(self, mode='human'):
        pass
