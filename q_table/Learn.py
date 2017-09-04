from q_table.GameEnvironment import GameEnvironment
import numpy as np
import numpy.lib.recfunctions as rfn
import pandas as pd

# Consider using pandas


class Learn:
    def __init__(self):
        self.game_size = 3

        ####
        #  Q table
        # - row: Game state is represented by string containing flattened matrix. For example: [[x,o],[o,x]] becomes "xoox"
        # - column: Action is a tuple representing move coordinates
        # - value: reward value
        #
        self.n_possible_states = 5812  # TODO do it differently
        self.n_possible_actions = self.game_size * self.game_size

        # One of the possible examples of using Q table: q["oo.xoxxo.", (1, 2)] = 0
        self.q = pd.DataFrame.from_items([('.........', np.zeros(self.n_possible_actions))], orient='index',
                                         columns=range(self.n_possible_actions))

        self.gamma = 0.8
        self.alpha = 1.0
        self.epsilon = 0.05

        self.n_episodes = 1000

        self.env = GameEnvironment(self.game_size)

        self.all_possible_actions = self.env.get_all_game_actions()

    def get_q_value(self, state):
        print("checking for " + state)
        if state not in self.q.index:
            self.q.loc[state] = np.zeros(self.n_possible_actions)
        return self.q.loc[state]


    def solve(self):
        # print(self.q)


        # Core algorithm

        rand = np.random.RandomState(777)

        for e in range(self.n_episodes):
            self.env.reset()
            goal = False
            while not goal:
                print(self.q)
                current_state = self.env.get_state()
                print(current_state)
                actions_weights = self.get_q_value(current_state)
                # print(actions_weights)
                if np.sum(actions_weights) > 0:
                    action = np.argmax(actions_weights) # Indices of the maximum values along an axis.
                else:
                    action = rand.choice(self.all_possible_actions)

                # next_state = action

                reward = self.update_q(current_state, action)

                if reward != 0:
                    goal = True
                print(reward)

    def update_q(self, current_state, action):

        reward = self.env.step(action)  # Get R(state, action)
        next_state = self.env.get_state()
        next_state_actions_weights = self.get_q_value(next_state)
        next_q_max = np.amax(next_state_actions_weights)

        # Calculate new Q
        new_q = reward + self.gamma * next_q_max

        # Set Q(state, action)
        self.q.loc[current_state][action] = new_q

        return new_q


l = Learn()
l.solve()