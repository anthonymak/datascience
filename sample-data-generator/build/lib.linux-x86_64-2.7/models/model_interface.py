import abc

# Implement this interface to supply your own model for sample data generation
class IModel(metaclass=abc.ABCMeta):

    def __init__(self, fuzzingRatio = 0.0):
      self.fuzzingRatio = fuzzingRatio

    @abc.abstractmethod
    def transform(self, featuresArray):
        pass