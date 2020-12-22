"""Docstring."""


class Environment():
    """A simple environment."""

    def __init__(self):
        self.weather = 0
    
    def update_weather(self, new_weather):
        assert new_weather in (0, 1), "Not appropriate weather."
        self.weather = new_weather
    