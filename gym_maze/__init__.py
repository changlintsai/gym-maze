from gym.envs.registration import register

register(
    id='maze-v0',
    entry_point='gym_maze.envs:MazeEnv',
)

register(
    id='maze-v1',
    entry_point='gym_maze_1.envs:MazeEnv',
)

register(
    id='maze-v2',
    entry_point='gym_maze_2.envs:MazeEnv',
)
