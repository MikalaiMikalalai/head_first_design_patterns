######################################################
#                 Observer                           #
######################################################

import abc
import collections

######################################################
#                   Interfaces                       #
######################################################

WeatherParams = collections.namedtuple('WeatherParams', ['temperature', 'humidity', 'pressure'])


class Subject(abc.ABC):

    @abc.abstractmethod
    def register_observer(self, observer):
        pass

    @abc.abstractmethod
    def remove_observer(self, observer):
        pass

    @abc.abstractmethod
    def notify_observers(self):
        pass


class Observer(abc.ABC):

    @abc.abstractmethod
    def update(self):
        pass


class DisplayElement(abc.ABC):

    @abc.abstractmethod
    def display(self, weather_params: WeatherParams):
        pass


######################################################
#                   Implementations                  #
######################################################

class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.__temperature: float
        self.__humidity: float
        self.__pressure: float

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for obs in self.observers:
            obs.update()

    def measurements_changed(self):
        self.notify_observers()

    def set_measurments(self, temperature, humidity, pressure):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.measurements_changed()

    def get_weather_params(self):
        return WeatherParams(self.__temperature,
                             self.__humidity,
                             self.__pressure)


class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self):
        self.display(self.weather_data.get_weather_params())

    def display(self, weather_params):
        print(f'Current conditions: {weather_params.temperature}F degrees'
              f' and {weather_params.humidity}% humidity')


class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self):
        curr_weather_params = self.weather_data.get_weather_params()
        statistics_weather_params = WeatherParams(curr_weather_params.temperature - 2,
                                                  curr_weather_params.humidity - 2,
                                                  curr_weather_params.pressure - 2)
        self.display(statistics_weather_params)

    def display(self, weather_params):
        print(f'Previous conditions: {weather_params.temperature}F degrees'
              f' and {weather_params.humidity}% humidity')


class ForecastDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self):
        curr_weather_params = self.weather_data.get_weather_params()
        forecast_weather_params = WeatherParams(curr_weather_params.temperature + 2,
                                                curr_weather_params.humidity + 2,
                                                curr_weather_params.pressure + 2)
        self.display(forecast_weather_params)

    def display(self, weather_params):
        print(f'Tomorrow conditions: {weather_params.temperature}F degrees'
              f' and {weather_params.humidity}% humidity')


if __name__ == '__main__':

    # Initializing objects
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    # Starting weather station
    weather_data.set_measurments(80, 65, 30.4)
    weather_data.set_measurments(82, 70, 29.2)
    weather_data.set_measurments(78, 90, 29.2)
