from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from drone_env import DroneEnv  # Import the custom environment

# Create the environment
env = DroneEnv()
check_env(env)

# Instantiate the RL model
model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./ppo_drone_tensorboard/")

# Train the model
model.learn(total_timesteps=100)

# Save the model
model.save("ppo_drone_model")
