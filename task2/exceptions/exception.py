class FuelDeficiencyException(ValueError):
    def __init__(self, value=None, label=None):
        self.value = value

        self.label = ''
        if label is not None:
            self.label = f'{label}: '

    def __str__(self):
        if self.value is None:
            return 'Недостаточно топлива'

        return f'{self.label}Недостаточно топлива, нужно еще {self.value:0.0f} л.'


class VehicleStateException(ValueError):
    def __init__(self, label=None):
        self.label = ''
        if label is not None:
            self.label = f'{label}:'

    def __str__(self):
        return f'{self.label} Не можем поехать, нужен ремонт'


class WeatherStateException(ValueError):
    def __init__(self, label=None):
        self.label = ''
        if label is not None:
            self.label = f'{label}:'

    def __str__(self):
        return f'{self.label} Не можем поехать, плохая погода'
