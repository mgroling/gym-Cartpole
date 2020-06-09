from gym.envs.registration import register

register(
    id='cartpole_custom-v0',
    entry_point='gym_cartpole.envs:CartpoleEnv',
)