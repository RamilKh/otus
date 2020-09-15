from dataclasses import dataclass
from task2.configs.const import WeatherDirectory


@dataclass()
class Weather:
    state: WeatherDirectory = WeatherDirectory.SUNNY

    def set_weather(self, state):
        self.state = state
        print(f'Погода: {self.state.value}')

    def sunny(self):
        self.state = WeatherDirectory.SUNNY
        print(f'Погода: {self.state.value}')

    def rain(self):
        self.state = WeatherDirectory.RAIN
        print(f'Погода: {self.state.value}')
