from models.model_interface import IModel
import random


class WeatherModel(IModel):

    def transform(self, featuresArray):
        if random.random() < self.fuzzingRatio:
            return random.choice(['Sunny', 'Cloudy', 'Rain', 'Snow'])

        weatherStationInfo = featuresArray[0].split(",")
        altitute = float(weatherStationInfo[len(weatherStationInfo)-1])
        temperature = float(featuresArray[2])
        pressure = float(featuresArray[3])
        humidity = float(featuresArray[4])
        # high humidity or high pressure makes it more likely to rain
        rainliness = pressure/10.0 + humidity
        if rainliness > 180:
            # Low temperature or high altitute makes it more likely to snow
            if (temperature < 0 ) or (altitute > 1000):
                weather = "Snow"
            else:
                weather = "Rain"
        elif rainliness > 150:
            weather = "Cloudy"
        else:
            weather = "Sunny"
        return weather
