"""Docstring."""


class Agent():
    """A simple agent."""
    
    def __init__(self):
        self.pos = 0
        self.obs = None
    
    def get_observation(self, obs):
        self.obs = (obs, self.pos)

    def move_left(self):
        if self.pos == 0:
            self.pos = 0
        elif self.pos == 1:
            self.pos = 0

    def move_right(self):
        if self.pos == 0:
            self.pos = 1
        elif self.pos == 1:
            self.pos = 1

    def act(self):
        if self.obs[0] == 1:
            self.move_left()
            return 0
        elif self.obs[0] == 0:
            self.move_right()
            return 1
    