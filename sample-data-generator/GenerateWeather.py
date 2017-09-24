from sample_data_generator import SampleDataGenerator
import json
from models.weather_model import WeatherModel

g = SampleDataGenerator(json.loads(open("features/features.json").read()),
                        WeatherModel(fuzzingRatio=0.05),
                        open('output/output.txt','w'))
g.generateSampleData(numOfRows=1000)