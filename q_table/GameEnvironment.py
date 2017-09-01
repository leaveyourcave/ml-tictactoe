import numpy as np


class GameEnvironment:
    def __init__(self, size):
        self.size = size
        self.board = np.chararray((self.size, self.size))
        self.reset()

    def reset(self):
        self.board[:] = '.'

    def get_state(self):
        return ''.join(self.board.flatten())

    def get_all_game_actions(self):
        return range(0, self.size * self.size)
        # one_dim = [i for i, e in enumerate(self.board)]
        # ret = []
        # for y in one_dim:
        #     sec_dim = [i for i, e in enumerate(self.board[y])]
        #     for x in sec_dim:
        #         ret.append((y, x))
        # return ret


    def check_game_state(self):
        # check horizontal
        for y in range(0, self.size):
            all_ok = True
            prev = self.board[y, 0]
            for x in range(1, self.size):
                if prev == '.' or self.board[y, x] != prev:
                    all_ok = False

            if all_ok:
                return prev  # WINNER

        # check vertical
        for x in range(0, self.size):
            all_ok = True
            prev = self.board[0, x]
            for y in range(1, self.size):
                if prev == '.' or self.board[y, x] != prev:
                    all_ok = False

            if all_ok:
                return prev  # WINNER

        # check diagonal, TODO add checking second diagonal
        prev = self.board[0, 0]
        all_ok = True
        for xy in range(1, self.size):
            if prev == '.' or self.board[xy, xy] != prev:
                all_ok = False

        if all_ok:
            return prev  # WINNER

        # check if draw
        all_marked = True
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.board[y, x] != '.':
                    all_marked = False

        if all_marked:
            return '.'  # DRAW

        return None

    def make_computer_move(self):
        available_indexes = np.where(self.board == '.')
        random_choice = np.random.randint(0, available_indexes[0].size)
        rand_y = available_indexes[0][random_choice]
        rand_x = available_indexes[1][random_choice]
        self.board[rand_y, rand_x] = 'o'

    def step(self, action):
        x_coordinate = action % self.size
        y_coordinate = action / self.size

        if y_coordinate >= self.size or x_coordinate >= self.size:
            # Wrong move - field doesn't exist
            return -3

        if self.board[y_coordinate, x_coordinate] != '.':
            # Wrong move - field already taken
            return -3

        self.board[y_coordinate, x_coordinate] = 'x'

        state = self.check_game_state()
        if state is None:
            # if not end, make COM move
            self.make_computer_move()
            # checkGameState and return reward
            state = self.check_game_state()

        # Interpret the state
        if state is None:
            return 0
        if state == '.':
            return 1
        elif state == 'x':
            return 2
        elif state == 'o':
            return -1
        else:
            return 0  # shouldn't happen

#
# d = GameEnvironment(3)
# print(d.board)
# print(d.step(2))
# print(d.board)
# print(d.step(0))
# print(d.board)
# print(d.step(8))
# print(d.board)
# print(d.get_all_game_actions())