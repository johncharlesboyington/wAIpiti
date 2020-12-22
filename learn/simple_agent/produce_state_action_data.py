"""Docstring."""
import numpy as np
from environment import Environment
from agent import Agent


def produce_data():
    """Produces state action pairs for our agent's behavior"""
    
    # create a weather pattern for our guy
    weather_pattern = [np.random.randint(0, 2) for _ in range(10000)]
    
    # initialize environment and agent
    env = Environment()
    guy = Agent()
    
    # get place to store the guy's actions and observations
    actions = []
    observations = []

    # do it
    for w in weather_pattern:
        env.update_weather(w)
        guy.get_observation(env.weather)
        actions.append(guy.act())
        observations.append(guy.obs)

    # store the data
    s = ''
    for i in range(len(actions)):
        s += '{} {}\n'.format(actions[i], observations[i])
    with open('state_action_pairs.txt', 'w+') as F:
        F.write(s)
    return
    

if __name__ == '__main__':
    produce_data()
