from q_table.GameEnvironment import GameEnvironment
import numpy as np

game_size = 3

####
#  Q table
# - row: Game state is represented by string containing flattened matrix. For example: [[x,o],[o,x]] becomes "xoox"
# - column: Action is a tuple representing move coordinates
# - value: reward value
#
all_possible_states = 5812  # TODO do it differently
all_possible_actions = game_size * game_size

# One of the possible examples of using Q table: q["oo.xoxxo.", (1, 2)] = 0
q = np.zeros((all_possible_states, all_possible_actions))


env = GameEnvironment(game_size)

# Core algorithm
gamma = 0.8
alpha = 1.0
epsilon = 0.05

n_episodes = 1000

rand = np.random.RandomState(777)

for e in range(n_episodes):
    pass