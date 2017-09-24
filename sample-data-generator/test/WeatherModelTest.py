import unittest
from models.weather_model import WeatherModel

class WeatherModelTest(unittest.TestCase):

    def setUp(self):
      self.model = WeatherModel(fuzzingRatio=0.0)

    def testTransform(self):
      self.assertEqual(self.model.transform(["PER|-31.95,115.86,20", "2015-12-23T09:18:12Z","-1","1200.0","95.0"]), "Snow")
      self.assertEqual(self.model.transform(["PER|-31.95,115.86,20", "2015-12-23T09:18:12Z", "1", "1200.0", "95.0"]),
                     "Rain")
      self.assertEqual(self.model.transform(["PER|-31.95,115.86,20", "2015-12-23T09:18:12Z", "1", "950.0", "40.0"]),
                     "Sunny")


if __name__ == '__main__':
    unittest.main()